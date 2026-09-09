# Connected architecture project guides

Use one project to connect **business requirement → architectural decision → technical mechanism → AWS implementation → AI controls → experiment → artifact → interview explanation**. These are transfer companions to the existing [grooming programme](../software-architect-grooming-programme-v5.html), not additional syllabuses. Reviewed 9 September 2026.

## Choose the question you need to practise

| Programme location | Project companion | Distinctive question |
| --- | --- | --- |
| Unit 1 | [National patient access portal](../patient-portal-connected-learning.md) | Who authorises a read, and who can confirm a booking? |
| Unit 2 | [Regulated payments startup](regulated-payments.md) | How does a small team choose boundaries without losing payment correctness? |
| Unit 3 | [Global product catalogue and price service](catalogue-and-pricing.md) | Which reads can be stale, and how does checkout stay correct? |
| Unit 4 | [Omnichannel order placement](omnichannel-orders.md) | How do partial failure, unknown outcomes and compensation differ? |
| Unit 5 | [Retail inventory intelligence](inventory-intelligence.md) | How do late events, operational truth and forecasts fit together? |
| Unit 6 | [Digital wallet and refunds platform](wallet-and-refunds.md) | What prevents duplicate value movement and unauthorised refunds? |
| Unit 7 | [Legacy order-management modernisation](legacy-modernisation.md) | How do you change the writer without losing or duplicating orders? |
| Unit 8 | [Online professional learning platform](professional-learning-platform.md) | How do different architecture views describe the same system consistently? |
| Unit 9 | [Multi-team commerce platform governance](commerce-governance.md) | Which constraints should be automated while preserving team choices? |
| Unit 10 and capstone | [NorthStar Retail synthesis](northstar-retail.md) | How do you mobilise an ambiguous brief and defend one coherent modernisation plan? |

The retail cases are related exercises with different scopes. NorthStar is the explicit synthesis. Do not silently copy a unit's workload numbers, ownership decisions or SLOs into another case. For example, Unit 3's 150k reads/s is not a supplied NorthStar baseline.

For the quickest transfer, practise **orders → inventory → modernisation → NorthStar**. For security interviews, add payments and wallet. For architecture communication and organisational influence, add the learning platform and governance. The catalogue case develops performance reasoning. Select your next case from the decision you cannot yet explain; completing every page is not a prerequisite for practising interviews.

## How to work each case

Use six passes, initially 60–90 minutes each; implementation can require additional sessions:

1. **Frame:** reproduce the source brief, identify authority, list unknowns and write measurable quality scenarios.
2. **Compare:** draw the proposed request/data path and one viable alternative; write the decision and its reversal trigger.
3. **Predict and experiment:** predict a failure result, adapt a selected lab, execute it, and record what actually happened.
4. **Add AI deliberately:** identify the decision AI assists, its permitted inputs/outputs, baseline, evaluation and fallback. “No AI in the transaction path” is a valid choice.
5. **Package evidence:** complete the original unit's required artifacts; connect each claim to an observation or labelled hypothesis.
6. **Defend and revise:** explain without notes, answer a changed-constraint question, and record the revision.

Use the [patient portal evidence template](../patient-portal-connected-learning.md#7-build-one-evidence-pack-over-eight-sessions) and the [programme assessment](../software-architect-grooming-programme-v5.html#assessment). Each guide includes a worked ADR and a concrete experiment specification. Proposed diagrams, example decisions and expected test outcomes are **not executed evidence**.

All added workload thresholds are teaching hypotheses unless explicitly attributed to the programme brief. All data and external providers in exercises should be synthetic or sandboxed. The companions do not deploy AWS resources, process real payments, grant regulatory approval or establish production readiness. Preserve actual versions, configuration, commands, observations and teardown results when you run an AWS lab. Do not put private customer, employer or financial records in this public repository.

## Locate the AWS labs accurately

Open the [AWS lab manual](../../../handbooks/aws-saa-c03/saa-c03-lab-manual-v2.1.html) and choose the display number/title. There are no stable per-lab URL anchors. Internal IDs are supplied to disambiguate older handoff numbering.

| Display | Title | ID |
| --- | --- | --- |
| 00 | Guardrails & the CI/CD Spine | `p0` |
| 01 | ShelfLife — 3-Tier Bookstore | `l1` |
| 02 | LinkForge — Serverless URL Shortener | `l2` |
| 03 | OrderFlow — Event-Driven Order Pipeline | `l3` |
| 04 | CraftRoast — Global Static Storefront | `l4` |
| 05 | FreshTrack — Containerised Produce API | `l5` |
| 06 | ClipPress — Media Processing Pipeline | `l6` |
| 07 | StreamSight — Clickstream Analytics Lake | `l7` |
| 08 | VaultGrade — Storage & DR Drill Range | `l8` |
| 09 | SecureLanding — Identity, Encryption & Detection | `l9sec` |
| 10 | HybridHub — Multi-VPC & Private Connectivity | `l10net` |
| 11 | DataShift — Database Scale, Cache & Migration | `l11data` |
| 12 | SageStart — Managed AI Services Bench | `l9` |
| 13 | DocuMind — Bedrock RAG Assistant | `l10` |
| 14 | OpsPilot — Agentic FinOps Copilot | `l11` |

The lab runbooks/handoffs describe work to assemble and execute. They are not complete deployed implementations of these projects. Keep lab learning shortcuts separate from the proposed target architecture.

The [official SAA-C03 guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) groups scored content into secure (30%), resilient (26%), high-performing (24%) and cost-optimised (20%) architectures. Each companion identifies the relevant lenses. AI depth and business governance extend interview preparation; they do not replace the exam blueprint.
