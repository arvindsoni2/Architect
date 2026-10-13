# Shared evidence bank

**Status:** Owner-reviewed · **Last reviewed:** 13 October 2026

This is the factual base for all five role guides. On 13 October 2026 the owner confirmed that the portfolio case-study narratives (written early in 2026) are accurate, including the personal decisions they describe. Figures are self-reported professional outcomes, not an independent audit: know how each was measured, then state it plainly. Public portfolio links are the reader-facing references.

## Employment chronology

| Period | Actual role and context | Boundary |
| --- | --- | --- |
| August 2018–March 2020 | TCS Product Owner on the Northern Powergrid account | Initially small features and other initiatives; Smart Timesheet ran in 2019–March 2020 |
| March 2020–May 2022 | TCS Agile Delivery Manager, Northern Powergrid infrastructure upgrade | Separate initiative from Smart Timesheet; TCS employment ended May 2022 |
| May 2022–March 2026 | Natoora Scrum Master / Product Delivery Lead | Role made redundant in March 2026; describe it in the past tense |
| April 2026–present | Job search; no long-term role or contract secured yet | Use the agreed wording in the Accenture playbook (Q2) |

The role lens used in a portfolio URL is a way to explain the work. It is not a retrospective change of job title or an assertion that every architecture or engineering task was personally implemented.

## S1 GenAI order automation

**Context:** Natoora email-to-order workflow. Customer support previously read each incoming order email and manually entered it into the system, typically taking 2–3 minutes per order.

**Owner-confirmed outcome:** approximately **90% reduction in manual effort**. Exceptions remained when the agent could not complete an order. This is not a claim of 90% model accuracy or 90% of orders completed without intervention.

**Owner-confirmed decision rights:** the CTO decided to limit the rollout to London and Paris. Arvind identified customer service as a key stakeholder group during stakeholder analysis and involved them in the solution design and rollout.

**Owner-confirmed involvement:** rollout in **London and Paris**. Six-region deployment was a wider target; completion in other regions is not established by this record. The portfolio places this work in March–September 2025. **Owner-confirmed procurement systems:** London used **Marketman**; Paris used **Lightspeed**. Do not describe both regions as using Marketman.

**Decisions to discuss:** manageable pilot scope; customer-support participation; exception handling; integration with the order system; quality and cost trade-offs; rollout readiness and learning from operational feedback. Explain your decision rights and your collaboration with the developer.

**Metric defence:** describe how manual effort was measured, baseline workload, period and scope of comparison, exceptions and review effort. Time released is an operational benefit; cash savings require a separate cost calculation.

**Technical boundary:** GPT-4o-mini extracted order information with validation and exception handling. The model name is owner-confirmed. Do not claim zero risk, eliminated errors or an independently calibrated confidence score without evidence.

