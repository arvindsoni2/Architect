# October Handbook Freshness Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement the approved updates inline.

**Goal:** Apply the six approved freshness updates and reconcile the affected catalogue metadata in one reviewable PR.

**Architecture:** Preserve the standalone HTML learning experiences and stable Markdown paths. Replace versioned publications, update dependent links and validation paths, and use Git history for previous editions.

**Tech Stack:** HTML, embedded JavaScript, Markdown, Python/Node validation, Playwright.

**Spec:** The owner's approved 5 October 2026 freshness audit; implementation evidence is recorded in [the review note](../../handbook-freshness-review-2026-10-05.md).

## Global constraints

- Work from the current `main` snapshot, on a separate review branch; open a PR without merging.
- Agent Manual v2.8; AI Engineering v3.2; FDE v1.4; Interview Accelerator v4.4; AWS lab v2.2.
- Keep certification roadmap path stable and retain the owner's $170 credit / $100 soft limit / $70 reserve scenario.
- Preserve existing lesson IDs, progress storage keys and sound architectural guidance.
- Date source snapshots; distinguish focused freshness checks from original lesson or exam-content reviews.
- Do not change substantive interview-prep draft content or unrelated handbook content; update their navigation links when required by renamed editions.

## Review focus

- Renames must leave catalogue entries, cross-guide links, validator fixtures and browser tests reachable.
- Sonnet cost arithmetic must match the published base rates and sequential optimization assumptions.
- Provider limits and prices are dated evidence, not permanent defaults or automatic migration recommendations.
- AWS new-account offers must not imply the owner's existing credit entitlement or universally free deployments.
- Old lesson review dates must remain visible when the whole lesson was not re-reviewed.

### Task 1: Recheck evidence and update AI publications

- [x] Read repository conventions and verify the local snapshot against upstream Git blob hashes.
- [x] Replace Claude snapshots and Sonnet cost arithmetic in the Agent Manual and AI Engineering handbook.
- [x] Replace legacy Evals learning references with current evaluation practice and an explicit retirement notice.
- [x] Adopt the dedicated OWASP 2026 resource in the four affected publications; revise the interview threat exercise.
- [x] Replace the expired OpenAI vacancy anchor with stable careers discovery and retain dated role examples.

### Task 2: Certification and AWS updates

- [x] Describe the MLA English beta as active; remove the unsupported GA estimate and disclose the official exam-code discrepancy.
- [x] Align Amazon Quick / Quick Sight and Amazon Data Firehose naming.
- [x] Clarify Free/Paid plans and account-specific eligibility; retain illustrative costs and the $170 scenario.

### Task 3: Integrate editions and metadata

- [x] Rename the five HTML publications, update all active links and existing validation/test paths, and retain progress keys.
- [x] Reconcile System Design and Agent review metadata, AWS visual edition and catalogue dates.
- [x] Record source links, review scope and verification results in the review note.

### Task 4: Verify and publish

- [x] Run the catalogue validator, Python suites, Node suites and generated interview-view check.
- [x] Run browser smoke checks and inspect desktop/mobile and print output for the edited HTML.
- [x] Review the complete diff, sensitive-content changes, internal navigation and whitespace.
- [ ] Publish a single commit on the review branch, verify the remote diff and open the PR.
