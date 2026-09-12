#!/usr/bin/env python3
"""Validate catalogue integrity and local Markdown/HTML links without network access."""

from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit


CATALOG_COLUMNS = [
    "Title",
    "Domain",
    "Path",
    "Format",
    "Status",
    "Edition",
    "Last reviewed",
]
AWS_SECTION = "Scoped AWS study-resource exception"
AWS_PATHS = {
    "AWS SAA-C03 Visual Handbook": "handbooks/aws-saa-c03/saa-c03-visual-handbook-2026.09.html",
    "The $170 Cloud — SAA-C03 Lab Manual": "handbooks/aws-saa-c03/saa-c03-lab-manual-v2.1.html",
}
VALID_STATUSES = {"Current", "Review due", "Draft", "Superseded"}
FORMAT_SUFFIXES = {"Markdown": ".md", "HTML": ".html", "PDF": ".pdf"}
CATALOG_LINK_RE = re.compile(r"^\[[^\]]+\]\(([^)]+)\)$")
SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
REFERENCE_DEFINITION_RE = re.compile(r"^ {0,3}\[[^\]]+\]:\s*(.*)$")


class _AnchorTargetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for name, value in attrs:
            if name.lower() == "href" and value:
                self.targets.append(value.strip())


def _table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _catalogue_rows(catalogue: pathlib.Path) -> tuple[list[dict[str, str]], list[str]]:
    lines = catalogue.read_text(encoding="utf-8").splitlines()
    section = ""
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1)
        if _table_cells(line) == CATALOG_COLUMNS:
            if index + 1 >= len(lines):
                errors.append(f"CATALOG.md:{index + 1}: catalogue table has no separator")
                break
            separator = _table_cells(lines[index + 1])
            if len(separator) != len(CATALOG_COLUMNS) or not all(
                SEPARATOR_CELL_RE.fullmatch(cell) for cell in separator
            ):
                errors.append(f"CATALOG.md:{index + 2}: invalid catalogue table separator")
            index += 2
            while index < len(lines) and lines[index].strip() and "|" in lines[index]:
                cells = _table_cells(lines[index])
                if len(cells) != len(CATALOG_COLUMNS):
                    errors.append(
                        f"CATALOG.md:{index + 1}: catalogue row has {len(cells)} columns; "
                        f"expected {len(CATALOG_COLUMNS)}"
                    )
                else:
                    row = dict(zip(CATALOG_COLUMNS, cells))
                    row["Section"] = section
                    row["Line"] = str(index + 1)
                    rows.append(row)
                index += 1
            continue
        index += 1
    return rows, errors


def _catalogue_errors(root: pathlib.Path) -> list[str]:
    catalogue = root / "CATALOG.md"
    if not catalogue.is_file():
        return ["missing CATALOG.md"]

    rows, errors = _catalogue_rows(catalogue)
    if not rows:
        errors.append("CATALOG.md contains no recognised catalogue rows")
        return errors

    seen_titles: set[str] = set()
    seen_paths: set[str] = set()
    aws_titles: set[str] = set()

    for row in rows:
        title = row["Title"]
        display_title = title or f"line {row['Line']}"
        for field in CATALOG_COLUMNS:
            if not row[field]:
                errors.append(f"catalogue field is empty for {display_title}: {field}")
        if title in seen_titles:
            errors.append(f"duplicate catalogue title: {title}")
        seen_titles.add(title)

        match = CATALOG_LINK_RE.match(row["Path"])
        if not match:
            errors.append(f"catalogue path is not a Markdown link: {row['Path']}")
            continue
        relative_path = unquote(match.group(1).split("#", 1)[0])

        target = (root / relative_path).resolve()
        try:
            canonical_path = target.relative_to(root.resolve()).as_posix()
        except ValueError:
            errors.append(f"catalogue path escapes repository: {relative_path}")
            continue
        if canonical_path in seen_paths:
            errors.append(f"duplicate catalogue path: {canonical_path}")
        seen_paths.add(canonical_path)
        if not target.is_file():
            errors.append(f"catalogue path does not exist: {relative_path}")

        expected_suffix = FORMAT_SUFFIXES.get(row["Format"])
        if expected_suffix is None:
            errors.append(f"unsupported catalogue format for {title}: {row['Format']}")
        elif pathlib.PurePosixPath(canonical_path).suffix.lower() != expected_suffix:
            errors.append(f"catalogue format does not match path for {title}")

        if row["Status"] not in VALID_STATUSES:
            errors.append(f"invalid catalogue status for {title}: {row['Status']}")
        try:
            dt.date.fromisoformat(row["Last reviewed"])
        except ValueError:
            errors.append(f"invalid review date for {title}: {row['Last reviewed']}")

        if row["Section"] == AWS_SECTION:
            aws_titles.add(title)
            if not canonical_path.startswith("handbooks/aws-saa-c03/"):
                errors.append(f"scoped AWS resource is outside handbooks/aws-saa-c03: {title}")
            expected_path = AWS_PATHS.get(title)
            if expected_path and canonical_path != expected_path:
                errors.append(f"{title} must use {expected_path}")
        elif canonical_path.startswith("handbooks/aws-saa-c03/"):
            errors.append(f"AWS catalogue entry must be in the scoped exception: {title}")

    if aws_titles != set(AWS_PATHS):
        errors.append("scoped AWS exception must catalogue exactly the handbook and lab manual")
    if not (root / "handbooks" / "aws-saa-c03" / "README.md").is_file():
        errors.append("scoped AWS resources require handbooks/aws-saa-c03/README.md")
    return errors


