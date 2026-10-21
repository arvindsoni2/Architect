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
    "The $170 Cloud — SAA-C03 Lab Manual": "handbooks/aws-saa-c03/saa-c03-lab-manual-v2.2.html",
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


LENS_KINDS = ("fp", "pareto", "visual", "feynman")
LENS_MAX_LEARN_ITEMS = 3


class _LearningLensParser(HTMLParser):
    """Collects learning-lens units, blocks, Feynman text and diagram metadata.

    See docs/learning-lens-standard.md. A unit is any element carrying
    ``data-lens-unit``. An empty value means the unit is the element itself;
    ``until-next`` means it runs until the next unit starts (for flat,
    heading-based documents).
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.events: list[tuple[str, str, int]] = []
        self.units: list[dict] = []
        self.unknown: list[tuple[str, int]] = []
        self.learn_lists: list[tuple[int, int]] = []
        self.feynman: list[tuple[str, int]] = []
        self.svgs: list[dict] = []
        self._depth: dict[str, int] = {}
        self._open_units: list[dict] = []
        self._feynman_open: list[dict] = []
        self._learn_open: list[dict] = []
        self._svg: dict | None = None

    def _line(self) -> int:
        return self.getpos()[0]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): (value or "") for name, value in attrs}
        tag = tag.lower()
        depth = self._depth.get(tag, 0) + 1
        self._depth[tag] = depth
        position = len(self.events)
        if "data-lens-unit" in attributes:
            unit = {
                "line": self._line(),
                "mode": attributes["data-lens-unit"],
                "start": position,
                "end": None,
                "tag": tag,
                "depth": depth,
            }
            self.units.append(unit)
            if unit["mode"] != "until-next":
                self._open_units.append(unit)
        kind = attributes.get("data-lens-block")
        if kind is not None:
            if kind in LENS_KINDS:
                self.events.append(("block", kind, self._line()))
            else:
                self.unknown.append((kind, self._line()))
            if kind == "feynman":
                self._feynman_open.append({"tag": tag, "depth": depth, "text": [], "line": self._line()})
        classes = attributes.get("class", "").split()
        if tag == "ul" and "lens-learn" in classes:
            self._learn_open.append({"depth": depth, "items": 0, "line": self._line()})
        if tag == "li" and self._learn_open:
            if self._depth.get("ul", 0) == self._learn_open[-1]["depth"]:
                self._learn_open[-1]["items"] += 1
        if tag == "svg" and "lens-svg" in classes:
            self._svg = {"line": self._line(), "role": attributes.get("role", ""), "title": False, "desc": False, "depth": depth}
        elif self._svg is not None and tag in ("title", "desc"):
            self._svg[tag] = True
        self.events.append(("start", tag, self._line()))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        depth = self._depth.get(tag, 0)
        if self._open_units and self._open_units[-1]["tag"] == tag and self._open_units[-1]["depth"] == depth:
            self._open_units.pop()["end"] = len(self.events)
        if self._feynman_open and self._feynman_open[-1]["tag"] == tag and self._feynman_open[-1]["depth"] == depth:
            block = self._feynman_open.pop()
            self.feynman.append((" ".join(" ".join(block["text"]).split()), block["line"]))
        if tag == "ul" and self._learn_open and self._learn_open[-1]["depth"] == depth:
            block = self._learn_open.pop()
            self.learn_lists.append((block["items"], block["line"]))
        if tag == "svg" and self._svg is not None and self._svg["depth"] == depth:
            self.svgs.append(self._svg)
            self._svg = None
        if depth:
            self._depth[tag] = depth - 1
        self.events.append(("end", tag, self._line()))

    def handle_data(self, data: str) -> None:
        for block in self._feynman_open:
            block["text"].append(data)


def _learning_lens_errors(root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    for document in sorted(root.rglob("*.html")):
        text = document.read_text(encoding="utf-8")
        if "data-lens-unit" not in text and "data-lens-block" not in text and "lens-svg" not in text:
            continue
        relative_document = document.relative_to(root).as_posix()
        parser = _LearningLensParser()
        parser.feed(text)
        parser.close()
        for kind, line in parser.unknown:
            errors.append(f"{relative_document}:{line}: unknown data-lens-block value: {kind}")
        units = parser.units
        for index, unit in enumerate(units):
            if unit["mode"] == "until-next":
                end = units[index + 1]["start"] if index + 1 < len(units) else len(parser.events)
            else:
                end = unit["end"] if unit["end"] is not None else len(parser.events)
            found = {name for event, name, _ in parser.events[unit["start"]:end] if event == "block"}
            missing = [kind for kind in LENS_KINDS if kind not in found]
            if missing:
                errors.append(
                    f"{relative_document}:{unit['line']}: learning-lens unit is missing: {', '.join(missing)}"
                )
        for items, line in parser.learn_lists:
            if items > LENS_MAX_LEARN_ITEMS:
                errors.append(
                    f"{relative_document}:{line}: Pareto learn-first list has {items} items; the limit is {LENS_MAX_LEARN_ITEMS}"
                )
        seen: dict[str, int] = {}
        for body, line in parser.feynman:
            if body in seen:
                errors.append(
                    f"{relative_document}:{line}: Feynman block repeats the one at line {seen[body]}; prompts must be written for each unit"
                )
            else:
                seen[body] = line
        for svg in parser.svgs:
            if svg["role"] != "img" or not svg["title"] or not svg["desc"]:
                errors.append(
                    f"{relative_document}:{svg['line']}: learning-lens diagram needs role=\"img\", <title> and <desc>"
                )
    return errors


def validate_repository(root: pathlib.Path) -> list[str]:
    root = root.resolve()
    return (
        _catalogue_errors(root)
        + _markdown_link_errors(root)
        + _html_link_errors(root)
        + _learning_lens_errors(root)
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
