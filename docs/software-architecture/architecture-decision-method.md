# Architecture Decision Method

## Purpose and scope

Architecture is a reasoned choice under constraints, not a component diagram. A diagram can show what a system contains; it cannot by itself explain which outcome matters, whose concern dominates, why one structure was chosen, what was sacrificed, or what evidence would justify changing course. This note owns the method for making that reasoning explicit: frame the problem, identify architecture drivers, express qualities as measurable scenarios, compare viable options, record a decision hypothesis, and define its evidence and reversal trigger.

Use the method for consequential choices: decisions that strongly affect an important quality, constrain many later choices, or are expensive to reverse. Apply less ceremony to local, reversible choices. The few decisions that determine most system outcomes deserve most of the analysis.

Adjacent notes own the implementation detail. Runtime failure controls belong in reliability and failure control; correctness across duplicated or restarted work belongs in durable workflows and idempotency; AI-specific release evidence and autonomy controls belong in production AI assurance. This note determines *why* their targets matter and *what* evidence a decision needs, without redefining those controls.

## First-principles model

Start with this traceability chain:

`outcome → stakeholders → drivers → measurable scenarios → constraints/assumptions → options → consequences → evidence → decision/reversal trigger`

- An **outcome** is the change the system must produce or protect. Ask what fails for the organisation or user if the architecture is wrong.
- **Stakeholders** are people who experience, operate, fund, govern, change, or bear the consequences of the system. Name a decision owner as well as interested parties.
- **Architecture drivers** are the small set of functional needs, quality attributes, constraints, and risks that materially shape the design. They are contextual, not a generic checklist.
- A **quality-attribute scenario** makes a quality testable by naming the source, stimulus, environment, affected artifact, response, and response measure. “Fast” becomes a latency percentile under a stated load; “available” becomes a service level for a defined operation and period.
- **Constraints** are boundaries the design must respect. **Assumptions** are beliefs that could be wrong. Keep them separate because an assumption needs an owner and validation plan.
- **Options** must be genuinely viable responses to the drivers, not a preferred choice beside two straw alternatives.
- **Consequences** include gains, costs, weakened qualities, new organisational demands, and options closed or preserved.
- **Evidence** is an observation capable of increasing or reducing confidence: a capacity model, prototype, failure test, threat model, migration rehearsal, operational measurement, or user outcome.
- A **reversal trigger** is an observable condition that causes review, not an automatic redesign.

A decision is therefore a **falsifiable hypothesis**: given this context, choosing this option is expected to protect stated outcomes within measurable bounds. It remains defensible only while evidence supports its assumptions and consequences.

## Core decisions and trade-offs

First separate **functional need**—what the system must do—from **quality attributes**—how well it must do it in a particular context. “Submit a claim” is functional. “During regional peak load, 95% of accepted claims receive acknowledgement within two seconds” is a performance scenario. Architecture changes when the latter becomes precise.

Next rank the dominant qualities. Availability, latency, auditability, security, changeability, and cost often interact; equal weighting avoids the decision. A useful priority combines business impact with architectural difficulty. The result is not a universal hierarchy: privacy may limit observability, redundancy may improve availability while increasing cost, and stronger consistency may reduce availability or throughput. When sources or stakeholders conflict, identify the different workload, consequence, risk tolerance, or organisational capability behind their advice.

Prefer the simplest option that satisfies the dominant scenarios. Simplicity reduces coordination and operational burden; optionality buys room for uncertain change but charges complexity immediately. Preserve options cheaply through clear module boundaries, stable interfaces, and reversible rollout steps. Do not purchase speculative distribution merely because future scale is imaginable.

Sequence decisions by reversibility and uncertainty. Delay a hard-to-reverse commitment when learning is cheap, but do not use uncertainty to postpone every choice. Present evidence may justify a reversible default; a high-consequence assumption may justify a focused spike before commitment. The trade is always explicit: what confidence is gained, what time or flexibility is spent, and which uncertainty remains.

A **trade-off record** names the choice, what it improves, what it may weaken, the controls that limit harm, and when to revisit it. An **evidence plan** pairs each material uncertainty with a focused test, owner, acceptance signal, and decision date. Together they make a short decision defence possible: outcome, drivers, options, choice, consequences, risks, and evidence.

Record each consequential choice in an **architecture decision record (ADR)** containing:

- context and desired outcome;
- forces: drivers, constraints, assumptions, and uncertainties;
- viable options and rejection rationale;
- the decision and accountable owner;
- positive and negative consequences, including the deliberate sacrifice;
- evidence available now and evidence still required;
- status; and
- a review or reversal trigger.

An ADR preserves reasoning, not just the winner. Its value is that a later team can distinguish a bad decision from a sound decision whose context changed.

## Failure modes and warning signs

- **Solution-first framing:** technology appears before the workflow, outcome, or constraint. A large diagram cannot repair an undefined problem.
- **Adjective-only requirements:** “fast,” “secure,” or “reliable” lacks stimulus, environment, response, and measure, so options cannot be evaluated.
- **Hidden assumptions:** estimates or dependencies are presented as facts. Warning signs include no owner, expiry, or validation action.
- **Equal weighting:** every quality is “critical.” This conceals whose loss matters most and produces no basis for sacrifice.
- **Decision-matrix theatre:** arbitrary scores manufacture precision, criteria overlap, or weights are tuned to select a predetermined winner. Use a matrix to expose reasoning, not replace it.
- **Consensus without accountability:** everyone agrees, but nobody owns the outcome, evidence plan, or revisit decision.
- **Winner-only ADRs:** the record omits viable alternatives and negative consequences, making later review depend on memory.
- **No invalidation signal:** a decision claims benefits but names no measurement or condition under which confidence should fall.

