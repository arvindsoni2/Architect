#!/usr/bin/env python3
"""Local teaching lab: SQLite reservation, atomic outbox and duplicate-safe effect.

No cloud services or payment calls. Default runs disposable experiments; --serve
offers a loopback-only browser/API/database path using a temporary database.
"""
import argparse
import concurrent.futures
import contextlib
import http.server
import json
import pathlib
import sqlite3
import tempfile
import time


@contextlib.contextmanager
def connection(db):
    conn = sqlite3.connect(str(db), timeout=5, isolation_level=None)
    try:
        yield conn
    finally:
        conn.close()


def initialise(db, stock=1):
    with connection(db) as conn:
        conn.executescript('''
          CREATE TABLE stock (id INTEGER PRIMARY KEY, available INTEGER NOT NULL CHECK(available >= 0));
          CREATE TABLE requests (key TEXT PRIMARY KEY, quantity INTEGER NOT NULL, status TEXT NOT NULL);
          CREATE TABLE outbox (key TEXT PRIMARY KEY, delivered INTEGER NOT NULL DEFAULT 0);
          CREATE TABLE effects (key TEXT PRIMARY KEY);
        ''')
        conn.execute('INSERT INTO stock VALUES (1, ?)', (stock,))


def reserve(db, key, quantity, crash_before_commit=False):
    if not isinstance(key, str) or not key.strip() or len(key) > 100:
        raise ValueError('key must be a nonempty string of at most 100 characters')
    if type(quantity) is not int or not 1 <= quantity <= 1000:
        raise ValueError('quantity must be an integer from 1 to 1000')
    with connection(db) as conn:
        conn.execute('BEGIN IMMEDIATE')
        previous = conn.execute('SELECT quantity, status FROM requests WHERE key=?', (key,)).fetchone()
        if previous:
            if previous[0] != quantity:
                raise ValueError('idempotency key reused with a different quantity')
            conn.commit()
            return {'key':key, 'quantity':quantity, 'status':previous[1]}
        updated = conn.execute('UPDATE stock SET available=available-? WHERE id=1 AND available>=?', (quantity,quantity)).rowcount
        status = 'reserved' if updated else 'rejected'
        conn.execute('INSERT INTO requests VALUES (?,?,?)', (key,quantity,status))
        if updated:
            conn.execute('INSERT INTO outbox(key) VALUES (?)', (key,))
        if crash_before_commit:
            raise RuntimeError('simulated interruption before commit')
        conn.commit()
        return {'key':key, 'quantity':quantity, 'status':status}


def relay(db, crash_after_effect=False):
    """Two commits expose the duplicate-delivery window; effect is a local receipt.

The effects table models a consumer's atomic deduplication + local effect. It
does not prove exactly-once delivery or idempotency of an external payment API.
"""
    with connection(db) as conn:
        keys = conn.execute('SELECT key FROM outbox WHERE delivered=0 ORDER BY key').fetchall()
        for (key,) in keys:
            conn.execute('BEGIN IMMEDIATE')
            conn.execute('INSERT OR IGNORE INTO effects VALUES (?)', (key,))
            conn.commit()
            if crash_after_effect:
                raise RuntimeError('simulated interruption after effect, before delivery acknowledgement')
            conn.execute('UPDATE outbox SET delivered=1 WHERE key=?', (key,))
    return len(keys)


def snapshot(db):
    with connection(db) as conn:
        return {
            'stock':conn.execute('SELECT available FROM stock WHERE id=1').fetchone()[0],
            'reservations':conn.execute("SELECT COUNT(*) FROM requests WHERE status='reserved'").fetchone()[0],
            'outbox':conn.execute('SELECT COUNT(*) FROM outbox').fetchone()[0],
            'pending':conn.execute('SELECT COUNT(*) FROM outbox WHERE delivered=0').fetchone()[0],
            'effects':conn.execute('SELECT COUNT(*) FROM effects').fetchone()[0],
        }


