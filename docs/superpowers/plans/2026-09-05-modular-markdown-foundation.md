# Modular Markdown Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish four stable, cross-source Markdown notes that form the first maintainable knowledge layer for the Architect repository.

**Architecture:** Synthesize the eight current artifacts into four notes with exclusive concept ownership and relative cross-links at topic boundaries. Preserve the existing handbooks and learning paths as published sources; expose the new living notes through `README.md` and `CATALOG.md`, then validate structure, traceability, freshness, safety, and link integrity before opening one review-only pull request.

**Tech Stack:** Git, GitHub pull requests, Markdown, HTML source inspection, POSIX shell, `rg`, `sed`, `wc`, `sort`, `diff`, Python 3 for local Markdown-link resolution, and primary-source web checks.

**Spec:** `docs/superpowers/specs/2026-09-05-modular-markdown-foundation-design.md`

## Global Constraints

- Work only on `docs/modular-markdown-foundation` in the isolated worktree based on merged `origin/main` at `e7630cccc4a394dd7d83b2c05e489db91337bb4a`.
- Do not stage, overwrite, or commit the unrelated modification to `handbooks/ai-engineering/ai-engineering-handbook-v3.0.html` in the original checkout.
- Create exactly four stable, unversioned Markdown note paths.
- Use cross-source synthesis; do not mirror or convert complete source chapters.
- Keep every concept in one canonical home and cross-link instead of redefining it.
- Keep each note approximately 1,200–1,800 words and use the nine approved top-level sections in the approved order.
- Use Pareto prioritisation, first-principles explanation, and Feynman questions.
- Preserve precise, load-bearing wording when paraphrasing would weaken it; remove repeated introductions, navigation, roadmaps, and resource lists.
- Treat frameworks, cloud services, and model providers as examples rather than the organising structure.
- When sources conflict, state the contextual difference—such as workload, consistency need, consequence, latency budget, risk tolerance, or organisational maturity—and the condition under which each recommendation fits.
- Prefer durable principles; verify and visibly qualify any time-sensitive statement that remains.
- Remove a dated claim that cannot be verified unless its date/version and uncertainty can be stated visibly and usefully.
- Link every note to its contributing repository artifacts and use concise numbered external references.
- Every one of the eight current artifacts must contribute to at least one note.
- Leave all eight current source artifacts unchanged.
- Complete AWS certification packs remain excluded.
- Include visible source provenance, review status, and review date `2026-09-05`; do not add hidden metadata, authoring-tool identifiers, prompts, conversation identifiers, or private excerpts.
- Do not include credentials, personal/contact/immigration data, confidential client material, internal URLs, or unsupported factual claims.
- Use one reviewable branch and pull request; do not merge automatically.

---

## File map

| Path | Responsibility |
| --- | --- |
| `docs/software-architecture/architecture-decision-method.md` | Canonical method for requirements, quality attributes, evidence, trade-offs, ADRs, and decision defence. |
| `docs/system-design/reliability-and-failure-control.md` | Canonical reliability model for failure domains, overload controls, service objectives, recovery, and learning. |
| `docs/cross-cutting-patterns/durable-workflows-and-idempotency.md` | Canonical workflow-correctness model for retries, delivery semantics, idempotency, outbox, checkpoints, and compensation. |
| `docs/ai-architecture/production-ai-assurance.md` | Canonical production-AI model for evaluation, autonomy, observability, economics, rollout, and acceptance. |
| `README.md` | Direct entry point to the four maintainable notes and their domain directories. |
| `CATALOG.md` | Four `Current`/`Living` entries and the remaining focused-notes migration item. |
| `docs/superpowers/specs/2026-09-05-modular-markdown-foundation-design.md` | Approved design already committed on the branch; it remains unchanged during implementation. |

The shared top-level note contract is exact:

```markdown
# Note title

## Purpose and scope
## First-principles model
## Core decisions and trade-offs
## Failure modes and warning signs
## Practical decision checklist
## Worked architecture scenario
## Feynman questions
## Related canonical notes
## Sources and review status
```

Each `Sources and review status` section ends with:

```markdown
**Status:** Current  
**Edition:** Living  
**Last reviewed:** 2026-09-05
```

---

### Task 1: Publish the Architecture Decision Method

**Files:**

- Create: `docs/software-architecture/architecture-decision-method.md`

**Interfaces:**

- Consumes: the approved spec plus decision material in the System Design handbook, Software Architect curriculum and grooming programme, AI Architect handbook, and FDE handbook.
- Produces: the canonical definitions for architecture drivers, quality-attribute scenarios, decision hypotheses, trade-off records, ADRs, evidence, and reversal triggers. Tasks 2–4 may link to these definitions but must not restate them.

- [ ] **Step 1: Confirm the branch and demonstrate that the note does not exist yet**

