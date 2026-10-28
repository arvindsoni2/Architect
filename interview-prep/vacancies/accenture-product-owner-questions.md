# Accenture Product Owner — extra questions and research

**Status:** Owner-reviewed facts · **Last reviewed:** 13 October 2026 · **Use with:** the [Accenture PO playbook](accenture-product-owner.md)

The playbook covers the 15 questions most likely to decide the interview. This page covers depth and quick-fire questions that may come up as follow-ups. Answers are short on purpose: say the point, give one example, stop. Facts come from the [evidence bank](../shared/evidence-bank.md).

Jump to: [API-first](#what-is-api-first-and-whats-your-experience) · [SAFe](#what-do-you-know-about-safe) · [AI risks](#what-risks-do-you-watch-in-an-ai-product) · [Consulting situations](#consulting-situations) · [Research register](#research-register)

## Scrum and product ownership

### What is the Product Owner accountable for?

> “Maximising the value of the product. In practice that means owning the product goal, ordering the backlog and making sure everyone understands it. I can delegate backlog work to a BA, but the accountability stays with me.”

### What does the PO do in each Scrum event?

> “In sprint planning I bring the product goal and the most valuable items, and we agree the sprint goal together; the developers decide how much they can take on. In refinement I clarify items with the BA, designers and developers. At the sprint review I show the increment to stakeholders and we adapt the backlog. I join the retrospective as a team member.”

### Definition of Ready and Definition of Done?

> “Done is in the Scrum Guide: the quality standard every increment must meet — for example tested, accessible and deployable. Ready isn't in the Scrum Guide; it's a team agreement that an item is clear enough to start. I use it lightly, so it doesn't become a gate. On the Natoora SaaS team we agreed one together, and it stayed part of how we worked.”

### Write a user story and acceptance criteria

> “As a field engineer, I want to submit my weekly timesheet from my phone, so I don't have to drive to the depot. Acceptance criteria: given a completed week, when I submit, it goes to my supervisor for approval and I see its status; given a missing required field, I can't submit and I see a clear message; given I submit twice, only one timesheet is created.”

This example uses the Smart Timesheet context to show the format. The acceptance criteria are illustrations, not a record of the actual backlog.

### Scrum or Kanban?

> “Scrum when the work benefits from a fixed rhythm and regular stakeholder reviews, for example building a new product. Kanban when work arrives continuously and unpredictably, for example support or BAU change. Often a team uses Scrum for product work and limits work in progress the Kanban way.”

### What do you know about SAFe?

> “In SAFe, the Product Manager owns the programme backlog and features, and Product Owners own team backlogs and stories. Teams plan together every 8–12 weeks in PI Planning, and priorities use WSJF: cost of delay divided by job size. I haven't worked on a formal Agile Release Train, but at Northern Powergrid I coordinated distributed teams across Chennai, Kolkata and Newcastle around shared dependencies, which is the problem SAFe solves. I'd be happy to take the POPM certification.”

## Delivery, technology and risk

### What is API-first, and what's your experience?

This is a reported Accenture Digital Product Owner question (see G1 below). Evidence: [S3 Smart Timesheet](../shared/evidence-bank.md#s3-smart-timesheet).

> “API-first means designing the interface between systems as a contract before building the screens. For a PO, it means agreeing early what data is exchanged, who uses it and what happens when it fails. On Smart Timesheet our OutSystems front end on AWS depended on a .NET integration with Oracle HCM and CRM for employee data, so integration failure, data quality and permissions were backlog items from the start, not surprises at the end.”

### What cloud experience do you have?

> “Smart Timesheet ran on AWS. At Natoora the SaaS product ran on Google Cloud with Terraform templates, which we reused from Client 1 for Client 2 to cut onboarding time. I passed AWS Certified AI Practitioner in April 2026 and I'm studying for Solutions Architect Associate. As a PO, I care about cloud cost, security and the support model as much as the features.”

### How do you balance technical debt against new features?

> “I make the cost of the debt visible in business terms — slower delivery, incidents, security risk — and give it a regular share of capacity rather than one big clean-up. On the SaaS product I owned the technical-debt plan: removing more than 200 hard-coded references so each client could run in its own environment, and tracking every open security item in Jira until the Angular migration closed them. Without that work, we couldn't safely onboard a second client.”

### How do you handle security, compliance and regulation?

> “Mandatory obligations go to the top of the backlog with a deadline, and the controls go into the Definition of Done. At Nationwide I delivered regulated banking work such as Open Banking and GDPR, where the date was fixed by regulation. For a public-sector client I'd involve security and data-protection colleagues in refinement, not at the end.”

### What risks do you watch in an AI product?

> “Wrong outputs, sensitive data leaking, prompt injection — for example an email with hidden instructions — cost, and model changes from the vendor. I manage them with validation, a human on consequential decisions, monitoring of exception rates, and clear ownership of exceptions. On the Natoora tool, validation checked customers and products, and anything uncertain went to a person.”

### How do you run a team split across locations?

> “At Natoora the SaaS team had nine people across the UK and Brazil. We protected overlap hours for collaboration, wrote decisions down, and ran a joint stand-up plus written end-of-day updates. At Northern Powergrid I ran teams across India and Newcastle. The rule is the same: make work and decisions visible so nobody waits for a meeting.”

## Consulting situations

### The client changes the objective from profit to quality halfway through. What do you do?

This is a reported Accenture consulting case theme (see G2 below). Answer with the [scenario method](accenture-product-owner.md#4-scenario-method).

> “I'd clarify what ‘quality’ means to them and why it changed now. Then I'd re-order the backlog against the new goal and show which planned work no longer adds value. I'd agree new success measures and check whether the change affects the contract, because a new objective can be a change request. Finally I'd tell the team why priorities moved.”

### Stakeholders don't engage or take responsibility. What do you do?

> “I find out why — usually unclear benefit, no time or fear of the decision. I make it easy: short decision notes with a recommendation and a deadline, and a demo of working software rather than documents. If a decision still doesn't come, I escalate through the agreed route, presenting it as a risk to their outcome rather than a complaint.”

### What would you do in your first 90 days?

> “Days 1 to 30: learn the client, users, decision rights and baseline measures — and change very little. Days 31 to 60: tighten the backlog around the product goal and ship one small, valuable release. Days 61 to 90: measure the outcome, adjust the roadmap and set up the mentoring rhythm with the POs and BAs I support.”

## Research register

Reviewed 5 October 2026 and kept for reference. These are anecdotal reports, not Accenture's question bank or confirmation of this vacancy's format.

| Code | Source | Supports |
| --- | --- | --- |
| G1 | [Glassdoor Digital Product Owner reports](https://www.glassdoor.co.uk/Interview/digital-product-owner-interview-questions-SRCH_KO0%2C21.htm), 2023–2024 | Accenture API-first question (30 September 2023, location unknown); stakeholder conflict |
| G2 | [Glassdoor Accenture client-objective case](https://www.glassdoor.co.uk/Interview/Case-study-question-If-the-client-was-interested-in-growing-profit-at-the-start-of-the-project-but-at-midway-they-change-QTN_1587563.htm) | Changing client objective (asked of a consulting senior manager, not this role) |
| R1 | [Reddit: Senior Agile PO interview](https://www.reddit.com/r/ProductOwner/comments/1m6f92w/senior_agile_product_owner_interview/), 2025 | Cooperation and capacity scenarios |
| R2 | [Reddit: PO interview tips](https://www.reddit.com/r/ProductOwner/comments/1r1fedm/product_owner_interviews_tips/), 2026 | Ambiguous requests broken into deliverable work |
| L1 | [LinkedIn: PO interview questions](https://business.linkedin.com/hire/resources/how-to-hire-guides/product-owner-interview-questions) | Roadmap, backlog, value and stakeholder questions |
| D1 | [Accenture: behavioural interview preparation](https://www.accenture.com/us-en/blogs/blogs-careers/how-to-prepare-for-a-behavioral-interview) | Accenture recommends STAR for past examples |
| D2 | [Scrum Guide 2020](https://scrumguides.org/scrum-guide.html) | PO accountability, events, Definition of Done; still the current official version in October 2026 |
| D3 | [GDS Service Standard](https://www.gov.uk/service-manual/service-standard) | Public-service expectations |
| D4 | [GOV.UK: Understanding WCAG 2.2](https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag) | Accessibility standard for public services |
