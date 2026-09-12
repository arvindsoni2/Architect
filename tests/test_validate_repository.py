import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate_repository import validate_repository


CATALOG_HEADER = """\
| Title | Domain | Path | Format | Status | Edition | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- |
"""


class RepositoryValidationTests(unittest.TestCase):
    def make_repository(self):
        temporary = tempfile.TemporaryDirectory()
        root = pathlib.Path(temporary.name)
        (root / "docs").mkdir()
        (root / "docs" / "architecture-note.md").write_text("# Note\n", encoding="utf-8")
        aws = root / "handbooks" / "aws-saa-c03"
        aws.mkdir(parents=True)
        (aws / "README.md").write_text("# AWS resources\n", encoding="utf-8")
        (aws / "saa-c03-visual-handbook-2026.09.html").write_text(
            "<!doctype html>\n", encoding="utf-8"
        )
        (aws / "saa-c03-lab-manual-v2.1.html").write_text(
            "<!doctype html>\n", encoding="utf-8"
        )
        catalog = (
            "# Content Catalogue\n\n"
            f"{CATALOG_HEADER}"
            "| Architecture Note | Software architecture | [docs/architecture-note.md](docs/architecture-note.md) | Markdown | Current | Living | 2026-09-08 |\n\n"
            "## Scoped AWS study-resource exception\n\n"
            f"{CATALOG_HEADER}"
            "| AWS SAA-C03 Visual Handbook | AWS solution architecture | [handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html](handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html) | HTML | Current | v1 | 2026-09-08 |\n"
            "| The $170 Cloud — SAA-C03 Lab Manual | AWS architecture practice | [handbooks/aws-saa-c03/saa-c03-lab-manual-v2.1.html](handbooks/aws-saa-c03/saa-c03-lab-manual-v2.1.html) | HTML | Current | v1 | 2026-09-08 |\n"
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")
        return temporary, root

    def test_accepts_valid_catalogue_and_local_links(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text("See [the catalogue](CATALOG.md).\n", encoding="utf-8")

        self.assertEqual(validate_repository(root), [])

    def test_reports_duplicate_catalogue_paths_and_missing_targets(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8")
        catalog = catalog.replace(
            "| Architecture Note | Software architecture | [docs/architecture-note.md](docs/architecture-note.md)",
            "| Architecture Note | Software architecture | [docs/missing.md](docs/missing.md)",
        ).replace(
            "handbooks/aws-saa-c03/saa-c03-lab-manual-v2.1.html](handbooks/aws-saa-c03/saa-c03-lab-manual-v2.1.html)",
            "handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html](handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html)",
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        errors = validate_repository(root)

        self.assertIn("catalogue path does not exist: docs/missing.md", errors)
        self.assertIn(
            "duplicate catalogue path: handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html",
            errors,
        )

    def test_normalizes_catalogue_paths_before_duplicate_detection(self):
        aliases = [
            "docs/./architecture-note.md",
            "docs/%61rchitecture-note.md",
            "docs/architecture-note-link.md",
        ]
        for alias in aliases:
            with self.subTest(alias=alias):
                temporary, root = self.make_repository()
                self.addCleanup(temporary.cleanup)
                if alias.endswith("-link.md"):
                    (root / alias).symlink_to(root / "docs" / "architecture-note.md")
                catalog = (root / "CATALOG.md").read_text(encoding="utf-8")
                extra = f"| Architecture Alias | Software architecture | [alias]({alias}) | Markdown | Current | Living | 2026-09-08 |\n\n"
                catalog = catalog.replace(
                    "\n## Scoped AWS study-resource exception", extra + "## Scoped AWS study-resource exception"
                )
                (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

                self.assertIn(
                    "duplicate catalogue path: docs/architecture-note.md",
                    validate_repository(root),
                )

    def test_requires_exact_canonical_paths_for_aws_resources(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8").replace(
            "saa-c03-visual-handbook-2026.09.html",
            "saa-c03-lab-manual-v2.1.html",
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        self.assertIn(
            "AWS SAA-C03 Visual Handbook must use handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html",
            validate_repository(root),
        )

    def test_rejects_aws_directory_entry_outside_scoped_section(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8")
        extra = "| AWS Supporting File | AWS architecture practice | [handbooks/aws-saa-c03/README.md](handbooks/aws-saa-c03/README.md) | Markdown | Current | Living | 2026-09-08 |\n\n"
        catalog = catalog.replace(
            "\n## Scoped AWS study-resource exception", extra + "## Scoped AWS study-resource exception"
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        self.assertIn(
            "AWS catalogue entry must be in the scoped exception: AWS Supporting File",
            validate_repository(root),
        )

    def test_reports_broken_relative_markdown_link(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text("See [missing](docs/missing.md).\n", encoding="utf-8")

        self.assertIn("README.md: broken local link: docs/missing.md", validate_repository(root))

    def test_reports_broken_relative_html_link(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "guide.html").write_text(
            '<!doctype html><a href="missing.md">Missing note</a>\n',
            encoding="utf-8",
        )

        self.assertIn(
            "docs/guide.html: broken local link: missing.md",
            validate_repository(root),
        )

    def test_ignores_external_and_fragment_html_links(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "guide.html").write_text(
            '<!doctype html><a href="#section">Section</a>'
            '<a href="https://example.com/reference">Reference</a>\n',
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(root), [])

    def test_reports_malformed_html_links_without_crashing(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "guide.html").write_text(
            '<!doctype html><a href="http://[">Absolute</a>'
            '<a href="//[">Protocol relative</a>\n',
            encoding="utf-8",
        )

        self.assertEqual(
            [
                "docs/guide.html: malformed href: http://[",
                "docs/guide.html: malformed href: //[",
            ],
            [error for error in validate_repository(root) if "malformed href" in error],
        )

    def test_ignores_markdown_links_inside_indented_code(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text(
            "Example command output:\n\n    [example](docs/not-a-link.md)\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(root), [])

    def test_handles_balanced_link_destinations_and_optional_titles(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "architecture-(worked)-note.md").write_text(
            "# Worked note\n", encoding="utf-8"
        )
        (root / "README.md").write_text(
            '[worked](docs/architecture-(worked)-note.md "Worked example")\n',
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(root), [])

    def test_validates_reference_style_link_destinations(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text(
            "Read [the missing note][missing].\n\n[missing]: docs/missing.md\n",
            encoding="utf-8",
        )

        self.assertIn("README.md: broken local link: docs/missing.md", validate_repository(root))

    def test_ignores_links_in_inline_code_and_tilde_fences(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text(
            "`[inline](docs/missing-inline.md)`\n\n~~~markdown\n[example](docs/missing-fenced.md)\n~~~\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(root), [])

    def test_reports_malformed_catalogue_separator_and_row(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8")
        catalog = catalog.replace(
            "| --- | --- | --- | --- | --- | --- | --- |",
            "| -- | --- | --- | --- | --- | --- | --- |",
            1,
        ).replace(
            "| Architecture Note | Software architecture | [docs/architecture-note.md](docs/architecture-note.md) | Markdown | Current | Living | 2026-09-08 |",
            "| Architecture Note | Software architecture | [docs/architecture-note.md](docs/architecture-note.md) | Markdown | Current | Living |",
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        errors = validate_repository(root)

        self.assertTrue(any("invalid catalogue table separator" in error for error in errors))
        self.assertTrue(any("catalogue row has 6 columns; expected 7" in error for error in errors))

    def test_parses_catalogue_row_without_outer_pipes(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8").replace(
            "| Architecture Note | Software architecture | [docs/architecture-note.md](docs/architecture-note.md) | Markdown | Current | Living | 2026-09-08 |",
            "Architecture Note | Software architecture | [docs/missing.md](docs/missing.md) | Markdown | Current | Living | 2026-09-08",
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        self.assertIn(
            "catalogue path does not exist: docs/missing.md",
            validate_repository(root),
        )

    def test_reports_empty_catalogue_metadata(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8").replace(
            "| Architecture Note | Software architecture |",
            "| Architecture Note |  |",
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        self.assertTrue(
            any("catalogue field is empty for Architecture Note: Domain" in error for error in validate_repository(root))
        )

    def test_validates_multiline_reference_destination(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text(
            "Read [the missing note][missing].\n\n[missing]:\n  docs/missing.md\n",
            encoding="utf-8",
        )

        self.assertIn("README.md: broken local link: docs/missing.md", validate_repository(root))

    def test_unescapes_punctuation_in_markdown_destination(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "architecture-(worked)-note.md").write_text(
            "# Worked note\n", encoding="utf-8"
        )
        (root / "docs" / "topic#one.md").write_text("# Topic one\n", encoding="utf-8")
        (root / "docs" / "topic?draft.md").write_text("# Topic draft\n", encoding="utf-8")
        (root / "README.md").write_text(
            r"[worked](docs/architecture-\(worked\)-note.md)" + "\n"
            r"[hash](docs/topic\#one.md)" + "\n"
            r"[question](docs/topic\?draft.md)" + "\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(root), [])

    def test_fence_with_trailing_text_does_not_close_code_block(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text(
            "```markdown\n```not-a-closing-fence\n[example](docs/missing.md)\n```\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(root), [])

    def test_requires_both_scoped_aws_resources(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        catalog = (root / "CATALOG.md").read_text(encoding="utf-8")
        catalog = "\n".join(
            line for line in catalog.splitlines() if "The $170 Cloud" not in line
        )
        (root / "CATALOG.md").write_text(catalog, encoding="utf-8")

        self.assertIn(
            "scoped AWS exception must catalogue exactly the handbook and lab manual",
            validate_repository(root),
        )

    def test_aws_regressions_support_unittest_discovery(self):
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "handbooks/aws-saa-c03/tests",
                "-p",
                "test_*.py",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
