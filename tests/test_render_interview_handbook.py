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


    def test_page_mode_links_to_sibling_html_pages(self):
        documents = {"roles/product-owner.md": "product-owner", "shared/evidence-bank.md": "evidence", "README.md": "start"}
        result = renderer.render_markdown(
            "[Story](../shared/evidence-bank.md#s3-smart-timesheet) [Home](../README.md) [Own](#plan) [Repo](../../docs/method.md)",
            "roles/product-owner.md", documents, page=True)
        self.assertIn('href="../shared/evidence-bank.html#s3-smart-timesheet"', result)
        self.assertIn('href="../index.html"', result)
        self.assertIn('href="#plan"', result)
        self.assertIn('href="../../docs/method.md"', result)

    def test_page_mode_wraps_questions_for_practice(self):
        documents = {"roles/ai-engineer.md": "ai-engineer"}
        result = renderer.render_markdown(
            "## Bank\n\n### Q1. Why?\n\n**Model answer:** Because.\n\n## Next\n\n1. **How do you plan?** Carefully.",
            "roles/ai-engineer.md", documents, page=True)
        self.assertIn('<div class="qa" data-qa="q1-why">', result)
        self.assertIn('<h3 id="q1-why">', result)
        self.assertIn('<div class="qa-body">', result)
        self.assertIn('</div></div>\n<h2 id="next">', result)
        self.assertIn('<li class="qa-li"><strong>How do you plan?</strong> <span class="qa-ans">Carefully.</span></li>', result)

    def test_every_source_has_a_page(self):
        pages = renderer.build_pages()
        self.assertEqual(len(pages), len(renderer.SOURCES) + 1)
        self.assertIn("index.html", pages)
        self.assertIn("roles/ai-engineer.html", pages)
        self.assertIn("dot-drill.html", pages)

    def test_drill_reads_grid_prompts_and_roles_from_the_method_page(self):
        data = renderer.drill_data()
        self.assertEqual(len(data["prompts"]), len(data["lenses"]))
        self.assertTrue(all(len(s["values"]) == len(data["lenses"]) for s in data["stories"]))
        self.assertTrue(any(s["personal"] for s in data["stories"]))
        self.assertTrue(any(r["technical"] for r in data["roles"]))
        page = renderer.build_pages()["dot-drill.html"]
        self.assertIn('id="drill" hidden', page)
        self.assertIn('id="without-the-interactive-drill"', page)


if __name__ == '__main__':
    unittest.main()
