# Reliability and Failure Control

## Purpose and scope

Reliability is useful behaviour under expected and adverse conditions, not merely a process being up. A reliable design keeps important promises when demand spikes, dependencies slow down, machines fail, and operators make mistakes. It contains the blast radius, preserves capacity for valuable work, and provides a tested route back to normal.

This note owns runtime failure containment and recovery: failure domains, deadlines, dependency and retry budgets, overload control, degradation, service objectives, data recovery objectives, drills, and incident learning. Choosing reliability targets is an architecture decision; use the [Architecture Decision Method](../software-architecture/architecture-decision-method.md) to express the stakeholder outcome as a measurable quality scenario and record the trade-off. Correctness across duplicate delivery and partial progress belongs to the durable-workflow note, while AI behavioural quality belongs to production AI assurance.

## First-principles model

Five facts explain most reliability choices:

1. **Capacity is finite.** A service has a safe operating envelope for CPU, memory, connections, worker slots, storage I/O, and dependencies.
2. **Failures are partial.** One region, tenant, pool, dependency, request class, or data partition can fail while the rest appears healthy.
3. **Latency has a tail.** Averages hide the slow requests users wait for, so percentiles and deadline misses matter.
4. **Queues store waiting; they do not create capacity.** A bounded queue can absorb a short burst. Persistent arrival above service rate only grows delay and makes work stale.
5. **Retries spend more capacity.** They can turn a transient fault into recovery, but during overload they add demand precisely where capacity is scarce.

A compact safety condition is:

`demand × work per request ≤ safe capacity`

Admission control lowers demand; efficient execution lowers work; scaling may raise capacity. Retries raise work per request; longer queues raise time and resource occupancy. When the inequality cannot hold, reject or degrade selected work early.

An end-to-end deadline bounds how long one request may consume resources. Allocate that budget across local work, each dependency, any permitted retry, and response overhead; propagate the remaining deadline so downstream work cannot outlive its caller. A failure-domain boundary—separate pools, partitions, accounts, zones, or regions—bounds how far exhausted capacity or corrupt state can spread. Deadlines bound amplification in time; retry budgets bound it in attempts; bulkheads bound it in space.

## Core decisions and trade-offs

- **Allocate the deadline end to end.** Give each dependency a budget derived from the user objective, reserving time for local work and the response. A timeout beyond its caller's remaining deadline wastes work; one set too aggressively creates false failures. Measure tail latency before choosing values.
- **Put retries in one layer.** Name the owner, eligible transient errors, maximum attempts, total retry time, and capacity budget. Use capped backoff with jitter to spread attempts. Do not retry permanent failures, expired work, or unsafe side effects; reduce retries during saturation. Idempotency belongs to [Durable Workflows and Idempotency](../cross-cutting-patterns/durable-workflows-and-idempotency.md).
- **Distinguish circuit breaking from shedding.** A circuit breaker stops calls to an unhealthy dependency and probes recovery. Load shedding rejects work because the caller is near saturation. Both fail fast but observe different conditions; poorly tuned breakers can oscillate.
- **Isolate with bulkheads.** Separate concurrency, thread, connection, and queue budgets for failure domains and request classes. Isolation protects critical traffic from a noisy tenant or optional dependency, at the cost of unused capacity in one pool while another is full.
- **Control admission and pressure.** Rate limits decide who enters, priority shedding preserves valuable work, and backpressure asks upstream producers to slow down. Bound every queue by count or age and define rejection semantics; otherwise waiting destroys latency predictability.
- **Choose failure behaviour per capability.** Fail closed when proceeding could violate authorization, money, safety, privacy, or inventory invariants. Fail open only when the cost of denial is greater and the residual risk is explicit. Degrade when a smaller, clearly labelled result remains useful. A fallback that is stale, less safe, or semantically different needs an expiry, eligibility rule, and user-visible status.
- **Define SLIs, SLOs, and error-budget policy.** An SLI measures user-observed behaviour; an SLO sets its target over a window. The error budget is the tolerated shortfall, used to balance reliability work against change [2, 3]. Specify exclusions and degraded-response treatment so teams cannot redefine success.
- **Set RPO and RTO from impact.** Recovery point objective is the maximum tolerable data loss measured in time; recovery time objective is the maximum tolerable time to restore service. Lower targets cost more replication, automation, testing, and operational skill, so they follow business impact and data semantics.

## Failure modes and warning signs

- **Nested retries:** several layers retry independently, multiplying calls to the weakest dependency. Attempt counts per original request rise during failure.
- **Retry synchronisation:** clients use the same delay and create periodic load spikes. Dependency traffic arrives in waves after each timeout.
- **Unlimited queues:** throughput stays flat while queue age, memory, and timeouts climb; obsolete work remains queued.
- **Deadline inversion:** a dependency timeout or retry window is longer than the caller's remaining deadline. Traces show work completing after the response was abandoned.
- **Shallow health checks:** probes report “healthy” while critical dependencies, writes, or fresh reads fail. Routing sends traffic to instances unable to serve it.
- **Shared pools:** optional and critical paths compete for the same workers or connections. One slow dependency exhausts unrelated traffic.
- **Average-only latency:** dashboards look normal while p95 or p99 and deadline misses grow. The affected users disappear inside the mean.
- **Untested failover:** backups exist, but restore time, credentials, routing, capacity, or integrity are unknown. RPO/RTO lacks drill evidence.
- **Unsafe degradation:** fallback data is unmarked, too stale, or used for a decision that requires authority. Availability improves on paper while correctness falls.
- **Ownerless incident actions:** a post-incident list has no owner, due condition, verification, or review. The same failure recurs because learning never changes a control or test.

