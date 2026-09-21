"""Offline regression checks; no AWS requests and no deployment claims."""
import json
import pathlib
import re
import subprocess
import sys
import types
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
manual_arg = next((arg for arg in sys.argv[1:] if arg.lower().endswith('.html')), None)
if manual_arg:
    sys.argv.remove(manual_arg)
MANUAL = pathlib.Path(manual_arg) if manual_arg else ROOT.parent / 'saa-c03-lab-manual-v2.1.html'
DATA = json.loads(subprocess.check_output(['node', str(ROOT / 'extract.cjs'), str(MANUAL)]))
APPS = {a['id']: a for a in DATA['APPS']}
HTML = MANUAL.read_text(encoding='utf-8')

def css_vars(block):
    return dict(re.findall(r'--([\w-]+)\s*:\s*(#[0-9A-Fa-f]{3,6})',block))

def luminance(colour):
    value=colour.lstrip('#')
    if len(value)==3: value=''.join(c*2 for c in value)
    channels=[int(value[i:i+2],16)/255 for i in (0,2,4)]
    channels=[x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4 for x in channels]
    return 0.2126*channels[0]+0.7152*channels[1]+0.0722*channels[2]

def contrast(a,b):
    high,low=sorted((luminance(a),luminance(b)),reverse=True)
    return (high+0.05)/(low+0.05)

def snippet(lab, title):
    return next(s['c'] for s in APPS[lab]['snippets'] if s['t'] == title)

