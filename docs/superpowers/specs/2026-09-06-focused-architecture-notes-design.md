# Focused Architecture Notes — Design

**Status:** Approved design

**Repository:** `arvindsoni2/Architect`

**Date:** 2026-09-06

**Visibility:** Public, curated

**Delivery branch:** `docs/focused-architecture-notes`

## 1. Purpose

Complete the repository's focused-architecture-note migration by distilling durable material from the CS336 model and inference notebook, the reasoning-model visual guide, the CS329A self-improving-agent notes, and the current repository handbooks into four narrowly owned Markdown notes.

This is synthesis, not course conversion. The notes will explain the few system relationships that govern most architecture decisions, expose trade-offs and failure modes, and give readers a compact way to test their understanding. The source notebooks, guides, and handbooks remain the richer learning material.

## 2. Scope

The pull request will create these stable, unversioned paths:

1. `docs/ai-architecture/llm-inference-systems.md`
2. `docs/ai-architecture/reasoning-system-design.md`
3. `docs/ai-architecture/model-adaptation-and-training.md`
4. `docs/agent-architecture/self-improving-agent-systems.md`

It will also update `README.md` and `CATALOG.md` so the new notes are directly discoverable. Existing handbooks, learning paths, and the four canonical notes published in the modular Markdown foundation remain unchanged.

### Non-goals

- Do not import, publish, or convert complete course notebooks, book chapters, lecture notes, certification packs, or their page images.
- Do not reproduce copyrighted wording, diagrams, exercises, code, or a source's chapter order.
- Do not create a CUDA programming tutorial, kernel-optimisation manual, mathematical derivation guide, or end-to-end model-training course.
- Do not prescribe one inference engine, model family, framework, cloud, or agent platform.
- Do not repeat production-release controls, generic reliability patterns, durable-workflow mechanics, or ADR guidance already owned by existing canonical notes.
- Do not present recursive self-improvement, model-generated evaluation, or chain-of-thought visibility as inherently safe or reliable.
- Do not add a website, generated navigation, binary assets, or automated source ingestion.
- Complete AWS certification packs remain outside repository scope.

## 3. Editorial and evidence approach

Each note will use the repository's standing learning model:

1. **Pareto:** lead with the small set of mechanisms that explain most architecture behaviour.
2. **First principles:** derive decisions from computation, memory, feedback, uncertainty, and consequence rather than product labels.
3. **Feynman:** end with questions that require a reader to explain the system plainly and apply it to a new case.

The editing process will:

1. Extract load-bearing mechanisms, constraints, trade-offs, metrics, and failure modes from the source set.
2. Group equivalent concepts across the sources and existing handbooks.
3. Assign each concept one canonical home using the ownership rules below.
4. Rewrite the synthesis in original, plain language; use quotations only when strictly necessary and legally supportable.
5. Prefer durable guidance; qualify any retained benchmark, API, product, or research claim with its applicable date or experimental context.
6. Link to public primary sources for claims that require external support.
7. Cross-link existing canonical notes instead of re-explaining their material.

The target is approximately 1,100–1,600 words per note. This keeps the four-note pull request reviewable while leaving enough room for one coherent scenario, one or two compact diagrams, and the required provenance.

## 4. Canonical notes and ownership

### 4.1 LLM Inference Systems

**Path:** `docs/ai-architecture/llm-inference-systems.md`

**Purpose:** Explain how autoregressive model behaviour becomes a serving-capacity, latency, memory, and cost problem.

**Canonical ownership:**

- prefill versus decode;
- model weights, KV cache, temporary buffers, and runtime overhead;
- compute-bound versus memory-bandwidth-bound work;
- static, dynamic, and continuous batching as scheduling choices;
- concurrency, saturation, queueing, and fairness;
- time to first token, inter-token latency, throughput, cache pressure, and cost per accepted outcome;
- correlation of application, inference-engine, and GPU signals;
- capacity tests and bottleneck-driven optimisation.