Other warning signs are architecture elements that cannot be traced to a driver, irreversible commitments made before risky assumptions are tested, and evidence that measures a component while ignoring the real workflow outcome.

## Practical decision checklist

Before accepting a consequential decision, ask:

- What outcome is at risk if this choice is wrong?
- Which stakeholder experiences the consequence, and who owns the decision?
- What measurable quality-attribute scenario drives the structure?
- Which hard constraint rules out otherwise attractive options?
- Which viable alternative was rejected, and for what contextual reason?
- What benefit did we choose, and what sacrifice did we deliberately accept?
- What evidence supports the decision now?
- Which assumption or uncertainty has the greatest product of impact and doubt?
- What observable reversal trigger will reopen the decision, and who reviews it?
- Which communication artifact—ADR, focused diagram, experiment result, or risk log—lets the intended audience inspect the reasoning?

If these answers do not form one coherent argument, more boxes will not make the architecture defensible.

## Worked architecture scenario

A regional insurer asks to “modernise claims with microservices.” Today, adjusters use a single claims application plus manual hand-offs. The business outcome is shorter settlement time without losing regulatory evidence. Product owns cycle time; operations owns service recovery; compliance owns audit and residency obligations; engineering owns change safety and cost.

The team converts ambiguity into scenarios before choosing structure:

- **Latency:** at normal regional load, 95% of claim submissions receive a durable acknowledgement within two seconds.
- **Availability:** during a single downstream outage, intake remains available for 99.9% of monthly minutes and accepted work is not lost.
- **Auditability:** every status change records actor, time, reason, and prior state; authorised reviewers can reconstruct a claim history.
- **Data residency:** claimant records and backups remain in the mandated region, including during recovery.
- **Changeability:** a team can change one claim rule and deploy it within one business day without unrelated module changes.
- **Cost:** monthly platform cost remains within the approved per-claim envelope at forecast volume.

Hard constraints include the residency rule, a fixed migration window, and a small on-call team. The main uncertainty is whether claim domains and team ownership are stable enough to operate independent services.

Two options remain viable. Early microservices offer independent deployment and scaling, but add remote failure modes, data coordination, observability, release, and on-call costs before the boundaries are proven. A modular monolith with enforced domain modules and a queue for slow external checks keeps one primary deployment and transaction boundary while decoupling intake from variable downstream latency. It sacrifices independent module scaling and permits some shared-release coordination.

The ADR chooses the modular monolith plus queue because it meets the measured scenarios with the lower current operational burden. Evidence includes a peak-load capacity test, a queue-backlog recovery test, an audit-history demonstration, residency review, and deployment lead-time measurements. The reversal trigger is not “the system grows.” Review decomposition when two modules repeatedly require independent releases, a module exhausts the shared scaling envelope, or team ownership is stable and cross-module change coupling exceeds the agreed threshold for three review periods. Those signals would support extracting a particular service; they do not imply rewriting the whole system.

## Feynman questions

1. Why is an architecture decision a hypothesis rather than a permanent truth? Explain what could falsify one choice you have made.
2. Turn “the system must be fast and reliable” into two scenarios with a source, stimulus, environment, response, and numeric measure.
3. What does an ADR preserve that the chosen architecture or its diagram cannot?
4. Name one quality your current design deliberately weakens. What stronger quality or outcome does that sacrifice protect?
5. Which observed evidence would cause you to revisit the decision, who would review it, and why is that evidence more useful than a calendar reminder alone?

## Related canonical notes

- [Reliability and Failure Control](../system-design/reliability-and-failure-control.md) owns runtime failure domains, overload controls, service objectives, recovery, and incident learning.
- [Durable Workflows and Idempotency](../cross-cutting-patterns/durable-workflows-and-idempotency.md) owns correctness across duplicate delivery, partial progress, retries, replay, and compensation.
- [Production AI Assurance](../ai-architecture/production-ai-assurance.md) owns task-specific evaluation, autonomy boundaries, AI observability, unit economics, rollout, and rollback evidence.

## Sources and review status

Repository sources:

- [System Design Concept Handbook v5](../../handbooks/system-design/system-design-concept-handbook-v5.html)
- [Software Architect Curriculum Guide v3](../../learning-paths/software-architect/software-architect-curriculum-guide-v3.md)
- [Software Architect Grooming Programme v5](../../learning-paths/software-architect/software-architect-grooming-programme-v5.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)

External references (verified 2026-09-05):

1. Software Engineering Institute, [Quality Attribute Workshop](https://www.sei.cmu.edu/library/the-sei-quality-attribute-workshop/)
2. Software Engineering Institute, [Architecture Tradeoff Analysis Method collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)
3. ADR GitHub organisation, [Architecture Decision Records](https://adr.github.io/)

**Status:** Current

**Edition:** Living

**Last reviewed:** 2026-09-05
