# Contributing and Curation Rules

This repository is a public, curated architecture knowledge base. Every change should improve retrieval, correctness, or maintainability without turning the repository into an indiscriminate file archive.

## Content boundary

Accepted material covers software architecture, system design, AI architecture, agent architecture, cross-cutting architectural patterns, and architect learning paths.

Complete certification packs, course notebooks, unrelated project files, personal records, and general technical-learning collections are excluded. Durable architectural lessons may be distilled from those sources into focused notes.

## Canonical content and versions

1. Maintain one current artifact for each title.
2. Do not add obsolete duplicates merely to preserve history; Git records future revisions.
3. Compare ambiguous editions before selecting the canonical version.
4. Use lowercase kebab-case for repository paths.
5. Keep canonical Markdown paths stable. Published HTML or PDF filenames may include meaningful edition numbers.
6. Update `CATALOG.md` whenever content is added, removed, renamed, or superseded.

## Public-content safety

Before opening a pull request, review all changed files for:

- credentials, passwords, API keys, bearer values, authorization headers, and internal URLs;
- personal contact, immigration, or visa information;
- confidential employer, client, or project information;
- private conversation excerpts or prompts;
- unsupported factual claims;
- broken or expired references;
- hidden file metadata or embedded provenance.

Remove or generalize unsafe material. Technical uses of terms such as “token” must be reviewed in context rather than deleted mechanically.

The repository does not intentionally add hidden provenance metadata. Visible status labels, edition numbers, dates, and review information are allowed when they help readers assess the content.

## Editorial standard

- Prefer durable principles, decisions, trade-offs, failure modes, and operational judgment over framework-specific detail.
- Use first-principles explanations and plain language.
- Retain load-bearing ideas and avoid information overload.
- Preserve correct existing wording; migration is not permission for unnecessary rewriting.
- Verify links and time-sensitive claims before merge. Label unresolved freshness concerns as **Review due** in `CATALOG.md`.
- Include concise references for factual claims that depend on external sources.

## Rendered artifacts

Rendered HTML or PDF belongs under `handbooks/` only when its layout or learning experience adds value beyond Markdown.

Before merge, open rendered HTML locally and check:

- table-of-contents and internal navigation;
- missing images, fonts, stylesheets, or scripts;
- clipped or overlapping text;
- code blocks and diagrams;
- print layout when the document supports printing.

Published artifacts are outputs. Maintainable concepts and patterns should progressively move into modular Markdown under `docs/`.

## Pull-request checklist

- [ ] The change is within the repository’s architecture scope.
- [ ] The selected edition is canonical.
- [ ] Public-content and sensitive-data review is complete.
- [ ] Links and time-sensitive claims have been checked.
- [ ] Rendered files have been opened and visually inspected.
- [ ] `CATALOG.md` has been updated when required.
- [ ] No obsolete duplicate or empty directory has been added.
- [ ] `git diff --check` reports no whitespace errors.
