# Production AI Assurance

## Purpose and scope

Production AI assurance is the evidence and controls that justify letting an AI system influence real work. Model capability is necessary, but fitness also requires value, consequence-aware quality, safety, operability, viable economics, and adoption in the actual workflow.

This note owns AI-specific evaluation evidence, acceptance gates, autonomy levels, human escalation, AI observability, unit economics, adoption, phased rollout, production acceptance, and behavioural rollback. It deliberately delegates generic quality-attribute scenarios, alternatives, and ADRs to the [Architecture Decision Method](../software-architecture/architecture-decision-method.md); infrastructure failure containment and recovery to [Reliability and Failure Control](../system-design/reliability-and-failure-control.md); and duplicate-safe side effects, checkpoints, and compensation to [Durable Workflows and Idempotency](../cross-cutting-patterns/durable-workflows-and-idempotency.md).

## First-principles model

Use one evidence loop:

`task and consequence → representative cases → component/workflow/outcome evaluation → threshold → bounded authority → production signals → scale/hold/narrow/stop`

Start with the unit of work and the harm of a wrong, missing, delayed, or unauthorized result. Build cases from real tasks, important segments, boundaries, and adversarial behaviour. Evaluate parts, workflow, and outcome because success at one level cannot prove the others. Set thresholds from the non-AI baseline, consequence, measurement uncertainty, and accountable owner's risk tolerance—not a generic accuracy target. Grant only supported authority, compare production with evaluation assumptions, and turn new failures into cases.

This treats risk management as part of design, development, use, and evaluation, matching the stated scope of the NIST AI RMF [1].

Production readiness is the **intersection**, not the average, of six gates:

| Gate | Evidence question | If it fails |
| --- | --- | --- |
| Value | Does the workflow beat the current process or a credible non-AI alternative on a worthwhile outcome? | Redesign or stop. |
| Quality | Does the system meet consequence- and segment-aware criteria on representative work? | Improve or narrow scope. |
| Safety | Are authority, abuse, security, privacy, policy, and consequential failures bounded? | Reduce influence or block release. |
| Operability | Can owners observe, diagnose, contain, change, and roll back it? | Keep it outside production influence. |
| Economics | Is cost per successful outcome viable at realistic volume? | Change architecture, scope, or investment. |
| Adoption | Can representative users use it correctly, understand limits, and escalate? | Repair workflow fit before scaling. |

Strong quality cannot compensate for unsafe authority; low inference cost cannot compensate for unusable work.

## Core decisions and trade-offs

- **Evaluation contract:** Name the decision, population, evaluation unit, risk segments, dataset and system versions, graders, acceptance owner, thresholds, limitations, and review trigger. Response scoring is cheap but can miss a wrong tool action or failed outcome; workflow scoring is realistic but costlier. Cover common, rare severe, ambiguous, missing-evidence, tool-failure, and adversarial cases. Preserve held-out evidence and add de-identified production failures.
- **Evaluator portfolio:** Use deterministic checks for schema, citations, permissions, tool arguments, and prohibited actions. Use calibrated model judges for rubric-bound nuance, comparing disagreements with representative human labels. Use domain review for high-consequence ambiguity. Current OpenAI guidance likewise recommends task-specific cases reflecting production distributions and human calibration [2]. Link component measures to workflow completion and outcomes. Outcome-only evaluation may reward luck; trajectory-only evaluation may punish a valid path.
- **Segment thresholds:** Averages describe a mixture, not who was harmed. Define task, user, language, risk, and failure-mode segments. Justify thresholds by consequence and measurement quality. Route weak or undersampled segments to assistance, human review, or refusal.
- **Autonomy boundary:** In **shadow**, the system drafts without live influence. In **assist**, it recommends and a person acts. In **supervised action**, it executes only after approval where consequences begin. In **bounded autonomy**, it acts inside deterministic scope, tool, data, time, spend, and reversibility limits. Promotion requires evidence about added authority; deterioration moves it down the ladder. A human needs context, authority, and safe rejection or escalation.
- **AI observability:** Join an outcome to a run, system/model/prompt/policy versions, retrieval and tools, decisions, approvals, escalation, latency, usage, cost, errors, and scores. Prefer metadata, stable identifiers, hashes, classifications, and derived signals. Capture content only for a named diagnostic need with access, retention, and redaction controls. As of 2026-09-05, OpenTelemetry's GenAI conventions moved repositories and remain **Development**; pin the version behind a mapping layer [3].
- **Economics and adoption:** Measure cost per *accepted successful outcome*, not tokens per call. Include models, tools, retrieval, storage, infrastructure, retries, failures, evaluation, telemetry, human review, support, and change; expose quality or latency sacrificed by optimization. Assign workflow, representative-user, operational, and risk ownership.
- **Rollout, acceptance, and rollback:** Promotion is evidence-driven, not elapsed time or a fixed percentage. Before handoff, name product, workflow, technical, incident, and acceptance owners; transfer access; prove dashboards, escalation, support, and rollback; record limitations and a dated scale, hold, narrow, or stop decision. Reduce authority when safety, segment quality, lineage, adoption, economics, or unresolved incidents invalidate evidence.

## Failure modes and warning signs

