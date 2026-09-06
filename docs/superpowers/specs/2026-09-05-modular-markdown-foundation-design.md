# Modular Markdown Foundation — Design

**Status:** Approved design
**Repository:** `arvindsoni2/Architect`
**Date:** 2026-09-05
**Visibility:** Public, curated
**Delivery branch:** `docs/modular-markdown-foundation`

## 1. Purpose

Create the first maintainable Markdown layer for the Architect knowledge repository by extracting four canonical, cross-source notes from the eight current artifacts. The notes will make durable architectural reasoning easy to review and update without replacing the richer handbook and learning-path editions.

This work is a synthesis project, not a format conversion. Each note combines the strongest explanations from multiple artifacts, removes repeated framing, assigns every concept one canonical home, and links readers back to the contributing sources.

## 2. Scope

The pull request will create these stable, unversioned paths:

1. `docs/software-architecture/architecture-decision-method.md`
2. `docs/system-design/reliability-and-failure-control.md`
3. `docs/cross-cutting-patterns/durable-workflows-and-idempotency.md`
4. `docs/ai-architecture/production-ai-assurance.md`

It will also update `README.md` and `CATALOG.md` so readers can find the notes directly.

The eight current artifacts remain unchanged:

| Source artifact | Repository path |
| --- | --- |
| System Design Concept Handbook v5 | `handbooks/system-design/system-design-concept-handbook-v5.html` |
| Agent Engineering Master Manual v2.7 | `handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html` |
| AI Engineering Handbook v3.0 | `handbooks/ai-engineering/ai-engineering-handbook-v3.0.html` |
| Software Architect Curriculum Guide v3 | `learning-paths/software-architect/software-architect-curriculum-guide-v3.md` |
| Software Architect Grooming Programme v5 | `learning-paths/software-architect/software-architect-grooming-programme-v5.html` |
| Forward Deployed AI Engineer Handbook v1.3 | `handbooks/fde/fde-handbook-v1.3.html` |
| The AI Architect's Handbook v1.2 | `handbooks/ai-architecture/ai-architects-handbook-v1.2.html` |
| Interview Resource Accelerator v4.3 | `learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html` |

### Non-goals

- Do not convert whole handbooks or learning paths to Markdown.
- Do not edit, supersede, or remove the eight current source artifacts.
- Do not extract the focused notes planned from the reasoning-model guide, CS336 model/inference notebook, CS329A self-improving-agent notes, or course and certification material.
- Do not import complete AWS certification packs.
- Do not add framework-specific tutorials, exhaustive interview resources, a website, generated navigation, or automated ingestion.
- Do not make the new notes a parallel versioned archive; Git history will record their revisions.

## 3. Editorial approach

The notes will use cross-source synthesis rather than mirroring source chapters. The editing sequence is:

1. Identify the load-bearing claim, model, trade-off, failure mode, or operating rule in each contributing source.
2. Group equivalent ideas even when their terminology differs.
3. Resolve the group into one plain-language explanation using first principles.
4. Preserve distinctive source wording only when paraphrasing would reduce precision.
5. Place the concept in its single canonical note and add a cross-link wherever another note needs it.
6. Remove handbook navigation, roadmaps, repeated introductions, complete resource lists, and material outside the note's declared scope.
7. Verify external claims and label volatile examples or dated claims with sufficient context.

The target is approximately 1,200–1,800 words per note. This is a decision-support constraint, not a rigid quota: a note may be shorter when the concept is complete, but it should not grow by reproducing source material.

The default voice follows the repository's Pareto and Feynman standard: retain the few ideas that govern most decisions, explain them in ordinary language, and test understanding with concrete questions.

## 4. Canonical notes and ownership

### 4.1 Architecture Decision Method

**Path:** `docs/software-architecture/architecture-decision-method.md`

**Purpose:** Provide a repeatable way to turn requirements and uncertainty into defensible architecture decisions.

**Canonical ownership:** requirements framing, stakeholder outcomes, quality attributes, constraints, evidence, alternatives, trade-offs, ADRs, validation, and decision defence.

**Principal sources:**

- Software Architect Curriculum Guide v3
- Software Architect Grooming Programme v5
- System Design Concept Handbook v5
- The AI Architect's Handbook v1.2
- Forward Deployed AI Engineer Handbook v1.3