Run:

```bash
git branch --show-current
git rev-parse e7630cccc4a394dd7d83b2c05e489db91337bb4a
test ! -e docs/software-architecture/architecture-decision-method.md
```

Expected: the branch is `docs/modular-markdown-foundation`; the SHA resolves; the absence check exits 0.

- [ ] **Step 2: Read the bounded source slices before drafting**

Run:

```bash
sed -n '68,130p' learning-paths/software-architect/software-architect-curriculum-guide-v3.md
sed -n '297,395p' learning-paths/software-architect/software-architect-curriculum-guide-v3.md
sed -n '118,128p' handbooks/system-design/system-design-concept-handbook-v5.html
sed -n '309,315p' handbooks/system-design/system-design-concept-handbook-v5.html
rg -n -i 'quality attribute|decision record|trade-off|architecture hypothesis|evidence plan|decision defence' learning-paths/software-architect/software-architect-grooming-programme-v5.html
sed -n '5459,5735p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
sed -n '6908,6975p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
sed -n '649,725p' handbooks/fde/fde-handbook-v1.3.html
```

Expected: the extracts cover problem framing, measurable quality scenarios, evidence-based trade-offs, ADR structure, validation, and production acceptance. Do not copy the surrounding learning roadmaps or handbook navigation.

- [ ] **Step 3: Create the note using the approved contract and content boundary**

Create the file with `apply_patch` and implement this map:

| Section | Required content |
| --- | --- |
| Purpose and scope | State that architecture is a reasoned choice under constraints, not a component diagram. Own the decision method; delegate runtime failure controls, workflow correctness, and AI-specific release evidence. |
| First-principles model | Explain `outcome → stakeholders → drivers → measurable scenarios → constraints/assumptions → options → consequences → evidence → decision/reversal trigger`. Define a decision as a falsifiable hypothesis. |
| Core decisions and trade-offs | Cover functional need versus quality attribute; dominant qualities; reversible versus hard-to-reverse choices; simplicity versus optionality; present evidence versus deferred learning; contextual conflicts; and an ADR containing context, forces, options, decision, consequences, evidence, status, and review trigger. |
| Failure modes and warning signs | Include solution-first framing, adjective-only requirements, hidden assumptions, equal weighting of all qualities, decision-matrix theatre, consensus without accountability, winner-only ADRs, and decisions with no invalidation signal. |
| Practical decision checklist | Ask for the outcome at risk, stakeholder and owner, measurable scenario, hard constraint, rejected alternative, accepted sacrifice, evidence, uncertainty, reversal trigger, and communication artifact. |
| Worked architecture scenario | Modernise a regional claims workflow. Convert ambiguity into latency, availability, auditability, data-residency, changeability, and cost scenarios; compare a modular monolith plus queue with early microservices; choose the simpler boundary and define decomposition evidence. |
| Feynman questions | Explain why a decision is a hypothesis; turn “fast and reliable” into scenarios; name what an ADR preserves; explain a deliberate sacrifice; identify reversal evidence. |
| Related canonical notes | Link to the other three notes with one sentence describing each delegated concern. |
| Sources and review status | Link to the five repository artifacts below, cite SEI QAW, SEI ATAM, and ADR resources, and add the exact status block. |

Repository links:

```markdown
- [System Design Concept Handbook v5](../../handbooks/system-design/system-design-concept-handbook-v5.html)
- [Software Architect Curriculum Guide v3](../../learning-paths/software-architect/software-architect-curriculum-guide-v3.md)
- [Software Architect Grooming Programme v5](../../learning-paths/software-architect/software-architect-grooming-programme-v5.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)
```

External references to verify before publication:

```markdown
1. Software Engineering Institute, [Quality Attribute Workshop](https://www.sei.cmu.edu/library/the-sei-quality-attribute-workshop/)
2. Software Engineering Institute, [Architecture Tradeoff Analysis Method collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)
3. ADR GitHub organisation, [Architecture Decision Records](https://adr.github.io/)
```

- [ ] **Step 4: Validate the note contract, size, and source paths**

Run:

```bash
note=docs/software-architecture/architecture-decision-method.md
test -f "$note"
test "$(rg -c '^# Architecture Decision Method$' "$note")" -eq 1
for heading in '## Purpose and scope' '## First-principles model' '## Core decisions and trade-offs' '## Failure modes and warning signs' '## Practical decision checklist' '## Worked architecture scenario' '## Feynman questions' '## Related canonical notes' '## Sources and review status'; do rg -Fqx "$heading" "$note"; done
words=$(wc -w < "$note")
test "$words" -ge 1200 && test "$words" -le 1800
for source in '../../handbooks/system-design/system-design-concept-handbook-v5.html' '../../learning-paths/software-architect/software-architect-curriculum-guide-v3.md' '../../learning-paths/software-architect/software-architect-grooming-programme-v5.html' '../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html' '../../handbooks/fde/fde-handbook-v1.3.html'; do rg -Fq "$source" "$note"; done
git diff --check -- "$note"
```

