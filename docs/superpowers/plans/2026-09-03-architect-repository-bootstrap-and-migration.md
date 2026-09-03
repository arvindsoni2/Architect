# Architect Repository Bootstrap and Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap `arvindsoni2/Architect` as a navigable public architecture knowledge base and migrate the five approved current artifacts through focused, reviewable pull requests.

**Architecture:** Use a hybrid publication model: stable Markdown paths under `docs/` for maintainable knowledge, current rendered editions under `handbooks/`, and architect development material under `learning-paths/`. `README.md` and `CATALOG.md` provide retrieval without requiring filename recall; Git history replaces a duplicate-file archive.

**Tech Stack:** Git, GitHub pull requests, Markdown, self-contained HTML, authenticated source storage, and shell validation with `rg`, `file`, `wc`, and `git diff --check`.

**Spec:** `docs/repository-design.md`

## Global Constraints

- Repository visibility remains public and every artifact must be curated before publication.
- Scope is limited to software architecture, system design, AI architecture, agent architecture, cross-cutting architectural patterns, and architecture learning paths.
- Complete course notebooks, certification study packs, unrelated projects, job-search material, personal records, and general technical-learning files are excluded.
- Markdown under `docs/` is the evolving source of truth; `handbooks/` contains only current rendered editions.
- Import only the latest useful edition; do not publish obsolete duplicates.
- File and directory names use lowercase kebab-case.
- Canonical Markdown paths remain stable; meaningful edition numbers may appear in published artifact filenames.
- Remove or generalize personal, proprietary, security-sensitive, stale, and unsupported content before publication.
- Do not intentionally add hidden provenance metadata.
- Preserve correct existing wording; migration is not permission for unnecessary rewriting.
- Use focused branches and pull requests for all work after the design document that seeded `main`.

---

## File Map

| Path | Responsibility |
| --- | --- |
| `README.md` | Concise repository entry point and domain navigation. |
| `CATALOG.md` | Authoritative inventory of current content, editions, formats, status, and review dates. |
| `CONTRIBUTING.md` | Curation, naming, safety, versioning, and pull-request rules. |
| `handbooks/system-design/system-design-concept-handbook-v5.html` | Current rendered System Design Concept Handbook. |
| `handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html` | Current rendered Agent Engineering Master Manual. |
| `handbooks/ai-engineering/ai-engineering-handbook-v3.0.html` | Current rendered AI Engineering Handbook. |
| `learning-paths/software-architect/software-architect-curriculum-guide-v3.md` | Current Markdown architect curriculum. |
| `learning-paths/software-architect/software-architect-grooming-programme-v5.html` | Current rendered architect development programme. |

The initial migration does not create empty taxonomy directories. `docs/software-architecture/`, `docs/system-design/`, `docs/ai-architecture/`, `docs/agent-architecture/`, and `docs/cross-cutting-patterns/` will appear only when modular Markdown notes are extracted in later plans.

---

### Task 1: Bootstrap repository navigation and governance

**Pull request:** `bootstrap/knowledge-base` → `main`

**Files:**

- Create: `README.md`
- Create: `CATALOG.md`
- Create: `CONTRIBUTING.md`

**Interfaces:**

- Consumes: `docs/repository-design.md`
- Produces: stable navigation and catalogue conventions used by every migration task

- [ ] **Step 1: Create the bootstrap branch from current `main`**

```bash
git switch main
git pull --ff-only
git switch -c bootstrap/knowledge-base
```

- [ ] **Step 2: Create `README.md` with the approved repository boundary**

Use this structure and wording:

```markdown
# Architect

A curated, version-controlled knowledge base for software architecture, system design, AI architecture, and agent architecture.

## Start here

- [Content catalogue](CATALOG.md)
- [Repository design](docs/repository-design.md)
- [Contribution and curation rules](CONTRIBUTING.md)

## Domains

- Software architecture
- System design
- AI architecture
- Agent architecture
- Cross-cutting patterns
- Architect learning paths

Directories are added as curated material is migrated. This repository intentionally excludes complete certification packs, course notebooks, unrelated project files, and obsolete artifact duplicates.
```

- [ ] **Step 3: Create `CATALOG.md` with an explicit schema and empty initial inventory**

```markdown
# Content Catalogue

This is the authoritative index of current material in the repository.

| Title | Domain | Path | Format | Status | Edition | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- |

## Status values

- **Current:** canonical or currently published material.
- **Review due:** usable material whose time-sensitive claims need checking.
- **Draft:** incomplete material not yet canonical.
- **Superseded:** retained only when a migration decision explicitly requires it.
```

- [ ] **Step 4: Create `CONTRIBUTING.md` with enforceable curation rules**

It must state:

