# Shared interview handbook

**Status:** Draft for owner review · **Last reviewed:** 1 October 2026

Use this handbook to explain your judgement. Choose relevant methods and artefacts, connect them to what you did, and show how the outcome changed. Definitions live here; [role guides](../README.md) apply them to different responsibilities. Historical facts live in the [evidence bank](evidence-bank.md).

## Decode the advert before rehearsing

For each important requirement, write: intended outcome; expected decision authority; user or stakeholder; matching example; gap or adjacent experience; likely follow-up. Identify whether the employer needs a product decision-maker, a delivery leader or a project controller. Titles vary, so test the remit with the recruiter.

Distinguish three levels honestly: **direct experience**, **adjacent experience**, and **knowledge you would apply with support**. Certifications demonstrate learning; formal role accountabilities still need examples.

## Behavioural answers

Use **Situation → Responsibility → Decision and Action → Result → Learning**. A familiar STAR structure is also suitable if the decision and learning are explicit.

1. Give enough context to explain the difficulty.
2. State your remit and authority.
3. Describe what you personally decided, the alternative, the trade-off and the action.
4. Explain the result, its measurement and any limit to attribution.
5. State what you changed afterwards or would do differently.

Prepare a 90-second version and a deeper follow-up. An artefact matters because it enabled a decision: a RACI clarified approvals, a RAID log surfaced a blocking dependency, or a prototype overturned an assumption. Naming a method alone does not establish competence.

Use several stories across an interview. Recent Natoora examples show current product and delivery capability; Northern Powergrid adds field adoption and infrastructure complexity; banking examples add regulated and supplier experience. Choose relevance over recency when a question demands a specific kind of evidence.

## Scenario answers

For a hypothetical, explain **assumptions → immediate protection → diagnosis → options → decision → sequence → measures**. Ask a few questions about users, impact, constraints and authority, then proceed with stated assumptions.

If a team is six weeks late after losing its lead, address immediate production, contractual or people risks straight away. Diagnose in parallel through team and stakeholder conversations, current commitments, delivery evidence and dependencies. Establish a small stabilisation plan with owners and dates; then agree a realistic forecast and improvement experiments. A first week of listening must not delay urgent protection.

Define progress in outcomes: reduced blocked time, clearer decisions, a reliable forecast, lower incident exposure or restored client confidence. Avoid promising that a particular ceremony, framework or headcount increase will repair every situation.

## Framework and artefact toolkit

| Decision | Useful tool | Explain its effect | Failure mode |
| --- | --- | --- | --- |
| Who can decide? | RACI or explicit decision-rights record | Owner, consultation and escalation boundary | A matrix with several accountable owners and no decision |
| Who needs what communication? | Stakeholder map and communication plan | Different needs, channels, cadence and feedback | Sending the same report to everyone |
| What could block the outcome? | RAID log, dependency map, pre-mortem | Risk response, owner, trigger, escalation and review | A register without action or closure |
| What should go first? | Cost of delay, MoSCoW, WSJF or an impact/effort comparison | Value, urgency, evidence, effort and opportunity cost | False precision; every item declared a must-have |
| What can we forecast? | Milestone plan, critical path, flow data, burn-up | Dependencies, remaining scope and uncertainty | Comparing velocity across teams or treating it as value |
| What constitutes acceptable completion? | Acceptance criteria and Definition of Done | Item behaviour versus shared quality standard | A checklist that cannot be tested |
| How do we release responsibly? | Readiness checklist, runbook, rollback and staged rollout | Operations, data, security, training and recovery | Treating a sprint review as the sole release gate |
| Why are people resisting? | ADKAR or a change-impact assessment | Awareness, practical ability, support and reinforcement | Labelling legitimate concerns as resistance |
| How do we learn inclusively? | 1-2-4-All, structured retrospective, 5 Whys | Voices heard, causal hypothesis and actionable experiment | Naming a method without changing the work |
| What must executives decide? | Concise decision paper | Recommendation, options, cost, risk and requested decision | Status reporting that hides a required choice |

