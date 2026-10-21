# Forward Deployed Engineer interview guide

**Status:** Draft for owner review · **Last reviewed:** 13 October 2026 · **Sources checked:** 13 October 2026

A forward deployed engineer (FDE) works inside a customer's organisation to get software — now usually AI systems — into production and producing value. Interviews therefore blend software engineering with consulting: you will decompose a vague problem, write practical code, design a system that survives a real customer environment, and handle a difficult customer conversation. For the Accenture vacancy, add the [Accenture FDE supplement](../vacancies/accenture-fde.md); for depth, use the [FDE Handbook](../../handbooks/fde/fde-handbook-v1.6.html).

**Your honest position:** years of client-facing delivery (TCS consulting for utilities and banking clients, external SaaS customers at Natoora), one production AI rollout, and current hands-on AI engineering shown through three public projects. Panels value end-to-end ownership and customer judgement; be precise about which parts you coded yourself.

## What the 2026 loop looks like

Public accounts describe these loops. They are second-hand and change often; confirm with the recruiter. [1][2][3]

| Employer | Reported stages | Distinctive round |
| --- | --- | --- |
| OpenAI | Recruiter screen; take-home of about five hours on its APIs (for example a RAG system, agent or eval harness); walkthrough; onsite with hiring manager, technical and design/case rounds | Defending your take-home decisions |
| Anthropic | Recruiter screen; take-home; hiring-manager deep dive on a project; timed coding where each level builds on your previous code; technical design (rate limiter, job queue, LLM system); mission round | Progressive coding and mission alignment |
| Palantir | Coding screen; coding; system or data design; a 60-minute decomposition with no code; a learning round fixing bugs in an unfamiliar codebase; behavioural; hiring manager | Decomposition and a real failure story |
| Consultancies | Typically screening, a technical or case interview and a leadership conversation | Client and commercial judgement; check the advert |

Across loops, interviewers grade four signals: **decomposition** of an ambiguous problem, **client conversation**, **learning an unfamiliar codebase quickly**, and **production system design** with evaluation, guardrails, cost and failure modes. A values round asks why this company and for a genuine failure. [3]

## Positioning and evidence

**Model answer — "Why FDE rather than a regular engineering role?":** "Because the hard part of AI today is not the model, it's getting it to work inside a real organisation — messy data, security reviews, users who were not asked, and a value case someone has to defend. I've spent my career on that side: leading delivery for utility and banking clients at TCS, taking an internal platform to external SaaS customers, and rolling out an AI order-automation workflow that cut manual effort by about 90% in London and Paris. Over the last year I've added the engineering half by building and evaluating agents myself. FDE is the role where both halves count."