1. one current artifact per title;
2. lowercase kebab-case paths;
3. no credentials, private conversation excerpts, immigration/contact details, confidential client material, or unsupported factual claims;
4. visible status and review dates are allowed, but hidden provenance metadata must not be added intentionally;
5. links and time-sensitive claims must be reviewed before merge;
6. each pull request must update `CATALOG.md` when it adds, removes, renames, or supersedes content;
7. rendered HTML must be opened locally and checked for missing assets, clipped content, and broken navigation;
8. migration should preserve correct wording and avoid gratuitous rewriting.

- [ ] **Step 5: Validate the bootstrap files**

```bash
git diff --check
rg -n "FIXME" README.md CATALOG.md CONTRIBUTING.md
rg -n --ignore-case "password|api[_-]?key|secret|bearer|authorization:|immigration|visa|confidential client" README.md CATALOG.md CONTRIBUTING.md
```

Expected: `git diff --check` exits 0; the `FIXME` scan returns no matches; the safety scan returns only intentional policy terms in `CONTRIBUTING.md`, which must be reviewed manually.

- [ ] **Step 6: Commit and open the bootstrap pull request**

```bash
git add README.md CATALOG.md CONTRIBUTING.md
git commit -m "docs: bootstrap architecture knowledge base"
git push -u origin bootstrap/knowledge-base
```

Pull-request title: `docs: bootstrap architecture knowledge base`

Acceptance check: GitHub renders the README and all three links resolve.

---

### Task 2: Migrate the System Design Concept Handbook

**Pull request:** `migrate/system-design-handbook-v5` → `main`

**Files:**

- Create: `handbooks/system-design/system-design-concept-handbook-v5.html`
- Modify: `CATALOG.md`

**Interfaces:**

- Consumes: approved source file `System_Design_Concept_Handbook_v5.html`
- Produces: the current published system-design handbook and its catalogue entry

- [ ] **Step 1: Materialize the exact Library source without renaming the source copy**

Download the approved source into a temporary migration workspace and record its byte count and SHA-256 hash before editing.

```bash
wc -c System_Design_Concept_Handbook_v5.html
sha256sum System_Design_Concept_Handbook_v5.html
```

- [ ] **Step 2: Confirm v5 is the canonical edition**

Compare its title, table of contents, chapter count, and final section against v4. Do not import v4. If v4 contains unique substantive material missing from v5, record the exact lost section in the pull-request description before deciding whether to restore it to v5.

- [ ] **Step 3: Run the public-content review**

```bash
rg -n --ignore-case "password|api[_-]?key|secret|token|bearer|authorization:|immigration|visa|internal only|client confidential" System_Design_Concept_Handbook_v5.html
rg -n --ignore-case "generated by|chatgpt|conversation transcript|prompt:" System_Design_Concept_Handbook_v5.html
rg -n "https?://" System_Design_Concept_Handbook_v5.html
```

Review every match. Remove unsafe content, retain legitimate technical uses of words such as “token,” and check every cited URL relevant to a time-sensitive claim.

- [ ] **Step 4: Copy the curated file to its canonical published path and render-check it**

```bash
mkdir -p handbooks/system-design
cp System_Design_Concept_Handbook_v5.html handbooks/system-design/system-design-concept-handbook-v5.html
file handbooks/system-design/system-design-concept-handbook-v5.html
rg --pcre2 -n '(?:src|href)="(?!https?://|#|mailto:|data:)[^"]+' handbooks/system-design/system-design-concept-handbook-v5.html
```

Open the target HTML locally. Confirm the table of contents, internal navigation, code blocks, diagrams, and print layout work without missing local assets.

- [ ] **Step 5: Add the exact catalogue row**

```markdown
| System Design Concept Handbook | System design | [handbooks/system-design/system-design-concept-handbook-v5.html](handbooks/system-design/system-design-concept-handbook-v5.html) | HTML | Current | v5 | 2026-09-03 |
```

- [ ] **Step 6: Validate, commit, and open the pull request**

```bash
git diff --check
git status --short
git add handbooks/system-design/system-design-concept-handbook-v5.html CATALOG.md
git commit -m "docs: migrate system design handbook v5"
git push -u origin migrate/system-design-handbook-v5
```

Acceptance check: the target file opens without missing assets and only one System Design Concept Handbook appears in `CATALOG.md`.

---

### Task 3: Migrate the Agent Engineering Master Manual

**Pull request:** `migrate/agent-engineering-manual-v2-7` → `main`

**Files:**

- Create: `handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html`
- Modify: `CATALOG.md`

**Interfaces:**

- Consumes: approved source file `Agent_Engineering_Master_Manual_v2.7_AI_Systems_Foundations.html`
- Produces: the current published agent-engineering manual and its catalogue entry

- [ ] **Step 1: Materialize and fingerprint the v2.7 source**