Use these as choices, not a mandatory stack. Story points do not measure customer value. Definition of Ready is an optional team practice, not a required Scrum artefact. Change governance should match the impact and client context; CAB approval is not universal.

## Applying the toolkit

**Decision rights and stakeholders.** RACI means Responsible, Accountable, Consulted and Informed. Map a small set of consequential decisions, not every activity. Confirm one accountable decision owner and the route when a decision exceeds their authority. A power/interest map can guide communication, but include affected users with little organisational power. In an answer, explain which delayed or duplicated decision the artefact resolved.

**Prioritisation.** MoSCoW distinguishes Must, Should, Could and Won't for the agreed time horizon. A Must requires a clear consequence if omitted; “the stakeholder wants it” is insufficient. WSJF compares cost of delay with job duration or a size proxy. In the SAFe formulation, cost of delay combines relative user/business value, time criticality and risk reduction/opportunity enablement. Dependencies and mandatory controls still constrain the order. Kano can help discuss basic needs, performance expectations and possible delights; validate those categories with users.

**Illustrative WSJF exercise:** option A has relative cost of delay 12 and size 3, giving 4; option B has cost of delay 15 and size 5, giving 3. On that limited evidence A comes first. Explain the scoring uncertainty, whether B enables A and whether either is mandatory. This is a reasoning exercise, not a historical prioritisation decision.

**Risk and forecasting.** RAID records Risks, Assumptions, Issues and Dependencies. A risk needs a response, owner and trigger; an issue needs action now. A pre-mortem asks why a future failure might happen and converts plausible causes into controls or experiments. Critical-path analysis identifies the dependency chain controlling completion under the current plan. Resource constraints or uncertainty can change it. A burn-up separates completed work from total scope; widening scope can explain why a stable completion rate still misses the date.

**Change and coaching.** ADKAR considers Awareness, Desire, Knowledge, Ability and Reinforcement. Diagnose the actual barrier: another training session does not fix a lack of time or tools to use the skill. For organisation-wide change, a coalition, clear purpose, removal of practical barriers, visible wins and reinforcement can help; do not present change as a rigid sequence that everyone experiences identically. Adapt coaching to the task and person's support needs, with feedback and a review point.

**Facilitation.** In 1-2-4-All, start with individual reflection, then pairs, fours and whole-group sharing to widen participation. “What, so what, now what” separates observation, interpretation and next action. Five Whys can produce a causal hypothesis, but verify it against evidence and avoid forcing every incident into one cause. Close with an owner, action and review date. The interview value is the better decision or changed behaviour, not the workshop name.

**Commercial contracts.** Time and materials, fixed-price and managed-service arrangements create different incentives and obligations. Establish the actual contract before discussing scope, capacity or billing. Prepare one example where a change process, milestone acceptance or forecast enabled a fair decision. Claim margin or utilisation ownership only if it was genuinely part of your remit.

## Scrum, Kanban and scaled delivery

In Scrum, the Product Owner is accountable for maximising value and effective Product Backlog management. Delegation does not transfer that accountability. The team collaborates on the Sprint Goal; Developers select and plan the work they can complete. The Scrum Master supports effectiveness and self-management. A review inspects outcomes and adapts direction; it is not merely a status demonstration.

Use Kanban thinking to understand work in progress, throughput, cycle time, ageing work and blocked time. Make workflow policies explicit, then test a change against the actual bottleneck. Local productivity gains can leave end-to-end flow unchanged.

For scaled delivery, explain the underlying problem: objectives, dependencies, capacity, integration, decision rights and shared outcomes. In a SAFe context, learn the employer's actual ART, PI planning and backlog arrangements. Product Management leads strategy and roadmapping across the ART; team-level ownership has a different remit. Do not retrospectively label multi-team work as a formal SAFe implementation.

## Measures and commercial fluency