**Reference:** [GenAI case study](https://arvind-portfolio-iota.vercel.app/product-owner/work/genai-order-automation).

## S2 SaaS transformation

**Context:** Natoora's internal warehouse platform was adapted for external customers. The portfolio describes a nine-person UK/Brazil team and two customer implementations in January 2024–May 2025.

**Owner-confirmed personal decisions:** for Client 1 the team estimated 6–8 weeks of white-labelling, but the client expected go-live in four weeks. Arvind built an impact matrix (user-facing visibility, frequency of use, complexity), prioritised customer-facing order screens, email templates, login pages, reports and app branding, and deferred internal admin screens. Client 1 went live on schedule with fewer than 10 issues in a 30-day pilot and no Sev 1s. For Client 2 he created the structured onboarding pack: a 30-question pre-sales questionnaire, financial health check, technical requirements form and capabilities document. He planned SaaS work on an assumed 70% team availability, agreed transparently with the CTO.

**Owner-confirmed commercial figures:** **£28k setup fee**, **£1.6k recurring monthly revenue**, and **£29k reported profit in the first five months following rollout**. Recurring revenue supported cloud operations, developer support and other customer expenses. The owner was not in charge of the initiative after that period. Do not infer continued profit or treat recurring revenue as pure margin. The owner has confirmed the profit figure; the precise accounting calculation and customer aggregation are not reconstructed here.

**Portfolio comparison:** implementation investment was £9k for Client 1 and £7k for Client 2, approximately **22% lower implementation cost**. Stated delivery duration was four months versus two months, **50% shorter elapsed time**. These are separate comparisons; neither proves a causal productivity gain or like-for-like scope.

**Decisions to discuss:** client discovery; adapting a proven internal product; scope negotiation under a fixed launch expectation; repeatable onboarding; tenant isolation and support readiness; shared team capacity and distributed working.

**Metric defence:** clarify which customer and period each financial figure covers, costs included in profit, scope differences between implementations and which benefits came from reuse.

**Reference:** [SaaS case study](https://arvind-portfolio-iota.vercel.app/project-manager/work/saas-transformation). Keep customer identities generic in this collection.

## S3 Smart Timesheet

**Owner-confirmed dates and role:** **2019–March 2020**, while a **TCS Product Owner** on the Northern Powergrid account.

**Owner-confirmed technology:** OutSystems frontend hosted on AWS; a **.NET backend** connected legacy **Oracle HCM and CRM** to obtain employee data. Do not replace this with an invented custom web stack. Offline capability, native versus responsive delivery and specific GPS behaviour are not confirmed in this record.

**Owner-confirmed personal role:** Arvind led the rollout and took part from discovery through delivery, release and handover to the support team. The portfolio narrative is confirmed: field research with engineers at several depots; workshops with field operations, union representatives, payroll and IT; positioning the tool as making engineers' lives easier rather than tracking them; an alpha at one depot with 50 volunteer engineers for four weeks; a beta across three depots (200 engineers); phased depot-by-depot rollout over six months with a rollout playbook (pre-visit communication, on-site training, two-week hypercare, then BAU support); peer champions; monthly feedback sessions with a visible backlog of requested improvements.

**Portfolio-reported outcomes:** service for 2,000+ field engineers; approximately £500k annual savings; 50% fewer administrative office visits; eventual 3,000+ active users including supervisors and managers. Explain population, time window and calculation before using these figures. The earlier Accenture draft's >85% adoption within three months requires a denominator and supporting measurement before becoming a headline claim.

**Decisions to discuss:** research with field users; balancing payroll, operational and user needs; user stories and acceptance criteria; affordable platform choice; integration dependencies; phased rollout, champions and feedback.

**GDS bridge:** the alpha → beta → phased rollout, user research in the field and union/accessibility-style inclusion concerns are the closest real parallel to a government service lifecycle. Northern Powergrid was a regulated utilities client, so say "the same lifecycle principles" rather than claiming a formal GDS service assessment.

**Reference:** [Smart Timesheet case study](https://arvind-portfolio-iota.vercel.app/product-owner/work/smart-timesheet).

## S4 Infrastructure modernisation

**Owner-confirmed dates and role:** **March 2020–May 2022**, TCS Agile Delivery Manager at Northern Powergrid.

**Portfolio-reported scope and outcomes:** 120+ servers and 30+ applications, approximately £400k annual savings, distributed teams and controlled production migration. **£400k is a savings claim, not an established programme budget.** Do not turn 120 servers into 120 applications. The programme included different treatments such as retirement, upgrades and migration; distinguish these if asked how many systems were modernised.

**Decisions to discuss:** risk and business value ordering; dependency analysis; change preparation; rollback and production validation; documenting legacy knowledge; coordination with application owners and operations.

**Metric defence:** distinguish avoided support costs from cash released; state the affected period and which systems were counted. Do not claim all security or compliance risk was eliminated.

**Reference:** [Infrastructure case study](https://arvind-portfolio-iota.vercel.app/project-manager/work/infrastructure-modernisation).

## S5 Regulated banking delivery

**Context:** Nationwide work through TCS, including payments, Open Banking, GDPR and other regulatory initiatives. Previous guides and CVs describe cross-supplier coordination, release readiness and risk management.

**Use for:** compliance deadlines, supplier dependencies, escalation, testing, readiness and stakeholder influence. Select one initiative rather than combining several into one story. State the actual project role and your decision authority.

**Boundary:** the supplied portfolio has no standalone Nationwide case study that substantiates every number in earlier answer scripts. Specific dates, budgets, early-delivery claims and five-vendor counts require the owner's project records. Use the confirmed chronology and a defensible personal decision without unsupported precision.

## S6 ML recommendations — optional

**Portfolio-reported context:** recommendations for restaurant ordering, with user research, controlled testing and iterative placement. The portfolio reports a 10% average basket increase and 60% adoption; explain the cohort, comparison and adoption denominator before using them.

Do not call click-through or add-to-order measures **85% recommendation accuracy**. Precision, click-through and conversion are different measures. Keep this case optional until the measurement and personal technical contribution are sufficiently clear.

**Reference:** [Recommendation case study](https://arvind-portfolio-iota.vercel.app/product-owner/work/ml-recommendations).

## S7 Natoora Agile operating model and Jira

**Context:** when Arvind joined Natoora in 2022, delivery work was tracked in Trello with no velocity baseline, no delivery metrics and unpredictable releases.

**Owner-confirmed outcome:** time-to-market fell from **5+ weeks to under 3 weeks** (the portfolio rounds this to a 40% improvement). Arvind led the move from Trello to Jira and established the Agile operating model across engineering, product and design, with CI/CD, feature flags and automated deployments.

**How he won approval (from the owner's v9 preparation guide):** documented the symptoms for two weeks; compared Trello, Jira, Asana and ClickUp on workflow customisation, reporting, integration with GitHub/Slack and cost; asked the CTO and COO for permission to pilot one initiative on Jira's free tier (no cost, reversible); designed workflows around how the team actually worked, wrote a Jira guide and ran a workshop; then returned with pilot feedback and an updated cost-benefit case. Approval followed the evidence.

**Use for:** continuous improvement, Jira/Confluence, influencing senior stakeholders without authority, measuring delivery improvement.

**Metric defence:** time-to-market here means elapsed time from work starting to release. The improvement came from the operating model as a whole, not the tool alone.

## Behavioural stories (owner-supplied, 13 October 2026)

**B1 Conflict — one senior engineer, two launches (Natoora).** During implementation of the GenAI order automation and the multiple-basket feature, both initiatives turned out to need the same senior technical resource, which neither plan had identified. Losing that person from either project would derail both timelines. Arvind met Sales (multiple basket) and Customer Support (GenAI) separately with options — delay, reduce scope, phase the rollout — but neither would move on schedule or scope. He then ran a joint working session: made the dependency visible to everyone, circulated all options in advance, and tied the recommendation to the company's goals. GenAI carried higher strategic weight, while the multiple-basket go-to-market strategy was not yet finalised, so delaying it by 2–3 weeks (owner to confirm unit) cost little. He invited the CTO as the escalation route in case no option was workable. After negotiation, both teams agreed to finish the GenAI rollout first and then multiple basket. The meeting ended positively because everyone had seen the options beforehand.

**B2 Setback — delivered features nobody used (earlier consulting career).** Focused on delivering feature after feature, Arvind did not track usage after release. A client that had invested heavily in one feature came back because it had little traction, and he was asked to find out why and recommend a fix. He interviewed the teams involved and gathered customer feedback. The finding: the feature was built to specification without real users in mind, so users could not find it or use it meaningfully. He recommended a UI/UX expert review of the design for usability. Lesson he now applies: involve users, measure adoption after release and engage the customer regularly on feature utilisation. (Client and feature remain unnamed; supply them only if asked and permitted.)

**B3 Mentoring.** Arvind has mentored 20+ associates in Agile methods and 5 aspiring project managers into doing the PM job successfully, using Agile and DevOps games and coaching techniques gathered over his career. At Natoora he coached engineers on test-first development, pair programming and DevOps practices. Prepare one named-role example (for example, one aspiring PM: their starting gap, what you did together, what they then did independently).

**B4 Leadership mistake — backup (from the owner's v9 guide).** At Natoora, Arvind rolled out Scrum through team-wide announcements without first consulting a respected senior engineer, who then disengaged and influenced junior colleagues. He recovered through one-to-ones and a structural concession (no-meeting Fridays); the engineer became an advocate. Lesson: secure respected senior voices before announcing change. Use only if the panel asks specifically for a people or leadership mistake.

## Adding or correcting a story

Record context, actual role, dates, personal decision, action, alternative, result, measurement definition and source. Label a figure owner-confirmed, portfolio-reported or needing clarification. Change this record first; then review the role guides, vacancy supplements and corresponding portfolio text. A source agreement checks consistency, not truth on its own.