```bash
wc -c Agent_Engineering_Master_Manual_v2.7_AI_Systems_Foundations.html
sha256sum Agent_Engineering_Master_Manual_v2.7_AI_Systems_Foundations.html
```

- [ ] **Step 2: Compare v2.7 with the directly preceding v2.6 AI Systems Foundations edition**

Confirm v2.7 retains the model SDK, agent harness, orchestration runtime, interoperability protocol, failure-mode, memory-bank, exercise, and knowledge-check sections. Do not import v2.5 or v2.6 variants.

- [ ] **Step 3: Run the same public-content, provenance, link, local-asset, and browser render checks defined in Task 2**

Apply them to `Agent_Engineering_Master_Manual_v2.7_AI_Systems_Foundations.html`. Review technical “token” matches by context instead of deleting them mechanically.

- [ ] **Step 4: Copy the curated file to the canonical path**

```bash
mkdir -p handbooks/agent-engineering
cp Agent_Engineering_Master_Manual_v2.7_AI_Systems_Foundations.html handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html
```

- [ ] **Step 5: Add the exact catalogue row**

```markdown
| Agent Engineering Master Manual | Agent architecture | [handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html](handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html) | HTML | Current | v2.7 | 2026-09-03 |
```

- [ ] **Step 6: Validate, commit, and open the pull request**

```bash
git diff --check
git add handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html CATALOG.md
git commit -m "docs: migrate agent engineering manual v2.7"
git push -u origin migrate/agent-engineering-manual-v2-7
```

Acceptance check: all expected lesson components remain present and only v2.7 is published.

---

### Task 4: Migrate the AI Engineering Handbook

**Pull request:** `migrate/ai-engineering-handbook-v3` → `main`

**Files:**

- Create: `handbooks/ai-engineering/ai-engineering-handbook-v3.0.html`
- Modify: `CATALOG.md`

**Interfaces:**

- Consumes: approved source file `ai-engineering-handbook.html`
- Produces: the current published AI Engineering Handbook and its catalogue entry

- [ ] **Step 1: Materialize and fingerprint the source**

```bash
wc -c ai-engineering-handbook.html
sha256sum ai-engineering-handbook.html
```

- [ ] **Step 2: Verify the internal edition and canonical status**

Confirm the document identifies itself as v3.0, May 2026, and as the consolidated single source of truth. Compare the duplicate `ai-engineering-handbook(1).html` by hash; if hashes match, discard the duplicate without further review.

- [ ] **Step 3: Review freshness as well as public safety**

Run Task 2's public-content and provenance scans. In addition, review claims about current models, APIs, framework versions, service limits, pricing, or deprecations. Correct them with primary sources or mark the relevant section `Review due` in the catalogue; do not silently present stale May 2026 claims as current September 2026 facts.

- [ ] **Step 4: Copy and render-check the curated handbook**

```bash
mkdir -p handbooks/ai-engineering
cp ai-engineering-handbook.html handbooks/ai-engineering/ai-engineering-handbook-v3.0.html
```

- [ ] **Step 5: Add one of these exact catalogue rows based on the freshness review**

If all time-sensitive material is verified:

```markdown
| AI Engineering Handbook | AI architecture | [handbooks/ai-engineering/ai-engineering-handbook-v3.0.html](handbooks/ai-engineering/ai-engineering-handbook-v3.0.html) | HTML | Current | v3.0 | 2026-09-03 |
```

If unresolved time-sensitive claims remain:

```markdown
| AI Engineering Handbook | AI architecture | [handbooks/ai-engineering/ai-engineering-handbook-v3.0.html](handbooks/ai-engineering/ai-engineering-handbook-v3.0.html) | HTML | Review due | v3.0 | 2026-09-03 |
```

- [ ] **Step 6: Validate, commit, and open the pull request**

```bash
git diff --check
git add handbooks/ai-engineering/ai-engineering-handbook-v3.0.html CATALOG.md
git commit -m "docs: migrate AI engineering handbook v3.0"
git push -u origin migrate/ai-engineering-handbook-v3
```

Acceptance check: the catalogue status truthfully reflects the freshness audit.

---

### Task 5: Migrate the Software Architect learning path

**Pull request:** `migrate/software-architect-learning-path` → `main`

**Files:**

- Create: `learning-paths/software-architect/software-architect-curriculum-guide-v3.md`
- Create: `learning-paths/software-architect/software-architect-grooming-programme-v5.html`
- Modify: `CATALOG.md`

**Interfaces:**

- Consumes: approved source file `Software_Architect_Curriculum_Guide_v3.md`
- Consumes: approved source file `Software_Architect_Grooming_Programme_v5.html`
- Produces: the current software-architect curriculum and development programme

- [ ] **Step 1: Materialize and fingerprint both sources**