Expected: every command exits 0 and the note is within the approved range.

- [ ] **Step 5: Commit the decision note**

```bash
git add docs/software-architecture/architecture-decision-method.md
git commit -m "docs: add architecture decision method"
```

---

### Task 2: Publish Reliability and Failure Control

**Files:**

- Create: `docs/system-design/reliability-and-failure-control.md`

**Interfaces:**

- Consumes: the decision note's quality-scenario vocabulary and reliability material from System Design, the grooming programme, AI Architect, and FDE.
- Produces: canonical failure domains, latency/dependency budgets, bounded retries, overload control, degradation, SLOs/error budgets, RPO/RTO, recovery, and incident learning.

- [ ] **Step 1: Demonstrate that the note does not exist**

```bash
test ! -e docs/system-design/reliability-and-failure-control.md
```

- [ ] **Step 2: Read the bounded source slices**

```bash
sed -n '141,151p' handbooks/system-design/system-design-concept-handbook-v5.html
sed -n '221,305p' handbooks/system-design/system-design-concept-handbook-v5.html
rg -n -i 'failure domain|timeout|retry|backoff|jitter|circuit breaker|bulkhead|graceful degradation|load shedding|backpressure|error budget|RPO|RTO|incident' learning-paths/software-architect/software-architect-grooming-programme-v5.html
sed -n '1205,1270p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
sed -n '6003,6055p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
rg -n -i 'timeout|retry|degrad|SLO|recovery|rollback|incident' handbooks/fde/fde-handbook-v1.3.html
```

- [ ] **Step 3: Create the note using this content map**

| Section | Required content |
| --- | --- |
| Purpose and scope | Reliability is useful behaviour under expected and adverse conditions. Own containment/recovery; delegate target selection and cross-step correctness. |
| First-principles model | Capacity is finite, failures are partial, latency has a tail, queues store waiting rather than create capacity, and retries spend more capacity. Use `demand × work per request ≤ safe capacity`; show deadlines and failure domains bounding amplification. |
| Core decisions and trade-offs | End-to-end deadline allocation; retry location, eligibility, budget, backoff, and jitter; circuit breaking versus shedding; bulkheads; admission control/backpressure; fail-open/fail-closed/degraded behaviour; SLIs/SLOs/error budgets; RPO/RTO versus cost. |
| Failure modes and warning signs | Nested retries, retry synchronisation, unlimited queues, caller/dependency deadline inversion, shallow health checks, shared pools, average-only latency, untested failover, unsafe degradation, and ownerless incident actions. |
| Practical decision checklist | User SLO, dependency budget, saturation signal, admission rule, retry owner/budget, degradation matrix, failure-domain boundary, RPO, RTO, recovery drill, learning loop. |
| Worked architecture scenario | One-second checkout-read path with a slow inventory dependency: allocate deadlines, suppress nested retries, add jitter, isolate pools, shed low-priority work, serve a marked degraded result, define SLO impact, and separate service recovery from data RPO/RTO. |
| Feynman questions | Why retries cause outages; why queues do not create capacity; SLO versus dashboard metric; when to fail closed; RPO versus RTO. |
| Related canonical notes | Link to Decision Method, Durable Workflows, and Production AI Assurance; delegate ADRs, idempotency, and AI behavioural quality. |
| Sources and review status | Link to the four repository artifacts below, cite AWS Builders' Library and Google SRE sources, and add the status block. |

Repository links:

```markdown
- [System Design Concept Handbook v5](../../handbooks/system-design/system-design-concept-handbook-v5.html)
- [Software Architect Grooming Programme v5](../../learning-paths/software-architect/software-architect-grooming-programme-v5.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)
```

External references:

```markdown
1. Amazon Builders' Library, [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
2. Google, [Site Reliability Engineering: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
3. Google, [The Site Reliability Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)
```

- [ ] **Step 4: Validate and commit**

```bash
note=docs/system-design/reliability-and-failure-control.md
test "$(rg -c '^# Reliability and Failure Control$' "$note")" -eq 1
for heading in '## Purpose and scope' '## First-principles model' '## Core decisions and trade-offs' '## Failure modes and warning signs' '## Practical decision checklist' '## Worked architecture scenario' '## Feynman questions' '## Related canonical notes' '## Sources and review status'; do rg -Fqx "$heading" "$note"; done
words=$(wc -w < "$note")
test "$words" -ge 1200 && test "$words" -le 1800
for source in '../../handbooks/system-design/system-design-concept-handbook-v5.html' '../../learning-paths/software-architect/software-architect-grooming-programme-v5.html' '../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html' '../../handbooks/fde/fde-handbook-v1.3.html'; do rg -Fq "$source" "$note"; done
git diff --check -- "$note"
git add "$note"
git commit -m "docs: add reliability and failure controls"
```

