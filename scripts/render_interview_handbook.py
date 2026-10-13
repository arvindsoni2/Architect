"""Generate dependency-free HTML from the collection's Markdown subset.

Writes the tabbed all-in-one reading view (handbook.html) and one standalone page
per guide (README.md becomes index.html; every other .md gets a sibling .html).

Supports headings, paragraphs, flat lists, tables, quotes, bold, code and links.
Raw HTML is escaped. This is a scoped publication tool, not a general Markdown parser.
"""
import argparse
import html
import posixpath
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('README.md', 'start', 'Start here'),
    ('shared/handbook.md', 'methods', 'Shared methods'),
    ('shared/evidence-bank.md', 'evidence', 'Evidence bank'),
    ('roles/delivery-lead.md', 'delivery-lead', 'Delivery Lead'),
    ('roles/agile-delivery-lead.md', 'agile-delivery-lead', 'Agile Delivery Lead'),
    ('roles/product-owner.md', 'product-owner', 'Product Owner'),
    ('roles/product-manager.md', 'product-manager', 'Product Manager'),
    ('roles/senior-project-manager.md', 'senior-project-manager', 'Senior Project Manager'),
    ('roles/software-ai-architect.md', 'software-ai-architect', 'Software & AI Architect'),
    ('roles/ai-engineer.md', 'ai-engineer', 'AI Engineer'),
    ('roles/forward-deployed-engineer.md', 'forward-deployed-engineer', 'Forward Deployed Engineer'),
    ('vacancies/accenture-product-owner.md', 'accenture', 'Accenture PO playbook'),
    ('vacancies/accenture-product-owner-questions.md', 'accenture-questions', 'Accenture extra Qs'),
    ('vacancies/accenture-fde.md', 'accenture-fde', 'Accenture FDE'),
]


