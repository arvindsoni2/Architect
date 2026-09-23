# Architecture and Applied AI Certification Roadmap

**Status:** Current

**Edition:** Living roadmap

**Last reviewed:** 2026-09-23

## Purpose

This roadmap supports experienced technology, delivery and product professionals moving towards solution architecture, applied AI engineering, forward-deployed engineering and technical consulting. It prioritises credentials that strengthen a coherent role narrative and pairs each credential with evidence that can be inspected in an interview.

A certification validates a bounded body of knowledge. It does not prove that someone can discover requirements, make defensible trade-offs, integrate a system, operate it safely or recover it after failure. The governing rule is therefore:

> Use certification study to structure learning, then prove the learning through architecture decisions, deployments, tests, evaluations and operational evidence.

## Recommended sequence

| Stage | Credential or gate | Priority | Availability or status | Advance when |
| --- | --- | --- | --- | --- |
| 1 | AWS Certified Solutions Architect – Associate (SAA-C03) | Now | Current standard exam | Scenario questions and practical work show reliable decisions across security, resilience, performance and cost. |
| 2 | AWS architecture evidence gate | Mandatory | Portfolio evidence, not an exam | At least one workload has been designed and deployed with ADRs, threat boundaries, observability, cost reasoning, failure tests and teardown evidence. |
| 3A | Claude Certified Architect, Foundations | High when accessible | Access-dependent through Anthropic Partner Academy | The learner can design a production-oriented Claude application and can access the exam. |
| 3B | AWS Agentic AI Demonstrated | High | Free AWS hands-on microcredential | The learner can configure, troubleshoot and improve an agent in a provisioned AWS environment. |
| 4A | AWS Certified Generative AI Developer – Professional (AIP-C01) | Preferred AI/FDE branch | Current standard exam | Production-grade generative AI evidence meets the readiness gate below. |
| 4B | AWS Certified Machine Learning Engineer – Associate (MLA-C02) | Alternative ML/MLOps branch | Beta transition; check language and current exam version | The target role genuinely requires SageMaker, ML pipelines, model operations or LLMOps depth. |
| 5 | AWS Certified Solutions Architect – Professional | Later | Current exam; monitor announced updates | Multiple substantial AWS designs and deployments demonstrate organisational, migration, hybrid, resilience and governance depth. |

Stages 3A and 3B are complementary and can be completed in either order. Access should determine the order: take the Claude exam when Partner Academy access is available; otherwise continue with the AWS hands-on credential rather than waiting.

Do not plan AIP-C01 and MLA-C02 as an automatic pair. Their coverage increasingly overlaps. Choose the branch that matches the work being pursued, and reconsider the second credential only when target roles provide evidence that it would add material value.

## Why Claude Certified Architect belongs in the core path

Anthropic launched **Claude Certified Architect, Foundations** in March 2026 as its first technical certification. Anthropic describes it as an exam for solution architects building production applications with Claude. This makes it directly relevant to solution architecture, applied AI consulting and forward-deployed work rather than a generic prompting credential.

Its current limitation is access. The public launch announcement describes availability through the Claude Partner Network, and Anthropic states that certifications are earned by individuals through Anthropic Partner Academy exams. Public information does not establish universal exam access. Verify eligibility, price, syllabus and recertification rules in the Partner Academy before scheduling study time.

The credential adds a different signal from AWS certification:

- SAA-C03 validates broad cloud solution design;
- AWS Agentic AI Demonstrated validates practical work in an AWS environment;
- Claude Certified Architect validates vendor-specific Claude application architecture;
- AIP-C01 validates broader production generative AI delivery on AWS.

This is useful complementarity only when accompanied by implementation evidence. Do not let the Claude exam displace tool integration, retrieval, evaluation, security, observability or production deployment practice.

## Decision gates

### 1. SAA-C03 gate

Before taking SAA-C03, demonstrate that you can:

- translate requirements into secure, resilient, high-performing and cost-optimised designs;
- explain why a plausible alternative is wrong under the stated constraint;
- connect service choices to failure behaviour, recovery and operational ownership;
- complete representative labs without depending on an active coding-agent session; and
- identify what a lab proves, what it merely models and what remains untested.

