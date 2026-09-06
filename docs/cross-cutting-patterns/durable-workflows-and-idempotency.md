# Durable Workflows and Idempotency

## Purpose and scope

A durable workflow is explicit business state and recovery semantics around work that may outlive one process. It remains understandable and correct when a worker crashes, a message arrives twice, a dependency times out after acting, or a person responds hours later. Durability is not merely storing a job: the system must know what happened, what may safely happen again, and who resolves uncertainty.

This note owns cross-step correctness: delivery and processing semantics, stable operation identity, idempotency and deduplication, transactional outbox, state machines, checkpoints, replay, compensation, and reconciliation. It applies to ordinary distributed work as well as AI-assisted flows; an agent or model call is just one potentially retryable step.

Adjacent notes set other policy. [Reliability and Failure Control](../system-design/reliability-and-failure-control.md) owns deadlines, retry budgets, backpressure, poison-message capacity protection, and recovery objectives. [Architecture Decision Method](../software-architecture/architecture-decision-method.md) owns trade-off records. [Production AI Assurance](../ai-architecture/production-ai-assurance.md) owns model evaluation, autonomy, and approval authority. This note owns preserving a valid approval and its context across a pause, not deciding which actions require approval.

## First-principles model

Networks do not transmit knowledge perfectly. They can lose, delay, reorder, and duplicate messages. A timeout proves only that the caller stopped waiting; it does not prove that the callee did nothing. A worker may commit a change and crash before acknowledging the message, so the broker delivers it again.

Separate three facts:

1. **Delivery:** did a message reach a consumer, perhaps more than once?
2. **Processing:** did the handler validate and durably commit its transition?
3. **External effect:** did another system charge, notify, publish, or update—and can that outcome be queried?

Calling all three “processed” hides the most dangerous gaps. Build a correctness loop instead:

`stable operation ID → durable state transition → retryable step → effect record → observed outcome → reconciliation`

The operation ID names the business intent, not one HTTP attempt or queue delivery. Generate it at the intent boundary and reuse it across every retry, redelivery, restart, and status query. Each state transition records the operation, prior state, next state, attempt or effect identity, and relevant result. A worker acknowledges only after its durable commit. If an external outcome remains unknown, the workflow enters an explicit state such as `update_unknown`; it queries by the same operation ID before deciding whether to retry. Periodic reconciliation compares the workflow ledger with authoritative external state and repairs or escalates mismatches.

## Core decisions and trade-offs

- **Synchronous or queued:** synchronous work waits for an outcome within the caller's deadline and ties the caller to downstream latency; a timeout or connection loss can leave the effect unknown. A durable queue lets intake acknowledge accepted work and absorb short bursts, at the cost of delayed completion, duplicate delivery, ordering questions, and lifecycle state. Capacity and backlog policy remain reliability concerns.
- **Queue or stream:** a queue usually distributes work among consumers; a stream preserves an ordered history for independent consumer positions and replay. Choose from the business need for competing consumption, history, ordering, and reprocessing—not from product fashion.
- **Delivery guarantee:** at-most-once avoids broker redelivery but can lose work after a pre-commit failure. At-least-once preserves retryability but requires duplicate-safe processing. Treat “exactly once” as a claim inside a named boundary, such as one database transaction or broker feature; it does not automatically include a remote API, email provider, or human action.
- **Idempotency contract:** define the key’s namespace, owner or tenant, operation type, payload fingerprint, result returned on repeat, concurrency behaviour, and retention. The same key with a different payload must conflict. Retain records at least as long as retries and delayed deliveries remain possible; permanent retention creates unbounded state and may violate data policy.
- **Inbox or deduplication:** a consumer can atomically insert a message or effect ID into an inbox alongside its business update. A uniqueness constraint makes racing deliveries converge on one committed transition. Broker deduplication is useful but cannot replace a business-level invariant when its scope or time window is narrower.
- **Transactional outbox:** commit business state and an outbox event in one local transaction, then let a relay publish committed rows. This closes the database-success/message-failure dual-write gap [2]. The relay can still publish twice, so events need stable IDs and consumers remain idempotent.
- **State machine and checkpoints:** model legal states, transitions, terminal outcomes, waits, timeouts, and owners explicitly. Checkpoint only durable, validated state at a defined boundary. Replay must be deterministic from recorded history: use replay-safe APIs whose time and randomness values are recorded, and put external interactions in activities whose results are recorded and reused rather than re-executed during replay [1]. Version workflow logic so old executions can still resume safely.
- **Compensation and reconciliation:** when one transaction cannot span systems, define forward recovery. Compensation is a new business action—release a reservation or mark a case for correction—not time travel, and it can fail. Irreversible or legally meaningful effects require status inquiry, reconciliation, and sometimes a named human decision rather than an invented inverse.

## Failure modes and warning signs

