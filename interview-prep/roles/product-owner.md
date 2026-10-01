# Product Owner interview guide

**Status:** Draft for owner review · **Last reviewed:** 1 October 2026

Prepare to show how you turn a product goal and user evidence into an ordered backlog and usable increments. The panel needs decisions, trade-offs and results alongside familiarity with Scrum. For the supplied vacancy, add the [Accenture supplement](../vacancies/accenture-product-owner.md).

## Positioning and evidence

A defensible opening: “My background combines product ownership and delivery leadership. I was a Product Owner on the Northern Powergrid account before moving into infrastructure delivery, and later worked on product and delivery initiatives at Natoora. I bring experience translating operational problems into priorities, coordinating technical dependencies and supporting adoption. For this role, I would focus that experience on an evidence-led backlog and measurable client value.” Add one concrete decision you can defend; keep this under 90 seconds.

| Requirement | Best starting evidence | What to demonstrate |
| --- | --- | --- |
| User-centred discovery and requirements | [S3 Smart Timesheet](../shared/evidence-bank.md#s3-smart-timesheet) | Field-user needs, payroll constraints, prioritisation and acceptance |
| Backlog trade-offs and full lifecycle | [S2 SaaS](../shared/evidence-bank.md#s2-saas-transformation) | Launch scope, reusable capability and operational support |
| AI, rollout and continuous improvement | [S1 order automation](../shared/evidence-bank.md#s1-genai-order-automation) | London/Paris scope, exceptions and manual-effort measurement |
| Technical dependencies and risk | [S4 infrastructure](../shared/evidence-bank.md#s4-infrastructure-modernisation) | Transferable dependency judgement; state the actual delivery role |

## Questions to rehearse

1. **How do you establish product vision and a roadmap?** Start with the user problem, desired business outcome and constraints. Explain research, assumptions and an outcome-oriented roadmap. Distinguish the Product Goal from a list of features. Show how new evidence changes priorities.
2. **How do you order a backlog with conflicting stakeholder demands?** Establish mandatory obligations, value, urgency, risk and dependencies. Compare credible options, expose opportunity cost, make a decision within your authority and record the reason. A score supports judgement; it does not decide automatically.
3. **How do you work with BAs and UCD?** Explain shared discovery, clear problem framing, research findings, traceable decisions and collaborative story refinement. Avoid assigning all requirements to the BA or treating UCD as a final design hand-off.
4. **What makes a good user story and acceptance criteria?** Explain the beneficiary and outcome, a small end-to-end slice, examples and edge cases. Acceptance criteria describe this item; the Definition of Done sets product-wide quality expectations. Neither replaces accessibility, security or performance work.
5. **What if work is incomplete near sprint end?** Inspect the Sprint Goal and evidence with the Developers. Clarify scope without weakening quality. Do not mark unfinished work Done or unilaterally add work. Review what caused the gap and adapt future planning.
6. **How do you measure value after release?** Establish a baseline, cohort, time window and owner before rollout. Pair an outcome measure with adoption and guardrails. Separate delivered functionality from realised benefits.
7. **How do you act as a proxy PO?** Agree which decisions are delegated, how priorities are approved and when the client PO must decide. Maintain a transparent backlog and decision log. Proxy arrangements must preserve a clear accountable decision-maker.
8. **How have you mentored a PO or BA?** Prepare one real coaching example: observed gap, agreed practice, feedback and resulting improvement. If you have coached team members without formally mentoring a PO, say that and explain the transferable approach.

## Worked answer and follow-up

For “tell me about a product you owned”, use this factual core: “Smart Timesheet ran in 2019–March 2020, when I was a TCS Product Owner on Northern Powergrid. The service addressed field timesheet administration. We used an OutSystems frontend hosted on AWS, with a .NET backend connecting Oracle HCM and CRM for employee data. The reported outcomes include fewer administrative office visits and annual savings.” Then supply **your actual** discovery activity, one contested priority, the alternative you rejected and how you checked release readiness. Use the [shared answer structure](../shared/handbook.md#behavioural-answers); do not memorise unverified actions as history.

Expect: Who owned funding? Who selected the platform? Which story did you defer? What did users change your mind about? How were savings measured? Were you responsible for architecture or for product decisions? The story succeeds when those boundaries are clear.

## Practical exercise — illustrative, not historical

A field user must submit a weekly timesheet without returning to the office. Propose a thin slice: select the week, review employee details, enter hours, submit and see status. Acceptance examples: valid submission reaches the correct approver; missing required data prevents submission with a clear message; a duplicate request does not create a second timesheet. Confirm authorisation, audit needs, integration behaviour and error recovery with the team. Treat offline support as a discovery question; it is not established in the historical case.

## Scenario

A client asks for a dashboard before launch; research shows users are struggling to complete the core workflow, and security review identifies a release blocker. Clarify the launch outcome and mandatory control. Present options: resolve the core workflow and security issue; simplify the dashboard; or change the date. Explain impact and who approves the trade-off. Reorder transparently, preserve quality and review adoption after release. The strong answer includes a decision, rather than simply arranging another meeting.

## First 90 days and panel questions

In days 1–30, learn users, strategy, decision rights, team constraints and baseline measures. In days 31–60, improve backlog clarity and test a high-value assumption with a small release. In days 61–90, assess outcome evidence, strengthen rollout/support ownership and adapt the roadmap. Sequence this around the client's existing phase and commitments.

Ask: Who owns product strategy and final priority decisions? How much access does the PO have to users? What has made benefits hard to realise? How are security, UCD and operations involved? What would good performance look like in six months?

**Rehearsal:** one product story, one rejected priority, one user insight, one metric defence, one coaching example and the scenario above. Use Cracking the PM Career as supplementary preparation; translate its product-career material to this role's backlog, client and delivery context.
