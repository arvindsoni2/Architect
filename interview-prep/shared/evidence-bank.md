# Shared evidence bank

**Status:** Owner-reviewed · **Last reviewed:** 28 October 2026

This is the factual base for all eight role guides. On 13 October 2026 the owner confirmed that the portfolio case-study narratives (written early in 2026) are accurate, including the personal decisions they describe. Figures are self-reported professional outcomes, not an independent audit: know how each was measured, then state it plainly. Public portfolio links are the reader-facing references. On 26–28 October 2026 the owner also confirmed decision rights and architecture details for each story; these are marked “Owner-confirmed” below and set out story by story in the [decision lists](decision-ledger.md), using the method in [Connect the dots](connect-the-dots.md).

## Employment chronology

| Period | Actual role and context | Boundary |
| --- | --- | --- |
| September 2017–June 2018 | TCS project manager, Nationwide Building Society GDPR programme | Owner-confirmed in October 2026; see S5 |
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

**Owner-confirmed on 26–28 October 2026:** Arvind wrote the product requirements (risk, cost and benefit), shared them with customer support, and defined the evaluation approach and success metrics. Using an LLM came out of a discussion he was part of, backed by the CTO. The tech lead chose GPT-4o-mini for cost and latency, and the developer built the integration into WS (Natoora's warehouse system) through its API, with Python and scheduled jobs. Orderers' names and addresses were stripped or randomised before anything reached the model, and the CTO and lead developer reviewed data protection and security. Duplicates were prevented by checking the order reference and order items, with WS flagging likely duplicates. The 90% figure compares average handling time per order before and after, including time still spent on exceptions, over two to three months of experiments as each procurement system was added; Arvind presented it to stakeholders.

**Architecture in three boxes:** order emails and PDFs → GPT-4o-mini extraction → validation and order creation in WS, with human review for exceptions. **Decision list and follow-ups:** [S1 in the decision lists](decision-ledger.md#s1-genai-order-automation); one level down, [System Design v6, chapter 11](../../handbooks/system-design/system-design-concept-handbook-v6.html#c11) on idempotency and the [AI Evaluation Field Guide](../../handbooks/ai-evaluation/ai-evaluation-field-guide-2026.html).

**Metric defence:** describe how manual effort was measured, baseline workload, period and scope of comparison, exceptions and review effort. Time released is an operational benefit; cash savings require a separate cost calculation.

**Technical boundary:** GPT-4o-mini extracted order information with validation and exception handling. The model name is owner-confirmed. Do not claim zero risk, eliminated errors or an independently calibrated confidence score without evidence.

**Reference:** [GenAI case study](https://arvind-portfolio-iota.vercel.app/product-owner/work/genai-order-automation).

## S2 SaaS transformation

**Context:** Natoora's internal warehouse platform was adapted for external customers. The portfolio describes a nine-person UK/Brazil team and two customer implementations in January 2024–May 2025.

**Owner-confirmed personal decisions:** for Client 1 the team estimated 6–8 weeks of white-labelling, but the client expected go-live in four weeks. Arvind built an impact matrix (user-facing visibility, frequency of use, complexity), prioritised customer-facing order screens, email templates, login pages, reports and app branding, and deferred internal admin screens. Client 1 went live on schedule with fewer than 10 issues in a 30-day pilot and no Sev 1s. For Client 2 he created the structured onboarding pack: a 30-question pre-sales questionnaire, financial health check, technical requirements form and capabilities document. He planned SaaS work on an assumed 70% team availability, agreed transparently with the CTO.

**Owner-confirmed commercial figures:** **£28k setup fee**, **£1.6k recurring monthly revenue**, and **£29k reported profit in the first five months following rollout**. Recurring revenue supported cloud operations, developer support and other customer expenses. The owner was not in charge of the initiative after that period. Do not infer continued profit or treat recurring revenue as pure margin. The owner has confirmed the profit figure; the precise accounting calculation and customer aggregation are not reconstructed here.

**Portfolio comparison:** implementation investment was £9k for Client 1 and £7k for Client 2, approximately **22% lower implementation cost**. Stated delivery duration was four months versus two months, **50% shorter elapsed time**. These are separate comparisons; neither proves a causal productivity gain or like-for-like scope.

**Decisions to discuss:** client discovery; adapting a proven internal product; scope negotiation under a fixed launch expectation; repeatable onboarding; tenant isolation and support readiness; shared team capacity and distributed working.

**Owner-confirmed on 26–28 October 2026:** each client had its own database, schema and cloud environment on Google Cloud, built from Terraform templates: one codebase with a separate stack per client (the silo model), not a shared multi-tenant database. The CTO and tech lead decided the architecture; Arvind took part in the architecture reviews and in the design and database decisions that affected delivery. Client 1 went live with some security items still open: the CTO reviewed it, the client signed off, and enough protection was in place that client data was not at risk. Arvind owned the technical-debt plan and tracked each open item in Jira until it was closed; finishing the Angular migration after go-live closed them. The sysadmin and CTO monitored cloud cost per client, because it affected both the client's margin and Natoora's.

**Decision list and follow-ups:** [S2 in the decision lists](decision-ledger.md#s2-saas-transformation); one level down, the architect guide's [multi-tenancy question](../roles/software-ai-architect.md#q22-how-do-you-design-for-multiple-tenants).

**Metric defence:** clarify which customer and period each financial figure covers, costs included in profit, scope differences between implementations and which benefits came from reuse.

**Reference:** [SaaS case study](https://arvind-portfolio-iota.vercel.app/project-manager/work/saas-transformation). Keep customer identities generic in this collection.

## S3 Smart Timesheet

**Owner-confirmed dates and role:** **2019–March 2020**, while a **TCS Product Owner** on the Northern Powergrid account.

**Owner-confirmed technology:** OutSystems frontend hosted on AWS; a **.NET backend** connected legacy **Oracle HCM and CRM** to obtain employee data. Do not replace this with an invented custom web stack. Owner-confirmed in October 2026: engineers used an OutSystems native app that stored timesheets on the phone and synced when back online; a responsive desktop web app was deferred from the first release. Specific GPS behaviour is not confirmed in this record.

**Owner-confirmed personal role:** Arvind led the rollout and took part from discovery through delivery, release and handover to the support team. The portfolio narrative is confirmed: field research with engineers at several depots; workshops with field operations, union representatives, payroll and IT; positioning the tool as making engineers' lives easier rather than tracking them; an alpha at one depot with 50 volunteer engineers for four weeks; a beta across three depots (200 engineers); phased depot-by-depot rollout over six months with a rollout playbook (pre-visit communication, on-site training, two-week hypercare, then BAU support); peer champions; monthly feedback sessions with a visible backlog of requested improvements.

**Portfolio-reported outcomes:** service for 2,000+ field engineers; approximately £500k annual savings; 50% fewer administrative office visits; eventual 3,000+ active users including supervisors and managers. Explain population, time window and calculation before using these figures. The earlier Accenture draft's >85% adoption within three months requires a denominator and supporting measurement before becoming a headline claim.

**Decisions to discuss:** research with field users; balancing payroll, operational and user needs; user stories and acceptance criteria; affordable platform choice; integration dependencies; phased rollout, champions and feedback.

**Owner-confirmed architecture and governance (26 October 2026):** TCS, as implementation partner, chose OutSystems for rapid prototype-to-production delivery. OutSystems hosted the platform on AWS; Northern Powergrid had no direct relationship with AWS. Arvind attended Northern Powergrid's Architecture Review Board in person, because the initiative needed rulings on data sovereignty, GDPR impact and design review. The board required employee data to stay in the UK and approved sharing only employee ID, name and day rate with the cloud app; that ruling decided whether the initiative was viable. The .NET middleware called Oracle HCM and CRM through APIs, and an approved timesheet triggered API calls to HCM, CRM and payroll.

**Decision list and worked answer:** [S3 in the decision lists](decision-ledger.md#s3-smart-timesheet) and the [Architecture review worked example](architecture-review.md#worked-example-smart-timesheet).

**GDS bridge:** the alpha → beta → phased rollout, user research in the field and union/accessibility-style inclusion concerns are the closest real parallel to a government service lifecycle. Northern Powergrid was a regulated utilities client, so say "the same lifecycle principles" rather than claiming a formal GDS service assessment.

**Reference:** [Smart Timesheet case study](https://arvind-portfolio-iota.vercel.app/product-owner/work/smart-timesheet).

## S4 Infrastructure modernisation

**Owner-confirmed dates and role:** **March 2020–May 2022**, TCS Agile Delivery Manager at Northern Powergrid.

**Portfolio-reported scope and outcomes:** 120+ servers and 30+ applications, approximately £400k annual savings, distributed teams and controlled production migration. **£400k is a savings claim, not an established programme budget.** Do not turn 120 servers into 120 applications. The programme included different treatments such as retirement, upgrades and migration; distinguish these if asked how many systems were modernised.

**Decisions to discuss:** risk and business value ordering; dependency analysis; change preparation; rollback and production validation; documenting legacy knowledge; coordination with application owners and operations.

**Owner-confirmed on 26–28 October 2026:** the programme ran in three phases. Arvind led delivery of phases 1 and 2 (six months of quick wins, then twenty months of complex migrations); phase 3 went ahead after he left TCS in May 2022. Engineers and architects created the retire, replatform, refactor and replace strategies; the project sponsor decided each application's treatment with Northern Powergrid and TCS architects; the TCS technical team chose target Windows and Oracle versions; Northern Powergrid's ARB approved upgrades, and the weekly CAB approved every production change. Arvind made sure every application was properly impact-assessed and that each treatment served the goal of fewer servers on legacy software. One migration failed, was rolled back to its previous state and moved to a later phase. The £400k a year is about £350k hard cash (Microsoft and Oracle extended-support fees no longer paid) and about £50k soft benefit (engineer time no longer spent on patching and upgrades). Lead with £400k and give the split if asked; the CV figure stays at £400k.

**Decision list and follow-ups:** [S4 in the decision lists](decision-ledger.md#s4-infrastructure-modernisation); one level down, the architect guide's [legacy modernisation question](../roles/software-ai-architect.md#q21-how-would-you-modernise-a-legacy-estate-without-stopping-the-business) and [Architecture review](architecture-review.md#what-a-review-board-is-for) on CAB versus ARB.

**Metric defence:** distinguish avoided support costs from cash released; state the affected period and which systems were counted. Do not claim all security or compliance risk was eliminated.

**Reference:** [Infrastructure case study](https://arvind-portfolio-iota.vercel.app/project-manager/work/infrastructure-modernisation).

## S5 Regulated banking delivery

**Context:** Nationwide work through TCS, including payments, Open Banking, GDPR and other regulatory initiatives. Previous guides and CVs describe cross-supplier coordination, release readiness and risk management.

**Use for:** compliance deadlines, supplier dependencies, escalation, testing, readiness and stakeholder influence. Select one initiative rather than combining several into one story. State the actual project role and your decision authority.

**Boundary:** the supplied portfolio has no standalone Nationwide case study that substantiates every number in earlier answer scripts. Specific dates, budgets, early-delivery claims and five-vendor counts require the owner's project records. Use the confirmed chronology and a defensible personal decision without unsupported precision.

**Owner-confirmed initiative (28 October 2026):** the GDPR programme, September 2017 to June 2018, with Arvind as TCS project manager. Five suppliers took part: Capgemini, IBM, Accenture, TCS and Infosys. Nationwide's release manager or programme manager had authority over scope and release. Arvind coordinated the suppliers, kept the end-to-end and integration test environments available when the test team needed them, drove programme-level defects to resolution, made sure every risk and issue raised at the bi-weekly governance meeting had a named owner, and reported progress. The test environments were available about 90% of the time; know the denominator before quoting it. The programme was signed off two weeks before the 25 May 2018 deadline. This replaces the boundary above for the GDPR programme.

**Decision list:** [S5 in the decision lists](decision-ledger.md#s5-gdpr-programme-at-nationwide).

## S6 ML recommendations — optional

**Portfolio-reported context:** recommendations for restaurant ordering, with user research, controlled testing and iterative placement. The portfolio reports a 10% average basket increase and 60% adoption; explain the cohort, comparison and adoption denominator before using them.

Do not call click-through or add-to-order measures **85% recommendation accuracy**. Precision, click-through and conversion are different measures. Keep this case optional until the measurement and personal technical contribution are sufficiently clear.

**Owner-confirmed role (28 October 2026):** Arvind owned the product discussions with stakeholders, including the COO's concern that recommendations would hurt sales of premium produce. Describe the 85% figure as a click-through and add-to-order rate, and lead with that stakeholder story rather than the model.

**Reference:** [Recommendation case study](https://arvind-portfolio-iota.vercel.app/product-owner/work/ml-recommendations).

## S7 Natoora Agile operating model and Jira

**Context:** when Arvind joined Natoora in 2022, delivery work was tracked in Trello with no velocity baseline, no delivery metrics and unpredictable releases.

**Owner-confirmed outcome:** time-to-market fell from **5+ weeks to under 3 weeks** (the portfolio rounds this to a 40% improvement). Arvind led the move from Trello to Jira and established the Agile operating model across engineering, product and design, with CI/CD, feature flags and automated deployments.

**How he won approval (from the owner's v9 preparation guide):** documented the symptoms for two weeks; compared Trello, Jira, Asana and ClickUp on workflow customisation, reporting, integration with GitHub/Slack and cost; asked the CTO and COO for permission to pilot one initiative on Jira's free tier (no cost, reversible); designed workflows around how the team actually worked, wrote a Jira guide and ran a workshop; then returned with pilot feedback and an updated cost-benefit case. Approval followed the evidence.

**Use for:** continuous improvement, Jira/Confluence, influencing senior stakeholders without authority, measuring delivery improvement.

**Owner-confirmed on 26 October 2026:** Arvind proposed feature flags, with examples from his own engineering work; engineering built them and found them useful. He coached DevOps practice, and engineering owned CI/CD. Time-to-market was baselined before the Jira move and measured again three and six months after. **Decision list:** [S7 in the decision lists](decision-ledger.md#s7-agile-operating-model-and-jira).

**Metric defence:** time-to-market here means elapsed time from work starting to release. The improvement came from the operating model as a whole, not the tool alone.

## Behavioural stories (owner-supplied, 13 October 2026)

**B1 Conflict — one senior engineer, two launches (Natoora).** During implementation of the GenAI order automation and the multiple-basket feature, both initiatives turned out to need the same senior technical resource, which neither plan had identified. Losing that person from either project would derail both timelines. Arvind met Sales (multiple basket) and Customer Support (GenAI) separately with options — delay, reduce scope, phase the rollout — but neither would move on schedule or scope. He then ran a joint working session: made the dependency visible to everyone, circulated all options in advance, and tied the recommendation to the company's goals. GenAI carried higher strategic weight, while the multiple-basket go-to-market strategy was not yet finalised, so delaying it by 2–3 weeks (owner to confirm unit) cost little. He invited the CTO as the escalation route in case no option was workable. After negotiation, both teams agreed to finish the GenAI rollout first and then multiple basket. The meeting ended positively because everyone had seen the options beforehand.

**B2 Setback — delivered features nobody used (earlier consulting career).** Focused on delivering feature after feature, Arvind did not track usage after release. A client that had invested heavily in one feature came back because it had little traction, and he was asked to find out why and recommend a fix. He interviewed the teams involved and gathered customer feedback. The finding: the feature was built to specification without real users in mind, so users could not find it or use it meaningfully. He recommended a UI/UX expert review of the design for usability. Lesson he now applies: involve users, measure adoption after release and engage the customer regularly on feature utilisation. (Client and feature remain unnamed; supply them only if asked and permitted.)

**B3 Mentoring.** Arvind has mentored 20+ associates in Agile methods and 5 aspiring project managers into doing the PM job successfully, using Agile and DevOps games and coaching techniques gathered over his career. At Natoora he coached engineers on test-first development, pair programming and DevOps practices. Prepare one named-role example (for example, one aspiring PM: their starting gap, what you did together, what they then did independently).

**B4 Leadership mistake — backup (from the owner's v9 guide).** At Natoora, Arvind rolled out Scrum through team-wide announcements without first consulting a respected senior engineer, who then disengaged and influenced junior colleagues. He recovered through one-to-ones and a structural concession (no-meeting Fridays); the engineer became an advocate. Lesson: secure respected senior voices before announcing change. Use only if the panel asks specifically for a people or leadership mistake.

## S8 Hatch — personal open-source project

**What it is:** a self-hosted, human-in-the-loop workspace for job search, applications and interview preparation, published at [github.com/arvindsoni2/hatch](https://github.com/arvindsoni2/hatch). It is a personal project, not a client deployment; say so plainly.

**Architecture (from the public repository):** a LangGraph supervisor coordinates four agents — Scout (discovers roles), Scorer (ranks them against the profile), Tailor (prepares evidence-grounded CV and cover-letter packs) and Coach (interview preparation). Python/FastAPI backend, Next.js frontend, Docker Compose deployment. AI can run locally through llama.cpp with a larger **primary** model for detailed work and a smaller **triage** model for fast relevance filtering, or through a configured cloud provider (Gemini, OpenRouter, OpenAI or Anthropic); the app also works with AI deferred.

**Trust boundary:** Hatch never submits an application; generated documents require human review; provider secrets stay on the host, not in the browser; optional OpenTelemetry traces exclude prompt, response, CV and job-description content.

**Evaluation evidence:** a staged local-model selection run on 18 July 2026 completed 27 of 27 scheduled pairs with 100% schema success and zero unsupported claims or numeric tokens. No challenger passed the hard quality gates, so the decision was to **retain the baseline model**. Use this as a story about letting evaluation, not novelty, decide a model change.

**Decisions to discuss:** human approval before any external action; primary/triage routing for cost and latency; local versus cloud models; hard gates before changing a model; observability without sensitive content.

## S9 IncidentPilot — personal open-source project

**What it is:** a local-first incident triage agent for Docker and Podman services, published at [github.com/arvindsoni2/IncidentPilot](https://github.com/arvindsoni2/IncidentPilot). It collects operational evidence (runtime status, bounded logs, HTTP health, dependencies, deployments, optional Prometheus), applies deterministic rules, optionally asks an Ollama-compatible model to rank evidence-grounded hypotheses, and writes JSON and SRE-style Markdown reports.

**Design decisions:** the MVP is deliberately **read-only** — it cannot restart containers, roll back or run shell commands. The model receives validated, structured evidence and **no tools**; deterministic rules keep control of severity, evidence references, actions and approval flags. If the model times out, the workflow falls back to rules-only diagnosis.

**Evaluation evidence:** golden-file evaluations for two injected failure scenarios (FS-001, FS-002). A run passes only if all ten checks pass, including `rank1_cause_correct`, `recommendation_action_correct` and `no_action_executed`. CI runs a live integration job that builds the demo stack, injects both failures, verifies the persisted diagnosis and resets the services. Stack: FastAPI, Jinja/HTMX dashboard, Typer CLI, SQLAlchemy with SQLite and versioned migrations. The owner has also used it as a benchmark project for comparing coding-agent harnesses (Claude Code, Codex, OpenCode and Cline).

**Decisions to discuss:** keeping consequential actions out of the model's reach; deterministic first, model second; graceful degradation; how the golden set was chosen and what it does not cover.

## S10 ResearchOps v2 — personal open-source project

**What it is:** an autonomous research digest, published at [github.com/arvindsoni2/researchops-v2](https://github.com/arvindsoni2/researchops-v2). The owner wrote the product requirements (dated 21 May 2026) after v1 — built on CrewAI with hard-coded sources — proved too narrow. v2 accepts any topic as a Markdown file, discovers and vets sources at run time, ranks every item on a five-factor rubric, writes a short "why it matters" note for the top items with Claude Haiku, and emails a digest on a cron schedule.

**Design decisions:** four of the five ranking sub-scores are deterministic; only relevance is model-judged, and every sub-score is visible so the ranking can be audited. Local Ollama (Qwen) does the scoring; the paid model is used only for the top-N synthesis, grounded in each item's own content. Hard caps on tokens, search queries and a daily cost ceiling; reported running cost is about £0.03 a day for three daily topics (target ≤ £5 a month). SQLite tracks seen items for novelty; each run writes a structured JSON log and failures send an error email.

**Decisions to discuss:** rewriting instead of extending v1; deterministic scoring with a narrow model role; cost as a design constraint; zero hard-coded credentials.

**Owner-confirmed boundary for S8–S10 (28 October 2026):** these are personal projects, used by the owner and shared with a few friends, not with customers. Design notes exist but are private; offer to share them if a panel asks. **Decision list:** [S8 to S10 in the decision lists](decision-ledger.md#s8-to-s10-personal-projects).

## S11 Computer vision QA — in progress, optional

**Owner-confirmed (28 October 2026):** Arvind was Product Owner on Natoora's computer vision quality-assurance initiative, working with stakeholders in operations. Classification accuracy was about 80% on quality parameters such as freshness and ripeness. The work is still in progress, and Arvind is also building his own version as a personal project, using mock data that simulates Natoora's API calls.

**Boundary:** present it as in progress, not as a delivered system, and don't quote delivered results such as reduced food waste or faster goods-in until they are established. Keep the personal build separate and call it a personal project. Hosting (managed cloud or on-premise edge) is not settled, so leave it out until it is.

## Credentials and learning

Owner-stated credentials: PMP, PMI-ACP, PSM I, PSPO I and PSPO II (Scrum.org, 16 October 2026, verifiable at scrum.org/certificates/1356776); AWS Certified AI Practitioner (AIF-C01), passed April 2026; currently preparing for AWS Solutions Architect Associate (SAA-C03). Completed course: **GeeksforGeeks — AI Engineering Course: Generative AI & Agentic AI** (certificate held by the owner). Coursera courses: to be added once the owner supplies the course names. Confirm credential IDs and dates before quoting them, and pair each with something you built or decided — certificates show learning, not role experience.

## Adding or correcting a story

Record context, actual role, dates, personal decision, action, alternative, result, measurement definition and source. Label a figure owner-confirmed, portfolio-reported or needing clarification. Change this record first; then review the role guides, vacancy supplements and corresponding portfolio text. A source agreement checks consistency, not truth on its own.
