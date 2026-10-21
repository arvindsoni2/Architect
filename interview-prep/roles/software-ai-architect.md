# Software and AI Architect interview guide

**Status:** Draft for owner review · **Last reviewed:** 13 October 2026 · **Sources checked:** 13 October 2026

Architect interviews test judgement: clarifying requirements before naming technology, choosing between credible options, explaining trade-offs in business terms and designing for failure. This guide has two tracks. **Track A** prepares solution and AI architect interviews: client-facing options, cloud and AI architecture, governance and the architecture review board. **Track B** prepares software architect interviews: system design depth, data, consistency and scaling. Most loops mix both.

**Your honest position:** your job titles were Product Owner, Agile Delivery Manager and Product Delivery Lead, not Architect. Your architecture evidence is the decisions you made or shaped in those roles, plus three public projects where you were the architect. Say that once, clearly, then let the reasoning carry the interview. Study depth is in the [AI Architect's Handbook](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html), the [System Design Concept Handbook](../../handbooks/system-design/system-design-concept-handbook-v6.html) and the [architecture curriculum](../../learning-paths/software-architect/software-architect-curriculum-guide-v3.md).

## What the 2026 loop looks like

| Format | What happens | What scores well |
| --- | --- | --- |
| Screening | Background, motivation and one architecture you can defend | A decision you made, with the alternative you rejected |
| Technical deep dive | Senior architects probe a design or a past system [1] | Clear non-functional requirements, trade-offs, failure modes |
| Whiteboard design | "Design a system for something we actually do" [2] | Your first three decisions and why, before any product names |
| Architecture presentation | You present a solution, then defend it | A story from problem to decision, not a tour of boxes |
| Leadership conversation | Influence, stakeholder conflict, cost [1] | Translating risk into money, time and outcomes |

Panels assess technical depth across the lifecycle, links from technical metrics to business outcomes, explaining complexity to non-technical people, and attention to total cost of ownership and maintainability. [1][2]

## Answer framework for any design question

Say the steps as you go: **clarify** users, use cases and non-functional requirements (scale, latency, availability, consistency, security, compliance) → **estimate** load and data volume → **sketch** the high-level design → **deep dive** on the riskiest part → **trade-offs** you chose and rejected → **failure modes and observability** → **security and compliance** → **cost** → **how it evolves**. For an AI system add four checks: how quality is **evaluated**, what **guardrails** bound the model, which **model** and why, and who is **accountable** when it is wrong. [3]

## Positioning and evidence

**Model opening (about 90 seconds):** "I've spent twenty years delivering technology in regulated sectors — utilities, banking, aviation and food tech — and the decisions I'm proudest of are architectural: how to adapt an internal platform for external customers without forking it, how to sequence 120-plus server upgrades without breaking production, and how to put an LLM into an order workflow with exceptions routed to people. I've also designed three AI systems myself, all built around one principle: the model proposes, deterministic controls decide. I'm moving into architecture because that's where I already add the most value — turning ambiguous requirements into decisions a team can build and operate."

| Evidence | Architectural decision to discuss | Boundary |
| --- | --- | --- |
| [S2 SaaS](../shared/evidence-bank.md#s2-saas-transformation) | Reusing an internal platform for external tenants; white-labelling scope; repeatable onboarding | Your role was delivery lead; name the engineers who implemented tenancy |
| [S4 infrastructure](../shared/evidence-bank.md#s4-infrastructure-modernisation) | Sequencing retirements, upgrades and migrations; rollback and validation | 120+ servers and 30+ applications; £400k is annual savings, not budget |
| [S1 order automation](../shared/evidence-bank.md#s1-genai-order-automation) | LLM extraction with validation and exception routing; pilot scope | The CTO limited the rollout to London and Paris |
| [S3 Smart Timesheet](../shared/evidence-bank.md#s3-smart-timesheet) | Low-code front end on AWS with a .NET integration layer to Oracle HCM and CRM | You owned product decisions; confirm who selected the platform before claiming it |
| [S9 IncidentPilot](../shared/evidence-bank.md#s9-incidentpilot--personal-open-source-project) | Read-only MVP; model with no tools; rules-only fallback | Personal project — you were the architect |
| [S8 Hatch](../shared/evidence-bank.md#s8-hatch--personal-open-source-project) | Human-in-the-loop trust boundary; primary/triage model routing; local or cloud | Personal project |
| [S10 ResearchOps v2](../shared/evidence-bank.md#s10-researchops-v2--personal-open-source-project) | Deterministic ranking with a narrow model role; cost ceilings | Personal project; v1 was redesigned |

## Track A — solution and AI architecture

### Q1. How do you design an AI solution that must run in a sovereign or UK-only cloud environment?

**Model answer:** "Start from the obligations: which data can leave which boundary, who may administer the platform, and what the customer must be able to audit. Then every component has to comply, not just storage — the model endpoint must be hosted in-region or self-hosted, logs and traces stay in-region, encryption keys are customer-managed, and support access is controlled. That often narrows the model choice, so I'd evaluate the in-region options on the actual workload early, before the design depends on a model that isn't available there." [1]

### Q2. Open-source models or proprietary API models for an enterprise?

**Model answer:** "Not a belief, a comparison on the workload. Proprietary APIs usually lead on capability and speed of adoption; open-weight models give control over data, versioning and cost at high volume, but the organisation then owns GPUs, patching, scaling and evaluation of every upgrade. I compare cost per successful task, data and contractual requirements, latency, and whether the team can operate it. A common answer is both: a hosted model for complex work and a small self-hosted model for high-volume simple tasks, behind one gateway."

### Q3. How do you ensure lineage, security and compliance in a distributed AI architecture?

**Model answer:** "Treat every derived artefact — chunks, embeddings, prompts, caches, fine-tuning sets, logs — as data with an owner, a purpose and a retention rule. Record lineage from source to answer: which documents and versions were retrieved for each response. Enforce access control at retrieval time, encrypt in transit and at rest, keep secrets out of model context, and make deletion propagate through every derived copy. Then prove it with audit logs and periodic tests rather than a policy document." [1]

### Q4. How do you manage model drift and keep performance up in production?

**Model answer:** "Distinguish three things that look alike: the world changing (new kinds of input), our system changing (prompt, index, model version) and the provider changing the model underneath us. Pin versions where possible, run a fixed evaluation set on every change and on a schedule, monitor online signals such as escalation and correction rates by segment, and add new failure cases to the evaluation set. A threshold breach triggers a defined response — rollback, reduced autonomy or retraining — not just an alert."

### Q5. Design a question-answering system over internal documentation that stays relevant and fresh.

**Model answer:** "Clarify users, document sources, permissions and how stale is acceptable. Ingest incrementally using content hashes so changed documents are re-indexed and deleted ones removed; carry access-control metadata onto every chunk and filter before generation. Use hybrid keyword and vector search with reranking, show citations with document dates, and let the system say when no current source answers. Measure retrieval recall and answer faithfulness on questions from real users, and give content owners a report of unanswered questions." [3]

### Q6. How would you reduce token costs at scale?

**Model answer:** "Measure cost per successful task by feature first. Then route simple requests to smaller models, cache stable prompt prefixes and repeated answers, send fewer and shorter retrieved chunks, cap output length, batch asynchronous work and remove retries that loop. Each change has to hold quality on the evaluation set. In ResearchOps I kept scoring on a local model and used the paid model only for the top items, with a hard daily cost ceiling."

### Q7. How do you detect and reduce ungrounded outputs?

**Model answer:** "Ground answers in retrieved sources with citations, check automatically that cited passages exist and support the claim where possible, allow the system to abstain, and measure the unsupported-claim rate on a labelled set. For high-consequence answers add human review. The architecture must make abstention a normal, visible outcome rather than an error."

### Q8. Fine-tune a model or use retrieval for a domain-specific assistant?

**Model answer:** "Retrieval first for knowledge that changes or must be cited — it is cheaper to update and easier to debug. Fine-tuning suits stable behaviour, style or format that prompting can't deliver reliably, or moving a proven task to a smaller model for cost or latency. The decision should come from an evaluation of both on the same cases, not from preference." [3]

### Q9. How do you decide between building and buying?

**Model answer:** "Buy what doesn't differentiate the business; build what does or what no product does well. I compare total cost over several years, including integration and operation, the exit cost if the vendor changes terms, data and security requirements, and how much the capability needs to change with the business. The Smart Timesheet is a useful example: an OutSystems front end on AWS for speed and cost, with a .NET integration layer to the client's Oracle HCM and CRM where control mattered." Say who made that platform decision. [2]

### Q10. A stakeholder wants everything multi-region active-active. How do you push back?

**Model answer:** "Ask what an hour of downtime actually costs for each service and what recovery time and data-loss limits the business needs. Active-active roughly doubles infrastructure and adds data-consistency complexity, so I'd propose it only where the numbers justify it and offer cheaper patterns elsewhere — a warm standby or backup-and-restore — with the cost and recovery time of each side by side. The stakeholder then chooses with the trade-off visible." [2]

### Q11. How do you keep a cloud bill from quietly tripling?

**Model answer:** "Treat cost as a design requirement: tag resources to owners and products, set budgets and anomaly alerts, review cost per transaction or per customer rather than the total, right-size and schedule non-production environments, and use committed-use pricing only for steady load. For AI workloads add token and request dashboards, because model spend grows with prompts and usage without any code change." [2]

### Q12. Which well-architected pillar do teams ignore most?

**Model answer:** "The AWS framework has six pillars: operational excellence, security, reliability, performance efficiency, cost optimisation and sustainability. In my experience operational excellence is the one most neglected — runbooks, observability, safe deployment and learning from incidents — because it doesn't show up in a demo. It's the pillar that decides whether the other five survive the first year in production."

### Q13. How does architecture make AI governance real rather than a document?

**Model answer:** "By turning obligations into enforced controls with evidence: an inventory of AI systems and their risk tier; approval gates in the deployment pipeline; access control and logging at the model gateway; evaluation results attached to every release; and a way to reduce or withdraw a system's authority quickly. Frameworks such as NIST's AI Risk Management Framework and ISO/IEC 42001 help structure this. In the EU, Article 50 transparency duties have applied since August 2026 and the AI Omnibus moved most high-risk obligations to December 2027, so the timeline must be checked for each system rather than assumed."

## Track B — software architecture and system design

### Q14. Design a system for something we actually do. What are your first three decisions?

**Model answer:** "First, what the system must guarantee — the one or two non-functional requirements that dominate, such as consistency for payments or latency for search. Second, the boundaries: which parts change together and which teams own them, which shapes services and data ownership. Third, the data model and where the source of truth lives. Technology choices come after those, and I'd say what would make me change each decision." [2]

### Q15. When would you choose a monolith over microservices?

**Model answer:** "Usually at the start, and whenever the team is small or the domain boundaries are still unclear. A well-structured modular monolith is faster to change and simpler to operate. I'd split a service out when there's a clear reason — independent scaling, a different release cadence, a separate team, or isolation of a risky component — and accept the cost in networking, observability and data consistency." [2]

### Q16. Strong or eventual consistency — how do you decide, and how do you keep data correct across services?

**Model answer:** "By the cost of a wrong or stale read. Balances and inventory reservations need strong consistency at the point of decision; a product catalogue or a feed can be eventually consistent. Across services I avoid distributed transactions: the transactional outbox pattern publishes events reliably with the local change, consumers are idempotent, and a saga with compensating actions handles multi-step business processes."

### Q17. How would you scale a read-heavy service?

**Model answer:** "Measure first. Then cache at the right layer — CDN for static content, an application cache for hot objects — with an explicit invalidation strategy, add read replicas and accept their replication lag where the use case allows, and denormalise or precompute views for expensive queries. Watch the cache hit rate and the load on the database when the cache is cold."

### Q18. Design a distributed job queue with priorities, retries and a dead-letter queue.

**Model answer:** "Producers write jobs with an ID, priority and idempotency key to a durable store or broker. Workers pull by priority with a visibility timeout, so a crashed worker's job reappears. Failures retry with exponential backoff and jitter up to a limit, then move to a dead-letter queue with the error for inspection and replay. Jobs must be idempotent because delivery is at least once. Expose queue depth, age of the oldest job and retry rates, and protect low-priority work from starvation." [4]

### Q19. Design a rate limiter with per-user and global limits.

**Model answer:** "A token bucket per user and one global bucket, both checked atomically on each request — in a shared store such as Redis with a script, so multiple API instances agree. Return a clear 429 with a retry-after time. Decide what happens if the store is unavailable — fail open for low-risk endpoints, closed for expensive ones — and monitor rejection rates so legitimate users aren't being throttled." [4]

### Q20. How do you design APIs that others can depend on?

**Model answer:** "Contract first: clear resources, consistent errors, pagination, idempotency keys for writes, and versioning with a deprecation policy. Design for the consumer's workflow rather than the database tables, document with examples, and test the contract automatically so a change that breaks consumers fails the build."

### Q21. How would you modernise a legacy estate without stopping the business?

**Model answer:** "Inventory and classify first — retire, upgrade, migrate or replace — then sequence by business risk and dependency, not by technology. Use the strangler-fig approach for applications: route traffic through a façade and move capabilities one at a time. Every change needs rollback and production validation agreed with the application owner. At Northern Powergrid we treated 120-plus servers and 30-plus applications differently by category rather than as one migration, which kept production stable."

### Q22. How do you design for multiple tenants?

**Model answer:** "Choose the isolation model per layer — shared, pooled with tenant IDs, or dedicated — based on security, noisy-neighbour risk and cost, and enforce tenant identity at every query, cache key, log and backup. When we adapted Natoora's internal platform for external customers, the decisions were about white-labelling and configuration without forking the product, plus a repeatable onboarding process, so a second customer did not mean a second codebase."

### Q23. How do you define and use SLOs?

**Model answer:** "Pick a few indicators users feel — availability, latency, correctness — set objectives with the business, and use the error budget to balance release speed and reliability: if the budget is spent, the team prioritises reliability work. For AI features add behavioural indicators such as unsupported-answer rate, because a fast, available service can still be wrong."

## Influence and judgement

### Q24. Tell me about a design you got wrong.

**Model answer:** "My first version of ResearchOps used CrewAI with hard-coded sources. It worked for AI topics but I'd designed the topic and the source list into the code, so every new subject meant code changes. I wrote proper requirements for version two — any topic as a configuration file, sources discovered and vetted at run time, ranking that can be audited, and a cost ceiling — and rebuilt it rather than patching. The lesson I apply now: separate what changes often from what doesn't, and write that down before choosing a framework." [2]

### Q25. You designed the right solution and the team didn't want to build it. What did you do?

**Model answer:** "Find out why before escalating — resistance often contains information. When I wanted Natoora to move from Trello to Jira, I documented the problems for two weeks, compared four tools on workflow, reporting, integrations and cost, and asked for a free, reversible pilot on one initiative. I designed the workflows around how the team actually worked and came back with the pilot results. Approval followed the evidence; I hadn't needed to win an argument." [2]

### Q26. Explain a hard technical trade-off as if I were the CFO.

**Model answer:** "Put it in money, time and risk. For example: 'A full white-label would take six to eight weeks; the client needs four. If we brand the customer-facing screens, emails, login and reports first and defer internal admin screens, we meet the date. The risk is that internal users work with unbranded admin screens for a while, which costs us nothing with the customer.' No jargon, one recommendation, and what would change it."

### Q27. Sales promised a client something the architecture can't do. What happens next week?

**Model answer:** "Separate what was promised from what is buildable, quickly and honestly. I'd find the outcome the client actually needs, propose what we can deliver and when, with the cost of the alternative, and go with the account lead to the client together rather than leaving sales to backtrack alone. Then fix the process: a technical review before commitments of that kind." [2]

### Q28. When is "good enough" the right architecture?

**Model answer:** "When it meets the requirement with a clear path to change, and the cost of more design exceeds the risk it removes. IncidentPilot's first version is deliberately read-only: it can't restart anything. That made it safe enough to run and evaluate now, and the evaluation will tell me when approval-gated actions are justified."

### Q29. What do you document, and what do you let the code carry?

**Model answer:** "Document the why: decisions, alternatives rejected and the conditions that would reopen them, in short architecture decision records next to the code. Let the code, tests and API contracts carry the what. A diagram that nobody updates is worse than none, so I keep a small number of current views." [2]

### Q30. Tell me about mentoring someone through a hard technical problem.

**Model answer:** Use the mentoring record in [B3](../shared/evidence-bank.md#behavioural-stories-owner-supplied-13-october-2026): at Natoora you coached engineers on test-first development, pair programming and DevOps practices. Prepare one specific person, the problem, how you helped them reason rather than handing over the answer, and what they then did on their own.

## Presenting an architecture

If asked to present, tell a story: the problem and who has it, the requirements that drive the design, two or three options with their trade-offs, the decision, how it fails and how you'd know, the cost, and what you'd do next. Leave time for questions; the defence matters more than the slides.

## Credibility probes

Were you the architect or the delivery lead? Who signed off the design? What did it cost to run? What broke in production? Which decision would you reverse? For the personal projects: what load have they handled, and what would you change before a customer used them? Answer within your actual role; reasoning quality earns the credit.

## Questions to ask the panel

How are architecture decisions made and recorded here? How much of the role is hands-on? Which non-functional requirement causes the most trouble today? How do you govern AI use across teams?

## Sources and freshness

Checked 13 October 2026.

1. [Capgemini AI Architect interview guide](https://dataford.io/interview-guides/capgemini/ai-architect) — Dataford, updated 1 August 2026.
2. [Solutions architect interview questions](https://www.kore1.com/solutions-architect-interview-questions/) — KORE1, 28 July 2026 (a recruiting firm's view).
3. [Generative AI system design interview guide](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/) — System Design Handbook, updated 15 July 2026.
4. [Forward Deployed Engineer interview guide](https://www.aced.io/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde) — Aced, for the job-queue and rate-limiter questions also used in engineering loops.
5. LinkedIn's hiring guides for [software architects](https://business.linkedin.com/talent-solutions/resources/how-to-hire-guides/software-architect/interview-questions) and [solution architects](https://business.linkedin.com/talent-solutions/resources/how-to-hire-guides/solution-architect/interview-questions) — generic scalability, API and influence questions.
6. EU AI Act dates as verified in the [AI Architect's Handbook](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html) on 13 October 2026.
