from html.parser import HTMLParser
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbooks" / "ai-engineering" / "ai-engineering-handbook-v3.1.html"


class TabSemanticsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tablist_count = 0
        self.tabs = []
        self.panels = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("role") == "tablist":
            self.tablist_count += 1
        if tag == "button" and attributes.get("role") == "tab":
            self.tabs.append(attributes)
        if tag == "section" and attributes.get("role") == "tabpanel":
            self.panels.append(attributes)


class AIEngineeringHandbookTests(unittest.TestCase):
    def test_tabs_expose_accessible_relationships_and_state(self):
        parser = TabSemanticsParser()
        parser.feed(HANDBOOK.read_text(encoding="utf-8"))

        self.assertEqual(parser.tablist_count, 1)
        self.assertEqual(len(parser.tabs), len(parser.panels))
        self.assertGreater(len(parser.tabs), 1)

        tabs_by_id = {tab.get("id"): tab for tab in parser.tabs}
        panels_by_id = {panel.get("id"): panel for panel in parser.panels}
        self.assertNotIn(None, tabs_by_id)
        self.assertNotIn(None, panels_by_id)
        self.assertEqual(len(tabs_by_id), len(parser.tabs))
        self.assertEqual(len(panels_by_id), len(parser.panels))

        selected = []
        visible = []
        for tab_id, tab in tabs_by_id.items():
            panel_id = tab.get("aria-controls")
            self.assertIn(tab.get("aria-selected"), {"true", "false"})
            self.assertIn(tab.get("tabindex"), {"0", "-1"})
            self.assertIn(panel_id, panels_by_id)
            panel = panels_by_id[panel_id]
            self.assertEqual(panel.get("aria-labelledby"), tab_id)
            self.assertIn(panel.get("aria-hidden"), {"true", "false"})
            if tab["aria-selected"] == "true":
                selected.append(tab_id)
                self.assertEqual(tab["tabindex"], "0")
            if panel["aria-hidden"] == "false":
                visible.append(panel_id)

        self.assertEqual(len(selected), 1)
        self.assertEqual(visible, [tabs_by_id[selected[0]]["aria-controls"]])


if __name__ == "__main__":
    unittest.main()