---

### Task 3: Publish Durable Workflows and Idempotency

**Files:**

- Create: `docs/cross-cutting-patterns/durable-workflows-and-idempotency.md`

**Interfaces:**

- Consumes: Reliability's bounded-failure vocabulary and workflow material from System Design, Agent Engineering, AI Architect, FDE, and Interview Resource artifacts.
- Produces: canonical delivery/processing semantics, stable operation identity, idempotency, deduplication, outbox, state machines, checkpoints, replay, compensation, and reconciliation.

- [ ] **Step 1: Demonstrate that the note does not exist**

```bash
test ! -e docs/cross-cutting-patterns/durable-workflows-and-idempotency.md
```

- [ ] **Step 2: Read the bounded source slices**

```bash
sed -n '221,241p' handbooks/system-design/system-design-concept-handbook-v5.html
rg -n -i '<h[1-4][^>]*>.*(state|checkpoint|durable|idempoten|compensat|retry|workflow)' handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html
sed -n '4200,4335p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
rg -n -i 'idempoten|checkpoint|compensat|replay|durable|partial success|duplicate' handbooks/fde/fde-handbook-v1.3.html
sed -n '1696,1775p' learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html
```

- [ ] **Step 3: Create the note using this content map**

| Section | Required content |
| --- | --- |
| Purpose and scope | A durable workflow is explicit state and recovery semantics around work that outlives one process. Own cross-step correctness; delegate capacity protection and AI authority. |
| First-principles model | Networks lose, delay, and duplicate knowledge; timeout means outcome unknown. Separate delivery, handler processing, and external side effects. Build the correctness loop from operation ID, durable transition, retryable step, effect record, and reconciliation. |
| Core decisions and trade-offs | Synchronous versus queued; queue versus stream; at-most-once/at-least-once; boundary-specific exactly-once claims; idempotency scope/retention; inbox/dedupe; outbox; state machines; checkpoint/replay; compensation/manual reconciliation. |
| Failure modes and warning signs | Ack before commit, dual writes, regenerated retry keys, permanent dedupe records, non-deterministic replay, hidden partial states, inverse-transaction compensation, ownerless poison messages, context-free or silently expired approval. |
| Practical decision checklist | Operation identity, state owner, commit/ack points, retry owner, duplicate rule, key retention, effect ledger, checkpoint/replay rule, compensation, poison owner, reconciliation, approval expiry. |
| Worked architecture scenario | AI-assisted claims evidence: accepted request, retrieval, generation, approval, external case update, notification, worker crash, duplicate delivery, idempotent update, outbox, checkpoint, approval expiry, compensation, and manual reconciliation for an irreversible notice. |
| Feynman questions | What timeout proves; why at-least-once needs idempotency; how outbox closes dual-write gap; why compensation is not rollback; state required after human pause. |
| Related canonical notes | Link to Decision Method, Reliability, and Production AI Assurance; delegate trade-off records, overload policy, and autonomy/evaluation. |
| Sources and review status | Link to the five repository artifacts below, cite Temporal and AWS outbox guidance as examples, and add the status block. |

Repository links:

```markdown
- [System Design Concept Handbook v5](../../handbooks/system-design/system-design-concept-handbook-v5.html)
- [Agent Engineering Master Manual v2.7](../../handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)
- [Interview Resource Accelerator v4.3](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html)
```

External references:

```markdown
1. Temporal, [What is a durable execution platform?](https://docs.temporal.io/evaluate/why-temporal)
2. AWS Prescriptive Guidance, [Transactional outbox pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)
```

- [ ] **Step 4: Validate and commit**

```bash
note=docs/cross-cutting-patterns/durable-workflows-and-idempotency.md
test "$(rg -c '^# Durable Workflows and Idempotency$' "$note")" -eq 1
for heading in '## Purpose and scope' '## First-principles model' '## Core decisions and trade-offs' '## Failure modes and warning signs' '## Practical decision checklist' '## Worked architecture scenario' '## Feynman questions' '## Related canonical notes' '## Sources and review status'; do rg -Fqx "$heading" "$note"; done
words=$(wc -w < "$note")
test "$words" -ge 1200 && test "$words" -le 1800
for source in '../../handbooks/system-design/system-design-concept-handbook-v5.html' '../../handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html' '../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html' '../../handbooks/fde/fde-handbook-v1.3.html' '../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html'; do rg -Fq "$source" "$note"; done
git diff --check -- "$note"
git add "$note"
git commit -m "docs: add durable workflow patterns"
```

---

### Task 4: Publish Production AI Assurance