| What the panel tests | Best evidence | What to show |
| --- | --- | --- |
| Customer deployment and scope negotiation | [S2 SaaS](../shared/evidence-bank.md#s2-saas-transformation) | Four-week go-live against a 6–8 week estimate; impact matrix; onboarding pack reused for Client 2 |
| AI in production with exceptions | [S1 order automation](../shared/evidence-bank.md#s1-genai-order-automation) | Pilot scope, customer-support involvement, exceptions, measured effort |
| Hands-on agent engineering | [S9 IncidentPilot](../shared/evidence-bank.md#s9-incidentpilot--personal-open-source-project) | Read-only design, rules in control, golden evaluations in CI |
| Human-in-the-loop product judgement | [S8 Hatch](../shared/evidence-bank.md#s8-hatch--personal-open-source-project) | No external action without the user; evaluation gates on model changes |
| Field research and adoption | [S3 Smart Timesheet](../shared/evidence-bank.md#s3-smart-timesheet) | Depot research, alpha → beta → phased rollout, champions |
| A real failure | [B2 setback](../shared/evidence-bank.md#behavioural-stories-owner-supplied-13-october-2026) | Features built to specification that nobody used; what you changed |

## Decomposition

Use one sequence and say it out loud: **clarify** the user, the outcome and how success is measured → **map** inputs, owners and freshness → **constraints** (security, regulation, budget, timeline) → **workstreams** → a **walking skeleton** that proves the path end to end in weeks → **risks and failure modes** → **measure and iterate**. Ask before solving; label assumptions; sequence by risk. [1][3]

### Q1. An insurer wants LLM-powered summaries across 30 million historical claims. Scope the first 90 days.

**Model answer:** "First, who reads the summaries and what decision do they support — a handler picking up a claim, fraud review, or a regulator? That decides what 'good' means. I'd ask how claims are stored, which documents are scanned, what personal and special-category data they hold, where processing is allowed, and what a handler does today and how long it takes. Then I'd propose a thin slice: one claim type, a few hundred historical claims, a summary format agreed with handlers, and an evaluation set they label — factual accuracy against source documents, missing critical facts, and time saved. Weeks one to four: data access, a secure processing path and the baseline. Weeks five to eight: pilot with ten handlers on live claims, summaries shown alongside the originals, never replacing them. Weeks nine to twelve: decide on scale from the numbers. I would not batch-process all 30 million until the quality, cost per claim and data-protection position are proven; at that volume a cost per summary that is a few pence too high is a real budget line."

### Q2. How would you help a wheelchair user get through a busy train station on their own?

**Model answer:** "I'd start with the person, not the technology: which part of the journey fails today — finding step-free routes, lifts out of service, boarding assistance not arriving, crowds? I'd want to shadow a few journeys. Data sources would include station maps, live lift status, platform changes and the assistance-booking system, each with an owner and a freshness problem; a lift status that is ten minutes stale is worse than none. A first version might be live step-free routing with lift status and a one-tap 'I need help at this point' that reaches staff. Success is a measure the user cares about — journeys completed without unplanned help — and the failure mode to design against is confident wrong directions." [3]

### Q3. A city wants to reduce emergency response times. Where do you start?

**Model answer:** "Break response time into its parts — call answering, triage, dispatch, travel and handover — and get data on each before assuming where the delay is. The fix for slow call answering is staffing or routing, not a model; for travel time it may be station placement. I'd pick the stage with the biggest measured delay and the fewest safety risks, ship a decision aid for dispatchers rather than an automated decision, and measure before and after."

## Customer conversations

Graders look for ownership language, diagnostic questions before solutions, honest options with trade-offs, and no promises you cannot keep. [1]

### Q4. The deployment has slipped three weeks and the customer's CTO is on the call.

**Model answer:** "I'd open with the facts and own them: what slipped, why, and what it affects for them. Then options, not excuses — for example go live on time with a reduced scope that still covers the main workflow, keep the full scope with a new date backed by a revised plan, or add specific capacity with its cost. I'd recommend one, say what I need from them to hit it, and agree when they'll next hear from me. When this happened with a SaaS client expecting go-live in four weeks against our six-to-eight-week estimate, an impact matrix let us agree which screens went first; we went live on schedule with fewer than ten issues in a 30-day pilot."

### Q5. The customer wants a feature that would break data-governance rules.

**Model answer:** "I'd find the outcome behind the request — usually speed or visibility — and say clearly that I can't build it the way it was asked and why, in their terms: the regulatory or reputational exposure, not 'policy says no'. Then I'd offer a compliant route to the same outcome, bring their data-protection or security owner into the decision, and record it. Holding the line once, politely and with an alternative, builds more trust than quietly building something that later has to be pulled."

### Q6. Explain to a non-technical VP why the assistant can't guarantee 100% accuracy.

**Model answer:** "The assistant predicts likely answers from the documents it finds; it doesn't look facts up like a database. So, like a well-briefed new colleague, it is usually right and occasionally wrong. What we can guarantee is how we manage that: it shows its sources, says 'I don't know' when evidence is missing, we measure its error rate on real questions before launch, and anything consequential gets a human check. The useful question is which error rate is acceptable for this task and what it costs compared with today."

### Q7. The customer's security team won't give you production credentials.

**Model answer:** "They're right to be careful, so I'd make their job easy rather than escalate. I'd ask what they need to approve access — a threat model, least-privilege scopes, audit logging, a named service identity — and offer a staged path: synthetic or masked data first, read-only access next, write access only for specific actions with approval. Meanwhile I'd build against a realistic test environment so the project keeps moving."

### Q8. You disagree with the architecture the customer has chosen.

**Model answer:** "I'd first make sure I understand why they chose it — there's often a constraint I can't see. If I still disagree, I'd put the concern in terms of their outcomes: cost, risk or time, with evidence, and propose the smallest test that would settle it. If they still choose their option, I'd document the risk, agree how we'd notice it, and commit to making their choice work. It is their system; my job is to make sure the decision is informed."

### Q9. The customer says the model is getting worse.

**Model answer:** "I'd ask for examples and dates, then check what changed: the inputs (new document types, a new user group), the retrieval index, the prompt or model version, and upstream data. I'd re-run the original evaluation set — if scores hold, the world has moved and the evaluation set needs new cases; if they dropped, something in our system changed and the traces will show where. I'd report back with evidence either way."

## Technical and system design

### Q10. Design a private, VPC-deployed RAG system for a healthcare customer with 50 million documents.

**Model answer:** "Clarify users, question types, latency, and the regulatory frame — in the UK that means UK GDPR, the NHS Data Security and Protection Toolkit and data-residency requirements. Everything runs inside their cloud account: ingestion workers that parse and chunk documents with access-control metadata, a vector and keyword index, a model either self-hosted or reached through a private endpoint in the right region, and an API behind their single sign-on. Permissions are filtered at retrieval time, before anything reaches the model. Audit logs record who asked what and which documents were used, with retention agreed with their information-governance team. At 50 million documents, incremental ingestion and re-indexing cost matter as much as query latency. I'd prove the path with one department's documents and an evaluation set clinicians help label, then scale."

### Q11. Build an evaluation harness for a shipment-rerouting agent with a 99% on-time target.

**Model answer:** "Separate the agent's decisions from the business outcome. Build scenarios from historical disruptions with known good reroutes, and grade the end state in a sandbox — was the shipment rerouted, within cost limits, without breaking a constraint — rather than trusting the agent's description. Add policy checks that must always pass, repeat each scenario several times because agents vary, and track cost per decision. In production, shadow the agent against planners before letting it act, and watch on-time rate by lane and carrier."

### Q12. How would you diagnose high latency in an LLM pipeline?

**Model answer:** "Trace one slow request end to end and split the time: network and queueing, retrieval, time to first token, generation, and tool calls. Long prompts raise time to first token; long outputs raise generation time; sequential tool calls add up. Fixes follow the finding — smaller or cached prompts, shorter outputs, streaming, parallel calls, a smaller model for simple requests, or more serving capacity if requests are queueing."

### Q13. Make an LLM-powered search go from 1.5 seconds to 100 milliseconds.

**Model answer:** "At 100 milliseconds a generative call is probably not on the critical path. I'd keep retrieval and ranking fast — precomputed embeddings, an approximate-nearest-neighbour index, caching of popular queries — and move generation off the hot path: show results instantly and stream a summary afterwards, or precompute summaries for common queries. I'd confirm with the customer which part must be 100 milliseconds."

### Q14. RAG, fine-tuning or prompting — how do you choose for a customer?

**Model answer:** "Prompting and examples first, measured on the customer's own evaluation set. Retrieval when the knowledge changes or must be cited. Fine-tuning only for stable behaviour or format the prompt cannot deliver, or to move a proven task to a smaller model — and only after the cheaper options have been tested on the same set."

### Q15. Hosted API or self-hosted open-weight model for an enterprise customer?

**Model answer:** "Data residency and contractual terms often decide it. Hosted models are stronger and faster to adopt; self-hosting gives control over data and cost at high volume but brings GPUs, patching, monitoring and capacity planning. I'd compare total cost per successful task, the customer's ability to operate it, and the evaluation results of both on their workload."

### Q16. A third-party API the customer depends on times out intermittently.

**Model answer:** "Set timeouts, retry with exponential backoff and jitter, and only retry idempotent calls or use idempotency keys. Add a circuit breaker so a failing dependency doesn't take everything down, a fallback or queued retry for the user, and alerting with the evidence the supplier will need. Then share the data with the supplier rather than absorbing the problem silently."

### Q17. It's 2 a.m. and your deployment in the customer's environment is down.

**Model answer:** "Contain first: restore service — roll back, switch to the fallback, or disable the failing feature — and tell the customer's on-call contact what is happening. Preserve logs and traces. Once stable, find the cause, run a blameless post-incident review with the customer, and turn the cause into a test or alert so it can't recur silently."

### Q18. How do you protect a customer-facing agent from prompt injection?

**Model answer:** "Assume injected instructions will get in, because filters miss some. Limit what they can achieve: least-privilege tools, no secrets in context, validation of every action outside the model, and approval for anything consequential. In IncidentPilot I went further — the model has no tools at all and only ranks evidence; deterministic rules decide what is recommended."

## Coding practice

FDE coding is practical rather than puzzle-heavy, often in Python, sometimes extended level by level. Practise these until you can narrate while coding: [1][2]

- A rate limiter with per-user and global limits (token bucket; explain the data structure and concurrency).
- Parse a messy CSV with inconsistent quoting into clean records, with tests for the edge cases.
- Exponential backoff with jitter for a flaky API.
- A streaming consumer that handles backpressure.
- A small RAG pipeline over a folder of documents, justifying the chunking.
- SQL: customers whose return rate exceeded 30% last quarter.
- Reading an unfamiliar 250-line codebase and fixing its bugs: read first, trace the one path that matters, then change it.

## Behavioural and values

### Q19. Tell me about a real failure.

**Model answer:** "Earlier in my consulting career I was focused on delivering feature after feature and didn't track usage after release. A client that had invested heavily in one feature came back because almost nobody used it. I interviewed the teams and gathered customer feedback: it had been built exactly to specification, but without real users in mind, so people couldn't find it or use it meaningfully. I recommended a UX review and redesign. What I changed in myself: I now involve users before building and measure adoption after release. That's why the Smart Timesheet went through depot research and a 50-engineer alpha before anything scaled."

### Q20. Tell me about spotting a pattern across customers that changed how the team worked.

**Model answer:** "After the first SaaS client at Natoora, I noticed most of our onboarding pain came from questions we hadn't asked before signing. For the second client I created a structured onboarding pack — a 30-question pre-sales questionnaire, a financial health check, a technical requirements form and a capabilities document. The second implementation took about half the elapsed time of the first, though the scopes weren't identical, so I present that as an observation rather than proof."

### Q21. The most technically challenging thing you've owned end to end.

**Model answer:** Use IncidentPilot from the [AI Engineer guide](ai-engineer.md#q33-walk-me-through-a-project-you-built-end-to-end): read-only by design, rules in control, model with no tools, and golden evaluations that inject real failures in CI. Be explicit that it is a personal project and what you would add before running it for a customer.

### Q22. Tell me about delivering bad news to a customer.

**Model answer:** Use the four-week go-live in [S2](../shared/evidence-bank.md#s2-saas-transformation): the honest estimate was six to eight weeks, so you told the client early, showed the impact matrix and agreed which internal screens to defer. Bad news delivered early with options is a negotiation; delivered late, it is a crisis.

### Q23. Why this company?

**Model answer:** Name two or three specific, recent facts — a product, a customer story, a published principle — and connect each to something you have done. For AI labs, read their published charter or safety policies first; generic enthusiasm scores poorly. [2][3]

## Credibility probes

Which code did you personally write, and which did a coding agent or a colleague write? Have you been embedded at a customer site as an engineer? What is the largest dataset you have processed? How was the 90% figure measured? What happened after you handed over? Answer precisely; the [Accenture supplement](../vacancies/accenture-fde.md#map-existing-stories-without-upgrading-the-claims) shows how to separate decisions, implementation and review.

## Questions to ask the panel

How long does an FDE typically stay with one customer? How is success measured — deployment, adoption or revenue? How do FDE findings reach the product team? What does the first month look like?

## Sources and freshness

Checked 13 October 2026. These describe reported patterns, not confirmed processes.

1. [Forward Deployed Engineer Interview: The Definitive 2026 Guide](https://www.aced.io/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde) — Aced (formerly Exponent), with salary data as of May 2026.
2. [The definitive guide to forward deployed engineer interviews in 2026](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026) — Sundeep Teki, 15 January 2026.
3. [FDE interview method](https://www.theforwarddeployed.io/interview/method) — The Forward Deployed, reviewed 13 July 2026; the site flags which loop details are its own synthesis.
4. [Palantir FDE interview guide](https://www.aced.io/guides/palantir-forward-deployed-engineer-interview) — Aced.

Search on X and LinkedIn surfaced several 2026 FDE guides and threads (including posts by Andrew Ng and Priyanka Vergadia on the role), but X pages cannot be opened for verification, so they are not used as sources here.