| Measure | What it establishes | Question to be ready for |
| --- | --- | --- |
| Revenue | Money earned from sales | Which customer, period and recognition basis? |
| Profit or contribution | Revenue after a defined set of costs | Which costs are included and who calculated it? |
| Budget and forecast | Funding authority and expected spend | What was your delegated authority and variance response? |
| Time released | Reduced effort for a defined workflow | Was time redeployed or converted into cash savings? |
| Adoption | Defined users taking the intended action | Active among whom, how often and within what period? |
| Flow | How work moves through the system | Are bottlenecks, rework and blocked time visible? |
| Quality and reliability | Whether the service meets defined expectations | Which users, transactions, failures and recovery window? |

Explain baseline, population, time window, source and comparison. Separate implementation cost, elapsed time and recurring operating expense. Do not claim account P&L ownership from programme budget management or a single commercial result.

In consultancy discussions, prepare contract model, scope/change process, team mix, utilisation where applicable, forecast, delivery cost and escalation to the account or finance owner. Protect client outcomes and commercial viability together.

## Public sector and regulated work

Know the distinction between the GDS Service Standard, Technology Code of Practice, user-centred design practice and formal assessment experience. Discovery investigates the problem and whether to proceed; alpha tests risky assumptions through prototypes; beta builds and tests the service; live includes continuing improvement and operations. Retirement is also part of lifecycle ownership.

For a government service, consider whole journeys across channels, accessibility and assisted digital support, privacy, security, performance and operational reliability. The Service Manual identifies cost per transaction, user satisfaction, completion and digital take-up as service KPIs; add measures for the specific service. Confirm which standards and publication requirements apply to the assignment.

In banking or utilities, use a real regulatory or operational constraint rather than claiming government delivery by association. In an AI service, consider data suitability, privacy, evaluation, user recourse, exception handling and monitoring. Define release thresholds with the relevant specialists and accountable owner.

## Technical fluency and the existing handbooks

| Interview need | Canonical reference | Preparation task |
| --- | --- | --- |
| Defend a technical trade-off | [Architecture Decision Method](../../docs/software-architecture/architecture-decision-method.md) | Explain context, options, consequences and evidence at the role's level |
| Discuss dependencies and modernisation | [Legacy modernisation guide](../../learning-paths/software-architect/connected-learning/legacy-modernisation.md) | Connect cutover, data, rollback and support to the delivery plan |
| Discuss production reliability | [Reliability and Failure Control](../../docs/system-design/reliability-and-failure-control.md) | Explain user impact and the response to ambiguous failures |
| Discuss safe AI rollout | [Production AI Assurance](../../docs/ai-architecture/production-ai-assurance.md) | Define outcome, evaluation, exception handling and review ownership |
| Discuss regulated integrations | [Regulated payments guide](../../learning-paths/software-architect/connected-learning/regulated-payments.md) | Connect constraints to acceptance, evidence and decision rights |

These connected-learning cases are teaching exercises; do not present them as your employment history.

## Rehearsal and self-review

Score each answer from 0–2 for relevance, personal ownership, judgement, evidence, calibration and clarity. A zero identifies a concrete rehearsal gap. Ask a partner to probe your metric, the rejected alternative and who held authority. This is a practice rubric, not an Accenture or Civil Service scoring scale.

Before an interview, confirm format, panel, case or presentation, duration and logistics. Prepare a specific motivation, three questions, a setback and a truthful current-status answer. Future interview formats are not established by the stages used in an earlier application.

## References

1. [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — accountabilities, events and artefacts.
2. [GOV.UK Service Standard](https://www.gov.uk/service-manual/service-standard) and [service phases](https://www.gov.uk/service-manual/agile-delivery).
3. [Service performance data](https://www.gov.uk/service-manual/measuring-success/data-you-must-publish).
4. [SAFe Product Management](https://www.scaledagileframework.com/product-management/) — ART-level product remit.
5. [Data and AI Ethics Framework](https://www.gov.uk/government/publications/data-ethics-framework/data-and-ai-ethics-framework).
6. [Cracking the PM Career](https://www.crackingthepmcareer.com/) — selected product, execution, strategy and leadership reading; use your own experience when applying the ideas.
7. [SAFe WSJF](https://framework.scaledagile.com/wsjf/) and [Prosci ADKAR](https://www.prosci.com/methodology/adkar) — prioritisation and change methods.