Use the repository's [SAA-C03 visual handbook and lab manual](../handbooks/aws-saa-c03/README.md) as the primary study pair, then use current official practice material to find remaining weak domains.

### 2. Architecture evidence gate

Before moving from SAA-C03 to an advanced AI credential, produce an evidence pack containing:

- a problem statement and measurable quality attributes;
- two credible architecture options and an ADR explaining the choice;
- deployment and data-flow views;
- identity, trust-boundary and threat analysis;
- cost assumptions and a teardown or cost-control plan;
- logs, traces, metrics and alerting decisions;
- one injected failure or recovery exercise; and
- limitations stated without turning proposed behaviour into claimed evidence.

The [connected architecture project guides](software-architect/connected-learning/README.md) provide suitable scenarios and artifact expectations.

### 3. Claude Certified Architect gate

Before attempting the Claude certification, be able to defend a Claude-based solution that includes:

- a justified model and access pattern;
- bounded context assembly and retrieval;
- typed tool contracts, least privilege and approval boundaries;
- prompt-injection and data-handling controls;
- evaluation criteria and a repeatable test set;
- latency, token and cost budgets;
- observability and production failure handling; and
- a migration or fallback path that avoids unnecessary vendor lock-in.

A suitable evidence vehicle is a bounded capability in a public, non-confidential assistant such as [Hatch](https://github.com/arvindsoni2/hatch), or an equivalent workflow. Certification access is a scheduling constraint, not a reason to postpone building the evidence.

### 4. AWS Agentic AI Demonstrated gate

Use this hands-on microcredential to close the gap between knowing services and working inside an AWS environment. AWS describes its microcredentials as live, provisioned assessments without multiple-choice questions. The Agentic AI credential covers troubleshooting, repairing, integrating and enhancing Bedrock-based agents and has been updated for Bedrock AgentCore capabilities.

Prepare through a small agent that has observable success criteria, constrained tools, failure handling, evaluation and cost controls. A limited job-coaching or incident-triage workflow is preferable to a broad demonstration with no measurable outcome. Public reference implementations include [Hatch](https://github.com/arvindsoni2/hatch) and [IncidentPilot](https://github.com/arvindsoni2/IncidentPilot); do not reuse confidential deployment or employer data.

### 5. Advanced AWS AI branch

Choose **AIP-C01** for roles centred on generative AI applications, agents, RAG, foundation-model integration and production AI delivery. Do not rush the professional-level exam: AWS targets candidates with substantial application, cloud and hands-on generative AI experience.

Choose **MLA-C02** for roles centred on ML engineering, MLOps, LLMOps, SageMaker, data and model pipelines, fine-tuning or production inference. The updated exam includes foundation models, RAG, Bedrock and agentic AI, but retains traditional ML engineering depth.

As of this roadmap's review date, MLA-C02 registration is open for an English-only beta whose delivery begins on 29 September 2026. MLA-C01 remains available in English through 28 September 2026 and in Japanese, Korean and Simplified Chinese until MLA-C02 general availability; AWS expects the standard MLA-C02 release in early 2027. Re-check the official exam page before choosing a version or language.

| Role direction | Preferred branch | Reason |
| --- | --- | --- |
| AI Solutions Engineer, FDE, GenAI consultant | AIP-C01 | Closest match to production generative AI integration and delivery. |
| Solution Architect with an applied AI specialism | AIP-C01 | Adds AI application depth to broad AWS architecture knowledge. |
| ML Engineer, MLOps Engineer, LLMOps Engineer | MLA-C02 | Stronger fit for model and ML-platform operations. |
| AI Product or transformation leadership | Project evidence first | A technical implementation signal is usually the more important gap; do not default to another business-level certificate. |

## Project-to-credential evidence map

| Credential | Evidence vehicle | Interview evidence |
| --- | --- | --- |
| SAA-C03 | One connected-learning scenario deployed as a bounded AWS slice | Service decisions, ADRs, security, failure behaviour, cost and cleanup. |
| Claude Certified Architect, Foundations | A bounded public assistant workflow using Claude | Context design, tools, retrieval, evals, guardrails, observability and fallback. |
| AWS Agentic AI Demonstrated | Bedrock/AgentCore implementation of one public agent workflow | Live configuration, troubleshooting, integrations, constrained actions and measured outcomes. |
| AIP-C01 | Production-oriented RAG or agent workflow on AWS | Evaluation, responsible AI, security, monitoring, deployment and cost controls. |
| MLA-C02 | Reproducible SageMaker/Bedrock ML or LLMOps pipeline | Data preparation, training or adaptation, deployment, monitoring and scaling. |
| AWS Certified Solutions Architect – Professional | Multi-account, hybrid, migration or regulated-system capstone | Organisational complexity, governance, recovery, migration and economic trade-offs. |

Do not publish employer, client, immigration or other private information in an evidence pack. Generalise scenarios and distinguish executed results from designs.

## Conditional additions

Add another certification only when repeated evidence from target roles justifies it.

| Certification | Add when | Do not add when |
| --- | --- | --- |
| TOGAF Enterprise Architecture Foundation and Practitioner | Enterprise Architect roles repeatedly require capability, portfolio and governance language. | The target remains hands-on solution architecture or applied AI delivery. |
| Certified Kubernetes Administrator | Platform-heavy FDE, AI infrastructure or Kubernetes operations appears consistently in target roles. | Kubernetes is only a résumé keyword and no cluster operations evidence exists. |
| AWS Certified Security – Specialty | Security architecture becomes a primary responsibility in regulated or high-assurance work. | General security depth can be demonstrated through SAA and project threat models. |
| AWS Certified DevOps Engineer – Professional | The role owns AWS delivery platforms, CI/CD and production operations at scale. | The goal is architecture breadth or generative AI application delivery. |
| AWS Certified Data Engineer – Associate | Data-platform design and operations become central to the target role. | Data work is only a supporting part of an AI application. |
| Another cloud provider | A target employer, client or market repeatedly requires that provider. | It is pursued only to collect a multi-cloud label. |

## Low-priority or redundant credentials

- **AWS Cloud Practitioner:** redundant after technical AWS study at SAA level.
- **Another AI fundamentals credential:** low incremental value when an AI foundation credential is already held.
- **AWS Certified AI Business Strategist (AIB-C01, beta):** relevant to non-technical AI transformation roles, but it deliberately excludes implementation and architecture depth. Treat it as an optional market-specific credential, not part of the core route, and re-check its beta status before acting.
- **Generic prompt-engineering course certificates:** completion evidence is weaker than a tested prompt/context system with versioning and eval results.
- **Product and Agile certificate stacking:** once recognised delivery/product credentials exist, technical evidence normally has higher marginal value.
- **Vendor credentials without access or a use case:** do not invest in preparation based on an assumed future catalog.

## Review rules

Review this roadmap quarterly and whenever one of these events occurs:

- an exam code, guide, availability rule or retirement date changes;
- Anthropic opens or changes access to its certification catalog;
- a target-role sample shows a repeated new requirement;
- project work shifts from generative AI applications to ML platforms, security, data or platform engineering; or
- a credential starts displacing higher-value deployment and interview evidence.

The review should answer three questions:

1. Which target role will this credential strengthen?
2. What capability does it add that the current credentials and projects do not already demonstrate?
3. What public, inspectable evidence will be built alongside it?

If those questions do not have precise answers, defer the credential.

## Official references

Time-sensitive claims were checked on 23 September 2026.

- [AWS Certified Solutions Architect – Associate](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
- [AWS Certified Generative AI Developer – Professional](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/)
- [AWS Certified Machine Learning Engineer – Associate](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)
- [AWS update to Machine Learning Engineer – Associate (MLA-C02)](https://aws.amazon.com/blogs/training-and-certification/updates-to-aws-certified-machine-learning-engineer-associate-mla-c02/)
- [AWS Certified Solutions Architect – Professional](https://aws.amazon.com/certification/certified-solutions-architect-professional/)
- [AWS Certified AI Business Strategist (AIB-C01) exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01.html)
- [AWS microcredentials](https://aws.amazon.com/training/digital/immersive-learning/)
- [AWS Agentic AI and MLOps microcredential updates](https://aws.amazon.com/blogs/training-and-certification/may-2026-new-offerings/)
- [Anthropic: Claude Partner Network and Claude Certified Architect, Foundations](https://www.anthropic.com/news/claude-partner-network)
- [Anthropic: Services Track and Partner Academy certification model](https://www.anthropic.com/news/services-track-partner-hub)
