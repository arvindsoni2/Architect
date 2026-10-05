# Accenture Forward Deployed AI Engineer

**Status:** Draft for owner review · **Vacancy:** R00345109 · **Checked:** 5 October 2026

## Role and evidence boundary

Accenture lists this Newcastle role at Team Lead/Consultant level. The advert combines production AI engineering, customer deployment, programme outcomes, executive engagement and engineering people management. It names OpenAI, Claude, Vertex AI and open models, including provider abstraction. It explicitly excludes internal projects, vendor labs and team-only deployments as substitutes for client-embedded delivery. Read the live advert before applying; a title or portfolio score does not establish eligibility. [1]

This supplement contains **inferred practice questions**, not reports of questions asked by Accenture or a confirmed interview process. Answer outlines describe sound reasoning; they are not claims about the candidate's past actions. Confirm the actual assessment format with the recruiter.

Start with the [FDE handbook](../../handbooks/fde/fde-handbook-v1.4.html), [shared answer methods](../shared/handbook.md#behavioural-answers) and [evidence bank](../shared/evidence-bank.md). Use STAR for a past event, PEARL when a genuine change of understanding is central, and the [scenario sequence](../shared/handbook.md#scenario-answers) for a hypothetical. EVIDENCE in the FDE handbook is a technical completeness check, not another script to recite. Accenture's general behavioural guidance recommends STAR; it does not confirm the stages of this vacancy. [2]

## Requirement to preparation map

| Area to demonstrate | Canonical preparation | Evidence to bring |
| --- | --- | --- |
| Cloud-native production engineering | [Software](../../handbooks/fde/fde-handbook-v1.4.html#software), [platform](../../handbooks/fde/fde-handbook-v1.4.html#platform) | A deployed service, tests, trace, deployment and recovery explanation |
| Agents, retrieval and context | [Agent engineering](../../handbooks/fde/fde-handbook-v1.4.html#ai), [context practice](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.4.html#harness) | Held-out cases, retrieval failures and bounded action policy |
| Provider portability | [Provider lab](../../handbooks/fde/fde-handbook-v1.4.html#provider-lab) | Capability matrix, adapter tests and a policy-constrained fallback |
| Enterprise controls | [Security](../../handbooks/fde/fde-handbook-v1.4.html#security) | Identity and data boundaries, approval evidence, residual-risk owner |
| Programme outcomes | [Programme leadership](../../handbooks/fde/fde-handbook-v1.4.html#programme-leadership) | Capacity decision, dependencies, outcome measures and release authority |
| Commercial strategy | [Investment decisions](../../handbooks/fde/fde-handbook-v1.4.html#investment-decisions) | Defensible baseline, benefit assumptions, costs and stop criteria |
| People management | [Engineering people leadership](../../handbooks/fde/fde-handbook-v1.4.html#people-leadership) | Actual reporting responsibility, feedback, development and follow-up |
| Adoption and reuse | [Delivery loop](../../handbooks/fde/fde-handbook-v1.4.html#delivery) | User behaviour, handoff acceptance and a maintained reusable asset |

These preparation choices interpret the remit in [1]; they are not an employer scoring scheme. The platform examples do not imply that mastery of every vendor is mandatory.

## Map existing stories without upgrading the claims

Use the source records for dates, technologies and measurements. Keep a private rehearsal note for personal contribution; do not publish confidential customer artefacts.

| Existing evidence | Useful angle | Still needs establishing |
| --- | --- | --- |
| [S1: GenAI order automation](../shared/evidence-bank.md#s1-genai-order-automation) | AI workflow, exceptions, operational benefit and rollout | Exact personal coding/debugging role; whether the engagement meets this advert's client-embedded boundary |
| [S2: SaaS transformation](../shared/evidence-bank.md#s2-saas-transformation) | External implementation, reuse, support and commercial choices | Personal engineering ownership, accounting basis and customer acceptance; it is not automatically an agentic-AI example |
| [S3: Smart Timesheet](../shared/evidence-bank.md#s3-smart-timesheet) | Client context, legacy integration and adoption | Separate Product Owner decisions from engineering implementation; do not relabel it an AI deployment |
| [S4: Infrastructure modernisation](../shared/evidence-bank.md#s4-infrastructure-modernisation) | Operational risk, dependencies and migration | Actual technical and service responsibility, distinct from coordination |
| People leadership | A specific real example, if available | Direct reports, development plans, performance decisions and career conversations are not established by the shared bank |
| Personal projects and exercises | Demonstrate present implementation skill | Label their setting honestly; they do not replace the advert's customer experience requirement |

For each story, record: what I decided; what I implemented; what I reviewed; what another person owned; what happened after launch; how the result was measured. If a requirement is only adjacent, say so. Several stories can show complementary strengths, but must not be blended into one invented deployment.

## Practice questions and answer reasoning

For each drill, give a recommendation, explain what could change it, and name the evidence you would inspect. The outlines below are authored exercises inferred from the role, not employer answers.

### Q1: Walk through a deployment you personally owned

**Answer outline:** Choose one real deployment. Establish the customer workflow, your remit and the baseline. Trace one request across identity, model, data, tool and system-of-record boundaries. Identify the code or configuration you personally changed, the alternative rejected, a failure encountered, and who accepted the service. End with the observed result and measurement limits. Where your role was product or delivery leadership, say that explicitly and use a separately labelled practical exercise to demonstrate current coding capability.

**Probe:** Which test caught a defect? What did the production trace show? Who could authorise rollback? What did you learn after handoff?

**Weak answer:** A team achievement told entirely as “I”, or a polished demo without operating evidence.

### Q2: Three workstreams need the same integration engineer

**Answer outline:** Make remaining capacity, dependencies, operational risk and deadlines visible. Protect incident response and essential control work first. Compare the smallest independently valuable slices rather than dividing the specialist's week equally. Recommend a sequence, identify what stops, and take the commercial or scope decision to the authorised sponsor. Pair another engineer on the bottleneck so the capacity problem becomes less dependent on one person. Reforecast using observed throughput.

**Probe:** What changes if a deadline is contractual? How do you account for support and code review? What evidence justifies moving the engineer again?

**Weak answer:** Full utilisation as the objective, hidden overtime, or three simultaneous commitments with no contingency.

### Q3: An engineer repeatedly misses an agreed quality bar

**Answer outline:** Discuss specific observable examples privately. Distinguish unclear expectations, missing support, overload and skill gaps before drawing conclusions. Agree the required behaviour, support, review points and a manageable development task. Reduce immediate production risk through pairing or review without public blame. Keep factual records and follow the organisation's people process if improvement does not occur. Discuss longer-term aspirations separately from urgent corrective feedback.

**Probe:** How would you measure progress? What if this person is the strongest coder but undermines colleagues? When do you involve the people partner?

**Weak answer:** Claiming delivery coordination proves line management, diagnosing motives, or promising an immediate dismissal.

### Q4: The CFO challenges a claim of substantial savings

**Answer outline:** Separate potential hours released, usable capacity, avoided expenditure, cash savings and revenue. Establish volume, adoption, exception effort, quality and the measurement period. Include implementation, inference, infrastructure, review and support costs. Show base/downside scenarios, the accountable benefit owner and the mechanism by which the benefit can be realised. Recommend continued learning or a hold if the commercial case is not yet evidenced.

**Probe:** Who validates the calculation? Are review minutes counted twice? What if headcount stays unchanged? Work through the [case below](#worked-programme-and-commercial-case).

**Weak answer:** Multiplying all employees by an optimistic time saving and describing it as profit.

### Q5: The CTO wants speed while the CISO restricts data movement

**Answer outline:** Clarify the exact data classification, permitted processing locations and actions. Bring the workflow and service owners into one decision. Compare a narrow approved-data slice, private managed access and self-hosted inference against operational cost and required controls. Recommend one reversible experiment with acceptance criteria. Present the executive decision first, then use an architecture walkthrough or code-with session to demonstrate the riskiest assumption with engineers.

**Probe:** Who accepts residual risk? Which records stay out of the model? What remains blocked even if the demo succeeds?

**Weak answer:** Treating private connectivity as proof of complete compliance or promising that a prompt prevents disclosure.

### Q6: Your provider fails halfway through an action workflow

**Answer outline:** Identify whether generation, a tool proposal or an external write failed. A replacement provider must pass the same task-quality and data-policy gates and support the required contract. If a write's outcome is unknown, reconcile using operation identity before any replay. Do not send protected data to an unapproved provider to preserve availability. Bound retries and cost, persist state, and surface a recoverable hold when no safe route exists.

**Probe:** How do tool-call IDs, streaming events, structured output and usage accounting differ? What happens if the second provider lacks a required feature?

**Weak answer:** “They all use an OpenAI-compatible API, so just switch the URL.”

### Q7: Your retrieval assistant is fluent but wrong

**Answer outline:** Collect representative failed queries and segment by consequence. Check whether the authoritative source exists, is fresh and is permitted for this user. Measure retrieval independently of answer generation; inspect ranking and context assembly before changing prompts. Test abstention and escalation. Use held-out cases and regression checks, then compare downstream completion and correction effort.

**Probe:** What if top-k recall improves but operators take longer? How would you test cross-tenant leakage? How do you avoid tuning against the final test set?

**Weak answer:** Adding more documents or a larger context window without identifying the failing stage.

### Q8: Choose serverless, a container service or microservices

**Answer outline:** Start with runtime duration, burstiness, concurrency, private connectivity, state, operational skills and recovery requirements. A short stateless handler may fit serverless; long-running or specialised processes may fit managed containers. Keep durable waiting outside a request process. Split services only when an ownership, scaling or isolation boundary justifies the extra deployment and failure paths. Explain the simplest acceptable initial design and a measurable trigger for change.

**Probe:** What happens during a 24-hour approval wait? How do you control cold-start or scale-to-zero effects? Which boundary needs its own release cadence?

**Weak answer:** Kubernetes or microservices chosen for prestige without workload evidence.

### Q9: Strong evaluation scores, weak user adoption

**Answer outline:** Observe the actual task and compare eligible use with completed use. Investigate integration friction, review burden, trust, incentives and exceptions. Segment by user group and workflow. Try a narrow change with representative users and compare completion, corrections, abandonment and outcomes. Agree an expansion or stop decision with the workflow owner; model accuracy alone does not justify rollout.

**Probe:** What if users prefer the manual process for good reasons? Can the workflow be simplified without AI?

**Weak answer:** Mandatory training as the universal fix.

### Q10: Turn a one-off integration into a reusable accelerator

**Answer outline:** Extract the stable contract and keep customer-specific policy and configuration explicit. Remove confidential data and check reuse rights. Add compatibility tests, supported versions, applicability limits, ownership and a deprecation path. Validate with a second deployment and compare effort on equivalent tasks, including maintenance costs. Feed recurring product limitations to the platform team.

**Probe:** Who funds maintenance? What would make you keep two implementations separate? How do you prove reuse reduced effort rather than scope?

**Weak answer:** Copying a customer repository and calling it a platform.

### Q11: Debug and explain during a code-with session

**Practice task:** Take your own small integration service and inject a timeout after a simulated external commit. In 40 minutes, reproduce the failure, inspect state and traces, explain an unknown outcome, implement reconciliation and run the regression test. The timer is a practice choice, not an Accenture test duration. Follow the actual assessment rules on AI assistance; be able to explain every change yourself.

**Pass evidence:** One operation identity, no duplicate side effect, bounded retries, meaningful caller status and a trace that explains the final state. A mock proves the tested integration behaviour only.

**Probe:** What if the external API has no status endpoint or idempotency support? A good answer considers manual reconciliation or an altered workflow rather than claiming exactly-once delivery.

## Worked programme and commercial case

**Synthetic exercise:** All numbers, constraints and outcomes in this section are invented for rehearsal. They are not candidate achievements or Accenture benchmarks.

A case-processing pilot has 20,000 eligible cases per month. The existing process takes six minutes per case. The proposed process reaches 60% adoption; an adopted case is expected to average two minutes of remaining human work, including exceptions and corrections. Loaded labour cost is £30/hour. Implementation costs £45,000. Recurring technology and support cost £6,000/month, excluding human case handling already captured in those two minutes.

| Calculation | Result | Interpretation |
| --- | --- | --- |
| Adopted cases: 20,000 × 60% | 12,000/month | Non-adopted cases retain the baseline |
| Released effort: 12,000 × (6 − 2) ÷ 60 | 800 hours/month | Potential capacity; validate through observation |
| Capacity value: 800 × £30 | £24,000/month | Not automatically cash savings |
| Assume 50% can be productively redeployed: £24,000 × 50% | £12,000/month | A benefit hypothesis requiring an owner |
| Net economic benefit: £12,000 − £6,000 | £6,000/month | Conditional on that realisation assumption |
| Simple payback: £45,000 ÷ £6,000 | 7.5 months | Undiscounted, steady-state assumption; ramp-up would extend it |
| First 12 steady-state months: (£6,000 × 12 − £45,000) ÷ £45,000 | 60% | Simple net return on implementation spend under these assumptions |

Do not report £24,000/month as payroll savings. If finance cannot identify avoided spend or a valued use for released time, the cash-saving case is unproven. Revenue benefit needs its own causal evidence; avoid adding the same benefit twice.

**Downside:** At 30% adoption and 25% realisation, 6,000 adopted cases release 400 hours. £12,000 capacity value × 25% = £3,000; after £6,000 recurring cost, net benefit is **−£3,000/month**. There is no positive payback in this scenario. At 50% realisation and fixed recurring cost, break-even adoption is 30%: each adopted case releases four minutes worth £2, of which £1 is realised, so 6,000 adopted cases cover £6,000. Check variable costs before using that threshold at scale.

**Recommended decision:** Authorise a bounded measurement pilot if its cost and risk are acceptable. Assign the workflow owner to adoption, finance to benefit assumptions, engineering to task reliability and cost, and security to control evidence. Expand only when observed quality, economics and adoption justify it; a positive spreadsheet is not acceptance evidence.

### Capacity and roadmap exercise

Six engineers provide 60 engineer-days over a ten-day period. Reserve 12 days for support and unplanned work, leaving 48. One integration specialist has only eight planned days available after that reserve. These are planning assumptions, not a universal staffing ratio.

| Workstream | Total demand | Specialist demand | Decision context |
| --- | --- | --- | --- |
| A: mandatory access-control remediation | 18 days | 6 days | Confirmed control deadline |
| B: optional claims pilot | 24 days | 4 days | Value hypothesis above; no committed release date |
| C: sales demonstration | 18 days | 2 days | Optional; no contractual obligation in this case |

All three require 60 days and 12 specialist days, exceeding both limits. Recommend A plus an eight-day, read-only slice of B using two specialist days. The remaining 22 planned days support independent evaluation, training, documentation and other agreed work; do not assume spare generalist capacity removes the specialist bottleneck. Defer C unless the sponsor changes priorities or capacity. Confirm any new dependency before committing the slice.

**Roadmap:** In the first 30 days, establish controls and the baseline. In days 31–90, test the slice and acceptance gates. In months 4–12, expand only to comparable workflows with named benefit and service owners. In year two, consider reuse across business units after evidence of repeatability, capacity and support economics. Revisit each horizon when assumptions change; this is a conditional strategy, not a two-year promise.

## Rehearsal rubric and focused route

Score each dimension 0–2: absent, mentioned, or supported by a decision and evidence. This is a self-review tool, not an Accenture hiring threshold.

| Dimension | What earns 2 |
| --- | --- |
| Personal ownership | Clear distinction between own work, collaboration and others' authority |
| Engineering depth | Explains state, interfaces, failure and a concrete test or trace |
| Commercial reasoning | Defensible baseline, denominator, costs, uncertainty and benefit owner |
| Leadership | Clear capacity or people decision with support and follow-up |
| Safety and operations | Enforced boundaries, recovery and accepting service owner |
| Communication | Direct recommendation, alternative and evidence that would reverse it |

Do not average away a fabricated claim, unsafe action or missing client-experience requirement. Rehearse gaps honestly and identify the next evidence needed.

1. Map the advert to two truthful stories and identify unestablished requirements.
2. Complete the [provider practical](../../handbooks/fde/fde-handbook-v1.4.html#provider-lab) and Q11 debugging drill.
3. Recalculate the commercial case without looking; change adoption, support cost and the realisation factor.
4. Rehearse Q2, Q3 and Q5 with a partner changing one constraint.
5. Use the accelerator's [evaluation](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.4.html#evals) and [orchestration](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.4.html#orchestration) resources only for demonstrated weaknesses.

For motivation, connect the actual work to your interest in customer outcomes and engineering responsibility, then support that with a real example. Ask the recruiter about expected personal coding depth, team/reporting responsibilities, client assignment and assessment format. Ask how deployment acceptance and benefits are measured. Do not assume that an adjacent Product Owner interview process applies here.

## Sources and freshness

1. [Accenture: Forward Deployed AI Engineer, R00345109](https://www.accenture.com/gb-en/careers/jobdetails?id=R00345109_en) — role evidence checked 5 October 2026; vacancy content may change or close.
2. [Accenture: behavioural interview preparation](https://www.accenture.com/us-en/blogs/blogs-careers/how-to-prepare-for-a-behavioral-interview) — general STAR guidance, not a verified process for this role.
3. [Google: scale agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) — current destination of the former Vertex AI Agent Engine overview, checked 5 October 2026. Follow supported SDK/version guidance when implementing; retain the vacancy's own platform wording when discussing its requirements.
4. [Anthropic: Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy) — announced 2 October 2026; Accenture is among initial participants. Participation is through organisational nomination, not an open individual course. See the [handbook training note](../../handbooks/fde/fde-handbook-v1.4.html#frontier-academy) for the distinction from certification and deployment evidence.

The source check covers this vacancy and the new references. It is not a claim that every linked handbook or all 76 accelerator resources were re-audited. The numbered questions, scoring rubric and commercial case are editorial practice material.
