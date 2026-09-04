# Software Architect Curriculum Guide v3

**Public repository edition:** reviewed 4 September 2026
**Purpose:** define what an aspiring software architect should learn, why it matters, and the order in which the capabilities build on one another.

This guide is the durable curriculum map. It deliberately excludes dated calendars, daily exercises, saved progress and mentor workflow. Use the companion [Software Architect Grooming Programme v5](software-architect-grooming-programme-v5.html) for diagnostic bridge modules, worked scenarios, exercises, oral defences and capstone assessment.

## The outcome

Software architecture is the disciplined practice of making consequential system decisions under uncertainty. A capable architect can:

1. connect business outcomes to measurable quality attributes;
2. compare viable options instead of presenting one design as inevitable;
3. reason about boundaries, data, runtime behaviour and failure;
4. make security, operability, cost and evolution part of the design;
5. preserve important decisions in reviewable evidence; and
6. explain the same architecture appropriately to executives, product teams, engineers, security and operations.

The curriculum develops three mutually reinforcing capabilities:

- **Think:** frame problems, identify architecture drivers, expose assumptions and reason in trade-offs.
- **Design:** choose structures, interactions, data models and operational mechanisms that fit the context.
- **Communicate:** make decisions visible through diagrams, records, reviews, roadmaps and concise narratives.

## How to use the curriculum

Work through the modules in order. The sequence is intentional:

```text
problem and drivers
        ↓
system structure
        ↓
runtime and data
        ↓
security and operations
        ↓
communication and governance
        ↓
synthesis and defence
```

For each module, aim to answer three questions in plain language:

1. What problem does this concept solve?
2. What does it improve, and what does it make harder?
3. What evidence would justify or reverse the decision?

Technology names are examples, not curriculum outcomes. Prefer principles and decision criteria that survive product churn.

## Curriculum map

| Module | Capability | Central question |
| --- | --- | --- |
| 1 | Architecture thinking | What makes this decision architecturally significant? |
| 2 | Architecture styles | Which structure best fits the drivers and constraints? |
| 3 | Scalability, availability and performance | How will the system behave under load and failure? |
| 4 | APIs, integration and distributed workflows | How do components collaborate without losing correctness? |
| 5 | Data architecture | Who owns each fact, and how does it remain trustworthy? |
| 6 | Security and resilience | What must be protected, and how does the system recover? |
| 7 | Cloud-native design and evolution | How will the system run, change and remain affordable? |
| 8 | Architecture communication | Which views and records make the decision understandable? |
| 9 | Governance and influence | How do teams preserve useful constraints without creating bureaucracy? |
| 10 | Synthesis and architecture defence | Can the design be traced from outcome to evidence? |

---

## Module 1 — Architecture thinking and quality attributes

### Why it matters

Architecture begins before technology selection. The first responsibility is to understand the business outcome, stakeholders, constraints, uncertainty and the qualities that will shape the system.

### Core knowledge

- Architecture as the set of important, difficult-to-reverse decisions.
- Business outcomes, capabilities, value streams and constraints.
- Stakeholder concerns and competing definitions of success.
- Functional requirements versus quality attributes.
- ISO/IEC 25010:2023 product-quality characteristics as a vocabulary, not a substitute for context.
- Measurable quality-attribute scenarios: stimulus, environment, affected component, response and response measure.
- Utility trees and the Quality Attribute Workshop for prioritisation.
- Assumptions, risks and evidence as first-class design inputs.

### Decision questions

- Which business outcome would fail if this architecture decision were wrong?
- Which qualities are architecturally significant, and how will they be measured?
- Whose concern is missing from the current problem statement?
- What is known, assumed or still uncertain?

### Core references

