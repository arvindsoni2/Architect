# Delivery Lead interview guide

**Status:** Draft for owner review · **Last reviewed:** 1 October 2026

Show how you create dependable delivery across teams, clients and operations. A senior answer connects delivery health, decisions, commercial constraints and business outcomes. Reporting status is useful only when it changes what happens next.

## Positioning and evidence

A useful opening: “I have led product and technology delivery across utilities, banking and operational software. My approach is to make risks and dependencies visible, establish clear decisions and sequence delivery around business outcomes. I combine technical understanding with stakeholder coordination and operational readiness.” Follow with one real recovery or scope decision, rather than a list of technologies.

| Evidence | Best interview use | Boundary |
| --- | --- | --- |
| [S4 infrastructure](../shared/evidence-bank.md#s4-infrastructure-modernisation) | Dependency sequencing, production risk and operations | £400k refers to reported annual savings, not budget |
| [S2 SaaS](../shared/evidence-bank.md#s2-saas-transformation) | Commercial trade-offs, distributed teams, repeatable onboarding | Separate implementation cost, elapsed time, revenue and profit |
| [S1 order automation](../shared/evidence-bank.md#s1-genai-order-automation) | Pilot, adoption, exception handling and rollout | Personal rollout scope was London and Paris |
| [S5 banking](../shared/evidence-bank.md#s5-regulated-banking-delivery) | Supplier coordination and regulated readiness | Use one specific initiative and defensible authority |

## Questions to rehearse

1. **How do you know delivery is healthy?** Combine outcome progress, work flow, quality, dependency age, decision latency, team capacity and release readiness. Explain which threshold triggers an action. Avoid a dashboard with no accountable owner.
2. **Tell me about a programme you recovered.** State the original commitment, evidence of risk, what you protected immediately and the diagnosis. Compare scope/date/capacity choices, obtain the relevant decision and show a measurable recovery. Use an actual case; do not retrofit the hypothetical below into history.
3. **What if the client demands an unrealistic date?** Clarify the business event and contractual obligation. Test a minimum viable scope, sequencing, dependencies and quality constraints. Present options and consequences; record the agreed decision and confidence range.
4. **How do you manage multiple suppliers?** Establish deliverables, interface owners, acceptance evidence, escalation paths and shared milestones. Surface dependencies before they become blame. Commercial changes require the appropriate authority.
5. **How do you manage delivery economics?** Distinguish budget, forecast, burn, margin and benefits. Examine scope growth, rework and capacity assumptions. Explain what you controlled and what finance or the account lead approved.
6. **How do you lead distributed teams?** Describe protected overlap, asynchronous decisions, clear ownership, equitable participation and handling missed hand-offs. Give a real example where the working arrangement changed an outcome.
7. **How do you ensure rollout and support readiness?** Include support ownership, training, observability, runbooks, rollback, acceptance and operational capacity. Treat go-live as a transition into a supported service.
8. **How do you handle poor performance or conflict?** Diagnose expectations and constraints, give specific feedback, agree support and follow-up, and escalate fairly if needed. Do not substitute velocity comparisons for a performance conversation.

## Worked commercial answer

The SaaS case connects a nine-person UK/Brazil team with client onboarding and launch constraints. A defensible answer explains a particular decision: how you narrowed launch scope, managed competing capacity or applied learning to a subsequent implementation. The portfolio reports implementation cost falling from £9k to £7k and elapsed delivery from four months to two. Present these as separate comparisons and acknowledge scope differences.

The £28k setup fee and £1.6k monthly recurring revenue were revenue; recurring revenue supported ongoing customer costs. The £29k reported profit covers the first five months after rollout, and your responsibility ended after that period. Prepare the relevant customer/period and cost definition rather than inventing a margin calculation.

## Recovery scenario — illustrative, not historical

You inherit delivery six weeks before a contractual milestone. Two dependencies are late, test defects are rising, the plan is green and the team doubts it. Protect urgent safety, security and customer risks immediately. In parallel, validate completed work, remaining effort, dependency dates, capacity and acceptance criteria with the teams. Identify the true critical path and compare a reduced milestone, changed sequence/date and targeted additional capacity. Explain the consequences and who decides.

Publish a credible forecast and recovery actions with owners, decision dates and evidence of completion. Use short review cycles focused on critical work and quality; update the client without concealing uncertainty. Monitor defect trend, dependency closure and accepted scope. Learn why reporting and reality diverged. “Spend the first week observing without acting” is inadequate when urgent risks exist.

## Technical and governance probes

Be ready to explain why a migration requires dependency discovery, rollback and business validation; why AI needs exception handling and evaluation; and why multi-tenancy affects access, isolation and support. Your technical depth should illuminate a delivery decision. State when the architect, engineer, security lead or sponsor made the design/approval decision.

Expect: Which commitment did you change? What did the client disagree with? Who signed off risk? What did you escalate and when? What was the financial effect? How was benefit realised after launch?

## Additional scenario drills

These are fictional practice cases, not reported interview questions or employment examples. Use the [shared scenario method](../shared/handbook.md#scenario-answers), then defend your recommendation under a changed constraint.

**DL1 — client escalation and supplier dependency.** An integration supplier misses its milestone; the client threatens commercial escalation and requests weekend working. Clarify the contract, actual critical path, remaining work and team capacity. Compare resequencing, a reduced release, supplier recovery and targeted temporary support. Recommend a credible recovery option with the accountable commercial/delivery owners, making cost and people impacts visible. Track dependency evidence, forecast confidence and quality. **Probe:** what if the supplier's recovery plan is unsupported? **Weak response:** promising overtime before diagnosing the bottleneck or approving commercial concessions beyond your authority.

**DL2 — benefits lag despite green delivery.** Milestones are on time, but operations has not adopted the service and the sponsor sees no benefit. Check the business-case assumptions, adoption cohorts, workflow barriers and benefits owner. Compare enablement/support, product changes and a pause in further rollout. Recommend a bounded intervention with product and operations, then review actual use and the intended operational benefit. **Probe:** what if the benefit forecast was overstated? **Weak response:** declaring success because the agreed scope shipped or retroactively changing the success measure.

## Bridge questions

These questions cross from your story into the system behind it and back. Each answer follows the five beats in [Connect the dots](../shared/connect-the-dots.md) (Stakes, Split, Sketch, Shape, Show); the decisions behind them are in the [decision lists](../shared/decision-ledger.md).

1. **A governance board's process threatened your date. What did you do?** “At Northern Powergrid every production change in the infrastructure programme needed the weekly change board, and one rejection cost a week. I was the TCS Agile Delivery Manager, and the board's approval wasn't mine to give, so I made approval predictable: templated change requests, an informal pre-check with the CAB chair and related changes batched together. Every change carried a rollback plan and production validation scripts. When one migration did fail, we rolled it back to its previous state and moved it to the next phase rather than force it into that window. The controls protected the date because they were built in, not added at the end.”
2. **What did the architecture choice cost to run, and who paid?** “On Natoora's SaaS product each client had its own database, schema and cloud environment, built from Terraform templates. That's the silo model: the strongest isolation, but the highest cost per client. The CTO and tech lead chose it; the sysadmin and CTO tracked cloud cost per client, because it hit both the client's margin and ours, and the £1.6k monthly fee had to cover running costs and support. Reusing the templates was one reason Client 2 cost 22% less to implement than Client 1. So the choice was paid for twice: by the client in fees, and by us in margin, which is why we watched it per client.”
3. **Who could stop a release, and how did you keep a fixed deadline safe with several suppliers?** “On Nationwide's GDPR programme the deadline was set in law, 25 May 2018, and five suppliers (Capgemini, IBM, Accenture, TCS and Infosys) depended on shared test environments. Nationwide's release or programme manager owned scope and release; I was the TCS project manager, and my power was visibility. Nothing went to the bi-weekly governance meeting without a named owner and a next action, and I kept the end-to-end and integration environments available when the test team needed them, about ninety per cent of the time. The programme was signed off two weeks before the deadline.”

## First 90 days and panel questions

Initially establish commitments, clients, decision rights, delivery health and urgent risks. Next improve one significant constraint and stabilise a credible forecast. Then strengthen cross-team planning, operational transition and benefits ownership based on measured results. Adapt the sequence if delivery is already in crisis.

Ask: What commercial commitments shape this role? Which decisions can the lead make? Where do dependencies commonly fail? How do account, product and delivery responsibilities interact? Who owns benefits after handover?

**Rehearsal:** one recovery, one scope negotiation, one supplier conflict, one commercial decision, one leadership setback and one operational transition. Use the [shared handbook](../shared/handbook.md) for frameworks and answer scoring.