**Files:**

- Create: `docs/ai-architecture/production-ai-assurance.md`

**Interfaces:**

- Consumes: the earlier canonical boundaries plus assurance material from AI Engineering, Agent Engineering, AI Architect, FDE, and Interview Resource artifacts.
- Produces: canonical AI-specific evaluation evidence, production gates, autonomy levels, AI observability, unit economics, phased adoption, acceptance, and rollback.

- [ ] **Step 1: Demonstrate that the note does not exist**

```bash
test ! -e docs/ai-architecture/production-ai-assurance.md
```

- [ ] **Step 2: Read the bounded source slices**

```bash
sed -n '1287,1410p' handbooks/ai-engineering/ai-engineering-handbook-v3.0.html
rg -n -i '<h[1-4][^>]*>.*(evaluation|observability|autonomy|human|cost|production)' handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html
sed -n '213,310p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
sed -n '7784,8175p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
sed -n '8600,8905p' handbooks/ai-architecture/ai-architects-handbook-v1.2.html
sed -n '690,770p' handbooks/fde/fde-handbook-v1.3.html
sed -n '1364,1515p' learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html
```

- [ ] **Step 3: Create the note using this content map**

| Section | Required content |
| --- | --- |
| Purpose and scope | Assurance is evidence and controls that justify production influence. Model capability is necessary; fitness requires value, quality, safety, operability, economics, and adoption. Delegate generic ADRs, service reliability, and workflow idempotency. |
| First-principles model | `task and consequence → representative cases → component/workflow/outcome evaluation → threshold → bounded authority → production signals → scale/hold/narrow/stop`. Production readiness is the intersection, not average, of six gates. |
| Core decisions and trade-offs | Evaluation unit and representativeness; deterministic checks, calibrated model judges, human review, production outcomes; segment thresholds; shadow/assist/supervised/bounded autonomy; consequence-boundary approval; metadata-first observability; cost per successful outcome; adoption ownership; rollout, rollback, handoff. |
| Failure modes and warning signs | Demo-as-evidence, averages hiding risky segments, uncalibrated judge, stale eval set, outcome-only/trajectory-only evaluation, authority from average accuracy, sensitive trace capture, token cost mistaken for unit economics, end-stage adoption, calendar-driven promotion. |
| Practical decision checklist | Workflow outcome, non-AI baseline, error consequence, segments, eval lineage, acceptance owner, autonomy boundary, escalation, production signals, cost per accepted outcome, user friction, rollback test, dated decision. |
| Worked architecture scenario | AI claims-evidence assistant with baseline, representative/adversarial cases, component/workflow/outcome metrics, segment thresholds, shadow-to-assist rollout, approval at case-update boundary, privacy-aware traces, override metrics, full economics, promotion/rollback evidence. |
| Feynman questions | Why a high model score can fail production; why one average hides risk; when authority may increase; what successful-outcome cost includes; how shadow mode changes evidence. |
| Related canonical notes | Link to Decision Method, Reliability, and Durable Workflows; delegate quality scenarios/ADRs, infrastructure failure controls, and side-effect correctness. |
| Sources and review status | Link to five artifacts, cite NIST AI RMF and current primary evaluation/telemetry guidance where used, date changing schema claims, and add status. |

Repository links:

```markdown
- [AI Engineering Handbook v3.0](../../handbooks/ai-engineering/ai-engineering-handbook-v3.0.html)
- [Agent Engineering Master Manual v2.7](../../handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)
- [Interview Resource Accelerator v4.3](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html)
```

Primary references:

```markdown
1. NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
2. OpenAI, [Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
3. OpenTelemetry, [Generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
```

Verify the OpenTelemetry status during implementation. Do not reproduce model prices, fixed rollout percentages, or generic accuracy thresholds.

- [ ] **Step 4: Validate and commit**

```bash
note=docs/ai-architecture/production-ai-assurance.md
test "$(rg -c '^# Production AI Assurance$' "$note")" -eq 1
for heading in '## Purpose and scope' '## First-principles model' '## Core decisions and trade-offs' '## Failure modes and warning signs' '## Practical decision checklist' '## Worked architecture scenario' '## Feynman questions' '## Related canonical notes' '## Sources and review status'; do rg -Fqx "$heading" "$note"; done
words=$(wc -w < "$note")
test "$words" -ge 1200 && test "$words" -le 1800
for source in '../../handbooks/ai-engineering/ai-engineering-handbook-v3.0.html' '../../handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html' '../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html' '../../handbooks/fde/fde-handbook-v1.3.html' '../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html'; do rg -Fq "$source" "$note"; done
git diff --check -- "$note"
git add "$note"
git commit -m "docs: add production AI assurance"
```

---

### Task 5: Complete cross-note and root navigation

**Files:**