def _without_inline_code(line: str) -> str:
    output = list(line)
    index = 0
    while index < len(line):
        if line[index] != "`":
            index += 1
            continue
        run_end = index
        while run_end < len(line) and line[run_end] == "`":
            run_end += 1
        delimiter = line[index:run_end]
        close = line.find(delimiter, run_end)
        if close == -1:
            index = run_end
            continue
        for position in range(index, close + len(delimiter)):
            output[position] = " "
        index = close + len(delimiter)
    return "".join(output)


def _destination(value: str) -> str:
    value = value.strip()
    if value.startswith("<"):
        close = value.find(">", 1)
        return value[1:close] if close != -1 else value
    escaped = False
    for index, character in enumerate(value):
        if escaped:
            escaped = False
        elif character == "\\":
            escaped = True
        elif character.isspace():
            return value[:index]
    return value


def _unescape_destination(value: str) -> str:
    return re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", value)


def _path_without_suffix(value: str) -> str:
    escaped = False
    for index, character in enumerate(value):
        if escaped:
            escaped = False
        elif character == "\\":
            escaped = True
        elif character in "#?":
            return value[:index]
    return value


def _inline_link_targets(line: str) -> list[str]:
    targets: list[str] = []
    cursor = 0
    while True:
        marker = line.find("](", cursor)
        if marker == -1:
            return targets
        if line.rfind("[", 0, marker) == -1:
            cursor = marker + 2
            continue
        index = marker + 2
        depth = 1
        escaped = False
        while index < len(line):
            character = line[index]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0:
                    targets.append(_destination(line[marker + 2 : index]))
                    cursor = index + 1
                    break
            index += 1
        else:
            return targets


def _markdown_link_errors(root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    for document in sorted(root.rglob("*.md")):
        relative_document = document.relative_to(root).as_posix()
        fence_character = ""
        fence_length = 0
        pending_reference = False
        for line in document.read_text(encoding="utf-8").splitlines():
            fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if fence_character:
                if (
                    fence
                    and fence.group(1)[0] == fence_character
                    and len(fence.group(1)) >= fence_length
                    and not fence.group(2).strip()
                ):
                    fence_character = ""
                    fence_length = 0
                continue
            if fence:
                fence_character = fence.group(1)[0]
                fence_length = len(fence.group(1))
                continue
            if line.startswith(("    ", "\t")):
                continue
            visible_line = _without_inline_code(line)
            raw_targets: list[str] = []
            if pending_reference:
                if visible_line.startswith((" ", "\t")) and visible_line.strip():
                    raw_targets.append(_destination(visible_line.strip()))
                pending_reference = False
            reference = REFERENCE_DEFINITION_RE.match(visible_line)
            if reference:
                if reference.group(1).strip():
                    raw_targets.append(_destination(reference.group(1)))
                else:
                    pending_reference = True
            raw_targets.extend(_inline_link_targets(visible_line))
            for raw_target in raw_targets:
                target_text = raw_target.strip()
                if not target_text or target_text.startswith("#"):
                    continue
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target_text):
                    continue
                path_text = _unescape_destination(
                    unquote(_path_without_suffix(target_text))
                )
                target = (document.parent / path_text).resolve()
                try:
                    target.relative_to(root.resolve())
                except ValueError:
                    errors.append(f"{relative_document}: local link escapes repository: {target_text}")
                    continue
                if not target.exists():
                    errors.append(f"{relative_document}: broken local link: {target_text}")
    return errors


def _html_link_errors(root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    for document in sorted(root.rglob("*.html")):
        relative_document = document.relative_to(root).as_posix()
        parser = _AnchorTargetParser()
        parser.feed(document.read_text(encoding="utf-8"))
        for raw_target in parser.targets:
            try:
                parsed = urlsplit(raw_target)
            except ValueError:
                errors.append(f"{relative_document}: malformed href: {raw_target}")
                continue
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path_text = unquote(parsed.path)
            target = (
                root / path_text.lstrip("/")
                if path_text.startswith("/")
                else document.parent / path_text
            ).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append(
                    f"{relative_document}: local link escapes repository: {raw_target}"
                )
                continue
            if not target.exists():
                errors.append(
                    f"{relative_document}: broken local link: {raw_target}"
                )
    return errors


def validate_repository(root: pathlib.Path) -> list[str]:
    root = root.resolve()
    return (
        _catalogue_errors(root)
        + _markdown_link_errors(root)
        + _html_link_errors(root)
    )


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Repository content validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
