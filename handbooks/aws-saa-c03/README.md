# AWS SAA-C03 study pair

To connect these labs to an end-to-end solution and interview explanations, use the [patient portal connected-learning case](../../learning-paths/software-architect/patient-portal-connected-learning.md). It maps the current lab display numbers and titles to architecture decisions and evidence.

Owner-approved repository exception, 7 September 2026. These two resources are maintained as a pair; the exception does not admit other certification packs or course notebooks.

- [Visual Handbook — v2026.09.25.1](saa-c03-visual-handbook-2026.09.html)
- [The $170 Cloud Lab Manual — v2.1](saa-c03-lab-manual-v2.1.html)

Download the HTML files and open them locally for their navigation and interactive features; GitHub's source viewer does not run them. The lab manual stores progress in browser-local storage. Its export/import feature transfers status, recorded costs and evidence ticks, not AWS account data. The print-all control prepares every lab and tab for printing.

## Revision scope

The 21 September exam-readiness update maps all 14 exam tasks to the actual handbook sections and lab IDs. The core labs now include an **Exam route** with practical checks for policy denial, DynamoDB queries and consistency, container recovery/scaling, stream replay, shared storage, read replicas and stale caches. Cross-account, hybrid migration and cost exercises explicitly distinguish modeled decisions from deployed and tested evidence. A skipped deployment remains a practical gap.

The handbook adds 18 expandable mechanism/decision explanations, a deeper DynamoDB explanation, four worked cost worksheets with fictional prices, and active-recall prompts. Section 40 provides 20 original mixed questions for a 40-minute closed-notes session, including distractor explanations and changed-requirement variants. This is a teaching assessment, not an official exam or a calibrated pass predictor. Use unfamiliar official practice resources after working through it.

Section 41 is a redraw route through eight architecture patterns. It points back to the existing two-AZ drawing and adds visual comparisons for routing, database replication, storage selection, event flows, hybrid connectivity, security boundaries and disaster recovery. Each pattern asks what the components do, what failure they address, the cost drivers, and which changed requirement alters the design. The drawings and answer prompts stay collapsed until you reveal them; links connect to the fuller topic and companion lab. These eight patterns are a study framework, not an official list of exam diagrams or complete exam coverage.

The September revision corrects RI capacity scope, NAT availability modes, API types, SQS limits, DynamoDB expiry, and service-availability caveats. It adds worked decisions and a 14-task exam coverage map, repairs misleading topology, and improves SVG connector endpoints and canvas bounds.

Lab corrections include OIDC environment subjects, Identity Center prerequisites, gross-cost budgets, database-backed recovery probes, atomic inventory/outbox processing, version-aware cleanup, CloudFront failover conditions, key-specific encryption policy, deployment ordering, data-fixture comparisons, per-store RPO, chunking and API response contracts. Personal project references were generalized for publication.

The estimates remain illustrative and Region/runtime-dependent. ShelfLife's component arithmetic is reconciled to $15.30; total listed core estimates are $61.80 and all modules total $76.80. These are not quotes or hard spending caps. Track gross usage, net bill and eligible remaining credit separately.

The new exam exercises can add chargeable resources and runtime beyond those original estimates, particularly ECS task count, WAF, EFS, Kinesis, a database replica and ElastiCache. Review current regional prices and the remaining budget before each exercise; delete short-lived resources in its cleanup step. Worksheet prices must not be used as AWS price quotes.

## What validation means

Run the offline regressions with Python 3 and Node.js:

```bash
python3 handbooks/aws-saa-c03/tests/test_resources.py
```

The tests execute embedded Python examples with controlled external-service boundaries, including FreshTrack's Decimal quantity write, parse the full manual JavaScript, validate progress records, and check all diagram node bounds and connector endpoints. Repository DOM tests cover handbook filtering and reachable review progress. They make no AWS requests.

No lab was deployed as part of this revision. The manual includes file-writing starter scripts and guided Console/CLI runbooks; advanced handoffs still contain implementation excerpts. Offline execution of a starter script proves file generation, not successful AWS deployment. Before spending, complete the permission and resource-manifest review, exercise failure cases, and verify teardown in the actual account. Locked or intentionally retained resources must be recorded with cost and expiry.

Full browser/mobile interaction and print output were not verified in the editing environment because local browser access was blocked. JavaScript/source checks and selected static SVG rendering do not establish those broader behaviors. Do a local browser pass before relying on those controls during study.

Visible metadata includes edition, review dates and source references. No hidden provenance was intentionally added. The files are independent study aids, not AWS publications, exam dumps or guarantees of exam coverage/pass results.