def slug(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return text.replace(' ', '-').strip()


def page_path(source):
    """Standalone page written for a Markdown source (README becomes the index)."""
    return 'index.html' if source == 'README.md' else source[:-3] + '.html'


def resolve_link(target, source, documents, page=False):
    parsed = urlsplit(target)
    if parsed.scheme:
        return target if parsed.scheme in ('https', 'http') else None
    if parsed.netloc:
        return None
    path = posixpath.normpath(posixpath.join(posixpath.dirname(source), parsed.path)) if parsed.path else source
    fragment = '#' + parsed.fragment if parsed.fragment else ''
    if page:
        rel = lambda p: posixpath.relpath(p, posixpath.dirname(source) or '.')
        if path in documents:
            return (fragment or '#') if path == source else rel(page_path(path)) + fragment
        return rel(path) + ('?' + parsed.query if parsed.query else '') + fragment
    if path in documents:
        return '#' + documents[path] + ('--' + parsed.fragment if parsed.fragment else '')
    if path == 'handbook.html':
        return '#start'
    return path + ('?' + parsed.query if parsed.query else '') + fragment


def inline(text, source, documents, page=False):
    tokens = re.compile(r'\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*')
    result, end = [], 0
    for match in tokens.finditer(text):
        result.append(html.escape(text[end:match.start()]))
        label, target, code, bold = match.groups()
        if target is not None:
            href = resolve_link(target, source, documents, page)
            safe_label = html.escape(label)
            result.append(f'<a href="{html.escape(href, quote=True)}">{safe_label}</a>' if href else safe_label)
        elif code is not None:
            result.append('<code>' + html.escape(code) + '</code>')
        else:
            result.append('<strong>' + html.escape(bold) + '</strong>')
        end = match.end()
    result.append(html.escape(text[end:]))
    return ''.join(result)


def render_markdown(content, source, documents, page=False):
    lines = content.splitlines()
    prefix, output, seen, index = documents[source], [], {}, 0
    fmt = lambda text: inline(text, source, documents, page)
    open_qa = False
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        heading = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading:
            level, title = len(heading[1]), heading[2]
            base = slug(title)
            count = seen.get(base, 0)
            seen[base] = count + 1
            anchor = base + (f'-{count}' if count else '')
            if page and open_qa and level <= 3:
                output.append('</div></div>')
                open_qa = False
            is_question = page and level == 3 and re.match(r'^Q\d+\.\s', title)
            if is_question:
                output.append(f'<div class="qa" data-qa="{anchor}">')
            element_id = anchor if page else f'{prefix}--{anchor}'
            output.append(f'<h{level} id="{element_id}">{fmt(title)}</h{level}>')
            if is_question:
                output.append('<div class="qa-body">')
                open_qa = True
            index += 1
        elif line.startswith('|') and index + 1 < len(lines) and re.match(r'^\|[\s:|\-]+\|$', lines[index + 1]):
            cells = lambda row: [cell.strip() for cell in row.strip().strip('|').split('|')]
            output.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th>' + fmt(c) + '</th>' for c in cells(line)) + '</tr></thead><tbody>')
            index += 2
            while index < len(lines) and lines[index].startswith('|'):
                output.append('<tr>' + ''.join('<td>' + fmt(c) + '</td>' for c in cells(lines[index])) + '</tr>')
                index += 1
            output.append('</tbody></table></div>')
        elif re.match(r'^(?:- |\d+\. )', line):
            ordered = bool(re.match(r'^\d+\. ', line))
            pattern = r'^\d+\. (.*)$' if ordered else r'^- (.*)$'
            tag = 'ol' if ordered else 'ul'
            output.append('<' + tag + '>')
            while index < len(lines) and (item := re.match(pattern, lines[index])):
                question = re.match(r'^\*\*([^*]+\?)\*\*\s+(.+)$', item[1]) if page else None
                if question:
                    output.append('<li class="qa-li"><strong>' + html.escape(question[1]) + '</strong> <span class="qa-ans">' + fmt(question[2]) + '</span></li>')
                else:
                    output.append('<li>' + fmt(item[1]) + '</li>')
                index += 1
            output.append('</' + tag + '>')
        elif line.startswith('> '):
            output.append('<blockquote>' + fmt(line[2:]) + '</blockquote>')
            index += 1
        else:
            paragraph = [line.strip()]
            index += 1
            while index < len(lines) and lines[index].strip() and not re.match(r'^(?:#|\||> |\d+\. |- )', lines[index]):
                paragraph.append(lines[index].strip())
                index += 1
            output.append('<p>' + fmt(' '.join(paragraph)) + '</p>')
    if open_qa:
        output.append('</div></div>')
    return '\n'.join(output)


STYLE = """
:root{color-scheme:light;--bg:#f3f5f9;--paper:#fff;--ink:#19293a;--muted:#536679;--line:#d5deea;--accent:#2257a5;--soft:#edf3fc}
html.dark{color-scheme:dark;--bg:#111b28;--paper:#192638;--ink:#eaf0f7;--muted:#b4c3d5;--line:#354960;--accent:#9cc3ff;--soft:#233752}
*{box-sizing:border-box}html{scroll-padding-top:24px}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 system-ui,-apple-system,sans-serif}
a{color:var(--accent);text-underline-offset:3px}a:focus-visible,button:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:10px;background:var(--paper);padding:8px;z-index:2}
header{background:var(--paper);border-bottom:1px solid var(--line);padding:22px max(24px,calc((100vw - 1300px)/2))}
.heading-row{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand{font-size:23px;font-weight:750;letter-spacing:-.4px}.subtitle{color:var(--muted);margin:3px 0 0;font-size:14px}
button{font:inherit;border:1px solid var(--line);border-radius:8px;padding:7px 12px;color:var(--ink);background:var(--paper);cursor:pointer}
.layout{display:grid;grid-template-columns:240px minmax(0,1fr);gap:30px;max-width:1300px;margin:28px auto;padding:0 24px}
nav{align-self:start;position:sticky;top:24px}nav a{display:block;padding:10px 13px;margin:3px 0;border-radius:8px;text-decoration:none;color:var(--muted);font-size:15px}nav a.active{color:var(--accent);background:var(--soft);font-weight:700}
.nav-label{text-transform:uppercase;font-size:11px;font-weight:750;letter-spacing:1.3px;color:var(--muted);margin:15px 13px 5px}
main{min-width:0}.panel{background:var(--paper);padding:32px 40px;border:1px solid var(--line);border-radius:14px;margin-bottom:28px}
h1{font-size:32px;line-height:1.2;letter-spacing:-.7px;margin:0 0 24px}h2{font-size:23px;line-height:1.35;margin:36px 0 12px}h3{font-size:19px}p{margin:14px 0}li{padding-left:3px;margin:10px 0}strong{font-weight:700}
.table-wrap{overflow-x:auto;margin:20px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.5}th,td{border:1px solid var(--line);padding:12px;text-align:left;vertical-align:top}th{background:var(--soft)}code{font-size:.86em;background:var(--soft);padding:2px 5px;border-radius:4px;overflow-wrap:anywhere}
blockquote{margin:20px 0;padding:10px 18px;border-left:4px solid var(--accent);background:var(--soft)}footer{font-size:13px;color:var(--muted);margin:24px 0}.enhanced .panel[hidden]{display:none}
@media(max-width:850px){.layout{display:block;margin:16px auto;padding:0 14px}nav{position:static;display:flex;overflow:auto;gap:3px;margin:0 0 16px;padding-bottom:8px}nav a{white-space:nowrap;padding:9px 12px;border:1px solid var(--line)}.nav-label{display:none}.panel{padding:25px 20px}header{padding:18px 20px}h1{font-size:27px}body{font-size:16px}}
@media print{header,nav,footer,.skip{display:none}.layout{display:block;margin:0;padding:0}.panel,.enhanced .panel[hidden]{display:block!important;border:0;padding:0;margin:0;break-before:page}.panel:first-child{break-before:auto}body{background:#fff;color:#111;font-size:10pt}h1{font-size:20pt}h2{font-size:15pt;break-after:avoid}table{font-size:9pt}tr{break-inside:avoid}a{color:#111}html.dark{--paper:#fff;--ink:#111;--line:#ccc;--soft:#f4f4f4;--muted:#444}}
"""

SCRIPT = """
const panels=[...document.querySelectorAll('.panel')];
const links=[...document.querySelectorAll('nav a')];
function selectPanel(){
  const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));
  const chosen=(target?.closest('.panel'))||(target?.id==='content'?panels.find(panel=>!panel.hidden):null)||panels[0];
  panels.forEach(panel=>panel.hidden=panel!==chosen);
  links.forEach(link=>{const active=link.hash==='#'+chosen.id;link.classList.toggle('active',active);if(active)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');});
  if(target&&target!==chosen)target.scrollIntoView();
  else window.scrollTo(0,0);
}
document.documentElement.classList.add('enhanced');
window.addEventListener('hashchange',selectPanel);selectPanel();
const theme=document.getElementById('theme');
theme.addEventListener('click',()=>{const dark=document.documentElement.classList.toggle('dark');theme.setAttribute('aria-pressed',String(dark));theme.textContent=dark?'Light view':'Dark view';});
"""


PAGE_STYLE = """
:root{color-scheme:light;--bg:#f3f5f9;--paper:#fff;--ink:#19293a;--muted:#536679;--line:#d5deea;--accent:#2257a5;--soft:#edf3fc;--ok:#1f7a4d}
html.dark{color-scheme:dark;--bg:#111b28;--paper:#192638;--ink:#eaf0f7;--muted:#b4c3d5;--line:#354960;--accent:#9cc3ff;--soft:#233752;--ok:#6fd3a0}
*{box-sizing:border-box}html{scroll-padding-top:16px}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--accent);text-underline-offset:3px}a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:10px;background:var(--paper);padding:8px;z-index:2}
header{background:var(--paper);border-bottom:1px solid var(--line);padding:16px max(20px,calc((100vw - 1300px)/2))}
.heading-row{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}.brand{font-size:20px;font-weight:750;letter-spacing:-.3px;color:var(--ink);text-decoration:none}.subtitle{color:var(--muted);margin:2px 0 0;font-size:14px}
.tools{display:flex;gap:8px;flex-wrap:wrap}
button{font:inherit;font-size:15px;border:1px solid var(--line);border-radius:8px;padding:7px 12px;color:var(--ink);background:var(--paper);cursor:pointer}button[aria-pressed=true]{background:var(--accent);border-color:var(--accent);color:var(--paper)}
.layout{display:grid;grid-template-columns:230px minmax(0,1fr);gap:28px;max-width:1300px;margin:24px auto;padding:0 20px}
nav{align-self:start;position:sticky;top:16px;max-height:calc(100vh - 32px);overflow:auto}nav a{display:block;padding:8px 12px;margin:2px 0;border-radius:8px;text-decoration:none;color:var(--muted);font-size:15px}nav a[aria-current=page]{color:var(--accent);background:var(--soft);font-weight:700}
.nav-label{text-transform:uppercase;font-size:11px;font-weight:750;letter-spacing:1.3px;color:var(--muted);margin:14px 12px 4px}
main{min-width:0}.panel{background:var(--paper);padding:30px 38px;border:1px solid var(--line);border-radius:14px}
h1{font-size:31px;line-height:1.2;letter-spacing:-.6px;margin:0 0 20px}h2{font-size:23px;line-height:1.35;margin:36px 0 12px}h3{font-size:19px;line-height:1.4;margin:26px 0 8px}p{margin:12px 0}li{padding-left:3px;margin:10px 0}strong{font-weight:700}
.table-wrap{overflow-x:auto;margin:18px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.5}th,td{border:1px solid var(--line);padding:11px;text-align:left;vertical-align:top}th{background:var(--soft)}code{font-size:.86em;background:var(--soft);padding:2px 5px;border-radius:4px;overflow-wrap:anywhere}
blockquote{margin:18px 0;padding:10px 18px;border-left:4px solid var(--accent);background:var(--soft)}
.toc{border:1px solid var(--line);border-radius:10px;padding:8px 16px;margin:0 0 20px;background:var(--soft)}.toc summary{cursor:pointer;font-weight:700}.toc ol{margin:8px 0;padding-left:22px;columns:2;column-gap:28px}.toc li{margin:4px 0;font-size:15px;break-inside:avoid}
.practice-bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:0 0 20px;font-size:15px}
.meter{flex:1 1 160px;height:10px;border:1px solid var(--line);border-radius:6px;background:var(--paper);overflow:hidden}.meter span{display:block;height:100%;width:0;background:var(--ok)}
.qa{border-top:1px solid var(--line);padding-top:4px}.qa-tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:2px 0 6px;font-size:14px}.qa-tools button{font-size:14px;padding:4px 10px}
.qa-tools label{display:inline-flex;gap:6px;align-items:center;color:var(--muted);cursor:pointer}.qa-tools input{width:17px;height:17px;accent-color:var(--ok)}
.qa.practised h3::after{content:" ✓";color:var(--ok)}
.reveal-btn{display:none}.practice .reveal-btn{display:inline-block}
.practice .qa:not(.revealed) .qa-body,.practice .qa-li:not(.revealed) .qa-ans{display:none}
.qa-li .reveal-btn{margin-left:8px;font-size:13px;padding:2px 8px}
footer{font-size:13px;color:var(--muted);margin:20px 0}
@media(max-width:850px){.layout{display:block;margin:14px auto;padding:0 14px}nav{position:static;max-height:none;display:flex;overflow-x:auto;gap:4px;margin:0 0 14px;padding-bottom:8px}nav a{white-space:nowrap;padding:8px 11px;border:1px solid var(--line)}.nav-label{display:none}.panel{padding:22px 18px}header{padding:14px 16px}h1{font-size:26px}body{font-size:16px}.toc ol{columns:1}}
@media print{header,nav,footer,.skip,.toc,.practice-bar,.qa-tools,.reveal-btn{display:none!important}.layout{display:block;margin:0;padding:0}.panel{border:0;padding:0}.qa-body,.qa-ans{display:block!important}.qa-ans{display:inline!important}body{background:#fff;color:#111;font-size:10.5pt}h1{font-size:20pt}h2{font-size:15pt;break-after:avoid}h3{break-after:avoid}table{font-size:9pt}tr{break-inside:avoid}a{color:#111}html.dark{--paper:#fff;--ink:#111;--line:#ccc;--soft:#f4f4f4;--muted:#444}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important}}
"""

PAGE_SCRIPT = """
(function(){
var root=document.documentElement,store=null;
try{store=window.localStorage;store.getItem('ip-probe');}catch(e){store=null;}
function get(k){try{return store?store.getItem(k):null;}catch(e){return null;}}
function set(k,v){try{if(store)store.setItem(k,v);}catch(e){}}
var toc=document.querySelector('.toc');if(toc&&window.matchMedia&&window.matchMedia('(max-width:850px)').matches)toc.open=false;
var theme=document.getElementById('theme'),printBtn=document.getElementById('print'),practiceBtn=document.getElementById('practice');
theme.hidden=false;printBtn.hidden=false;
if(get('ip-theme')==='dark')root.classList.add('dark');
function syncTheme(){var d=root.classList.contains('dark');theme.setAttribute('aria-pressed',String(d));theme.textContent=d?'Light view':'Dark view';}
syncTheme();
theme.addEventListener('click',function(){root.classList.toggle('dark');set('ip-theme',root.classList.contains('dark')?'dark':'light');syncTheme();});
printBtn.addEventListener('click',function(){window.print();});
var qas=[].slice.call(document.querySelectorAll('.qa')),lis=[].slice.call(document.querySelectorAll('.qa-li'));
if(!qas.length&&!lis.length)return;
practiceBtn.hidden=false;
var page=document.body.getAttribute('data-page'),key='ip-practised:'+page,done={};
try{done=JSON.parse(get(key)||'{}')||{};}catch(e){done={};}
var bar=document.getElementById('practice-bar'),count=document.getElementById('practised-count'),meter=document.getElementById('practised-meter');
var speech=('speechSynthesis' in window)?window.speechSynthesis:null,speaking=null;
function progress(){if(!qas.length){bar.hidden=true;return;}bar.hidden=false;var n=qas.filter(function(q){return done[q.getAttribute('data-qa')];}).length;
 count.textContent=n+' of '+qas.length+' questions practised';meter.style.width=Math.round(100*n/qas.length)+'%';}
function revealButton(target,label){var b=document.createElement('button');b.type='button';b.className='reveal-btn';b.textContent=label;b.setAttribute('aria-expanded','false');
 b.addEventListener('click',function(){var open=target.classList.toggle('revealed');b.setAttribute('aria-expanded',String(open));b.textContent=open?'Hide answer':label;});return b;}
qas.forEach(function(q){var id=q.getAttribute('data-qa'),h=q.querySelector('h3'),tools=document.createElement('div');tools.className='qa-tools';
 tools.appendChild(revealButton(q,'Show model answer'));
 if(speech){var l=document.createElement('button');l.type='button';l.textContent='▶ Listen';l.setAttribute('aria-label','Read this question and model answer aloud');
  l.addEventListener('click',function(){if(speaking===l){speech.cancel();return;}speech.cancel();
   var u=new SpeechSynthesisUtterance((h.textContent+'. '+q.querySelector('.qa-body').textContent).replace(/\\s+/g,' '));u.lang='en-GB';u.rate=0.95;
   speaking=l;l.textContent='■ Stop';u.onend=u.onerror=function(){if(speaking===l){speaking=null;}l.textContent='▶ Listen';};speech.speak(u);});tools.appendChild(l);}
 var lab=document.createElement('label'),box=document.createElement('input');box.type='checkbox';box.checked=!!done[id];q.classList.toggle('practised',box.checked);
 box.addEventListener('change',function(){if(box.checked)done[id]=1;else delete done[id];q.classList.toggle('practised',box.checked);set(key,JSON.stringify(done));progress();});
 lab.appendChild(box);lab.appendChild(document.createTextNode(' Practised'));tools.appendChild(lab);
 h.insertAdjacentElement('afterend',tools);});
lis.forEach(function(li){li.querySelector('strong').insertAdjacentElement('afterend',revealButton(li,'Show'));});
practiceBtn.addEventListener('click',function(){var on=document.body.classList.toggle('practice');practiceBtn.setAttribute('aria-pressed',String(on));
 if(on){qas.concat(lis).forEach(function(x){x.classList.remove('revealed');var b=x.querySelector('.reveal-btn');if(b){b.setAttribute('aria-expanded','false');b.textContent=x.classList.contains('qa')?'Show model answer':'Show';}});}});
document.getElementById('practice-reset').addEventListener('click',function(){done={};set(key,'{}');qas.forEach(function(q){q.classList.remove('practised');var c=q.querySelector('.qa-tools input');if(c)c.checked=false;});progress();});
progress();
})();
"""

NAV_GROUPS = [('Start', ('README.md', 'shared/')), ('Role guides', ('roles/',)), ('Vacancies', ('vacancies/',))]


def build_page(source, documents, titles):
    here = posixpath.dirname(page_path(source)) or '.'
    rel = lambda p: posixpath.relpath(p, here)
    content = (ROOT / 'interview-prep' / source).read_text(encoding='utf-8')
    body = render_markdown(content, source, documents, page=True)
    nav = []
    for label, prefixes in NAV_GROUPS:
        nav.append(f'<div class="nav-label">{label}</div>')
        for path, _, title in SOURCES:
            if path.startswith(prefixes) or path in prefixes:
                current = ' aria-current="page"' if path == source else ''
                nav.append(f'<a href="{html.escape(rel(page_path(path)), quote=True)}"{current}>{html.escape(title)}</a>')
    nav.append('<div class="nav-label">All in one</div>')
    nav.append(f'<a href="{html.escape(rel("handbook.html"), quote=True)}">Tabbed reading view</a>')
    headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc = ''
    if len(headings) > 2:
        toc = '<details class="toc" open><summary>On this page</summary><ol>' + ''.join(
            f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in headings) + '</ol></details>'
    practice = ('<div class="practice-bar" id="practice-bar" hidden><span id="practised-count"></span>'
                '<div class="meter" aria-hidden="true"><span id="practised-meter"></span></div>'
                '<button type="button" id="practice-reset">Reset ticks</button></div>')
    title = titles[source]
    source_link = html.escape(posixpath.basename(source), quote=True)
    return ('<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{html.escape(title)} — Interview preparation</title><style>{PAGE_STYLE}</style></head>'
            f'<body data-page="{html.escape(source, quote=True)}"><a class="skip" href="#content">Skip to content</a>'
            f'<header><div class="heading-row"><div><a class="brand" href="{html.escape(rel("index.html"), quote=True)}">Interview preparation</a>'
            '<p class="subtitle">Shared methods · consistent evidence · role-specific practice</p></div>'
            '<div class="tools"><button id="practice" type="button" aria-pressed="false" hidden title="Hide model answers so you can answer first">Practice mode</button>'
            '<button id="theme" type="button" aria-pressed="false" hidden>Dark view</button><button id="print" type="button" hidden>Print</button></div></div></header>'
            f'<div class="layout"><nav aria-label="Guides">{"".join(nav)}</nav><main id="content"><article class="panel">'
            f'{_after_intro(body, toc + practice)}</article>'
            f'<footer>Generated from <a href="{source_link}">{html.escape(posixpath.basename(source))}</a>. Edit the Markdown, then run '
            '<code>python3 scripts/render_interview_handbook.py</code>.</footer></main></div>'
            f'<script>{PAGE_SCRIPT}</script></body></html>\n')


def _after_intro(body, insert):
    """Place page tools after the title and its status line, not above the title."""
    end = body.find('</h1>')
    if end == -1:
        return insert + body
    end += len('</h1>')
    status = body.find('</p>', end)
    if status != -1 and body[end:status].lstrip().startswith('<p>'):
        end = status + len('</p>')
    return body[:end] + insert + body[end:]


def build_pages():
    documents = {path: section for path, section, _ in SOURCES}
    titles = {path: title for path, _, title in SOURCES}
    return {page_path(path): build_page(path, documents, titles) for path, _, _ in SOURCES}


def build():
    documents = {path: section for path, section, _ in SOURCES}
    navigation, panels = [], []
    for path, section, title in SOURCES:
        navigation.append(f'<a href="#{section}">{html.escape(title)}</a>')
        content = (ROOT / 'interview-prep' / path).read_text(encoding='utf-8')
        panels.append(f'<section class="panel" id="{section}" aria-label="{html.escape(title)}">' + render_markdown(content, path, documents) + '</section>')
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Product and Delivery Interview Handbook</title><style>' + STYLE + '</style></head><body><a class="skip" href="#content">Skip to content</a><header><div class="heading-row"><div><div class="brand">Interview preparation</div><p class="subtitle">Shared methods · consistent evidence · role-specific practice</p></div><button id="theme" type="button" aria-pressed="false">Dark view</button></div></header><div class="layout"><nav aria-label="Guide navigation"><div class="nav-label">Choose your route</div>' + ''.join(navigation) + '</nav><main id="content">' + '\n'.join(panels) + '<footer>Generated from canonical Markdown. Review status and dates appear in each guide. Print includes all guides.</footer></main></div><script>' + SCRIPT + '</script></body></html>\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the committed HTML needs regeneration')
    args = parser.parse_args()
    base = ROOT / 'interview-prep'
    outputs = {'handbook.html': build(), **build_pages()}
    if args.check:
        stale = [name for name, rendered in outputs.items()
                 if not (base / name).exists() or (base / name).read_text(encoding='utf-8') != rendered]
        if stale:
            parser.exit(1, 'Interview HTML is stale (' + ', '.join(stale) + '); run python3 scripts/render_interview_handbook.py\n')
        print(f'Interview reading view and {len(outputs) - 1} guide pages match Markdown sources.')
    else:
        for name, rendered in outputs.items():
            (base / name).write_text(rendered, encoding='utf-8')
        print(f'Generated interview-prep/handbook.html and {len(outputs) - 1} guide pages')


if __name__ == '__main__':
    main()
