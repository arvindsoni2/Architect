# AWS SAA-C03 study pair

To connect these labs to an end-to-end solution and interview explanations, use the [patient portal connected-learning case](../../learning-paths/software-architect/patient-portal-connected-learning.md). It maps the current lab display numbers and titles to architecture decisions and evidence.

Owner-approved repository exception, 7 September 2026. These two resources are maintained as a pair; the exception does not admit other certification packs or course notebooks.

- [Visual Handbook — v2026.10.08.2](saa-c03-visual-handbook-2026.09.html)
- [The $170 Cloud Lab Manual — v2.2](saa-c03-lab-manual-v2.2.html)

Download the HTML files and open them locally for their navigation and interactive features; GitHub's source viewer does not run them. The lab manual stores progress in browser-local storage. Its export/import feature transfers status, recorded costs and evidence ticks, not AWS account data. The print-all control prepares every lab and tab for printing.

## Revision scope

The follow-up adds a user-paced, four-stage classic RDS Multi-AZ DB instance walkthrough: healthy replication, primary failure, standby promotion, then endpoint/client recovery. Optional path motion is off by default, stops when system reduced motion is enabled and has replay controls. The same explanation works without animation and prints all stages. SVG and browser-native animation keep the handbook self-contained.

The 8 October visual-handbook revision adds Cram/Core/Deep reading layers, red/amber/green confidence with a weak-card filter, 11 SVG study figures with component inspectors and selected failure probes, five walkable decision trees, a phrase trainer, table-derived flashcards and an 80-service cram glossary. Every tracked card has a summary of at most 25 words. Four printable one-hour domain sheets, a day-before checklist, safe mnemonics and a scoped stable-number sheet support revision. The lab manual is unchanged.

Section 40 now contains 65 original domain-tagged questions; section 42 runs shuffled question/option order, a two-minute-per-question session timer, exact-set scoring for multiple responses, per-domain results and a saved wrong/unanswered pile. Practice is instructional, not a calibrated pass predictor. Confidence is explicitly self-assessed; old reading ticks migrate to amber rather than being treated as mastery. Browser-local state stores confidence and wrong-question IDs only. Malformed or unavailable storage falls back safely.

Added diagrams and number-sheet facts were checked against linked AWS primary documentation on 8 October. This is a focused verification of additions, not a claim to have re-audited every existing service table. The IAM map branches by grant/principal context and includes applicable RCP/SCP gates. RDS instance/cluster/replica, Aurora storage versus compute, and SNS delivery versus SQS processing failures are kept distinct. Lambda's 15-minute value is scoped to standard functions and notes current Managed Instances exceptions.

The 5 October 2026 v2.2 freshness update aligns Amazon Quick / Quick Sight and Amazon Data Firehose naming and makes account-plan, trial and credit assumptions explicit. The owner-specific $170 credit scenario, $100 soft limit and $70 reserve remain; the public new-customer offer is not a substitute for the balance/expiry shown in Billing. The original 21 September exam-content check remains separately dated. The catalogue also reconciles the visual handbook to its existing v2026.09.25.1 edition.


The 21 September exam-readiness update maps all 14 exam tasks to the actual handbook sections and lab IDs. The core labs now include an **Exam route** with practical checks for policy denial, DynamoDB queries and consistency, container recovery/scaling, stream replay, shared storage, read replicas and stale caches. Cross-account, hybrid migration and cost exercises explicitly distinguish modeled decisions from deployed and tested evidence. A skipped deployment remains a practical gap.

The September handbook update added 18 expandable mechanism/decision explanations, a deeper DynamoDB explanation, four worked cost worksheets with fictional prices, and active-recall prompts. Its original 20-question assessment is preserved and expanded to 65 in the October revision, with distractor explanations and domain tags. Use unfamiliar official practice resources after working through it.

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

The tests execute embedded Python examples with controlled external-service boundaries, including FreshTrack's Decimal quantity write, parse the full manual JavaScript, validate progress records, and check all diagram node bounds and connector endpoints. Repository DOM tests cover handbook filtering, confidence and restored print state. They make no AWS requests.

No lab was deployed as part of this revision. The manual includes file-writing starter scripts and guided Console/CLI runbooks; advanced handoffs still contain implementation excerpts. Offline execution of a starter script proves file generation, not successful AWS deployment. Before spending, complete the permission and resource-manifest review, exercise failure cases, and verify teardown in the actual account. Locked or intentionally retained resources must be recorded with cost and expiry.

The October visual-handbook revision has Chromium coverage for reading layers, confidence persistence/filtering, diagrams and failure probes, decision walks, quiz interaction, flashcards, phrase recall, malformed/blocked storage, narrow-screen overflow and print visibility. Run `node handbooks/aws-saa-c03/tests/revision-browser.cjs` with Playwright and Chromium installed; CI runs this alongside the existing handbook browser checks. The earlier lab-manual deployment and verification boundaries remain unchanged.

Visible metadata includes edition, review dates and source references. No hidden provenance was intentionally added. The files are independent study aids, not AWS publications, exam dumps or guarantees of exam coverage/pass results.
