"""Generate a dependency-free reading view from the collection's Markdown subset.

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
    ('vacancies/accenture-product-owner.md', 'accenture', 'Accenture PO'),
    ('vacancies/accenture-product-owner-questions.md', 'accenture-questions', 'Accenture Q&A'),
    ('vacancies/accenture-fde.md', 'accenture-fde', 'Accenture FDE'),
]


def slug(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return text.replace(' ', '-').strip()


def resolve_link(target, source, documents):
    parsed = urlsplit(target)
    if parsed.scheme:
        return target if parsed.scheme in ('https', 'http') else None
    if parsed.netloc:
        return None
    path = posixpath.normpath(posixpath.join(posixpath.dirname(source), parsed.path)) if parsed.path else source
    if path in documents:
        return '#' + documents[path] + ('--' + parsed.fragment if parsed.fragment else '')
    if path == 'handbook.html':
        return '#start'
    return path + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')


def inline(text, source, documents):
    tokens = re.compile(r'\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*([^*]+)\*\*')
    result, end = [], 0
    for match in tokens.finditer(text):
        result.append(html.escape(text[end:match.start()]))
        label, target, code, bold = match.groups()
        if target is not None:
            href = resolve_link(target, source, documents)
            safe_label = html.escape(label)
            result.append(f'<a href="{html.escape(href, quote=True)}">{safe_label}</a>' if href else safe_label)
        elif code is not None:
            result.append('<code>' + html.escape(code) + '</code>')
        else:
            result.append('<strong>' + html.escape(bold) + '</strong>')
        end = match.end()
    result.append(html.escape(text[end:]))
    return ''.join(result)


def render_markdown(content, source, documents):
    lines = content.splitlines()
    prefix, output, seen, index = documents[source], [], {}, 0
    fmt = lambda text: inline(text, source, documents)
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
            output.append(f'<h{level} id="{prefix}--{anchor}">{fmt(title)}</h{level}>')
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
    parser.add_argument('--check', action='store_true', help='Fail if the committed reading view needs regeneration')
    args = parser.parse_args()
    target = ROOT / 'interview-prep/handbook.html'
    rendered = build()
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8') != rendered:
            parser.exit(1, 'Interview reading view is stale; run python3 scripts/render_interview_handbook.py\n')
        print('Interview reading view matches Markdown sources.')
    else:
        target.write_text(rendered, encoding='utf-8')
        print('Generated interview-prep/handbook.html')


if __name__ == '__main__':
    main()