- Modify: the four new notes
- Modify: `README.md`

**Interfaces:**

- Consumes: all four canonical paths.
- Produces: complete topic navigation and root discovery without duplicate definitions.

- [ ] **Step 1: Apply the exact related-note link matrix**

Use `apply_patch`; each link receives one boundary sentence:

| From | Required relative links |
| --- | --- |
| Architecture Decision Method | `../system-design/reliability-and-failure-control.md`, `../cross-cutting-patterns/durable-workflows-and-idempotency.md`, `../ai-architecture/production-ai-assurance.md` |
| Reliability and Failure Control | `../software-architecture/architecture-decision-method.md`, `../cross-cutting-patterns/durable-workflows-and-idempotency.md`, `../ai-architecture/production-ai-assurance.md` |
| Durable Workflows and Idempotency | `../software-architecture/architecture-decision-method.md`, `../system-design/reliability-and-failure-control.md`, `../ai-architecture/production-ai-assurance.md` |
| Production AI Assurance | `../software-architecture/architecture-decision-method.md`, `../system-design/reliability-and-failure-control.md`, `../cross-cutting-patterns/durable-workflows-and-idempotency.md` |

- [ ] **Step 2: Replace the README Domains list**

```markdown
## Domains

- [Software architecture](docs/software-architecture/)
- [System design](docs/system-design/)
- [AI architecture](docs/ai-architecture/)
- [Agent architecture](handbooks/agent-engineering/)
- [Cross-cutting patterns](docs/cross-cutting-patterns/)
- [Architect learning paths](learning-paths/software-architect/)
```

- [ ] **Step 3: Insert Maintainable notes after Start here**

```markdown
## Maintainable notes

- [Architecture Decision Method](docs/software-architecture/architecture-decision-method.md)
- [Reliability and Failure Control](docs/system-design/reliability-and-failure-control.md)
- [Durable Workflows and Idempotency](docs/cross-cutting-patterns/durable-workflows-and-idempotency.md)
- [Production AI Assurance](docs/ai-architecture/production-ai-assurance.md)
```

- [ ] **Step 4: Validate and commit**

```bash
for path in docs/software-architecture/architecture-decision-method.md docs/system-design/reliability-and-failure-control.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/ai-architecture/production-ai-assurance.md; do test -f "$path"; rg -Fq "($path)" README.md; done
test "$(rg -c '^## Maintainable notes$' README.md)" -eq 1
git diff --check -- README.md docs/software-architecture docs/system-design docs/cross-cutting-patterns docs/ai-architecture
git add README.md docs/software-architecture/architecture-decision-method.md docs/system-design/reliability-and-failure-control.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/ai-architecture/production-ai-assurance.md
git commit -m "docs: connect maintainable architecture notes"
```

---

### Task 6: Register the living notes in the catalogue

**Files:**

- Modify: `CATALOG.md`

**Interfaces:**

- Consumes: four complete canonical note paths.
- Produces: unique current entries and an accurate remaining-migrations list.

- [ ] **Step 1: Add the exact rows after the eight current artifacts**

```markdown
| Architecture Decision Method | Software architecture | [docs/software-architecture/architecture-decision-method.md](docs/software-architecture/architecture-decision-method.md) | Markdown | Current | Living | 2026-09-05 |
| Reliability and Failure Control | System design | [docs/system-design/reliability-and-failure-control.md](docs/system-design/reliability-and-failure-control.md) | Markdown | Current | Living | 2026-09-05 |
| Durable Workflows and Idempotency | Cross-cutting patterns | [docs/cross-cutting-patterns/durable-workflows-and-idempotency.md](docs/cross-cutting-patterns/durable-workflows-and-idempotency.md) | Markdown | Current | Living | 2026-09-05 |
| Production AI Assurance | AI architecture | [docs/ai-architecture/production-ai-assurance.md](docs/ai-architecture/production-ai-assurance.md) | Markdown | Current | Living | 2026-09-05 |
```

- [ ] **Step 2: Make Later migrations contain only the focused-notes item**

```markdown
## Later migrations

This candidate is intentionally not listed as current until it receives a separate public-safety, freshness, provenance, and canonical-version review:

1. **Focused architecture notes** — distil enduring material from the reasoning-model guide, CS336 model/inference notebook, CS329A self-improving-agent notes, and relevant course or certification material. Complete AWS certification packs remain outside repository scope.
```

- [ ] **Step 3: Validate and commit**