**Boundary:** It may name quantisation, paged KV management, kernel fusion, speculative decoding, and parallel placement as levers, but it will explain when they matter rather than teach their implementation. Training and behavioural evaluation belong elsewhere.

**Principal sources:**

- CS336 Handwritten Visual Notebook, especially inference and GPU-systems sections;
- AI Engineering Handbook v3.0;
- Agent Engineering Master Manual v2.7;
- The AI Architect's Handbook v1.2.

**Worked scenario:** Diagnose a serving endpoint whose throughput rises with concurrency while tail latency, queue time, and KV pressure become unacceptable. The scenario will separate prefill, decode, scheduler, engine, and hardware hypotheses before selecting an optimisation.

### 4.2 Reasoning System Design

**Path:** `docs/ai-architecture/reasoning-system-design.md`

**Purpose:** Explain how a system allocates extra inference work to improve multi-step outcomes without confusing longer traces with correctness.

**Canonical ownership:**

- reasoning as a multi-step inference behaviour rather than proof of correctness;
- parser, normaliser, verifier, scorer, and judgment roles;
- inference-time scaling through width, depth, and selection;
- majority voting, best-of-N, search, critique, and self-refinement;
- adaptive compute budgets and stopping rules;
- generator-verifier gaps, correlated errors, evaluator exploitation, and cost/latency trade-offs;
- choosing deterministic tools or bounded workflows when they provide stronger evidence.

**Boundary:** This note owns inference-time methods. SFT, reinforcement learning, distillation, and weight updates are delegated to Model Adaptation and Training. Production acceptance thresholds and rollout gates remain in Production AI Assurance.

**Principal sources:**

- Build a Reasoning Model visual chapter guide and its public companion repository;
- CS329A Self-Improving AI Agents notes, especially test-time compute and verification;
- Agent Engineering Master Manual v2.7;
- Production AI Assurance.

**Worked scenario:** Route mixed reasoning requests through a cheap single pass, bounded refinement, or multi-candidate search according to difficulty, consequence, verifier quality, and budget.

### 4.3 Model Adaptation and Training

**Path:** `docs/ai-architecture/model-adaptation-and-training.md`

**Purpose:** Provide an architectural decision guide for changing model behaviour with curated examples, successful trajectories, distillation, or verifiable rewards.

**Canonical ownership:**

- deciding whether to change prompts, the harness, retrieval, tools, or model weights;
- data curation, task distribution, contamination, and train/evaluation separation;
- supervised fine-tuning as behavioural imitation;
- distillation as capability and cost transfer with possible loss;
- reinforcement learning with verifiable rewards and group-relative optimisation at a conceptual level;
- reward design, parser/verifier integrity, reward hacking, and capability collapse;
- experiment lineage, reproducibility, offline comparison, staged release, and rollback.

**Boundary:** The note will not teach gradient derivations, optimizer internals, distributed training, or framework-specific code. Inference-time reasoning is delegated to Reasoning System Design; operational release evidence is delegated to Production AI Assurance.

**Principal sources:**

- Build a Reasoning Model visual chapter guide and its public companion repository;
- CS329A Self-Improving AI Agents notes;
- CS336 Handwritten Visual Notebook where it explains scaling, training systems, and evaluation constraints;
- AI Engineering Handbook v3.0;
- Production AI Assurance.

**Worked scenario:** Improve a code-repair model by comparing a better harness, SFT on reviewed examples, distillation of verified trajectories, and RL with test-based rewards. The decision will expose data, verifier, compute, regression, and rollback requirements.

### 4.4 Self-Improving Agent Systems

**Path:** `docs/agent-architecture/self-improving-agent-systems.md`

**Purpose:** Explain how an agent system can learn from execution evidence while keeping improvement bounded, observable, reversible, and subject to human authority.

**Canonical ownership:**