- Martin Fowler, [Who Needs an Architect?](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf)
- arc42 Quality Model, [ISO/IEC 25010 overview](https://quality.arc42.org/standards/iso-25010)
- Software Engineering Institute, [Quality Attribute Workshop](https://www.sei.cmu.edu/library/the-sei-quality-attribute-workshop/)

---

## Module 2 — Architecture styles and evidence-based trade-offs

### Why it matters

An architecture style packages a set of constraints and consequences. The goal is not to memorise style names; it is to identify when a style fits the workload, team, change pattern and operating model.

### Core knowledge

- Layered, modular-monolith, service-based, microservice, event-driven, serverless and cell-based structures.
- Coupling and cohesion across code, deployment, data and teams.
- Architecture characteristics such as deployability, scalability, testability, reliability, simplicity and cost.
- Decision matrices, sensitivity points and trade-off points.
- Architecture Tradeoff Analysis Method concepts.
- Fitness functions as repeatable evidence that important qualities remain within bounds.
- Evolution triggers: signals that justify revisiting an earlier structural choice.

### Decision questions

- Which quality attributes dominate this context?
- Which style is the simplest one that satisfies them?
- What operational and organisational capabilities does the style assume?
- Which evidence would trigger decomposition, consolidation or a different style?

### Core references

- Chris Richardson, [Microservice architecture pattern catalogue](https://microservices.io/patterns/)
- Software Engineering Institute, [ATAM collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)
- Thoughtworks, [Technology Radar](https://www.thoughtworks.com/radar)

---

## Module 3 — Scalability, availability and performance

### Why it matters

Capacity and resilience emerge from complete request paths, dependencies and failure behaviour—not from the presence of a load balancer or cache.

### Core knowledge

- Workload modelling: requests, concurrency, data volume, growth, peaks and skew.
- Back-of-envelope estimates as explicit models with revisable assumptions.
- Horizontal and vertical scaling; stateless and stateful constraints.
- Replication, partitioning, sharding and caching.
- CAP and PACELC as reasoning tools rather than slogans.
- Load shedding, admission control, rate limits and back pressure.
- Timeouts, retries with jitter, circuit breakers and bulkheads.
- Idempotency and bounded recovery.
- SLOs, error budgets, RTO, RPO and degraded modes.

### Decision questions

- Where is the bottleneck at normal load, expected peak and extreme peak?
- Which dependency failures propagate, and where is the blast radius contained?
- What work can be delayed, degraded or rejected safely?
- Which measurements demonstrate that the capacity model is still valid?

### Core references

- Donne Martin, [System Design Primer](https://github.com/donnemartin/system-design-primer)
- AWS, [Reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

---

## Module 4 — APIs, integration and distributed workflows

### Why it matters

Most serious distributed-system failures occur at boundaries: duplicated messages, partial completion, incompatible contracts, misplaced authority or recovery that depends on manual guesswork.

### Core knowledge

- Synchronous request/response and asynchronous messaging.
- REST, GraphQL, gRPC and event contracts; choose by interaction need rather than fashion.
- API gateways and backends for frontends.
- Events as facts; commands as requests; queries as information retrieval.
- CQRS and event sourcing—the problems they solve and the complexity they add.
- Saga choreography and orchestration.
- Transactional outbox, deduplication and idempotent consumers.
- Contract evolution, schema compatibility and consumer-driven testing.
- Dead-letter handling, reconciliation and human recovery.

### Decision questions

- Where is the business transaction boundary?
- Which component is authoritative for each state transition?
- What happens after partial success, duplicate delivery or out-of-order events?
- How can contracts evolve without coordinated deployment?

### Core references

- Chris Richardson, [Saga pattern](https://microservices.io/patterns/data/saga.html)
- Chris Richardson, [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html)
- AsyncAPI Initiative, [Event-driven architecture tutorial](https://www.asyncapi.com/docs/tutorials/getting-started/event-driven-architectures)

---

## Module 5 — Data architecture and information ownership

### Why it matters

Data architecture is not a catalogue of databases. It defines authority, meaning, lifecycle, consistency, access and the path from operational facts to trusted decisions.

### Core knowledge

- Workload-first storage selection: relational, document, graph, time-series, key-value, search, columnar and vector capabilities.
- Transaction boundaries and invariants.
- Replication, partitioning, consistency and conflict resolution.
- Operational versus analytical workloads.
- Batch, streaming and hybrid processing.
- Data products, domain ownership and federated governance.
- Lakehouse and data-mesh concepts, including when they add needless complexity.
- Schema evolution, lineage, retention, privacy and quality controls.
- Reconciliation between systems of record and derived views.

### Decision questions

- Who owns each fact, and which systems hold copies or projections?
- What consistency does the business process actually require?
- How will late, duplicate, missing or conflicting data be detected and repaired?
- Which lifecycle, retention and access rules apply?

### Core references

- Martin Kleppmann, [Designing Data-Intensive Applications](https://dataintensive.net/)
- Microsoft, [Supply-chain reference architecture](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/architectures/supply-chain)

---

## Module 6 — Security architecture and resilience engineering

### Why it matters

Security and resilience are system properties. They must be visible in identity, data flows, trust boundaries, deployment, monitoring, recovery and operational ownership.

### Core knowledge

- Assets, actors, entry points, trust boundaries and abuse cases.
- STRIDE and attack-tree reasoning.
- Authentication, authorisation, workload identity and least privilege.
- Zero-trust principles without assuming a specific vendor implementation.
- Encryption, key management and secrets handling.
- Secure software supply chain and dependency risk.
- Threat-informed controls and defence in depth.
- Failure-mode analysis, graceful degradation and recovery design.
- Risk scoring: understand CVSS v4.0 and legacy v3.1 usage; follow the version required by the governing organisation rather than treating a score as the whole risk decision.
- Security evidence, incident response and recovery testing.

### Decision questions

- What must be protected, from whom and under which failure conditions?
- Where does trust begin and end?
- Which controls reduce likelihood, impact or detection time?
- How will recovery be tested rather than merely documented?

### Core references

- OWASP, [Top 10:2025](https://owasp.org/Top10/2025/)
- OWASP, [Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- OWASP, [Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- FIRST, [CVSS](https://www.first.org/cvss/)

---

## Module 7 — Cloud-native design, operability and evolution

### Why it matters

Cloud architecture is an operating model, not a list of managed services. A sound design connects workload needs to deployment, identity, telemetry, recovery, cost and change.

### Core knowledge

- Regions, availability zones, networks and failure domains.
- Containers, orchestration, serverless and managed services as context-dependent choices.
- Twelve-factor operating principles and their limits.
- Infrastructure as code, immutable delivery and policy enforcement.
- Observability through logs, metrics and traces.
- Deployment strategies: rolling, blue-green and canary.
- FinOps: unit economics, ownership, budgets and cost-allocation signals.
- Strangler-fig migration, coexistence, rollback and data reconciliation.
- Portability versus the value of provider-specific capabilities.

### Decision questions

- Which capabilities should be managed, built or retained?
- What failure-domain and recovery assumptions does the deployment make?
- How will the cost per meaningful business outcome be measured?
- Which migration seam delivers value while preserving rollback?

### Core references

- AWS, [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- Twelve-Factor App, [methodology](https://12factor.net/)
- OpenTelemetry, [concepts](https://opentelemetry.io/docs/concepts/)
- AWS, [Strangler fig pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html)

---

## Module 8 — Architecture communication and decision records

### Why it matters

A diagram is a story for a specific audience. A decision record preserves why a choice was made. Neither artifact is useful when its scope, boundaries, ownership or consequences are unclear.

### Core knowledge

- C4 context, container, component and code views.
- Dynamic and deployment views for runtime and operational concerns.
- Diagram scope, legend, direction, protocols, ownership and boundaries.
- Architecture Decision Records: context, options, decision, consequences and status.
- arc42 as a documentation structure.
- Diagrams as code and generated views.
- Executive summaries and engineering-level explanations of the same decision.
- Documentation lifecycle, review ownership and staleness controls.

### Decision questions

- Who is the audience, and what decision must this view support?
- Which level of abstraction is appropriate?
- Which decisions deserve durable records?
- How will diagrams and records stay aligned with the running system?

### Core references

- C4 model, [introduction](https://c4model.com/introduction)
- Architecture Decision Records, [community resources](https://adr.github.io/)
- arc42, [overview](https://arc42.org/overview)
- Structurizr, [DSL](https://structurizr.com/dsl)
- Mermaid, [live editor](https://mermaid.live/)

---

## Module 9 — Governance, influence and evolutionary fitness

### Why it matters

Architecture succeeds through teams. Governance should make safe decisions easier, surface risky drift early and allow evidence-based exceptions; it should not turn an architecture group into a late approval queue.

### Core knowledge

- Decision rights, escalation paths and exception lifecycles.
- Guardrails, paved roads and platforms as products.
- Architecture reviews as structured conversations about drivers, options, risks and evidence.
- Fitness functions for continuously checked architecture characteristics.
- Technology radars and lifecycle visibility.
- Team boundaries, cognitive load and Conway's law.
- Influencing without direct authority.
- Presenting architecture to executive, product, engineering, security and operations audiences.
- Adoption through shadowing, phased rollout, champions and feedback loops.

### Decision questions

- Which decisions should be centralised, delegated or automated?
- What is the smallest guardrail that manages the material risk?
- How are exceptions recorded, reviewed and retired?
- Which adoption and outcome signals show that governance is helping?

### Core references

- Thoughtworks, [Technology Radar](https://www.thoughtworks.com/radar)
- SFIA 9, [Solution architecture](https://sfia-online.org/en/sfia-9/skills/solution-architecture)
- StaffEng, [leadership stories and guides](https://staffeng.com/)

---

## Module 10 — Synthesis, evolution and architecture defence

### Why it matters

Synthesis connects the complete argument: outcome, stakeholders, drivers, constraints, options, decisions, consequences, risks, migration and evidence. The design is credible only when reviewers can challenge parts of that chain without discovering hidden certainty.

### Core knowledge

- Architecture hypothesis: a decision, expected outcome and validating evidence.
- Option comparison and explicit rejection rationale.
- Risk and assumption logs with owners and decision triggers.
- Evidence planning: prototypes, capacity models, threat models, event proofs and migration spikes.
- Evolutionary roadmaps based on capabilities and risk retirement.
- Architecture review and oral defence.
- Traceability from business outcomes to quality scenarios, decisions and fitness measures.
- Integrity: disclose unknowns, uncertainty and limits.

### Decision questions

- Can every major component be traced to a driver or constraint?
- Which viable alternative was rejected, and why?
- Which consequence has been accepted deliberately?
- What evidence would change the recommendation?
- What happens during migration, rollback and degraded operation?

### Core references

- Software Engineering Institute, [ATAM collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)
- C4 model, [diagram guidance](https://c4model.com/diagrams)

---

## Recommended reading sequence

Books are listed for conceptual depth; editions and availability should be rechecked before purchase.

1. **Fundamentals of Software Architecture** — Mark Richards and Neal Ford. Start with architecture thinking and characteristics, then use the style chapters as references.
2. **Designing Data-Intensive Applications** — Martin Kleppmann. Prioritise reliability, data models, storage, replication, partitioning and stream processing.
3. **Software Architecture: The Hard Parts** — Neal Ford, Mark Richards, Pramod Sadalage and Zhamak Dehghani. Use it to deepen distributed trade-off reasoning.
4. **Building Evolutionary Architectures** — Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage. Connect fitness functions to governance and change.
5. **Release It!** — Michael Nygard. Use it for production failure modes, stability and recovery.
6. **Building Microservices** — Sam Newman. Read selectively when service boundaries and distributed operations are justified by the context.
7. **Team Topologies** — Matthew Skelton and Manuel Pais. Connect cognitive load, team interaction and platform design.

## Completion standard

The curriculum is complete when a learner can independently take an ambiguous scenario and produce a defensible architecture argument containing:

- a concise problem frame and stakeholder map;
- measurable quality-attribute scenarios;
- at least two viable architecture options;
- explicit trade-offs and decision triggers;
- coherent boundaries, runtime, data and failure behaviour;
- security, operability, cost and migration considerations;
- audience-appropriate diagrams and decision records;
- an evidence plan and evolutionary roadmap; and
- a short oral defence that acknowledges uncertainty.

A large document or diagram count is not evidence of architect readiness. The evidence is traceable judgment: the ability to explain why a decision fits its context, what it sacrifices and what would cause it to change.

## Reference status

The web references in this public edition were reviewed on 4 September 2026. Links, product documentation and standards can change; re-check time-sensitive recommendations before relying on them for certification, procurement or production decisions.
