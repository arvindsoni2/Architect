# Accenture FDE Preparation Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for the focused documentation tasks below; request one independent review before opening the PR.

**Goal:** Close the agreed FDE preparation gaps against vacancy R00345109 while preserving the latest handbook revisions.

**Architecture:** Keep transferable engineering and leadership guidance in FDE Handbook v1.4. Add one canonical Markdown vacancy supplement to the existing interview collection and register it in the generated reading view. Link to existing methods, evidence and technical resources instead of duplicating them.

**Tech Stack:** Markdown, standalone HTML, existing standard-library Python renderer and validator, existing Playwright smoke checks.

**Spec:** The approved inspection recommendations are captured in the scope below. This is a bounded editorial change, not a new application or renderer design.

**Recommended model:** GPT-6.1, medium reasoning for implementation; high reasoning for evidence and final review.

## Approved scope and latest baseline

The owner approved the targeted supplement and requested a review PR on 5 October 2026. Baseline main is `43a69c1f6b9d3dd57d3c01d72ab780ad27975fa3`: FDE v1.4 and Interview Resource Accelerator v4.4. Its OWASP 2026, current vacancy-discovery links and existing technical caveats remain intact. v1.4 still lacks the vacancy supplement, people-management drills, programme commercial case, provider practical and Frontier Academy update.

## Global constraints

- Keep the v1.4 path stable and reconcile its stale v1.3 footer; distinguish the September research cut from this focused October revision.
- Preserve existing sections, links, security guidance and readiness scores. Add a separate experience classification rather than inventing a hiring score.
- Mark all new interview questions as inferred practice and numerical cases as synthetic. Do not claim a verified interview format.
- Reuse the public-safe evidence bank without adding personal history or treating a simulation as client delivery.
- Keep employer qualifications separate from learning exercises. Flag unestablished coding ownership and line-management evidence.
- Retain Markdown as the supplement's canonical source; regenerate the HTML reading view.
- No credentials, private recruitment details, hidden provenance, paid deployment or changes to application code.
- Open a PR; do not merge it.

## Review focus

1. A simulated capstone must not imply qualifying client deployment; inspect the handbook readiness note and supplement evidence matrix.
2. A missing provider capability or residency constraint must prevent unsafe fallback; inspect the lab's expected failure outcomes.
3. Time released must not be presented as cash savings; independently recalculate the synthetic case including recurring costs and sensitivity.
4. The new route and cross-guide fragments must work in the generated view, mobile, print and no-JavaScript mode; extend the existing smoke check.
5. Prior v1.4 changes and source dates must survive; inspect the diff and dated source notes.

## Task 1: Transferable handbook additions

**File:** `handbooks/fde/fde-handbook-v1.4.html`.

- [x] Add a provider-contract practical: capability matrix, two real adapters plus an optional mocked third, policy-constrained routing, usage normalization and unknown-outcome tests.
- [x] Add programme and people-lead guidance with concrete decisions and observable evidence.
- [x] Add a CFO-facing investment worksheet and link to the worked synthetic case.
- [x] Distinguish study, simulation, internal production and client-embedded evidence alongside the existing scorecard.
- [x] Link STAR/PEARL and existing accelerator topics; add checked Google and Frontier Academy sources with access boundaries.
- [x] Verify anchors, latest security content, source dates and edition labels.

## Task 2: Vacancy supplement and reading route

**Create:** `interview-prep/vacancies/accenture-fde.md`.
**Modify:** `interview-prep/README.md`, `scripts/render_interview_handbook.py`, `tests/interview-browser-smoke.cjs`, `CATALOG.md`.
**Regenerate:** `interview-prep/handbook.html`.

- [x] Write a concise dated vacancy summary, requirement-to-learning map and truthful evidence matrix.
- [x] Add scenario questions with model reasoning, follow-up probes and weak-answer traps, including people leadership, engineering depth, provider failure and reusable assets.
- [x] Include a worked commercial/capacity case with calculations, uncertainty and staged roadmap.
- [x] Add a self-review rubric and focused preparation route; keep rubric separate from employer scoring.
- [x] Register the supplement as `accenture-fde`; extend route, fragment, mobile, print and no-JavaScript verification to eleven panels.
- [x] Update the catalogue and regenerate the reading view.

## Task 3: Validate and open review PR

- [x] Run repository validation, renderer consistency, repository Python tests and AWS tests required by CONTRIBUTING.md.
- [ ] Run browser/visual verification: local run blocked by unavailable Chromium and a network-denied download; PR browser CI will exercise the reading view. Visual screenshot review remains required before merge.
- [x] Check whitespace, public-safe content, arithmetic, anchors and the complete diff against this plan.
- [x] Obtain independent review: no material content or integration findings.
- [ ] Publish the branch and open the PR with verification evidence.

## Execution notes

- Baseline repository validation and renderer consistency passed before edits.
- A fresh checkout on the branch `docs/accenture-fde-preparation` isolates the work from other edits. The user already authorised the plan and PR; no additional approval gate is introduced.
- Existing validation covers the renderer. This change only registers content, so no new renderer implementation or mirrored unit tests are needed.
- Validation adjustment: Chromium is absent locally and its download was denied by the network allowlist. Local visual/browser verification is therefore unconfirmed. Register the existing interview smoke check in the existing GitHub browser workflow, with matching path filters, so PR checks cover the new reading route. This uses the repository's existing browser dependency and runner configuration.

## Verification record

Repository validator, generated-view consistency, whitespace and JavaScript syntax checks passed. The required repository Python suite passed 30 tests; the AWS suite passed 16. Independent review verified the source claims, preservation of v1.4 edits, local links/fragments, unique IDs and all synthetic calculations. No candidate eligibility, actual interview format, historical whole-corpus freshness or visual-layout approval is implied.