def experiments(directory):
    db = directory / 'concurrent.db'
    initialise(db)
    started = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda key: reserve(db,key,1), ['order-a','order-b']))
    winner = next(result for result in results if result['status']=='reserved')
    retry = reserve(db,winner['key'],1)  # Assume the first response was lost.
    try:
        relay(db,crash_after_effect=True)
    except RuntimeError:
        interrupted = snapshot(db)
    relay(db)
    rollback_db = directory / 'rollback.db'
    initialise(rollback_db)
    try:
        reserve(rollback_db,'order-c',1,crash_before_commit=True)
    except RuntimeError:
        pass
    return {
        'scope':'Local SQLite experiment; effect is a simulated receipt, not a payment.',
        'runtime':{'sqlite':sqlite3.sqlite_version,'elapsed_ms':round((time.perf_counter()-started)*1000,3)},
        'concurrent_results':results,
        'retry_matches':retry==winner,
        'after_relay_interruption':interrupted,
        'after_recovery':snapshot(db),
        'before_commit_interruption':snapshot(rollback_db),
    }


PAGE = '''<!doctype html><html lang="en"><meta charset="utf-8"><title>Reservation request trace</title>
<h1>Browser → API → SQLite</h1><p>Local teaching data. One item is available. Repeat a key to retry.</p>
<form id="form"><label>Request key <input id="key" value="order-a" required maxlength="100"></label>
<label>Quantity <input id="quantity" type="number" value="1" min="1" max="1000" required></label>
<button>Reserve</button></form><pre id="result" role="status"></pre>
<p>Inspect the POST /reserve in your browser Network panel and the terminal trace. Restart to reset the temporary database.</p>
<script>document.getElementById('form').onsubmit=async event=>{event.preventDefault();
try {const response=await fetch('/reserve',{method:'POST',headers:{'Content-Type':'application/json'},
body:JSON.stringify({key:document.getElementById('key').value,quantity:Number(document.getElementById('quantity').value)})});
document.getElementById('result').textContent=JSON.stringify(await response.json(),null,2);
} catch(error) {document.getElementById('result').textContent=error.message;}};</script></html>'''


def serve(db, port):
    class Handler(http.server.BaseHTTPRequestHandler):
        def send(self, status, payload, content_type='application/json'):
            body = payload.encode() if isinstance(payload,str) else json.dumps(payload).encode()
            self.send_response(status)
            self.send_header('Content-Type',content_type)
            self.send_header('Content-Length',str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path=='/':
                self.send(200,PAGE,'text/html; charset=utf-8')
            elif self.path=='/state':
                self.send(200,snapshot(db))
            else:
                self.send(404,{'error':'unknown route'})

        def do_POST(self):
            if self.path!='/reserve':
                self.send(404,{'error':'unknown route'})
                return
            self.connection.settimeout(5)
            try:
                size = int(self.headers.get('Content-Length','0'))
                if not 0 < size <= 4096:
                    raise ValueError('request body must contain 1–4096 bytes')
                data = json.loads(self.rfile.read(size))
                if not isinstance(data,dict):
                    raise ValueError('request body must be an object')
                result = reserve(db,data.get('key'),data.get('quantity'))
                print(json.dumps({'stage':'transaction committed','request_key':result['key'],'status':result['status']}),flush=True)
                self.send(200 if result['status']=='reserved' else 409,result)
            except (ValueError,UnicodeError) as error:
                self.send(400,{'error':str(error)})
            except sqlite3.Error:
                self.send(503,{'error':'database unavailable; inspect terminal and retry the same key'})

    with http.server.ThreadingHTTPServer(('127.0.0.1',port),Handler) as server:
        print(f'Open http://127.0.0.1:{server.server_port}/ — Ctrl-C stops and removes temporary data.',flush=True)
        server.serve_forever()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serve',action='store_true')
    parser.add_argument('--port',type=int,default=8765)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='architect-lab-') as folder:
        directory = pathlib.Path(folder)
        if args.serve:
            db = directory/'browser.db'
            initialise(db)
            try:
                serve(db,args.port)
            except KeyboardInterrupt:
                pass
        else:
            print(json.dumps(experiments(directory),indent=2))


if __name__ == '__main__':
    main()