```bash
wc -c Software_Architect_Curriculum_Guide_v3.md Software_Architect_Grooming_Programme_v5.html
sha256sum Software_Architect_Curriculum_Guide_v3.md Software_Architect_Grooming_Programme_v5.html
```

- [ ] **Step 2: Confirm the documents have distinct responsibilities**

The curriculum guide must describe what to learn and in what sequence. The grooming programme must describe the practice schedule, exercises, or development process. Remove repeated material only when it obscures those distinct purposes.

- [ ] **Step 3: Run public-content, provenance, link, and freshness reviews**

Apply the scans from Task 2 to both files. Check that named resources still exist and that course, certification, or product recommendations are labelled by review date when time-sensitive.

- [ ] **Step 4: Copy both curated files to canonical paths and render-check the HTML**

```bash
mkdir -p learning-paths/software-architect
cp Software_Architect_Curriculum_Guide_v3.md learning-paths/software-architect/software-architect-curriculum-guide-v3.md
cp Software_Architect_Grooming_Programme_v5.html learning-paths/software-architect/software-architect-grooming-programme-v5.html
```

- [ ] **Step 5: Add the exact catalogue rows**

```markdown
| Software Architect Curriculum Guide | Software architecture | [learning-paths/software-architect/software-architect-curriculum-guide-v3.md](learning-paths/software-architect/software-architect-curriculum-guide-v3.md) | Markdown | Current | v3 | 2026-09-03 |
| Software Architect Grooming Programme | Software architecture | [learning-paths/software-architect/software-architect-grooming-programme-v5.html](learning-paths/software-architect/software-architect-grooming-programme-v5.html) | HTML | Current | v5 | 2026-09-03 |
```

- [ ] **Step 6: Validate, commit, and open the pull request**

```bash
git diff --check
git add learning-paths/software-architect CATALOG.md
git commit -m "docs: migrate software architect learning path"
git push -u origin migrate/software-architect-learning-path
```

Acceptance check: the two files are complementary, rendered links work, and no earlier grooming-programme edition is published.

---

### Task 6: Close the initial migration and record deferred work

**Pull request:** `docs/close-initial-migration` → `main`

**Files:**

- Modify: `README.md`
- Modify: `CATALOG.md`

**Interfaces:**

- Consumes: merged outputs from Tasks 1–5
- Produces: a complete initial navigation surface and an explicit later-work boundary

- [ ] **Step 1: Add working domain links to the README**

Replace plain domain labels with links to the relevant catalogue anchors or migrated directories. Do not link to empty directories.

- [ ] **Step 2: Check catalogue uniqueness and target existence**

```bash
rg -n '^\|' CATALOG.md
find handbooks learning-paths -type f -print | sort
git diff --check
```

Manually confirm that every catalogue path exists and every migrated file has exactly one current catalogue row.

- [ ] **Step 3: Run the final repository-wide public-content scan**

```bash
rg -n --ignore-case "password|api[_-]?key|secret|bearer|authorization:|immigration|visa|internal only|client confidential" --glob '*.md' --glob '*.html' .
rg -n --ignore-case "generated by|chatgpt|conversation transcript|prompt:" --glob '*.md' --glob '*.html' .
```

Review all matches. Policy text in `CONTRIBUTING.md` is expected; unexplained matches elsewhere block the pull request.

- [ ] **Step 4: Record deferred work without creating empty content files**

Add a `Later migrations` section to `CATALOG.md` containing only these named candidates:

- AI Architect Handbook v1.2 — canonical source not yet located;
- modular Markdown extraction from the five published artifacts;
- focused architecture notes distilled from relevant course or certification material.

Do not add tracking-stub files or empty directories.

- [ ] **Step 5: Commit and open the closing pull request**

```bash
git add README.md CATALOG.md
git commit -m "docs: complete initial architecture migration index"
git push -u origin docs/close-initial-migration
```

Acceptance check: a new reader can reach every current artifact from `README.md` or `CATALOG.md` without knowing its filename.

---

## Execution order and review gates

1. Merge Task 1 before starting content migrations because it defines catalogue and curation rules.
2. Tasks 2–4 may be prepared independently after Task 1, but each receives its own review and merge decision.
3. Merge Task 5 after Task 1; it does not depend on Tasks 2–4.
4. Start Task 6 only after Tasks 2–5 are merged.
5. Do not merge a migration pull request when public-safety findings, broken local assets, or unresolved canonical-version differences remain.

## Completion verification

Before declaring the initial migration complete, verify:

```bash
git status --short
git diff --check
find . -type f -not -path './.git/*' -print | sort
rg -n '^\|.*\| (Current|Review due) \|' CATALOG.md
```

Expected:

- clean working tree;
- no whitespace errors;
- one design document, three root navigation/governance files, three published handbooks, and two learning-path files;
- five current or review-due catalogue entries;
- no obsolete handbook duplicates;
- no empty taxonomy directories.
