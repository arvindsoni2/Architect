import os
import pathlib
import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = pathlib.Path(os.environ.get('ARCHITECT_HTML', ROOT / 'software-architect-grooming-programme-v5.html')).read_text()


class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []

    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))


class HtmlTests(unittest.TestCase):
    def test_svg_marker_references_resolve(self):
        elements = Elements()
        elements.feed(HTML)
        ids = {attrs['id'] for _,attrs in elements.items if 'id' in attrs}
        for target in re.findall(r'url\(#([^)]*)\)',HTML):
            self.assertIn(target,ids,'Unresolved SVG reference removes arrowheads')

    def test_diagrams_are_valid_and_have_accessible_names(self):
        for svg in re.findall(r'<svg.*?</svg>',HTML,re.S):
            root = ET.fromstring(svg)
            self.assertTrue(root.get('aria-label'))

    def test_navigation_and_local_files_resolve(self):
        elements = Elements()
        elements.feed(HTML)
        ids = [attrs['id'] for _,attrs in elements.items if 'id' in attrs]
        self.assertEqual(len(ids),len(set(ids)),'Duplicate DOM IDs break navigation')
        for _,attrs in elements.items:
            for key in ['data-target','data-jump']:
                if key in attrs:
                    self.assertIn(attrs[key],ids)
            href=attrs.get('href','')
            if href and not re.match(r'^(https?:|mailto:|#)',href):
                self.assertTrue((ROOT/href.split('#')[0]).is_file(),href)


if __name__=='__main__':
    unittest.main()
