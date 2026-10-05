# Connect the dots: decision models and forward deployed architecture

Use this route when you can explain a concept in one guide but need to connect it to implementation, assurance or customer delivery. Each guide remains independent. The links below identify the owner of each explanation; do not repeat its full content elsewhere.

**Reviewed:** 2026-09-28 · **Scope:** decision models and forward deployed architecture. Examples are exercises, not measured deployments or claims of role readiness.

## Choose your entry point

| Your question | Understand | Build | Evaluate | Deliver |
| --- | --- | --- | --- | --- |
| Should this step use rules, a classifier, Jev/Laya or an LLM? | [Decision mechanism selection](../docs/ai-architecture/reasoning-system-design.md#decision-mechanism-selection) | [Engineering Practice: decision-model comparison](../handbooks/ai-engineering/ai-engineering-handbook-v3.2.html#t-practice) | [Decision-model acceptance](../docs/ai-architecture/production-ai-assurance.md#decision-model-acceptance) | [Cost per successful outcome](../handbooks/fde/fde-handbook-v1.4.html#value) |
| How do I put a fast decision inside an agent safely? | [Decision boundaries](../docs/ai-architecture/reasoning-system-design.md#decision-mechanism-selection) | [Bounded routing exercise](../handbooks/agent-engineering/agent-engineering-master-manual-v2.8.html#decision-model-workflow) | [Durable workflows and idempotency](../docs/cross-cutting-patterns/durable-workflows-and-idempotency.md) | [FDE production gates](../handbooks/fde/fde-handbook-v1.4.html#delivery) |
| What does a forward deployed architect own? | [Role and responsibility](../handbooks/fde/fde-handbook-v1.4.html#forward-deployed-architect) | [Optional curriculum pathway](software-architect/software-architect-curriculum-guide-v3.md#forward-deployed-architecture-pathway) | [Programme assessment](software-architect/software-architect-grooming-programme-v5.html#assessment) | [Engagement capstone](../handbooks/fde/fde-handbook-v1.4.html#capstone) |
| How do I defend this in an interview? | [AI architecture bridge](../handbooks/ai-architecture/ai-architects-handbook-v1.2.html#decision-model-architecture) | [Connected project cases](software-architect/connected-learning/README.md) | [Production AI assurance](../docs/ai-architecture/production-ai-assurance.md) | [Behavioural and architecture interview drills](ai-ml-interview/interview-resource-accelerator-v4.4.html#behavioural) |

Tabbed guides open the named panel; use its “Connect the dots” block for the exercise. Keep the evidence packet below as you move between guides so each jump answers a concrete question.

## One connected exercise

Use a synthetic support-ticket workflow. The customer asks for an agent that “handles everything”. Reframe the first useful outcome as fewer misrouted tickets without increasing missed urgent cases. No refunds or account changes are authorised by the exercise.

1. **Understand:** write an ADR using the [Architecture Decision Method](../docs/software-architecture/architecture-decision-method.md). Compare rules, a conventional classifier, a typed decision model and a generative baseline. State the evidence that would reverse your choice.
2. **Build:** complete the AI Engineering comparison, then the Agent Engineering failure exercise. Reuse the same labels, case IDs and decision contract. Jev access is optional; mark unavailable candidates as not evaluated. A mock proves integration behaviour only.
3. **Evaluate:** apply decision-model acceptance criteria to both the selected component and the complete workflow. Show which cases were accepted, escalated, misrouted or rejected. Keep calibration/development and final test cases separate.
4. **Deliver:** use the FDE capstone to assign architecture, implementation, workflow and service ownership. Present a scale, hold or stop recommendation using the six production gates.
5. **Defend:** explain the decision in five minutes, then repeat with a tighter latency budget, missing evidence, a new language or an unavailable model provider.

## Evidence to carry between guides

| Artifact | Keep consistent | Update when |
| --- | --- | --- |
| Problem and baseline | Workflow, users, decision owner, outcome metric | Discovery changes the problem |
| Decision contract | Permitted inputs, labels, unknown path, schema and policy versions | Meaning or action boundary changes |
| Evaluation packet | Case IDs, label provenance, splits, metrics and segments | Data or model changes |
| Operational evidence | Latency, fallback, failures, replay and rollback results | Integration or deployment changes |
| Delivery decision | Named owners, accepted risks, adoption evidence and reversal trigger | Rollout authority changes |

A diagram or proposed target is a hypothesis until an experiment supports it. Label simulated stakeholder feedback and synthetic data. Public portfolio work must not contain confidential records.

## Continue into another project

Apply the same sequence to [inventory intelligence](software-architect/connected-learning/inventory-intelligence.md), [legacy modernisation](software-architect/connected-learning/legacy-modernisation.md) or the [patient portal](software-architect/patient-portal-connected-learning.md). Transfer the method; derive new labels, risk limits and acceptance thresholds for each domain. AWS study remains available through those project guides; decision-model experiments are not SAA-C03 exam requirements.

## Maintenance rule

Keep **Understand → Build → Evaluate → Deliver** labels consistent. Link to the owning section and include a return to this route. Retain stable paths and verify fragments in the rendered guide, especially where tabs hide content. Refresh dated product and vacancy evidence at its canonical source; a navigation-only edit does not imply a full handbook audit.