```bash
test "$(rg -c '^\| Architecture Decision Method \|' CATALOG.md)" -eq 1
test "$(rg -c '^\| Reliability and Failure Control \|' CATALOG.md)" -eq 1
test "$(rg -c '^\| Durable Workflows and Idempotency \|' CATALOG.md)" -eq 1
test "$(rg -c '^\| Production AI Assurance \|' CATALOG.md)" -eq 1
test "$(rg -c '\| Markdown \| Current \| Living \| 2026-09-05 \|$' CATALOG.md)" -eq 4
! rg -q 'Modular Markdown extraction' CATALOG.md
test "$(rg -c 'Focused architecture notes' CATALOG.md)" -eq 1
test "$(rg -c 'Complete AWS certification packs remain outside repository scope' CATALOG.md)" -eq 1
git diff --check -- CATALOG.md
git add CATALOG.md
git commit -m "docs: catalogue modular architecture notes"
```

---

### Task 7: Run integrated quality, safety, and provenance verification

**Files:** Verify `README.md`, `CATALOG.md`, the four notes, and unchanged `handbooks/` and `learning-paths/`.

**Interfaces:**

- Consumes: complete branch content.
- Produces: fresh evidence that the branch satisfies the approved spec.

- [ ] **Step 1: Validate all note contracts**

```bash
python3 - <<'PY'
from pathlib import Path
notes = [
    Path('docs/software-architecture/architecture-decision-method.md'),
    Path('docs/system-design/reliability-and-failure-control.md'),
    Path('docs/cross-cutting-patterns/durable-workflows-and-idempotency.md'),
    Path('docs/ai-architecture/production-ai-assurance.md'),
]
required = [
    '## Purpose and scope', '## First-principles model',
    '## Core decisions and trade-offs', '## Failure modes and warning signs',
    '## Practical decision checklist', '## Worked architecture scenario',
    '## Feynman questions', '## Related canonical notes',
    '## Sources and review status',
]
for note in notes:
    text = note.read_text(encoding='utf-8')
    positions = [text.index(heading) for heading in required]
    assert positions == sorted(positions), f'heading order: {note}'
    assert all(text.count(heading) == 1 for heading in required), f'heading count: {note}'
    words = len(text.split())
    assert 1200 <= words <= 1800, f'word count {words}: {note}'
    for field in ('**Status:** Current', '**Edition:** Living', '**Last reviewed:** 2026-09-05'):
        assert text.count(field) == 1, f'{field}: {note}'
print('note contracts: PASS')
PY
```

- [ ] **Step 2: Validate local Markdown links**

```bash
python3 - <<'PY'
from pathlib import Path
import re
files = [
    Path('README.md'),
    Path('CATALOG.md'),
    Path('docs/software-architecture/architecture-decision-method.md'),
    Path('docs/system-design/reliability-and-failure-control.md'),
    Path('docs/cross-cutting-patterns/durable-workflows-and-idempotency.md'),
    Path('docs/ai-architecture/production-ai-assurance.md'),
]
failures = []
pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for source in files:
    text = source.read_text(encoding='utf-8')
    for target in pattern.findall(text):
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        path_part, _, fragment = target.partition('#')
        resolved = (source.parent / path_part).resolve()
        if not resolved.exists(): failures.append(f'{source}: missing {target}')
        elif fragment and resolved.suffix == '.md':
            destination = resolved.read_text(encoding='utf-8').lower()
            if fragment.replace('-', ' ') not in destination:
                failures.append(f'{source}: unresolved fragment {target}')
assert not failures, '\n'.join(failures)
print('local links: PASS')
PY
```

- [ ] **Step 3: Verify all eight artifacts are represented**

```bash
notes=(docs/software-architecture/architecture-decision-method.md docs/system-design/reliability-and-failure-control.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/ai-architecture/production-ai-assurance.md)
for source in 'handbooks/system-design/system-design-concept-handbook-v5.html' 'handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html' 'handbooks/ai-engineering/ai-engineering-handbook-v3.0.html' 'learning-paths/software-architect/software-architect-curriculum-guide-v3.md' 'learning-paths/software-architect/software-architect-grooming-programme-v5.html' 'handbooks/fde/fde-handbook-v1.3.html' 'handbooks/ai-architecture/ai-architects-handbook-v1.2.html' 'learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html'; do rg -Fq "$source" "${notes[@]}"; done
```

- [ ] **Step 4: Review canonical ownership manually from targeted matches**

```bash
rg -n -i 'quality attribute|ADR|decision hypothesis|reversal trigger' docs/*/*.md
rg -n -i 'retry budget|backpressure|load shedding|error budget|RPO|RTO' docs/*/*.md
rg -n -i 'idempotency key|transactional outbox|checkpoint|compensation|reconciliation' docs/*/*.md
rg -n -i 'production gates|autonomy|evaluation|cost per successful outcome|adoption' docs/*/*.md
```

Expected: full definitions live only in their owner note; other matches are boundary statements, scenario applications, or links.

- [ ] **Step 5: Verify every external reference**

```bash
rg -No 'https://[^)> ]+' docs/software-architecture/architecture-decision-method.md docs/system-design/reliability-and-failure-control.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/ai-architecture/production-ai-assurance.md | sed 's/^[^:]*://' | sort -u
```