- **Demo as evidence:** curated prompts and a cooperative environment substitute for representative cases and a baseline.
- **Average as permission:** a headline score hides a risky language, workflow, user, or consequence segment.
- **Uncalibrated judge:** a model grader is trusted without human comparison, disagreement analysis, or a versioned rubric.
- **Stale evaluation:** policy, users, tools, attacks, or production tasks change while the dataset and threshold remain frozen.
- **One-level evaluation:** outcome-only scoring misses unsafe paths; trajectory-only scoring rejects safe paths that differ from the reference.
- **Accuracy grants authority:** a behavioural average is treated as permission for consequential action without deterministic policy and approval controls.
- **Trace everything:** sensitive prompts, retrieved records, tool arguments, or identities enter telemetry by default and outlive their purpose.
- **Token cost as economics:** dashboards omit review, retries, failures, tools, support, and the denominator of accepted outcomes.
- **Adoption at the end:** representative users first encounter the system after design, so overrides, workarounds, and support load appear late.
- **Calendar-driven promotion:** a stage advances because the pilot period ended, not because all six gates remain supported.

## Practical decision checklist

- What real workflow outcome and credible non-AI baseline define value?
- What is the evaluation unit, and what are the consequences of important errors?
- Which representative, boundary, adversarial, and underserved segments are explicit?
- Can each result be traced to the dataset, rubric, grader, system, and environment versions?
- Who owns acceptance, and why are the thresholds appropriate to consequence and uncertainty?
- What may the model suggest, what must deterministic code decide, and what must a human approve?
- Where is the consequence boundary, and what rejection, escalation, and safe fallback exist there?
- Which signals connect behaviour, friction, safety, cost, and outcome without unnecessary content?
- What is the cost per accepted successful outcome at realistic volume?
- Are corrections, overrides, abandonment, manual fallback, and support burden measured?
- Has the stop, authority-reduction, rollback, and handoff path been demonstrated?
- What dated scale, hold, narrow, or stop decision was recorded, with limitations and a re-review trigger?

## Worked architecture scenario

An insurer proposes an AI claims-evidence assistant. Adjusters currently search documents, assemble citations, and update cases. The baseline records handling time, rework, unsupported claims, escalation, user effort, and accepted outcomes. Value means improving this workflow, not producing fluent summaries.

The evaluation unit is one evidence package. Cases span claim types, document quality, languages, policy versions, and adjuster experience, plus conflicting sources, insufficient evidence, malicious document instructions, inaccessible records, unavailable tools, and crossed authority boundaries. Each records provenance, expected behaviour, segment, grading, and version lineage.

Component checks verify permissions, retrieval, citations, policy freshness, output structure, and tool arguments. Calibrated judges and claims experts assess support and uncertainty. Workflow evaluation tests retrieval, drafting, citation, stopping, and escalation; outcomes include accepted packages, rework, cycle time, reversals, complaints, and corrections. Baseline-derived thresholds vary by consequence; no average waives a weak high-consequence segment.

Shadow mode runs on eligible cases without changing the live workflow. It exposes distribution shift and tool faults while allowing comparison with human packages. If all six gates hold for defined segments, assist mode shows a labelled draft. Adjusters accept, edit, reject, or escalate; the team measures overrides, abandonment, reliance, and support burden.

The case update is the consequence boundary. An authorized adjuster sees changed fields, citations, uncertainty, and policy version before approval. The durable workflow preserves approval and duplicate-safe execution; assurance specifies why approval is required.

Traces connect a de-identified run to versions, retrieval and tools, policy decisions, approval, latency, usage, costs, and outcome. Raw content is excluded by default; samples require redaction, access, and retention controls. Economics divides full operating cost, including failures, review, evaluation, telemetry, support, and corrections, by accepted successful packages.

Promotion has no preset schedule. The acceptance owner records eligible segments. A privacy breach, consequential unsupported statement, segment regression, failed rollback, broken escalation, adverse outcome, or non-viable cost triggers hold, narrowing, or rollback to shadow. Supervised action needs new action-control evidence; bounded autonomy requires a separate six-gate decision.

## Feynman questions

1. How can a high model score still produce a production system with no value or unsafe authority?
2. Why can one average hide unacceptable risk? Give a segment that should be routed differently.
3. What evidence must change before authority may increase from assist to supervised action?
4. What costs belong in cost per successful outcome that do not appear in a token bill?
5. What can shadow mode reveal, and what can it not prove because the system has no live influence?

## Related canonical notes

- [Architecture Decision Method](../software-architecture/architecture-decision-method.md) owns quality scenarios, alternatives, trade-off reasoning, ADRs, and reversal triggers.
- [Reliability and Failure Control](../system-design/reliability-and-failure-control.md) owns infrastructure failure domains, deadlines, retry budgets, overload control, recovery objectives, and incident learning.
- [Durable Workflows and Idempotency](../cross-cutting-patterns/durable-workflows-and-idempotency.md) owns side-effect correctness under duplicate delivery, restart, partial progress, replay, and compensation.

## Sources and review status

Repository sources:

- [AI Engineering Handbook v3.0](../../handbooks/ai-engineering/ai-engineering-handbook-v3.0.html)
- [Agent Engineering Master Manual v2.7](../../handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)
- [Interview Resource Accelerator v4.3](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html)

External references (verified 2026-09-05):

1. NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — AI RMF 1.0 remains published and is under revision.
2. OpenAI, [Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices) — reviewed as guidance; the page notes that the legacy Evals platform is deprecated.
3. OpenTelemetry, [Generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) and [current GenAI repository](https://github.com/open-telemetry/semantic-conventions-genai/tree/main/docs/gen-ai) — the former page has moved; the current conventions are marked Development.

**Status:** Current

**Edition:** Living

**Last reviewed:** 2026-09-05