- the generate–execute–score–filter–learn–retest loop;
- the separation between test-time search, system configuration changes, memory updates, and model-weight updates;
- evidence quality, verifier coverage, human judgment, and the generator-verifier gap;
- trajectory selection, synthetic-data lineage, and feedback contamination;
- autonomy proportional to verifiability, reversibility, and consequence;
- sandboxing candidate changes, promotion gates, canary release, rollback, and kill controls;
- memory admission and expiry rules;
- reward hacking, evaluator drift, distribution shift, correlated failures, runaway loops, and self-confirming data.

**Boundary:** Generic workflow durability belongs in Durable Workflows and Idempotency; timeouts and overload belong in Reliability and Failure Control; production-AI acceptance evidence belongs in Production AI Assurance. This note will not claim that open-ended autonomous self-modification is production-ready.

**Principal sources:**

- CS329A Self-Improving AI Agents notes;
- Agent Engineering Master Manual v2.7;
- The AI Architect's Handbook v1.2;
- Forward Deployed AI Engineer Handbook v1.3;
- Production AI Assurance and Durable Workflows and Idempotency.

**Worked scenario:** Let a support agent propose prompt, routing, tool, or memory-policy changes from reviewed incidents. Candidate changes run in an isolated evaluation environment and reach production only through explicit evidence, approval, canary, monitoring, and rollback gates.

## 5. Shared note contract

Every note will use these top-level sections in this order:

1. **Purpose and scope** — the problem the note owns and the adjacent concerns it delegates.
2. **Pareto summary** — three to five ideas that explain most design outcomes.
3. **First-principles model** — the underlying system mechanics and one compact diagram where useful.
4. **Core decisions and trade-offs** — the choices, conditions, and consequences an architect must evaluate.
5. **Failure modes and warning signs** — recurrent ways the design produces false confidence or operational harm.
6. **Practical decision checklist** — evidence-oriented review questions rather than generic advice.
7. **Worked architecture scenario** — one coherent application of the model and its compromises.
8. **Feynman questions** — short teach-back and transfer questions.
9. **Related canonical notes** — relative links at meaningful topic boundaries.
10. **Sources and review status** — contributing repository artifacts, concise public references, and the visible status block.

Each note will finish with:

```markdown
**Status:** Current

**Edition:** Living

**Last reviewed:** 2026-09-06
```

## 6. Concept ownership and cross-linking

| Concept | Canonical home | Treatment elsewhere |
| --- | --- | --- |
| Prefill, decode, KV pressure, serving saturation | LLM Inference Systems | Other notes link to inference cost and latency rather than restating serving mechanics. |
| Test-time reasoning, candidate search, refinement, selection | Reasoning System Design | Agent and training notes describe why they invoke the method, not how it works. |
| SFT, RLVR, distillation, weight-changing experiments | Model Adaptation and Training | Reasoning remains inference-only; agent improvement distinguishes model updates from system updates. |
| Feedback flywheels, memory-policy change, promotion and rollback | Self-Improving Agent Systems | Model training owns weight updates; durable workflows own restart correctness. |
| Offline/online acceptance evidence and staged production rollout | Production AI Assurance | New notes state the needed interface and link to the existing control model. |
| Timeouts, retries, overload, failure containment | Reliability and Failure Control | Inference and agent notes identify applicable failure pressure and delegate the control mechanics. |
| Checkpoints, idempotency, replay, compensation | Durable Workflows and Idempotency | Self-improving agents use the pattern without redefining it. |
| ADRs and evidence-based architecture selection | Architecture Decision Method | Each worked scenario can reference the method rather than repeat it. |

When sources appear to disagree, the notes will expose the governing condition. For example, extra inference samples help only when candidates contain diverse useful attempts and selection is reliable; distillation is attractive when repeated test-time work can be transferred without unacceptable capability loss; autonomy can expand only when feedback and consequences justify it.

## 7. Diagrams

Use Mermaid only where topology or sequence is materially clearer than prose. Each note may contain one or two compact diagrams:

- LLM Inference Systems: request flow across queue, prefill, KV state, and iterative decode; optionally a saturation relationship described in prose or a table rather than a decorative chart.
- Reasoning System Design: adaptive width/depth/selection loop with verifier and stopping rule.
- Model Adaptation and Training: evidence-to-dataset-to-experiment-to-gated-release flow.
- Self-Improving Agent Systems: bounded improvement loop with an explicit production trust boundary.

