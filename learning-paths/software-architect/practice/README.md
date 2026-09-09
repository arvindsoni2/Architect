# Software architect practice guide

Reviewed 8 September 2026. Companion to the [curriculum](../software-architect-curriculum-guide-v3.md) and [programme](../software-architect-grooming-programme-v5.html). All businesses, prices and workload figures in the worked examples are teaching assumptions. Local experiment output is evidence only for the tested implementation and environment.

## Start here

Use Python 3.10 or later with its standard `sqlite3` module. No cloud account, paid service, package installation or credentials are needed. From the repository root:

```bash
python3 learning-paths/software-architect/practice/reservation-lab.py
python3 learning-paths/software-architect/practice/reservation-lab.py --serve
```

The first command runs isolated experiments and prints actual results. The second starts a tiny browser/API/database path at `http://127.0.0.1:8765/`. Stop with Ctrl-C. Each run uses temporary databases which are removed on exit; restart for clean stock. Save observations in your own workspace outside this public repository. The `--serve` mode reserves stock but does not run the relay; use the default experiment for outbox recovery.

If Python is not found, install it using your operating system's supported package source. If `sqlite3` is unavailable, use a Python installation that includes it. If the port is occupied, use `--port 8766`. Connection refused normally means the server has stopped or you selected the wrong port. The server binds only to this machine; do not expose this teaching server to a network.

## Six diagnostic bridges

Diagnose every bridge, including B3. A role suggests a starting order; it never proves competence. For each bridge, record an artefact, a short explanation, one reviewer challenge and a revision. Mark **demonstrated** only when the acceptance evidence below is met; unknown or incomplete means practice required. An independent learner can provisionally assess against these anchors, then seek an external review before claiming an assessment pass.

### B1 — Code to runtime

**First principle:** a request travels through processes and protocols. Each boundary can fail independently; a timeout describes what the caller observed, not necessarily what the server committed.

1. Start `--serve`, open the page and browser developer tools → Network. Submit `order-a`, quantity 1.
2. Inspect the method, URL, JSON body, status and response. Match the request key to the terminal's `transaction committed` trace.
3. Open `reservation-lab.py`. Follow `do_POST` → `reserve` → `BEGIN IMMEDIATE` → conditional stock update → request/outbox insert → commit → HTTP response.
4. Submit the same key again. Then submit `order-b`. Explain the successful retry and the 409 stock rejection.
5. Stop the server and submit again. Distinguish connection failure, invalid input, out-of-stock business rejection, database failure and a response lost after commit.

**Acceptance:** annotate browser, process, TCP/HTTP, handler and database on a request diagram; show one matching request/trace pair; explain five failure points without treating all failures as HTTP 500. Explain why source code is not a running process and where durable state resides.

**If stuck:** draw only one request first. Inspect the response before reading the whole script. Explain each arrow aloud using “sends”, “validates”, “commits” or “returns”.

### B2 — APIs, data and distributed failure

**First principle:** a business invariant must survive concurrency and retry. Messaging changes when work happens; it does not remove correctness obligations.

1. Predict the outcome of two distinct orders competing for one stock item. Run the default lab and compare predictions to output.
2. Locate the idempotency record and quantity check. Explain why a key must identify one operation with one payload and a defined retention period.
3. Locate the outbox insert in the reservation transaction. Interrupting before commit must leave no reservation and no event.
4. Follow `relay`: the receipt effect commits before delivery acknowledgement. A simulated interruption makes delivery repeat; the unique effect key prevents a second effect.
5. Draw synchronous checkout and durable workflow alternatives. Keep the stock decision synchronous if the customer requires immediate confirmation; move notification to asynchronous delivery. Define what “accepted” promises.

**Acceptance:** a legal state machine, three failure sequences and actual output proving no oversell, stable retry result, atomic rollback and one receipt after duplicate delivery. Explain why this does not prove exactly-once delivery or safe real payment capture.

**If stuck:** list facts known after each commit. Do not infer payment failure from a timeout. The `effects` table is a simulated consumer receipt, not a payment integration.

### B3 — Quality and resilience

**First principle:** a quality requirement is useful when a reviewer can construct a test that could disprove it.

Use six fields: source, stimulus, environment, artefact, response, response measure. Worked scenario: **source:** signed-in patient; **stimulus:** request for a previously synchronised emergency record; **environment:** one regional integration is unavailable and 200 requests/s are offered; **artefact:** portal read path; **response:** serve an authorised cached record with its freshness timestamp; **measure:** at least 99.9% of eligible requests succeed, p95 below 500 ms over a 15-minute test, no unauthorised records returned. These are assumed teaching targets requiring clinical agreement, not a healthcare policy recommendation.