The worked scenario will show how a team converts an ambiguous business request into measurable quality-attribute scenarios, compares alternatives, records a decision, and defines evidence that could invalidate it.

### 4.2 Reliability and Failure Control

**Path:** `docs/system-design/reliability-and-failure-control.md`

**Purpose:** Explain how to bound failures and design services that remain useful under stress.

**Canonical ownership:** failure domains, dependency budgets, timeouts, retry limits and jitter, load shedding, backpressure, circuit breaking, graceful degradation, SLOs, error budgets, RPO/RTO, recovery, and incident learning.

**Principal sources:**

- System Design Concept Handbook v5
- Software Architect Grooming Programme v5
- The AI Architect's Handbook v1.2
- Forward Deployed AI Engineer Handbook v1.3

The worked scenario will trace a dependency slowdown through an online request path and show how deadlines, bounded retries, capacity protection, degraded responses, and recovery objectives prevent amplification.

### 4.3 Durable Workflows and Idempotency

**Path:** `docs/cross-cutting-patterns/durable-workflows-and-idempotency.md`

**Purpose:** Show how multi-step work remains correct when messages are duplicated, processes restart, and partial progress survives.

**Canonical ownership:** queues, delivery semantics, stable operation identity, idempotency, deduplication, transactional outbox, state machines, checkpoints, compensation, replay, and durable execution.

**Principal sources:**

- System Design Concept Handbook v5
- Agent Engineering Master Manual v2.7
- The AI Architect's Handbook v1.2
- Forward Deployed AI Engineer Handbook v1.3
- Interview Resource Accelerator v4.3

The worked scenario will follow a long-running AI-assisted operation from accepted request through queued steps, external side effects, restart, duplicate delivery, compensation, and final reconciliation.

### 4.4 Production AI Assurance

**Path:** `docs/ai-architecture/production-ai-assurance.md`

**Purpose:** Define the evidence and controls required to move an AI capability from a compelling demo to an accountable production system.

**Canonical ownership:** task-specific evaluation, acceptance thresholds, offline and online evidence, autonomy boundaries, human escalation, safety controls, observability, trace review, unit economics, rollout stages, and rollback criteria.

**Principal sources:**

- AI Engineering Handbook v3.0
- Agent Engineering Master Manual v2.7
- The AI Architect's Handbook v1.2
- Forward Deployed AI Engineer Handbook v1.3
- Interview Resource Accelerator v4.3

The worked scenario will show a phased rollout of an AI workflow, connecting evaluation results to autonomy levels, operational signals, cost limits, exception handling, and the decision to expand or roll back.

## 5. Shared note structure

Every note will use these top-level sections in this order:

1. **Purpose and scope** — the problem the note solves and the adjacent concepts it deliberately delegates.
2. **First-principles model** — a compact mental model derived from system constraints rather than products.
3. **Core decisions and trade-offs** — the choices an architect must make and the consequences of each.
4. **Failure modes and warning signs** — recurring ways the design breaks and observable early signals.
5. **Practical decision checklist** — a short review aid phrased as decisions or evidence, not generic advice.
6. **Worked architecture scenario** — one coherent example that applies the model and exposes compromises.
7. **Feynman questions** — questions that reveal whether a reader can explain and apply the ideas simply.
8. **Related canonical notes** — relative links to the other new notes when the relationship is substantive.
9. **Sources and review status** — repository sources, concise numbered external references, and the review date.

Subheadings may vary to fit the subject, but the shared structure makes the collection predictable and mechanically checkable.

## 6. Deduplication and boundary rules

Each concept has one canonical home:

| Concept | Canonical home | Treatment elsewhere |
| --- | --- | --- |
| Quality attributes and ADRs | Architecture Decision Method | Refer to the decision method when selecting reliability or AI targets. |
| Timeouts, retries, backpressure, and SLOs | Reliability and Failure Control | Workflow and AI notes link to the reliability controls rather than redefine them. |
| Idempotency, outbox, checkpoints, and compensation | Durable Workflows and Idempotency | Reliability discusses their role only at a failure-boundary level. |
| Evaluations, autonomy, AI observability, and unit economics | Production AI Assurance | Decision Method links to production evidence; it does not reproduce AI-specific controls. |

Frameworks, cloud services, and model providers may appear as illustrative examples only. The organizing model must remain useful when those technologies change.

