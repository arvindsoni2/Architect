# Architect Knowledge Repository — Design

**Status:** Approved design  
**Repository:** `arvindsoni2/Architect`  
**Date:** 2026-09-03 · **Amended:** 2026-10-13 (HTML-first learning), 2026-10-21 (learning lens), 2026-10-29 (project and product field guide)\
**Visibility:** Public, curated

## 1. Purpose

`Architect` is the canonical knowledge repository for durable architecture material. It consolidates handbooks, modular notes, patterns, and learning paths created across earlier conversations into a searchable, maintainable, version-controlled body of knowledge.

The repository is designed to reduce retrieval friction without becoming an indiscriminate technical-file archive.

## 2. Scope

The repository includes:

- software architecture;
- system design;
- AI architecture;
- agent architecture;
- cross-cutting architectural patterns;
- curated architecture learning paths;
- current published editions of relevant handbooks.

Architecture-adjacent course or certification material may contribute distilled notes, patterns, or references. Complete course notebooks and certification study packs are outside the repository.

**Scoped amendment approved 7 September 2026:** include the AWS SAA-C03 Visual Handbook and its companion *The $170 Cloud* Lab Manual under `handbooks/aws-saa-c03/`, together with supporting validation. This is a two-resource exception; it does not broaden the general certification/course-material boundary.

**Scoped amendment approved 1 October 2026:** curated role-based interview preparation is maintained under `interview-prep/`, with shared methods, a public-safe factual evidence bank, role guides and vacancy supplements. Stable Markdown sources generate a tabbed HTML reading view and one HTML page per guide. Private recruitment feedback and personal eligibility records remain excluded.

**Scoped amendment approved 29 October 2026:** include one interactive revision guide to project and product management frameworks under `handbooks/project-product/`, supporting the delivery, project and product roles in the interview collection. This is a single-resource exception; it does not admit general project-management course material or certification packs.

Unrelated project files, general technical learning material, job-search material outside that collection, and personal records are excluded.

**Owner preference approved 13 October 2026 — HTML-first learning:** interactive HTML handbooks are the preferred way to learn from this repository, because they can carry diagrams, motion, labs, quizzes and read-aloud. Markdown notes are kept alongside them. Section 3 describes how the two formats work together.

## 3. Content model

The repository uses a hybrid model with **HTML as the primary learning format**.

### Interactive handbooks (primary)

`handbooks/` and the HTML files in `learning-paths/` are the main learning surface. They are edited directly and are not generated from Markdown. New learning material lands in the most relevant HTML handbook first, with explanatory diagrams and, where they help understanding, interactive or animated figures. Each handbook keeps one current edition; its visible edition line records what changed and when.

### Markdown companions (retained)

Markdown under `docs/` remains as plain-text companions for durable concepts, patterns, trade-offs, failure modes, checklists and references. They are easy to search, diff and reuse. They are not being retired. When a topic exists in both formats, keep the facts aligned in the same pull request; the HTML may teach more (figures, labs, motion) but must not contradict the note.

### HTML quality standard

Every HTML handbook change should meet these requirements:

- **Self-contained:** one file that works offline from a download. Inline CSS, JavaScript and SVG. External fonts are optional and must have a fallback; no external runtime dependencies.
- **Diagrams:** inline SVG with `role="img"`, a `<title>` and a `<desc>`, using the page's colour tokens so they work in every theme the page offers. Prefer SVG to raster images.
- **Interaction and motion:** controls are real buttons or inputs and work with a keyboard. Motion starts only when the reader presses play and respects `prefers-reduced-motion`. The same explanation must be readable without the animation, including in print.
- **Audio:** prefer read-aloud through the browser's Web Speech API, which needs no audio files. Hide the control when the browser does not support it.
- **Video:** link to it rather than embedding video files, to keep handbooks small and fast.
- **Layout:** no horizontal page scroll at 390 px wide; wide tables scroll inside their own container. Print shows all content.
- **Storage:** wrap browser storage in `try/catch` and render correctly without it.
- **Learning lens:** chapters and learning units carry first-principles, Pareto, visual and Feynman blocks as described in the [learning lens standard](learning-lens-standard.md) (amended 21 October 2026).

### Learning paths

`learning-paths/` contains curated curricula and development programmes directly related to becoming a software, solution, system, AI, or agent architect.

### Interview preparation

`interview-prep/` separates shared methods and evidence from role responsibilities and vacancy context. Markdown is canonical; the HTML reading view and per-guide HTML pages (with practice mode) are regenerated rather than independently edited. Git history replaces dated duplicate editions.

### Catalogue

`CATALOG.md` is the repository-wide content map. Each entry records title, domain, path, format, lifecycle status, current edition, last substantive review, and relationship to any source or published edition.