- **Acknowledge before commit:** a crash loses work that the broker believes finished.
- **Dual writes:** database state changes without its event, or an event announces a rolled-back change.
- **Regenerated retry keys:** each attempt looks new and repeats the external effect.
- **Permanent dedupe records:** an unbounded inbox grows forever without a retry-horizon or retention decision.
- **Non-deterministic replay:** current time, random values, mutable reads, or direct tool calls change the reconstructed path.
- **Hidden partial states:** one vague `failed` status conceals whether an effect occurred, remains unknown, or needs compensation.
- **Inverse-transaction compensation:** the design assumes “undo” restores the world despite fees, notifications, observations, or intervening changes.
- **Ownerless poison messages:** repeated deterministic failures cycle or accumulate without quarantine, diagnosis, replay criteria, and an accountable owner.
- **Context-free or silently expired approval:** a decision is detached from the exact payload and evidence, or old authority resumes work after its expiry.

Also watch for acknowledgements without transition records, duplicates without a stable correlation ID, dedupe hit rates that suddenly rise, outbox age that grows, workflow states with no exit, and reconciliation differences that have no response playbook.

## Practical decision checklist

- What business intent does the operation ID identify, who creates it, and where must it be propagated unchanged?
- Which store owns authoritative workflow state, and which transitions are legal?
- Exactly where do business commit and message acknowledgement occur?
- Which layer owns retries, and how does it distinguish safe retry, status inquiry, compensation, and escalation?
- What should a duplicate return, and what invariant prevents concurrent duplicates from both acting?
- How long are idempotency and inbox records retained relative to every delivery and client retry horizon?
- Which ledger records attempted, confirmed, rejected, and unknown external effects?
- What state is checkpointed, what history is replayed, and how is deterministic replay protected across code versions?
- For each partial success, what compensation is possible, what can compensation itself fail to do, and who owns that failure?
- Who owns quarantined poison messages, and what evidence permits replay or discard?
- Which reconciliation compares local intent with the external system of record, at what cadence, and with what escalation?
- What payload, evidence, approver, timestamp, expiry, and revocation state must survive an approval pause?

## Worked architecture scenario

An insurer accepts AI-assisted claims evidence. Intake validates the request, creates operation `claim-evidence:8427:v1`, commits an `accepted` state plus an outbox row, and returns `202 Accepted` with a status URL. The outbox relay publishes the stable event. A duplicate client submission with the same key and payload receives the existing operation; the same key with changed evidence conflicts.

Retrieval and draft generation run as retryable activities. Their source identifiers and results are checkpointed before the workflow advances. Model calls may vary, so replay reads their recorded outputs rather than silently generating a different draft. The workflow stores `awaiting_approval` with the exact proposed case-update hash, evidence version, approver scope, requested time, and expiry. Approval is valid only for that payload and while the authority remains current; expiry moves the operation to `approval_expired`, requiring fresh evidence or a new decision.

After approval, a worker calls the external case system with an effect ID derived from the stable operation and transition. The case system applies the update idempotently and records that key. The worker then crashes before its local commit and message acknowledgement. Redelivery does not mean the first call failed: the replacement worker finds no local confirmation, queries the case system by effect ID, observes the completed update, records `case_updated`, and continues without applying it twice.

That transition and a `notice_requested` outbox event commit together. The relay may publish the notification event twice; the notification service uses its own inbox/effect key so one logical notice is requested. If the case update is rejected after an earlier temporary evidence reservation, a compensating activity releases the reservation and records its outcome.

Suppose the notice provider times out and cannot query by key. The workflow immediately records `notice_outcome_unknown` and blocks automatic resend and completion. Later, reconciliation with provider records discovers confirmation that the legally meaningful notice was sent. A claims operator compares that confirmation with the effect ledger, decides the case disposition, and records the manual rationale. Sending a second notice or pretending to retract the first would be unsafe. The final state distinguishes completed, compensated, and manually reconciled outcomes instead of erasing partial history.

## Feynman questions

1. A request timed out. What does that prove, and which facts must you learn before trying again?
2. Why does at-least-once delivery need idempotent processing even when handlers usually succeed?
3. How does an outbox close the dual-write gap, and why can its relay still require a duplicate-safe consumer?
4. Why is compensation a new fallible action rather than database rollback? Give an effect that cannot truly be undone.
5. What state must survive a day-long human pause so that approval cannot be applied to changed or stale work?

## Related canonical notes

- [Architecture Decision Method](../software-architecture/architecture-decision-method.md) owns requirements, alternatives, trade-off records, evidence, and reversal triggers for choosing a workflow design.
- [Reliability and Failure Control](../system-design/reliability-and-failure-control.md) owns deadlines, bounded retries, overload policy, queue capacity, recovery objectives, and incident learning.
- [Production AI Assurance](../ai-architecture/production-ai-assurance.md) owns task-specific evaluation, autonomy boundaries, human escalation policy, AI observability, rollout, and rollback evidence.

## Sources and review status

Repository sources:

- [System Design Concept Handbook v5](../../handbooks/system-design/system-design-concept-handbook-v5.html)
- [Agent Engineering Master Manual v2.7](../../handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)
- [Interview Resource Accelerator v4.3](../../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.3.html)

External references (verified 2026-09-05):

1. Temporal, [Workflow replay](https://docs.temporal.io/workflows)
2. AWS Prescriptive Guidance, [Transactional outbox pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

**Status:** Current

**Edition:** Living

**Last reviewed:** 2026-09-05