## Practical decision checklist

- What user journey and SLO define useful behaviour, including tail latency and degraded responses?
- What is the end-to-end deadline, and what budget remains for each dependency and response work?
- Which leading saturation signal triggers admission control before latency collapse?
- Which work is rejected first, and what explicit response tells the caller to slow down or retry later?
- Which layer owns retries, which errors qualify, and what limits attempts, elapsed time, and retry load?
- For each dependency failure, does the capability fail open, fail closed, or degrade, and for how long?
- Which pool or partition is the failure-domain boundary, and can its exhaustion spread?
- What data can be lost (RPO), how quickly must service return (RTO), and who accepted the cost?
- Has recovery been drilled with realistic state, traffic, permissions, and dependency failure?
- Does every incident action have an owner, evidence of completion, and a path into tests, runbooks, alerts, or design review?

## Worked architecture scenario

Consider an illustrative checkout-read endpoint with a one-second user deadline. It reads the cart, current price, and reservable inventory, but does not place the order. Inventory begins responding slowly under load.

The team reserves 75 ms for the gateway, 125 ms for cart and price reads, 550 ms for inventory, 100 ms to compose the response, and 150 ms for network and scheduling. The gateway propagates an absolute deadline. Inventory gets a 250 ms first attempt, up to 50 ms of jitter, and one 250 ms retry only for an eligible transient read failure. Its client library does not retry. Saturation or insufficient remaining budget suppresses the second attempt, following the bounded-retry principle [1].

Inventory calls use their own connection and concurrency pool, so slow responses cannot occupy cart or price capacity. A breaker stops new inventory calls after a sustained qualifying failure rate and admits limited probes during recovery. Admission control monitors in-flight work and queue age. Under pressure, the service first sheds recommendation refreshes and other low-priority work; it then rejects excess checkout reads quickly instead of accepting an unbounded queue.

If cart and price are authoritative but inventory is unavailable, the endpoint can return a clearly marked `availability_unconfirmed` result with a short expiry. That response remains useful for review but is not permission to place an order. The later order-placement operation fails closed unless it obtains authoritative inventory confirmation. This separation makes degradation safe instead of silently weakening the invariant.

The team defines its SLI as the proportion of eligible checkout reads that return either a complete result or the approved marked degradation within one second, and separately tracks complete-result rate. The chosen SLO and error-budget policy determine when excessive degraded responses halt risky changes; the [decision method](../software-architecture/architecture-decision-method.md) owns the target and stakeholder approval.

Service recovery and data recovery are different. The breaker may close and normal responses resume within seconds, yet inventory data may still be stale or damaged. The owners therefore set separate, illustrative objectives—such as restoring the inventory service within 15 minutes and losing no more than one minute of acknowledged inventory changes—then prove them with failover and restore drills. An incident review traces attempts per original request, pool saturation, shedding, degraded outcomes, and recovery evidence. Actions update a control, drill, test, alert, or runbook and retain named owners until verified.

## Feynman questions

1. A dependency is overloaded. Explain, without jargon, how retries can convert slowness into an outage and how three different budgets stop that amplification.
2. Why can a queue absorb a burst but not create capacity? What happens to queue age when arrivals remain above completions?
3. How is a user-facing SLO different from a dashboard metric such as CPU utilization? Give one SLI that exposes tail behaviour.
4. When should a feature fail closed even if doing so reduces availability? Name the invariant being protected.
5. Explain RPO and RTO using one lost-data example and one unavailable-service example. Why can improving one leave the other unchanged?

## Related canonical notes

- [Architecture Decision Method](../software-architecture/architecture-decision-method.md) owns quality-attribute scenarios, target selection, evidence, trade-offs, and ADRs.
- [Durable Workflows and Idempotency](../cross-cutting-patterns/durable-workflows-and-idempotency.md) owns stable operation identity, duplicate delivery, checkpoints, replay, compensation, and cross-step correctness.
- [Production AI Assurance](../ai-architecture/production-ai-assurance.md) owns AI behavioural reliability, evaluation, autonomy boundaries, safe rollout, and AI-specific rollback evidence.

## Sources and review status

Repository sources:

- [System Design Concept Handbook v5](../../handbooks/system-design/system-design-concept-handbook-v5.html)
- [Software Architect Grooming Programme v5](../../learning-paths/software-architect/software-architect-grooming-programme-v5.html)
- [The AI Architect's Handbook v1.2](../../handbooks/ai-architecture/ai-architects-handbook-v1.2.html)
- [Forward Deployed AI Engineer Handbook v1.3](../../handbooks/fde/fde-handbook-v1.3.html)

External references (verified 2026-09-05):

1. Amazon Builders' Library, [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
2. Google, [Site Reliability Engineering: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
3. Google, [The Site Reliability Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)

**Status:** Current

**Edition:** Living

**Last reviewed:** 2026-09-05
