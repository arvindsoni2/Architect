"""Reader-facing renderer contracts: safe text and working cross-guide navigation."""
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    "interview_renderer", Path(__file__).resolve().parents[1] / "scripts/render_interview_handbook.py"
)
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class RenderTests(unittest.TestCase):
    def render(self, content):
        return renderer.render_markdown(
            content, "roles/product-owner.md",
            {"roles/product-owner.md": "product-owner", "shared/evidence-bank.md": "evidence"},
        )

    def test_cross_document_fragment_reaches_embedded_evidence(self):
        result = self.render("[Story](../shared/evidence-bank.md#s3-smart-timesheet)")
        self.assertIn('href="#evidence--s3-smart-timesheet"', result)

    def test_raw_html_and_unsafe_link_are_inert(self):
        result = self.render('<script>alert(1)</script> [bad](javascript:alert)')
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', result)
        self.assertNotIn('<script>', result)
        self.assertNotIn('href="javascript:', result)

    def test_repeated_headings_have_unique_fragment_targets(self):
        result = self.render('## Plan\n\nFirst\n\n## Plan\n\nSecond')
        self.assertIn('id="product-owner--plan"', result)
        self.assertIn('id="product-owner--plan-1"', result)

    def test_external_and_repository_links_remain_usable(self):
        result = self.render('[Docs](https://example.org/a) [Architecture](../../docs/method.md)')
        self.assertIn('href="https://example.org/a"', result)
        self.assertIn('href="../docs/method.md"', result)

    def test_tables_and_ordered_answers_preserve_structure(self):
        result = self.render('| Role | Focus |\n| --- | --- |\n| PO | **Value** |\n\n1. Discover\n2. Deliver')
        self.assertIn('<th>Role</th>', result)
        self.assertIn('<td><strong>Value</strong></td>', result)
        self.assertIn('<ol>', result)
        self.assertIn('<li>Discover</li>', result)


if __name__ == '__main__':
    unittest.main()