1. Convert “fast”, “secure”, “available”, “easy to change” and “recoverable” into five complete scenarios.
2. Define the eligible population, measurement window and pass/fail threshold for each. Distinguish a latency objective from an availability objective.
3. Run one failure exercise from B2 and attach observed results. For recovery, distinguish committed local state from temporary server lifetime and production backups.
4. Give a reviewer a scenario without explaining it. Ask whether they can design its test and identify contradictory requirements.

**Acceptance:** five complete scenarios, one measured experiment and one revised scenario following review. A vague adjective or missing measurement window requires revision.

### B4 — Business and domain framing

**First principle:** a boundary keeps a coherent meaning and set of rules together. A business noun alone is not a service boundary.

1. Trace “customer purchases stock” through promise, reservation, payment, fulfilment and finance. Write the outcome and owner of each step.
2. Ask whether “available” means physically present, unreserved, sellable, or deliverable by a date. Keep each meaning in an explicit bounded context.
3. Model a stock reservation aggregate around the rule “committed reservations cannot exceed allocatable stock”. Compare per-location stock ownership with central reservation authority.
4. Draw a context map. Identify upstream facts, downstream projections and a translation boundary for a legacy ERP's terminology.
5. Add an offline store: two channels cannot both consume the same last item during disconnection without an allocation rule or accepted oversell risk. Compare preallocated stock quotas, refusing risky promises, and business-approved reconciliation.

**Acceptance:** a capability map, glossary, invariant ownership and two credible boundary options with consequences. Different terms in different contexts are deliberate; shared database tables are not automatically shared ownership.