The catalogue is the primary retrieval surface after the root README.

## 4. Repository structure

```text
Architect/
├── README.md
├── CATALOG.md
├── CONTRIBUTING.md
├── docs/
│   ├── software-architecture/
│   ├── system-design/
│   ├── ai-architecture/
│   ├── agent-architecture/
│   └── cross-cutting-patterns/
├── handbooks/
│   ├── agent-engineering/
│   ├── ai-architecture/
│   ├── ai-engineering/
│   ├── ai-evaluation/
│   ├── aws-saa-c03/
│   ├── fde/
│   ├── project-product/
│   └── system-design/
├── interview-prep/
└── learning-paths/
    ├── ai-ml-interview/
    └── software-architect/
```

Directories are created only when they receive content. Empty placeholder directories are not committed.

File and directory names use lowercase kebab-case. Version numbers belong in published artifact filenames when the edition is meaningful; canonical Markdown paths remain stable across revisions.

## 5. Curation and versioning

1. Import only the latest useful edition of a work.
2. Do not import obsolete duplicates merely to preserve history.
3. Use Git history for all versions created after migration.
4. Compare ambiguous variants before selecting the canonical edition.
5. Remove or generalize personal, proprietary, security-sensitive, or stale material before publication.
6. Preserve substantive citations and label time-sensitive claims with a review date.
7. Prefer durable principles, trade-offs, failure modes, and judgment over framework-specific detail.
8. Keep prior wording when it remains correct; migration is not permission for unnecessary rewriting.

Superseded source files remain outside this repository unless a comparison shows that the latest edition accidentally lost unique, valuable content.

## 6. Public-repository safety

Every imported artifact receives a pre-publication review for:

- credentials, tokens, internal URLs, and account identifiers;
- personal contact or immigration information;
- confidential employer, client, or project information;
- private conversation excerpts;
- unsupported claims presented as facts;
- broken or expired references;
- hidden file metadata or embedded provenance.

The repository will not intentionally add hidden provenance metadata. Visible document status, dates, and review information are allowed and should remain understandable to readers.

Project examples may be included only when already public or sufficiently generalized.

## 7. Collaboration workflow

Content decisions follow this governance model:

1. inventory candidate material;
2. select the canonical version;
3. review and curate it;
4. map it to the repository taxonomy;
5. open a focused pull request;
6. review the rendered and source forms;
7. merge after approval;
8. update `CATALOG.md`.

Codex may be used when bulk conversion, repository-wide editing, link validation, formatting checks, or other code-oriented assistance is useful.

The design document seeds the otherwise empty default branch. All subsequent bootstrap and migration work uses reviewable branches and pull requests. Small corrections may be committed directly only when the repository owner explicitly chooses to do so.

## 8. Initial migration

The first migration batch will establish the root navigation and curate these candidates:

1. System Design Concept Handbook v5;
2. Agent Engineering Master Manual v2.7 — AI Systems Foundations;
3. AI Engineering Handbook v3.1;
4. Software Architect Curriculum Guide v3;
5. Software Architect Grooming Programme v5.

The batch also creates `README.md`, `CATALOG.md`, and `CONTRIBUTING.md`.

The AI Architect Handbook v1.2 and earlier architecture notes will be recovered and migrated in later focused batches after their canonical sources are located.

AWS certification material other than the two-resource exception in Section 2, and complete CS329A/CS336 study notebooks, remain excluded. Durable architecture insights from excluded material may later be rewritten as focused notes with appropriate references.

## 9. Quality standard

Every canonical note or handbook must make its purpose and scope clear and should include, where applicable:

- first-principles explanation;
- architectural context;
- decisions and trade-offs;
- failure modes;
- operational considerations;
- practical exercises or review questions;
- concise references.

The existing Pareto and Feynman editorial approach remains the default: retain load-bearing ideas, explain them plainly, and avoid information overload.

## 10. Success criteria

The repository is successful when:

- a reader can locate relevant material from the README or catalogue without remembering a filename;
- each subject has one clearly identified current source;
- Markdown changes are meaningfully reviewable in Git;
- interactive HTML handbooks are the first place a reader learns a topic, and meet the HTML quality standard in Section 3;
- Markdown companions stay factually aligned with the handbooks;
- obsolete duplicates do not compete with canonical content;
- public content passes the safety and provenance review;
- future architecture notes have an obvious destination and update workflow.

## 11. Non-goals

The repository will not initially:

- host every technical artifact created during exploratory work;
- preserve every historical file version;
- become a general-purpose personal knowledge-management system;
- include complete certification or course-note collections beyond the two-resource exception in Section 2;
- publish a website or GitHub Pages portal;
- automate content ingestion without human review.