Open every URL and confirm the authority and cited claim. Recheck OpenTelemetry GenAI convention status on `2026-09-05`; remove an unconfirmed status claim while retaining durable guidance.

- [ ] **Step 6: Run public-safety and provenance scans**

```bash
targets=(README.md CATALOG.md docs/software-architecture/architecture-decision-method.md docs/system-design/reliability-and-failure-control.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/ai-architecture/production-ai-assurance.md)
! rg -n --ignore-case 'password\s*[:=]|api[_ -]?key\s*[:=]|bearer\s+[a-z0-9._-]+|authorization\s*:|BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY' "${targets[@]}"
! rg -n --ignore-case 'immigration|visa|confidential client|internal only|private conversation|conversation transcript' "${targets[@]}"
! rg -n 'turn[0-9]+(search|view|fetch)|chatcmpl-|conversation[_ -]?id|tool[_ -]?call[_ -]?id|<!--' "${targets[@]}"
! rg -n --ignore-case 'generated by (chatgpt|codex)|prompt\s*:' "${targets[@]}"
```

Expected: zero matches. Abstract technical terms are acceptable only when they reveal no credential or hidden provenance.

- [ ] **Step 7: Verify immutability and exact branch file set**

```bash
git diff --exit-code e7630cccc4a394dd7d83b2c05e489db91337bb4a -- handbooks learning-paths
git diff --name-only e7630cccc4a394dd7d83b2c05e489db91337bb4a...HEAD | sort > /tmp/modular-actual-files.txt
printf '%s\n' CATALOG.md README.md docs/ai-architecture/production-ai-assurance.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/software-architecture/architecture-decision-method.md docs/superpowers/plans/2026-09-05-modular-markdown-foundation.md docs/superpowers/specs/2026-09-05-modular-markdown-foundation-design.md docs/system-design/reliability-and-failure-control.md > /tmp/modular-expected-files.txt
diff -u /tmp/modular-expected-files.txt /tmp/modular-actual-files.txt
git diff --check e7630cccc4a394dd7d83b2c05e489db91337bb4a...HEAD
git status --short
```

Expected: artifacts unchanged, file lists identical, whitespace clean, worktree clean.

---

### Task 8: Obtain independent review and open the pull request

**Files:** Review all files listed in Task 7; modify only for verified findings.

**Interfaces:**

- Consumes: clean, validated branch.
- Produces: independently reviewed GitHub pull request targeting `main`; it remains unmerged.

- [ ] **Step 1: Invoke `superpowers:requesting-code-review`**

Review the diff from `e7630cccc4a394dd7d83b2c05e489db91337bb4a` to `HEAD` for canonical ownership, faithful eight-source synthesis, first-principles clarity, trade-offs, failures, checklists, scenarios, Feynman questions, freshness, link accuracy, public safety, provenance, navigation/catalogue correctness, and source-artifact immutability. Classify findings as Critical, Important, or Minor with exact paths and passages.

Expected: no Critical or unresolved Important findings.

- [ ] **Step 2: Resolve verified findings and repeat Task 7**

If corrections are required:

```bash
git add README.md CATALOG.md docs/software-architecture/architecture-decision-method.md docs/system-design/reliability-and-failure-control.md docs/cross-cutting-patterns/durable-workflows-and-idempotency.md docs/ai-architecture/production-ai-assurance.md
git commit -m "docs: address modular notes review"
```

Repeat every Task 7 command from fresh output.

- [ ] **Step 3: Push without force**

```bash
git push -u origin docs/modular-markdown-foundation
```

- [ ] **Step 4: Open the PR with the GitHub plugin**

Use repository `arvindsoni2/Architect`, head `docs/modular-markdown-foundation`, base `main`, title `docs: add modular Markdown foundation`, and this body:

```markdown
## Summary
- add four cross-source canonical Markdown notes
- define single ownership for decision method, reliability, durable workflows, and production AI assurance
- update README domain navigation and register the living notes in CATALOG
- retain all eight published source artifacts unchanged

## Validation
- required section order and 1,200–1,800-word range checked for all notes
- local links and all eight-artifact source coverage checked
- external primary references and time-sensitive claims reviewed
- canonical-definition, public-safety, and provenance scans completed
- source-artifact immutability and git diff checks passed
- independent review completed with no unresolved Critical or Important findings

## Provenance notice
The notes intentionally include visible source links, review status, edition, and last-reviewed dates. They contain no hidden authoring-tool or conversation metadata.

Review only: please do not merge automatically.
```

- [ ] **Step 5: Report and stop before merge**

Provide the PR link, four note titles, final validation evidence, and visible-provenance warning. State that the PR is review-only and unmerged.