**Read:** [Fowler: Bounded Context](https://martinfowler.com/bliki/BoundedContext.html), especially the model boundaries and mapping discussion. Read to answer “where does the word change meaning?”

### B5 — Cloud, security and operations

**First principle:** deployment adds identities, failure domains, cost and operational ownership. Moving a process to the cloud does not supply these decisions automatically.

1. Turn the B1 local path into a hypothetical production deployment. Draw ingress, application, database, user/service/operator identities and trust boundaries.
2. State who may reserve stock, read records, deploy changes and perform recovery. Identify where credentials and keys live; the local lab intentionally has none of these production controls.
3. Compare one-zone and multi-zone operation. Define an SLO, RTO and RPO with a business owner and a test, not just a number.
4. Draft a restore experiment: create known records, take a backup, add more records, restore into a separate target and measure time and missing records. Do not describe the lab's temporary database as a backup mechanism.
5. Estimate monthly cost using the worked economics below, including operations time. Decide which failure or cost assumption needs measurement first.

**Acceptance:** deployment/trust diagram, access matrix, failure table, cost range and a recovery test protocol with owner and acceptance measures. If no restore was executed, label recovery evidence as **planned**, never **verified**.

**Read:** AWS Reliability Pillar sections on [backing up data](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/back-up-data.html) and [testing reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html); use them to challenge the restore protocol.

### B6 — Communication and review

**First principle:** a view answers an audience's question; a decision record preserves a reason that would otherwise disappear.

1. Draw the system context and container views for B1's hypothetical production service. State system scope; do not label every domain noun as a separately running container.
2. Add a dynamic view for a retry after a lost response. Number interactions, label protocols and distinguish commands from events.
3. Use the worked ADR below as a structure, then write your own for a different constraint. Keep status, rejected alternatives, consequences and decision triggers.
4. Explain the same choice in two minutes to a product owner and ten minutes to an engineer. Have the reviewer repeat the decision and its biggest sacrifice back to you.

**Acceptance:** understandable diagrams without narration, an ADR with two viable alternatives and recorded reviewer feedback. Revise any arrow the reviewer cannot interpret.

**Read:** [C4 diagram guidance](https://c4model.com/diagrams) and [ADR resources](https://adr.github.io/). Focus on context/container/dynamic views and one decision template, not the entire sites.

## Worked decision: two credible options

Assume five engineers, two people on call, 16 weeks to launch, 200 initial merchants and unknown growth. Both options use an external payment provider and controlled card-data scope. Option A is a modular monolith; B is three coarse services for merchant management, payment workflow and reporting. Neither requires a service mesh.

Scores below are illustrative judgments on a 1–5 scale, where 5 is a better fit. First eliminate options that violate mandatory controls. Then compare preferences; a high weighted total cannot compensate for failing a hard constraint.

| Criterion | Weight | A: modular monolith | B: three services | Reason for the assumed difference |
| --- | ---: | ---: | ---: | --- |
| Delivery speed | 30% | 5 | 3 | A needs fewer contracts and deployments initially |
| Operational fit | 25% | 5 | 3 | A fits the small on-call team |
| Transaction simplicity | 20% | 5 | 3 | A keeps more invariants in one transaction |
| Independent releases | 15% | 2 | 5 | B isolates release ownership |
| Independent scaling | 10% | 2 | 5 | B can scale reporting separately |
| Weighted result | 100% | **4.25** | **3.50** | Decision support, not a measurement of architectural quality |

Sensitivity check: if the weights become 15%, 15%, 15%, 30%, 25%, A scores **3.35** and B **4.10**. The answer changes when release autonomy and separate scaling dominate. Validate the scores with team experience, prototype evidence and operational capacity; do not adjust weights to manufacture the preferred answer.

### Worked ADR-001: initial deployment boundary

**Status:** proposed teaching decision; awaiting domain and security review.

**Context:** the team and launch constraints above dominate. Correct reservations, payment auditability and access control are mandatory. Reporting load is uncertain; a separate reporting read model can initially share the application deployment.

**Options:** A, a modular monolith with dependency checks and one transactional store; B, three coarse services with explicit contracts and service-level ownership. Retaining a third-party hosted commerce platform is a build/buy alternative to investigate if differentiation is limited.

**Decision:** choose A for the first increment, subject to passing the reservation and provider-integration experiments. Keep merchant, reservation and payment modules explicit. Application policy depends on a payment port; the provider adapter implements that port. Domain rules do not import the web framework or provider SDK. Reversing an import in a small module test should make the dependency check fail.

**Consequences:** accept one deployment and shared scaling. Gain fewer distributed failure modes. Pay for module enforcement and outbox operations. A provider abstraction cannot erase provider-specific settlement, refund or dispute semantics.

**Evidence:** the reservation lab demonstrates a local atomic invariant and duplicate-safe receipt. It does not establish provider correctness, production throughput, access control or disaster recovery. Run sandbox contract tests for authorisation, capture, timeout reconciliation and webhook duplication before real integration.

**Revisit when:** reporting consumes over 30% of database CPU during three representative peaks after query tuning; cross-module coordination blocks more than two releases per month for three months; or a team with funded on-call ownership needs an independent release cycle. These thresholds are assumed signals to review the choice, not automatic extraction commands.

**Owner/review:** lead architect and engineering lead; review after the first pilot and after any trigger. Record observed evidence, decision status and exceptions.

## Worked capacity and latency model

Assume 150,000 peak browse requests/s, 20,000 average requests/s, 2,000 updates/s and a 4 kB decimal response body. These are model inputs, not observed traffic.

- Peak payload egress: 150,000 × 4,000 = **600 MB/s**, about **4.8 Gbit/s**, excluding protocol overhead and compression.
- At a **95% measured hit rate**, origin reads would be **7,500/s**. At 80%, they become **30,000/s**, four times as many. Do not assume a hit rate without testing key popularity, invalidation and cold starts.
- If average origin residence time is 80 ms in a stable interval, Little's Law gives about **600 concurrent origin requests** at 7,500/s. Do not substitute p95 latency for the mean or use this steady-state estimate during an accumulating queue.
- Allocate a 300 ms promise-response budget: ingress/authentication 30 ms, application 40 ms, inventory dependency 150 ms, response overhead 30 ms, reserve margin 50 ms. These are engineering allocations; adding component p95 values does not calculate end-to-end p95. Measure the complete path.
- Three layers each making one initial attempt plus three retries can create up to **4³ = 64** downstream attempts for one request in the worst case. Put retry ownership, total deadline, jitter and admission limits at explicit boundaries.

**Experiment:** use representative keys, vary hot-key skew and cache warmness, record offered/achieved throughput, errors and end-to-end latency. If the queue grows continuously, the system is not sustaining the offered load. Do not extrapolate this SQLite teaching lab to the catalogue workload.

**Read:** [AWS dependency availability](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-dependencies.html). Treat availability multiplication as a simplified model for required dependencies with appropriate independence assumptions, not a prediction from vendor SLAs. Shared failure domains and degraded operation change the model.

## Worked workflow and transactional boundary

Reservation uses one atomic update conditional on remaining stock, plus the request record and outbox in the same transaction. The idempotency key is checked against the quantity. SQLite serialises writers; the lab's short transaction is intentional. PostgreSQL isolation and contention behaviour must be tested separately; do not transfer SQLite locking assumptions to another engine. [SQLite transactions](https://www.sqlite.org/lang_transaction.html), [SQLite isolation](https://www.sqlite.org/isolation.html), [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html)

Compare optimistic version checking and retry with pessimistic locking for a hot reservation key. Ask whether rejected competitors should retry, how starvation is bounded, and where lock duration is measured. An application-side read followed by a separate unguarded write does not establish the invariant.

| State | Event or observation | Permitted next action | Evidence retained |
| --- | --- | --- | --- |
| Created | Inventory reserved | Request payment authorisation | Reservation ID, expiry, command key |
| Awaiting authorisation | Provider confirms authorisation | Confirm order according to fulfilment policy | Provider ID and amount |
| Awaiting authorisation | Caller times out | Enter reconciliation; query provider with the same operation identity | Request key and last known result |
| Awaiting authorisation | Provider declines | Release reservation once | Decline and release receipt |
| Reconciling | Outcome still unknown at deadline | Escalate with a controlled recovery action | Attempts, timestamps and operator ownership |
| Confirmed | Fulfilment starts | Capture according to agreed business rules | Capture key and fulfilment evidence |

The table is a design example, not implemented payment code. Also design late authorisation after reservation expiry, partial fulfilment and cancellation/capture races. Compensation is a new business action and can itself fail. A timeout must never silently mean “payment definitely failed”.

The transactional outbox closes the state-change/publication gap. Delivery can still repeat, so each consumer must make its own effect duplicate-safe. [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html)

## Worked architecture economics

Assume managed option A costs £400/month plus four operating hours; self-managed B costs £180/month plus 16 hours. Value engineering time at an illustrative £50/hour: A = **£600/month**, B = **£980/month**. At 100,000 successful orders, that is **£0.006** versus **£0.0098 per order**. These are assumed inputs, not quotes or current market prices.

At 16 hours for both options, A becomes £1,200 and B £980. Investigate the operating-hour assumption instead of comparing infrastructure bills alone. Add implementation, migration, support, egress, licensing, exit cost and expected disruption before making a procurement recommendation. Compare build/buy/retain against the required differentiation, contractual constraints and time to value.

## Transfer task and evidence record

After understanding the worked examples, change the scenario: four independent product teams now release weekly; the reporting workload has been measured as dominant; stores are offline for two hours. Recalculate the decision matrix, change the ownership model, and identify what the local lab no longer proves. Do not copy the original ADR's conclusion.

For each experiment submit:

1. Hypothesis and exact acceptance condition.
2. Code revision, runtime versions, workload/input and reproduction command.
3. Actual observations, including failures and raw output location.
4. Interpretation and limitations; distinguish observed facts from projected behaviour.
5. Resulting decision or revision, plus what evidence is still missing.

Required capstone evidence includes two executed experiments, one covering concurrent/duplicate workflow correctness and one covering a different material risk such as recovery, contract compatibility, performance or migration reconciliation. At least one must change this lab's inputs or implementation meaningfully, or use a project of your own. A successful run of unchanged examples alone is not sufficient.

## Targeted preparation by unit

Use the programme's four concept definitions as a checklist for discussion, not as a scripted 45-minute lecture. Each selection below has a question and a stopping point. Videos and whole books remain optional depth resources.

| Unit | Required preparation | Question to bring to the exercise |
| --- | --- | --- |
| 1 | B3 six-field scenario and [SEI QAW overview](https://www.sei.cmu.edu/library/the-sei-quality-attribute-workshop/) | Can a reviewer design a test from my scenario? |
| 2 | Worked decision matrix and ADR above | Which weight or evidence would reverse my choice? |
| 3 | Worked capacity model above | Which uncertain input most affects capacity? |
| 4 | Workflow table above; outbox reference, Context through Result context | Which commit is authoritative after a timeout? |
| 5 | B4 ownership exercise and [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) | Which fact is authoritative and which is a projection? |
| 6 | [OWASP threat modelling](https://owasp.org/www-community/Threat_Modeling), process overview; B5 access matrix | Which trust crossing could cause the largest loss? |
| 7 | [Strangler fig](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html), Intent through Issues and considerations | How does ownership move, and what can actually roll back? |
| 8 | B6 and C4 context/container/dynamic guidance | What audience question does each view answer? |
| 9 | Worked economics above; programme guardrail example | Which decision is delegated, and how is an exception retired? |
| 10 | Transfer task and evidence record above | Which two experiments retire the most important uncertainties? |

## Validation for maintainers

From repository root:

```bash
node --test learning-paths/software-architect/tests/test_programme.cjs
python3 -m unittest discover -s learning-paths/software-architect/tests -p 'test_*.py' -v
python3 scripts/validate_repository.py
```

The browser programme retains its historical filename and storage keys. New diagnostic and assessment fields begin incomplete. Imported completion is recalculated against current gates. Backups contain learner-entered notes and a visible export timestamp; keep them private and out of the public repository.

Browser smoke tests run in a path-scoped GitHub Actions workflow using Playwright 1.62.1 and Chromium. The workflow checks navigation/history, diagnostic progress, assessment floors, import/export, blocked-storage fallback, desktop/mobile layout and print visibility. It uploads synthetic review screenshots and a print PDF for seven days; no learner data is used.