When contributing sources use conflicting advice, the note will not silently choose a winner. It will state the contextual difference—such as workload, consistency requirement, risk tolerance, latency budget, or organizational maturity—and then give the condition under which each recommendation is appropriate.

## 7. Source coverage and traceability

Every current artifact must contribute to at least one note. The planned source map is:

| Current artifact | Decision method | Reliability | Durable workflows | AI assurance |
| --- | :---: | :---: | :---: | :---: |
| System Design Concept Handbook v5 | Yes | Yes | Yes |  |
| Agent Engineering Master Manual v2.7 |  |  | Yes | Yes |
| AI Engineering Handbook v3.0 |  |  |  | Yes |
| Software Architect Curriculum Guide v3 | Yes |  |  |  |
| Software Architect Grooming Programme v5 | Yes | Yes |  |  |
| Forward Deployed AI Engineer Handbook v1.3 | Yes | Yes | Yes | Yes |
| The AI Architect's Handbook v1.2 | Yes | Yes | Yes | Yes |
| Interview Resource Accelerator v4.3 |  |  | Yes | Yes |

Each note's source section will link to its contributing repository artifacts using paths relative to the note. External references will be numbered, concise, and limited to sources that substantively support the note. A repository artifact link records where the synthesis came from; it does not claim that every sentence is a quotation from that artifact.

## 8. Freshness and evidence policy

Durable principles take priority over transient product facts. During extraction:

- Verify links and claims whose truth may have changed.
- Prefer primary sources for protocols, standards, research, and product behavior.
- Remove a dated claim when it is not necessary and cannot be verified.
- When a dated claim is useful, attach its applicable date or version and make the limitation visible in the prose.
- Mark the note's last substantive review as `2026-09-05`.
- Do not invent citations to make synthesis appear more authoritative.

The notes intentionally contain visible provenance: links to contributing repository artifacts, external references, review status, and review date. They must not contain hidden provenance, authoring-tool identifiers, conversation identifiers, prompts, private excerpts, or generated-file metadata.

## 9. Repository navigation and catalogue changes

### README

Add a **Maintainable notes** section with direct links to all four notes. Update domain links now that the corresponding `docs/` directories exist:

- Software architecture → `docs/software-architecture/`
- System design → `docs/system-design/`
- AI architecture → `docs/ai-architecture/`
- Cross-cutting patterns → `docs/cross-cutting-patterns/`

The Agent architecture domain continues to point to the current Agent Engineering handbook because this pull request does not create `docs/agent-architecture/`. Architect learning paths continue to point to `learning-paths/software-architect/`.

### Catalogue

Add one row for each note with:

- format: `Markdown`;
- status: `Current`;
- edition: `Living`;
- last reviewed: `2026-09-05`.

Remove **Modular Markdown extraction** from **Later migrations**, because this pull request completes that item. Retain **Focused architecture notes**, including the explicit exclusion of complete AWS certification packs.

## 10. Validation

Before the pull request is opened, verify:

1. All four files exist at the approved stable paths.
2. Every note contains all nine required top-level sections in the approved order.
3. Each of the eight current artifacts appears in at least one note's source map.
4. Repository artifact links, relative cross-note links, README links, and catalogue links resolve.
5. External references resolve and support the claims for which they are cited.
6. Canonical definitions are not duplicated across notes; cross-links are used at boundaries.
7. Time-sensitive claims are either verified and qualified or removed.
8. No credentials, private or confidential information, internal URLs, hidden provenance, conversation metadata, or unsupported personal examples are present.
9. Catalogue paths and titles are unique, and Markdown structure is valid.
10. `git diff --check` reports no whitespace errors.

The completed branch will receive an independent code/content review before a pull request is opened. Findings will be resolved on the branch, and the pull request will remain review-only for the repository owner to merge.

## 11. Delivery and isolation

Implementation will occur in an isolated Git worktree on `docs/modular-markdown-foundation`, based exactly on merged `origin/main` at `e7630cccc4a394dd7d83b2c05e489db91337bb4a`. This prevents the unrelated local modification to `handbooks/ai-engineering/ai-engineering-handbook-v3.0.html` in the existing checkout from being read as project work, staged, overwritten, or committed.

The pull request will contain the four notes plus the approved `README.md` and `CATALOG.md` navigation changes. It will not merge automatically.
