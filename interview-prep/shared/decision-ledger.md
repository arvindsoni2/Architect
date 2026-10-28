# Decision lists

**Status:** Owner-approved · **Last reviewed:** 28 October 2026

Each story below records who made each decision and what your part was, so you can answer boundary questions such as “what did you decide, and what did the architect decide?” without overclaiming or underclaiming. The method behind these lists is in [Connect the dots](connect-the-dots.md); the facts come from the [evidence bank](evidence-bank.md) and the owner's answers of 26–28 October 2026.

## How to read a decision list

| Label | Meaning |
| --- | --- |
| Owned | You made the call. |
| Recommended | You proposed it; someone else approved it. |
| Shaped | You supplied the requirement or constraint that drove someone else's call. |
| Accepted | It was decided elsewhere; you planned and delivered around it. |

Each story also has the question a panel is most likely to ask, a five-beat model answer (Stakes, Split, Sketch, Shape, Show) and the follow-ups one level down. Use **Practice mode** to hide the answers and say yours first.

## S3 Smart Timesheet

Northern Powergrid · 2019–March 2020 · TCS Product Owner. The full worked answer, with the architecture walk-through, is in [Architecture review](architecture-review.md#worked-example-smart-timesheet).

**Flow:** 1. Field engineers → Smart Timesheet app (OutSystems native app, works offline); 2. Supervisors → app (approval); 3. App → .NET integration layer; 4. .NET → Oracle HCM (risky arrow: employee data leaves Northern Powergrid's systems); 5. .NET → Oracle CRM (risky arrow: legacy integration); 6. Approval → API calls to HCM, CRM and payroll.

| Decision | Owner | Your part | Source |
| --- | --- | --- | --- |
| Who the users are and what they need (field research at depots) | You | Owned | Evidence bank |
| First release: the native mobile app; the desktop web app deferred | You | Owned | Owner answer, Oct 2026 |
| Offline submission: store on the phone, sync when back online | Built into the OutSystems native app | Shaped: a key constraint from field research | Owner answer, Oct 2026 |
| Positioning with the union: the tool saves a trip to the office; it doesn't track engineers | You, with field operations | Owned | Evidence bank |
| Alpha (1 depot, 50 engineers, 4 weeks), beta (3 depots, 200) and phased rollout with playbook, hypercare and champions | You | Owned | Evidence bank |
| Platform: OutSystems, for rapid prototype-to-production delivery | TCS, as implementation partner | Accepted: TCS's call, which you delivered | Owner answer, Oct 2026 |
| AWS hosting, infrastructure and operations | OutSystems, as a vendor-run cloud; Northern Powergrid had no direct AWS relationship | Accepted | Owner answer, Oct 2026 |
| Data sovereignty: employee data stays in the UK | Northern Powergrid Architecture Review Board | Shaped: you presented the initiative and its data needs to the board in person | Owner answer, Oct 2026 |
| Which employee data may be shared with the cloud app (GDPR impact); this ruling decided whether the initiative was viable | Northern Powergrid Architecture Review Board | Shaped: the product's data needs were your input. Approved: employee ID, name and day rate only | Owner answer, Oct 2026 |
| Integration design: a .NET layer in front of Oracle HCM and CRM | Architect and engineering | Shaped: you put the integration risks into the backlog early | Evidence bank |
| Identity, security and environments | Architect and client IT | Accepted | To confirm |
| Handover to the support team | You, with support | Owned | Evidence bank |

## S1 GenAI order automation

Natoora · Mar–Sep 2025 · delivery lead for the London and Paris rollout · 1 developer · CTO sponsor.

**Flow:** 1. Order emails → Scheduled job; 2. Scheduled job → GPT-4o-mini; 3. GPT-4o-mini → Validation (risky arrow); 4. Validation → WS (risky arrow); 5. Validation → Human review; 6. Human review → WS. 3–4: model output becoming a real order. Validation, duplicate rules and human review sit on that path.

| Decision | Owner | Your part | Source |
| --- | --- | --- | --- |
| Limit the rollout to London and Paris | CTO | Accepted | Evidence bank |
| Use an LLM instead of rules | Discussion you were part of; the CTO backed it | Shaped | Owner answer, Oct 2026 |
| Product requirements: risk, cost and benefit, shared with customer support | You | Owned | Owner answer, Oct 2026 |
| Evaluation approach and success metrics, reviewed by stakeholders | You | Owned | Owner answer, Oct 2026 |
| Model: GPT-4o-mini, for cost and latency | Tech lead | Accepted | Owner answer, Oct 2026 |
| Human review of exceptions; exception rules evolved from the experiments | You, the team and customer support | Shaped | Owner answer, Oct 2026 |
| Integration with WS through its API, Python and scheduled jobs | Developer | Accepted | Owner answer, Oct 2026 |
| Duplicate check on order reference and order items; WS also flags likely duplicates | Developer, in WS and the pipeline | Accepted | Owner answer, Oct 2026 |
| Data protection: people's names and addresses stripped or randomised before the model; reviewed by the CTO and lead developer | CTO and lead developer | Accepted | Owner answer, Oct 2026 |
| How the 90% effort reduction was measured and presented | You | Owned | Owner answer, Oct 2026 |

### Q1. On the GenAI order tool, what did you decide and what did the developer and the CTO decide? And how did you make sure the model didn't create wrong orders?

**Stakes.** “Customer service typed every emailed order into our warehouse system by hand: two to three minutes each, more than a hundred emails a day in a region. A wrong order meant a wrong delivery to a premium restaurant.”

**Split.** “I led the rollout in London and Paris, with the CTO as sponsor. I wrote the product requirements, covering risk, cost and benefit, and I defined how we'd evaluate it and what success meant. Using an LLM came out of a discussion I was part of and the CTO backed. Our tech lead chose GPT-4o-mini for cost and latency. The developer built the integration into WS, our warehouse system, and the CTO and lead developer reviewed data protection and security.”

**Sketch.** “A scheduled job picks up order emails and PDFs from Marketman in London and Lightspeed in Paris, and strips or randomises the orderer's name and address before anything reaches the model. GPT-4o-mini turns each order into structured JSON. Validation matches customers and products against WS, deterministic rules on the order reference and items stop the same order going in twice, and anything uncertain goes to a human review screen. The risky arrow was the model's output becoming a real order.”

**Shape.** “My job was making that arrow measurable before we trusted it. I set the success metrics and the evaluation first, and we ran experiments for two to three months as each procurement system came on, logging every exception. Human review did more than catch errors: it let customer service see exactly how orders from each system were handled, which is how they came to trust it. The exception rules grew out of what those experiments showed.”

**Show.** “We measured average handling time per order before, then after, including the time people still spent on exceptions. That came to about ninety per cent less manual effort, which I presented to the stakeholders. It's effort released, not model accuracy.”

**One level down:**

1. **Could the same email create two orders?** No: the pipeline checks the order reference and the order items, and WS flags likely duplicates as a second line. That's an idempotency key. System Design v6, chapter 11.
2. **How did you know extraction was good enough?** Your answer: two to three months of experiments per procurement system, with exceptions logged and timed. Name it in evaluation terms: a sample of real emails, the exception rate per system, and time per order.
3. **Order emails went to OpenAI. Who approved that?** The CTO and lead developer reviewed it, and people's names and addresses were stripped or randomised before the model saw anything. Say exactly that. It's data minimisation, the same principle as the three fields on Smart Timesheet.

## S2 SaaS transformation

Natoora · Jan 2024–May 2025 · delivery lead · 9 people across the UK and Brazil · CTO sponsor.

**Flow:** 1. Client staff → WS, per client; 2. B2B customers → PRO App; 3. PRO App → WS, per client; 4. WS, per client → Client's own database (risky arrow); 5. Terraform templates → WS, per client. A separate stack per client (the silo model): strongest isolation, highest cost per client.

| Decision | Owner | Your part | Source |
| --- | --- | --- | --- |
| Turn the internal warehouse platform into a SaaS product | Natoora board and CTO | Accepted | Evidence bank |
| Architecture: a separate database, schema and cloud environment for each client | CTO and tech lead | Accepted | Owner answer, Oct 2026 |
| Architecture reviews, design and database decisions that affected delivery | CTO and tech lead, with you | Shaped | Owner answer, Oct 2026 |
| Client 1 scope in four weeks: impact matrix, white-label customer-facing screens first, defer admin screens | You | Owned | Evidence bank |
| Plan SaaS work on 70% team availability | You, agreed with the CTO | Recommended | Evidence bank |
| Client 2 onboarding pack: questionnaire, financial health check, requirements form | You | Owned | Evidence bank |
| Go live with some security items still open, with enough protection in place; finish the Angular migration afterwards | CTO reviewed; client signed off | Owned the follow-up: each item tracked in Jira until closed | Owner answer, Oct 2026 |
| Watch cloud cost per client, because it hit both margins | Sysadmin and CTO | Accepted | Owner answer, Oct 2026 |

### Q2. Your portfolio's architect view says you led the move to a multi-tenant SaaS. Which design decisions were yours, and which were the engineers' and the CTO's?

**Stakes.** “Natoora decided to sell its internal warehouse platform to other food businesses. The first client was the reference case: if it failed, the SaaS strategy failed with it.”

**Split.** “I was delivery lead for a nine-person team across the UK and Brazil. The CTO and tech lead decided the architecture, and I took part in the architecture reviews and in the design and database decisions that affected delivery. I owned scope, sequencing and client onboarding, and I agreed capacity with the CTO: seventy per cent availability, because the same team still ran Natoora's own platform.”

**Sketch.** “One codebase, Django and PostgreSQL, but each client got its own database, schema and cloud environment on Google Cloud, built from Terraform templates, plus the PRO App for B2B ordering. That's the silo model: the strongest isolation, at a higher cost per client. So our sysadmin and the CTO watched cloud cost per client, because it hit both the client's margin and ours.”

**Shape.** “The four-week deadline against a six-to-eight-week estimate was mine to solve. I built an impact matrix of visibility, frequency of use and complexity, and we white-labelled the customer-facing order screens, emails, login pages, reports and app branding first, deferring internal admin screens. For Client 2 I turned the lessons into an onboarding pack, which caught scope problems before they reached engineering.”

**Show.** “Client 1 went live on schedule. Not every security item was closed at go-live: the CTO reviewed it, the client signed off, and there was enough protection that client data wasn't at risk. I owned the technical-debt plan and tracked every open security item in Jira until it was closed, and finishing the Angular migration after go-live closed them and cut the debt. The pilot had fewer than ten issues and no Sev 1s, Client 2 cost 22% less to implement, and the product reported £29,000 profit in its first five months.”

**One level down:**

1. **So was it multi-tenant?** Not in the shared-database sense. It was one codebase with a separate stack per client: the silo model. Say it that way, and know the trade-off against a shared database with a tenant ID: isolation and simpler compliance against cost and operational load per client. Architect guide Q22.
2. **How do you go live with known security issues?** Risk acceptance: who accepted the risk (the client signed off), what protection covered the gap, and a tracked plan to close it (your Jira items and the Angular migration). It's the “approve with conditions” outcome from the ARB section.
3. **What did one client's environment cost to run?** The sysadmin and CTO monitored it. If you know the figure, compare it with the £1.6k monthly fee. Architect guide Q11.

## S4 Infrastructure modernisation

Northern Powergrid · Mar 2020–May 2022 · TCS Agile Delivery Manager for phases 1 and 2 of 3 · teams in Chennai, Kolkata and Newcastle.

**Flow:** 1. 30+ applications → Treatment; 2. Treatment → NPg ARB; 3. Treatment → Weekly CAB; 4. Weekly CAB → 120+ servers (risky arrow); 5. Weekly CAB → Oracle 9 (risky arrow). 4–5: production change windows on tightly coupled systems, some from vendors that no longer existed.

| Decision | Owner | Your part | Source |
| --- | --- | --- | --- |
| Delivery of phase 1 (six months of quick wins) and phase 2 (twenty months of complex migrations); phase 3 ran after you left TCS | You | Owned | Owner answer, Oct 2026 |
| Assessment strategies: retire, replatform, refactor or replace | Engineers and architects | Accepted | Owner answer, Oct 2026 |
| Treatment for each application | Project sponsor, with NPg and TCS architects | Shaped: every application properly impact-assessed | Owner answer, Oct 2026 |
| Keep every treatment aimed at the goal: fewer servers on legacy software, decommissioned where possible | You | Owned | Owner answer, Oct 2026 |
| Target Windows and Oracle versions | TCS technical team assessed each server and application | Accepted | Owner answer, Oct 2026 |
| Approval of upgrades and uplifts | NPg ARB | Accepted | Owner answer, Oct 2026 |
| Approval of every production change | NPg weekly CAB | Shaped: templates, pre-checks, batching | Portfolio-reported |
| Rollback plan and validation scripts for every change | You | Owned | Portfolio-reported |
| After a failed migration and rollback, move that application to the next phase | You and the project team | Owned jointly | Owner answer, Oct 2026 |
| Capture each application's undocumented knowledge before migration | You | Owned | Portfolio-reported |

### Q3. Did you design the migration strategy, or did the architects? And how did you get changes through the CAB without losing weeks?

**Stakes.** “Northern Powergrid ran more than 120 servers on unsupported Windows versions and Oracle 9. That's critical national infrastructure exposed to unpatched vulnerabilities, and it was paying over £320,000 a year for Microsoft extended support alone.”

**Split.** “The programme ran in three phases. I was the TCS Agile Delivery Manager for the first two; the third went ahead after I left TCS in May 2022. The project sponsor decided each application's treatment with Northern Powergrid's and TCS's architects, using strategies our engineers and architects created. The TCS technical team chose target versions, and Northern Powergrid's ARB approved the upgrades. My job was to make sure every application was properly impact-assessed and that every treatment served the goal of fewer servers on legacy software. I owned delivery: the sequencing, the change packs and getting changes through the weekly CAB.”

**Sketch.** “Thirty-plus applications were assessed one by one, and each got a treatment: retire, replatform, refactor or replace. Upgrades went to the ARB, and every production change went through the weekly CAB in ServiceNow. The risky arrow was the production change window: tightly coupled systems, some from vendors that no longer existed.”

**Shape.** “Phase one was six months of quick wins: retiring obsolete applications and decommissioning thirty-plus servers. That built confidence and funded phase two, twenty months of complex migrations. Every change carried a rollback plan and production validation scripts. Before each migration we wrote down the application's undocumented knowledge, because with defunct vendors nobody else could help us.”

**Show.** “A rejected change cost a week, so I templated CAB submissions, pre-checked them with the CAB chair and batched related changes. One migration did fail. We rolled it back to its previous state and, rather than force it into that phase, moved it to the next one, because its complexity didn't fit. The programme saves about £400,000 a year: around £350,000 in Microsoft and Oracle extended-support fees no longer paid, and about £50,000 of engineer time no longer spent on patching and upgrades.”

**One level down:**

1. **CAB or ARB: what's the difference?** A CAB asks “is this change safe to make now?”; an ARB asks “is this the right design?”. This programme used both: the ARB approved the upgrades and target versions, and the weekly CAB approved every production change. S3 adds the ARB from the product side.
2. **Tell me about something that went wrong.** The failed migration: it rolled back cleanly because every change had a rollback plan, then moved to the next phase. It shows the controls working, not just the plan.
3. **How did you calculate £400k?** Lead with £400k a year. If asked how, split it: £350k hard cash (Microsoft and Oracle extended-support fees no longer paid) and £50k soft (engineer hours no longer spent on patching and upgrades). Keep the split ready; panels probe exactly this.

## S5 GDPR programme at Nationwide

Nationwide Building Society through TCS · Sep 2017–Jun 2018 · project manager · five suppliers · fixed legal deadline.

**Flow:** 1. Five suppliers → Test environments (risky arrow); 2. Test environments → Defects and RAID; 3. Defects and RAID → Bi-weekly governance; 4. Bi-weekly governance → Release decision. 1: five suppliers depending on shared test environments, against a date the law fixed.

| Decision | Owner | Your part | Source |
| --- | --- | --- | --- |
| Scope and release | Nationwide release manager or programme manager | Accepted | Owner answer, Oct 2026 |
| Coordinating five suppliers | You | Owned | Owner answer, Oct 2026 |
| Test environments available when the test team needed them | You | Owned | Owner answer, Oct 2026 |
| Driving programme-level defects to resolution | You, with the suppliers | Owned | Owner answer, Oct 2026 |
| Every risk and issue raised at governance with a named owner | You | Owned | Owner answer, Oct 2026 |
| Programme sign-off, two weeks before the 25 May 2018 deadline | Nationwide | Accepted | Owner answer, Oct 2026 |
| Progress reporting | You | Owned | Owner answer, Oct 2026 |

### Q4. In regulated banking, who could stop a release, and what did you do when a supplier dependency threatened a compliance deadline?

**Stakes.** “GDPR came into force on 25 May 2018, and nobody could move that date. Nationwide's programme had five suppliers working towards it.”

**Split.** “I was the TCS project manager from September 2017 to June 2018. Nationwide's release and programme managers owned scope and release. I owned what kept the date safe: coordinating the suppliers, keeping the test environments available, driving programme-level defects to resolution, and making sure every risk and issue had a named owner.”

**Sketch.** “Five suppliers (Capgemini, IBM, Accenture, TCS and Infosys) all tested in shared end-to-end and integration environments. Defects and risks went into the RAID log and on to a bi-weekly governance meeting, and Nationwide made the release call. The risky arrow was the shared environments: if one went down, every supplier's testing stopped.”

**Shape.** “With a fixed date, anything slipping had to be visible early, so nothing went to governance without a named owner and a next action. I matched environment availability to what the test team needed, so the suppliers weren't waiting on each other.”

**Show.** “We kept the shared test environments available about ninety per cent of the time, which kept testing on track, and the programme was signed off two weeks before the 25 May 2018 deadline.”

**One level down:**

1. **Who could stop a release?** Nationwide's release manager or programme manager. Your power was visibility: every risk had an owner and reached governance in time to act.
2. **How do you manage five suppliers in one programme?** A single RAID log with named owners, a shared environment schedule, and one escalation route to the client's programme manager.
3. **Is 90% availability good?** For shared test environments used by five suppliers it's a reasonable figure. Know the denominator (planned test hours, or all hours) before you quote it.

## S7 Agile operating model and Jira

Natoora · from 2022 · Scrum Master / Product Delivery Lead.

**Flow:** 1. Jira backlog → Two-week sprints; 2. Two-week sprints → CI/CD pipeline; 3. CI/CD pipeline → Release (risky arrow). 3: big, manual releases were where the weeks disappeared.

| Decision | Owner | Your part | Source |
| --- | --- | --- | --- |
| Move from Trello to Jira, starting with one initiative on the free tier | CTO and COO approved | Recommended | Evidence bank |
| Agile operating model across engineering, product and design | You | Owned | Evidence bank |
| Jira workflows designed around how the team worked; guide and workshop | You | Owned | Evidence bank |
| Feature flags | You proposed them, with examples from your engineering days; engineering built them | Recommended | Owner answer, Oct 2026 |
| CI/CD and DevOps practices | Engineering; you coached good practice | Shaped | Owner answer, Oct 2026 |
| Time-to-market baseline before Jira, then measured 3 and 6 months after | You | Owned | Owner answer, Oct 2026 |

### Q5. You say CI/CD and feature flags helped cut time-to-market. Who built the pipeline, and what exactly did you change?

**Stakes.** “When I joined Natoora in 2022, work lived in Trello with no velocity baseline, no delivery metrics and unpredictable releases. Getting from starting work to a release took over five weeks.”

**Split.** “I owned the operating model and the case for change, and the CTO and COO approved the tooling. On engineering practice I was an adviser, not the builder: I proposed feature flags, with examples from my own engineering days, and the team built them and found them useful. I also coached DevOps practices.”

**Sketch.** “Work flows from a Jira backlog through two-week sprints into a CI/CD pipeline with automated deployments, and releases go out behind feature flags. The risky arrow was the release: big, manual releases were where the weeks disappeared.”

**Shape.** “I documented the symptoms for two weeks and compared Trello, Jira, Asana and ClickUp on workflow, reporting, GitHub and Slack integration, and cost. Then I asked to pilot one initiative on Jira's free tier: no spend and fully reversible. I designed the workflows around how the team actually worked and ran the workshop.”

**Show.** “Approval followed the pilot evidence. I set a baseline before the move and measured again three and six months after: time-to-market fell from over five weeks to under three. The tool was the small part. One source of truth, smaller batches and feature flags did the work.”

**One level down:**

1. **Why do feature flags shorten time-to-market?** They separate deploying from releasing, so small changes ship often and risky ones stay switched off until ready.
2. **What would you measure besides time-to-market?** The DORA measures: deployment frequency, lead time, change failure rate and time to restore.

## S8 to S10 personal projects

For these three the decision split is simple: you owned every decision. That's what makes them your strongest evidence in architect, AI engineer and FDE interviews. Here, panels test a different boundary: personal project versus production. Your answers give the honest line: “These are personal projects. I use them myself and have shared them with a few friends, not with customers. The design notes are private, and I can share them if you'd like to see them.” Say it early, then pair each project with a work story that supplies the stakes.

**S8 Hatch.** Flow: 1. LangGraph supervisor → Scout · Scorer; 2. Scout · Scorer → Models; 3. Scout · Scorer → Your review (risky arrow); 4. Your review → Applications. There is no arrow from the agents to the outside world: you approve and submit everything. Decisions you own: human approval before any external action; primary/triage model routing for cost and latency; hard quality gates before changing a model (the July 2026 run kept the baseline); traces without prompt or CV content..

**S9 IncidentPilot.** Flow: 1. Evidence → Deterministic rules; 2. Evidence → Local model; 3. Local model → Deterministic rules (risky arrow); 4. Deterministic rules → Report. 3: the model suggests; rules decide. The tool is read-only and can't restart anything. Decisions you own: a read-only MVP; the model gets validated evidence and no tools; rules-only fallback when the model times out; golden-file evaluation with ten checks, including no_action_executed..

**S10 ResearchOps v2.** Flow: 1. Topic file → Source discovery; 2. Source discovery → Five-factor ranking; 3. Five-factor ranking → Claude Haiku (risky arrow); 4. Claude Haiku → Email digest. 3: the paid model sees only the top items, under hard token and cost caps. Decisions you own: rewriting v1 instead of extending it; four of five ranking scores deterministic and visible; the paid model only for top-N synthesis; token, query and daily cost caps, with a reported running cost of about £0.03 a day..

### Q6. Has any of this run for anyone other than you? What would you change before a customer used it?

**Model answer:** “These are personal projects. I use them myself and have shared them with a few friends, not with customers, so they haven't run at production load. Before a customer used one, I'd add authentication and per-user data separation, monitoring with alerts, a support route, and a security review. The design decisions I'd keep are the ones that matter in production: a person approves anything with consequences, deterministic rules sit around the model, and cost is capped. My design notes are private, and I can share them if you'd like to see them.”

> “Hatch is a personal project, not a client deployment. The design decision I'd defend first is that it never submits anything: agents draft, and I approve.”
> “IncidentPilot is a personal project. The decision I'd defend is keeping consequential actions out of the model's reach: deterministic rules first, the model second.”
> “ResearchOps is a personal project. I rewrote v1 rather than extend it, because hard-coded sources were the design flaw, not a missing feature.”
