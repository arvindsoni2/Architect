# AWS SAA-C03 study pair

Owner-approved repository exception, 7 September 2026. These two resources are maintained as a pair; the exception does not admit other certification packs or course notebooks.

- [Visual Handbook — v2026.09.07.1](saa-c03-visual-handbook-2026.09.html)
- [The $170 Cloud Lab Manual — v2.1](saa-c03-lab-manual-v2.1.html)

Download the HTML files and open them locally for their navigation and interactive features; GitHub's source viewer does not run them. The lab manual stores progress in browser-local storage. Its export/import feature transfers status, recorded costs and evidence ticks, not AWS account data. The print-all control prepares every lab and tab for printing.

## Revision scope

The September revision corrects RI capacity scope, NAT availability modes, API types, SQS limits, DynamoDB expiry, and service-availability caveats. It adds worked decisions and a 14-task exam coverage map, repairs misleading topology, and improves SVG connector endpoints and canvas bounds.

Lab corrections include OIDC environment subjects, Identity Center prerequisites, gross-cost budgets, database-backed recovery probes, atomic inventory/outbox processing, version-aware cleanup, CloudFront failover conditions, key-specific encryption policy, deployment ordering, data-fixture comparisons, per-store RPO, chunking and API response contracts. Personal project references were generalized for publication.

The estimates remain illustrative and Region/runtime-dependent. ShelfLife's component arithmetic is reconciled to $15.30; total listed core estimates are $61.80 and all modules total $76.80. These are not quotes or hard spending caps. Track gross usage, net bill and eligible remaining credit separately.

## What validation means

Run the offline regressions with Python 3 and Node.js:

```bash
python3 handbooks/aws-saa-c03/tests/test_resources.py
```

The tests execute the original embedded Python examples with controlled external-service boundaries, parse the full manual JavaScript, validate progress records, and check all diagram node bounds and connector endpoints. They make no AWS requests. Selected diagrams are also inspected through passive SVG rendering.

No lab was deployed as part of this editorial revision. The HTML contains implementation excerpts and handoffs, not a prebuilt, end-to-end-tested IaC/application repository. Before spending, implement the referenced files, complete the permission and resource-manifest review, exercise failure cases, and verify teardown in the actual account. Locked or intentionally retained resources must be recorded with cost and expiry.

Full browser/mobile interaction and print output were not verified in the editing environment because local browser access was blocked. JavaScript/source checks and selected static SVG rendering do not establish those broader behaviors. Do a local browser pass before relying on those controls during study.

Visible metadata includes edition, review dates and source references. No hidden provenance was intentionally added. The files are independent study aids, not AWS publications, exam dumps or guarantees of exam coverage/pass results.