class Tests(unittest.TestCase):
    def test_light_theme_accent_text_meets_wcag_aa(self):
        root=css_vars(re.search(r':root\{([^}]*)\}',HTML,re.S).group(1))
        self.assertGreaterEqual(contrast(root['amber'],root['bg']),4.5)
        self.assertGreaterEqual(contrast(root['amber'],root['panel']),4.5)

    def test_print_palette_keeps_diagram_categories_distinct(self):
        match=re.search(r'@media print \{ :root,\[data-theme="dark"\]\{([^}]*)\}',HTML,re.S)
        self.assertIsNotNone(match)
        palette=css_vars(match.group(1))
        for name in ('user','edge','compute','db','storage','integration','security','ops','ai','analytics'):
            with self.subTest(category=name):
                colour=palette.get('type-'+name)
                self.assertIsNotNone(colour,'Print mode must define every diagram category colour')
                self.assertGreaterEqual(contrast(colour,'#FFFFFF'),3.0)

    def test_theme_helpers_default_safely_and_toggle_both_ways(self):
        self.assertEqual(DATA['themeChecks'],['dark','light','light','dark','light'])

    def test_progress_import_rejects_unknown_or_invalid_records(self):
        checks=DATA['progressChecks']
        self.assertIsNotNone(checks,'Progress must be portable through validated import/export')
        self.assertEqual([x['ok'] for x in checks],[True,False,False,False,False])
        self.assertEqual(checks[0]['value']['l1']['actual'],2.5)

    def test_redirect_rejects_expired_item_before_async_cleanup(self):
        class Table:
            def get_item(self,**kw): return {'Item':{'url':'https://example.com','ttl':1}}
            def update_item(self,**kw): raise AssertionError('Expired item must not be counted or redirected')
        fake=types.SimpleNamespace(resource=lambda *_:types.SimpleNamespace(Table=lambda *_:Table()))
        with patch.dict(sys.modules,{'boto3':fake}), patch.dict('os.environ',{'TABLE':'fixture'}):
            ns={};exec(snippet('l2','redirect handler — handler.py'),ns)
            response=ns['handler']({'pathParameters':{'code':'old'}},None)
        self.assertEqual(response['statusCode'],410)
        self.assertNotIn('Location',response.get('headers',{}))

    def test_presigned_upload_returns_json_string_body(self):
        fake=types.SimpleNamespace(client=lambda *_:types.SimpleNamespace(generate_presigned_url=lambda *a,**k:'https://example.com/upload'))
        with patch.dict(sys.modules,{'boto3':fake}),patch.dict('os.environ',{'BUCKET':'fixture'}):
            ns={};exec(snippet('l6','Mint a pre-signed upload URL'),ns)
            response=ns['handler']({},None)
        self.assertIsInstance(response['body'],str)
        self.assertEqual(json.loads(response['body'])['uploadUrl'],'https://example.com/upload')

    def test_zero_overlap_preserves_every_word(self):
        ns = {}
        exec(snippet('l10', 'Chunker worth stealing'), ns)
        try:
            chunks = ns['chunk']('one two\n\nthree four\n\nfive six', 'fixture', max_tokens=3, overlap=0)
        except TypeError as exc:
            self.fail(f'Zero overlap must not corrupt the size accumulator: {exc}')
        self.assertEqual(' '.join(c['text'] for c in chunks).split(), ['one','two','three','four','five','six'])
        self.assertTrue(all(len(c['text'].split()) <= 3 for c in chunks))

    def test_long_paragraph_respects_chunk_limit_and_overlap(self):
        ns = {}
        exec(snippet('l10', 'Chunker worth stealing'), ns)
        chunks = ns['chunk']('one two three four five six seven', 'fixture', max_tokens=3, overlap=1)
        self.assertEqual([c['text'] for c in chunks], ['one two three','three four five','five six seven'])

    def test_order_writes_marker_stock_and_outbox_atomically(self):
        # AWS boundary fake: fail before commit, then commit all three writes.
        # The assertion covers emitted transaction contents, not fake existence.
        class Cancelled(Exception): pass
        class DB:
            exceptions = types.SimpleNamespace(TransactionCanceledException=Cancelled, ConditionalCheckFailedException=Cancelled)
            def __init__(self): self.done=False; self.fail=True; self.requests=[]
            def put_item(self, **kw):
                if self.done: raise Cancelled()
                self.done=True
            def get_item(self, **kw): return {'Item': {'orderId': {'S':'o1'}}} if self.done else {}
            def transact_write_items(self, **kw):
                if self.fail: self.fail=False; raise RuntimeError('before atomic commit')
                if self.done: raise Cancelled()
                self.requests.append(kw['TransactItems']); self.done=True
        db=DB()
        def crash(*args): raise RuntimeError('after premature marker')
        ns={'ddb':db,'json':json,'log':types.SimpleNamespace(info=lambda *a,**k:None),'decrement_stock':crash,'publish_event':lambda *a:None}
        exec(snippet('l3','Idempotent consumer core'),ns)
        order={'orderId':'o1','sku':'sku1','qty':2}
        with self.assertRaises(RuntimeError): ns['handle'](order)
        ns['handle'](order)
        ns['handle'](order)
        self.assertEqual(len(db.requests),1,'Retry must commit unfinished work once, not skip it')
        tx=db.requests[0]
        self.assertEqual([next(iter(x.values()))['TableName'] for x in tx],['processed','inventory','outbox'])
        self.assertEqual(tx[1]['Update']['ExpressionAttributeValues'][':qty'],{'N':'2'})
        self.assertEqual(tx[2]['Put']['Item']['eventId'],{'S':'o1'})

    def test_all_diagram_nodes_fit_canvas(self):
        for app in APPS.values():
            d=app['diagram']
            for node in d['nodes']:
                with self.subTest(lab=app['id'],node=node['id']):
                    self.assertGreaterEqual(node['x'],0)
                    self.assertGreaterEqual(node['y'],0)
                    self.assertLessEqual(node['x']+150,d['w'])
                    self.assertLessEqual(node['y']+52,d['h'])

    def test_arrowheads_do_not_end_inside_destination_nodes(self):
        tag='{http://www.w3.org/2000/svg}'
        for app, svg in zip(DATA['APPS'],DATA['svgs']):
            lines=[x for x in ET.fromstring(svg).findall(tag+'line') if 'marker-end' in x.attrib]
            by_id={n['id']:n for n in app['diagram']['nodes']}
            self.assertEqual(len(lines),len(app['diagram']['edges']))
            for edge,line in zip(app['diagram']['edges'],lines):
                n=by_id[edge['t']]; x=float(line.attrib['x2']); y=float(line.attrib['y2'])
                with self.subTest(lab=app['id'],edge=edge):
                    self.assertFalse(n['x'] < x < n['x']+150 and n['y'] < y < n['y']+52,'Arrowhead hidden beneath destination')

    def test_diagram_edge_labels_use_readable_pills(self):
        tag='{http://www.w3.org/2000/svg}'
        labelled_edges=sum(1 for app in DATA['APPS'] for edge in app['diagram']['edges'] if edge.get('l'))
        labels=[]
        for svg in DATA['svgs']:
            root=ET.fromstring(svg)
            labels.extend(root.findall(f".//{tag}g[@class='edge-label']"))
        self.assertEqual(len(labels),labelled_edges)
        for label in labels:
            with self.subTest(label=''.join(label.itertext())):
                self.assertIsNotNone(label.find(tag+'rect'),'Every arrow label needs a background pill')
                self.assertIsNotNone(label.find(tag+'text'),'Every arrow label needs visible text')

    def test_diagram_edge_labels_do_not_cover_nodes(self):
        tag='{http://www.w3.org/2000/svg}'
        for app,svg in zip(DATA['APPS'],DATA['svgs']):
            labels=ET.fromstring(svg).findall(f".//{tag}g[@class='edge-label']")
            for label in labels:
                x=float(label.attrib['data-x']); y=float(label.attrib['data-y'])
                w=float(label.attrib['data-width']); h=float(label.attrib['data-height'])
                for node in app['diagram']['nodes']:
                    overlaps=not (
                        x+w <= node['x'] or node['x']+150 <= x or
                        y+h <= node['y'] or node['y']+52 <= y
                    )
                    with self.subTest(lab=app['id'],label=''.join(label.itertext()),node=node['id']):
                        self.assertFalse(overlaps,'Arrow label overlaps an architecture node')

    def test_invalid_explicit_label_position_falls_back_to_safe_placement(self):
        tag='{http://www.w3.org/2000/svg}'
        root=ET.fromstring(DATA['invalidExplicitSvg'])
        label=root.find(f".//{tag}g[@class='edge-label']")
        x=float(label.attrib['data-x']); y=float(label.attrib['data-y'])
        w=float(label.attrib['data-width']); h=float(label.attrib['data-height'])
        for node in DATA['APPS'][0]['diagram']['nodes']:
            overlaps=not (x+w<=node['x'] or node['x']+150<=x or y+h<=node['y'] or node['y']+52<=y)
            self.assertFalse(overlaps,'Invalid manual placement must not bypass collision checks')

    def test_diagram_text_uses_handbook_font_stack(self):
        tag='{http://www.w3.org/2000/svg}'
        for app,svg in zip(DATA['APPS'],DATA['svgs']):
            for text in ET.fromstring(svg).findall('.//'+tag+'text'):
                with self.subTest(lab=app['id'],text=''.join(text.itertext())):
                    family=text.attrib.get('font-family','')
                    self.assertNotIn('IBM Plex',family)
                    self.assertTrue(
                        family.startswith('Inter') or family.startswith('SFMono-Regular'),
                        f'Unexpected diagram font stack: {family}'
                    )

if __name__=='__main__': unittest.main()