Diagrams must remain readable in raw Markdown, avoid product-specific iconography, and use no copied course or book artwork.

## 8. Source coverage and provenance

The source plan is:

| Source | Inference | Reasoning | Adaptation | Self-improving agents |
| --- | :---: | :---: | :---: | :---: |
| CS336 visual notebook | Yes |  | Yes |  |
| Reasoning-model visual guide and public companion |  | Yes | Yes |  |
| CS329A self-improving-agent notes |  | Yes | Yes | Yes |
| AI Engineering Handbook v3.0 | Yes |  | Yes |  |
| Agent Engineering Master Manual v2.7 | Yes | Yes |  | Yes |
| The AI Architect's Handbook v1.2 | Yes |  |  | Yes |
| Forward Deployed AI Engineer Handbook v1.3 |  |  |  | Yes |
| Existing canonical Markdown notes |  | Yes | Yes | Yes |

Library source assets guide synthesis but will not be copied into the repository or linked through private Library identifiers. Their source sections will instead identify the material by title and link to the appropriate public course, author, repository, paper, or handbook where available.

Every note must make provenance visible through contributing repository links, numbered public references, status, edition, and review date. It must contain no hidden metadata, prompts, conversation identifiers, private excerpts, authoring-tool identifiers, or unsupported personal examples.

## 9. Repository navigation and catalogue changes

### README

- Add the four notes to **Maintainable notes**, grouped under AI architecture and Agent architecture.
- Change the Agent architecture domain link to `docs/agent-architecture/` now that the directory exists.
- Preserve direct access to the Agent Engineering Master Manual as a richer published artifact.
- Avoid adding another navigation hierarchy or repeating the catalogue.

### Catalogue

- Add one row for each note with format `Markdown`, status `Current`, edition `Living`, and last reviewed `2026-09-06`.
- Remove **Focused architecture notes** from **Later migrations**, because this pull request completes that item.
- Remove the now-empty **Later migrations** section unless another reviewed candidate exists at implementation time.
- Retain the repository-scope statement that complete course notebooks and certification packs are not repository artifacts.

## 10. Validation

Before the pull request is opened, verify:

1. All four notes exist at the approved stable paths and contain the ten required top-level sections in order.
2. Each note remains within the agreed review-size range unless a clearly justified exception is recorded.
3. Every concept in the ownership table has one canonical home and substantive boundary references use relative links.
4. Repository links, cross-note links, README links, and catalogue paths resolve.
5. Public references resolve, are primary where practical, and substantively support the associated claims.
6. No course transcript, copyrighted diagram, long quotation, private Library URL, certification pack, or binary source asset has been imported.
7. Volatile claims are verified and dated or removed; research results are labelled as experimental evidence rather than universal laws.
8. No credentials, personal/contact/immigration data, confidential client material, internal URL, hidden provenance, conversation metadata, or unsupported factual claim is present.
9. Mermaid syntax and Markdown structure are mechanically checked.
10. `README.md` and `CATALOG.md` remain internally consistent, paths and titles are unique, and the completed migration entry is removed.
11. Existing handbooks, learning paths, and canonical notes are byte-for-byte unchanged.
12. `git diff --check` reports no whitespace errors.

The completed branch will receive independent content and implementation review. Findings will be resolved on the branch, and the pull request will remain unmerged for the repository owner to review.

## 11. Delivery and isolation

Implementation will occur only in the isolated worktree on `docs/focused-architecture-notes`, based on merged `origin/main` at `59cf1fef630bb98d8aff1b08d44e6b3c9450bd3a`.

The unrelated modification to `handbooks/ai-engineering/ai-engineering-handbook-v3.0.html` in the original checkout must not be staged, overwritten, reformatted, or committed. The pull request will contain the approved specification, implementation plan, four focused notes, and navigation/catalogue updates. It will not merge automatically.
