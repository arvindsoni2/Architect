# Focused Architecture Notes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish four focused, cross-source Markdown notes that explain durable inference, reasoning, model adaptation, and self-improving-agent architecture without converting their source courses or handbooks.

**Architecture:** Give each note one canonical ownership boundary, connect it to the existing production-assurance, reliability, workflow, and decision-method notes with relative links, and expose the four notes through grouped root navigation and the authoritative catalogue. Deliver the branch as an unmerged review-only pull request.

**Tech Stack:** Git, Markdown, Mermaid, rg, sed, wc, sort, POSIX shell, and Python 3 for deterministic Markdown structure, catalogue, and local-link checks.

**Spec:** docs/superpowers/specs/2026-09-06-focused-architecture-notes-design.md

## Global Constraints

- Work only on docs/focused-architecture-notes in the isolated worktree based on merged origin/main at 59cf1fef630bb98d8aff1b08d44e6b3c9450bd3a.
- Create exactly these four stable paths: docs/ai-architecture/llm-inference-systems.md, docs/ai-architecture/reasoning-system-design.md, docs/ai-architecture/model-adaptation-and-training.md, and docs/agent-architecture/self-improving-agent-systems.md.
- Use original cross-source synthesis; do not import complete course notebooks, book chapters, lecture notes, certification packs, page images, copied exercises, copied diagrams, or long quotations.
- Preserve all existing handbooks, learning paths, canonical notes, the approved design, and the unrelated ai-engineering-handbook-v3.0.html source artifact unchanged.
- Keep each note approximately 1,100–1,600 words and use the ten required top-level sections in the approved order.
- Apply Pareto prioritisation, first-principles explanation, and Feynman teach-back questions. Use one or two compact Mermaid diagrams only where topology or sequence is materially clearer than prose.
- Give every concept one canonical home. Link to existing notes for production acceptance, reliability/failure control, durable workflows/idempotency, and architecture decisions instead of redefining them.
- Date or qualify volatile product, API, benchmark, and research claims; remove claims that cannot be verified usefully.
- Keep provenance visible through contributing repository links, concise public primary references, Current status, Living edition, and review date 2026-09-06. Include no private Library URLs, prompts, hidden identifiers, credentials, or unsupported personal examples.
- The approved change spans eight paths: the design specification, this plan, four focused notes, README.md, and CATALOG.md. This final review-fix pass edits only the four notes and this plan; make exactly the requested local review-fix commit, and do not push, merge, or open a pull request.
- The eventual pull request is review-only and must remain unmerged for the repository owner.

---

## File map

| Path | Responsibility |
| --- | --- |
| docs/ai-architecture/llm-inference-systems.md | Canonical model for prefill/decode, memory state, serving capacity, scheduling, latency, throughput, and inference cost. |
| docs/ai-architecture/reasoning-system-design.md | Canonical model for inference-time reasoning work, candidate generation, verification, selection, adaptive budgets, and bounded stopping. |
| docs/ai-architecture/model-adaptation-and-training.md | Canonical guide for prompts/harnesses versus weight changes, SFT, distillation, verifiable rewards, experiment lineage, and rollback. |
| docs/agent-architecture/self-improving-agent-systems.md | Canonical model for bounded improvement loops, evidence, memory/configuration changes, promotion gates, human authority, and rollback. |
| README.md | Group the focused notes, point Agent architecture at docs/agent-architecture/, and retain direct Agent Engineering Master Manual access. |
| CATALOG.md | Add four Current/Living rows dated 2026-09-06, remove completed Later migrations, and retain the scope exclusion sentence. |
| docs/superpowers/specs/2026-09-06-focused-architecture-notes-design.md | Approved design and ownership contract; read-only input. |

Every note uses this exact section order:

    # Note title
    ## Purpose and scope
    ## Pareto summary
    ## First-principles model
    ## Core decisions and trade-offs
    ## Failure modes and warning signs
    ## Practical decision checklist
    ## Worked architecture scenario
    ## Feynman questions
    ## Related canonical notes
    ## Sources and review status

Each Sources and review status section ends with:

    **Status:** Current

    **Edition:** Living

    **Last reviewed:** 2026-09-06

### Task 1: Publish LLM Inference Systems

Files:
- Create: docs/ai-architecture/llm-inference-systems.md

Interfaces:
- Consumes: CS336 Handwritten Visual Notebook, AI Engineering Handbook v3.0, Agent Engineering Master Manual v2.7, The AI Architect's Handbook v1.2, and the approved design.
- Produces: canonical serving-capacity vocabulary; later notes link to inference latency/cost but do not redefine prefill/decode or KV pressure.

- [ ] Step 1: Confirm branch/base and inspect concurrent work.

    git branch --show-current
    git rev-parse 59cf1fef630bb98d8aff1b08d44e6b3c9450bd3a
    if test -e docs/ai-architecture/llm-inference-systems.md; then sed -n '1,220p' docs/ai-architecture/llm-inference-systems.md; else echo 'target absent; create it'; fi

Expected: branch/base resolve. If a concurrent draft exists, review it against the next steps and patch only verified gaps; never overwrite unrelated work.

- [ ] Step 2: Extract mechanisms before drafting.

Review the design section and search sources for prefill, decode, KV cache, batching, throughput, tail latency, queue, memory bandwidth, GPU, cost, and capacity. Record governing conditions, not product prescriptions. The note must link the four repository artifacts and public primary references where claims require them.

- [ ] Step 3: Create the note with apply_patch.

Write approximately 1,100–1,600 words and all ten sections. Cover: the request → queue → prefill → KV state → iterative decode flow; weights/cache/buffers/runtime overhead; compute versus memory bandwidth; static/dynamic/continuous batching; concurrency, saturation, fairness; TTFT, inter-token latency, throughput, cache pressure, and accepted-outcome cost; conditional optimisation levers; warning signs; an evidence-oriented checklist; and the worked endpoint scenario where throughput rises while tail latency, queue time, and KV pressure become unacceptable. Link to Production AI Assurance, Reliability and Failure Control, Architecture Decision Method, and Model Adaptation and Training without restating their definitions.

- [ ] Step 4: Validate the contract.

    note=docs/ai-architecture/llm-inference-systems.md
    test -f "$note"
    test "$(rg -c '^# LLM Inference Systems$' "$note")" -eq 1
    wc -w "$note"
    git diff --check -- "$note"

Run a Python check that each required heading occurs once and in order, the word count is 1,100–1,600, and each status marker occurs once. Check all local source links and confirm no private URL or copied source navigation appears.

### Task 2: Publish Reasoning System Design

Files:
- Create: docs/ai-architecture/reasoning-system-design.md

Interfaces:
- Consumes: reasoning-model visual guide/public companion, CS329A Self-Improving AI Agents notes, Agent Engineering Master Manual v2.7, Production AI Assurance, and Task 1's inference-cost vocabulary.
- Produces: canonical inference-time reasoning model; SFT, distillation, RL, weight changes, and rollout gates remain delegated.

- [ ] Step 1: Confirm branch/base and inspect the target without clobbering concurrent work.

Use Task 1's branch/base commands with docs/ai-architecture/reasoning-system-design.md substituted.

- [ ] Step 2: Extract mechanisms before drafting.

Search the design and sources for test-time compute, width, depth, selection, verifier, majority, best-of-N, search, critique, self-refinement, adaptive budget, stopping, correlated errors, and evaluator exploitation.

- [ ] Step 3: Create the note with apply_patch.

Write 1,100–1,600 words and all ten sections. Define reasoning as multi-step inference rather than proof; model parser, normaliser, generator, verifier, scorer, and judge roles; show adaptive width/depth/selection and stopping; cover majority voting, best-of-N, search, critique, self-refinement, deterministic tools, bounded workflows, cost/latency, and correlated errors; include the mixed-request routing scenario; and link explicitly to LLM Inference Systems, Model Adaptation and Training, Production AI Assurance, and Architecture Decision Method.

- [ ] Step 4: Validate heading order, size, status block, ownership links, provenance, and git diff --check. Confirm the note does not imply longer traces guarantee correctness.

### Task 3: Publish Model Adaptation and Training

Files:
- Create: docs/ai-architecture/model-adaptation-and-training.md

Interfaces:
- Consumes: reasoning-model visual guide/public companion, CS329A notes, CS336 notebook, AI Engineering Handbook v3.0, Production AI Assurance, and the ownership table.
- Produces: canonical conceptual guide for changing behaviour through data, SFT, distillation, and verifiable rewards; inference-time search stays in Task 2.

- [ ] Step 1: Confirm branch/base and inspect the target without clobbering concurrent work.

Use Task 1's commands with docs/ai-architecture/model-adaptation-and-training.md substituted.

- [ ] Step 2: Extract mechanisms before drafting.

Search for prompt, harness, retrieval, tool, data curation, contamination, train/evaluation separation, SFT, distillation, verifiable reward, group-relative optimisation, reward hacking, capability collapse, lineage, reproducibility, and rollback. Do not derive gradients, optimizer internals, distributed-training recipes, or framework code.

- [ ] Step 3: Create the note with apply_patch.

Write 1,100–1,600 words and all ten sections. Explain the prompt/harness/retrieval/tool/weight decision; curation and contamination; SFT as imitation; distillation as capability/cost transfer with possible loss; conceptual RL with verifiable or group-relative rewards; parser/verifier integrity; experiment lineage and staged rollback; and the code-repair scenario comparing a better harness, reviewed-example SFT, verified-trajectory distillation, and test-reward RL. Link to Reasoning System Design, Production AI Assurance, Architecture Decision Method, and Self-Improving Agent Systems.

- [ ] Step 4: Validate heading order, size, status block, ownership links, safe provenance, absence of training-framework tutorial material, and git diff --check.

### Task 4: Publish Self-Improving Agent Systems

Files:
- Create: docs/agent-architecture/self-improving-agent-systems.md

Interfaces:
- Consumes: CS329A notes, Agent Engineering Master Manual v2.7, The AI Architect's Handbook v1.2, FDE Handbook v1.3, Production AI Assurance, Durable Workflows and Idempotency, and the approved design.
- Produces: canonical bounded-improvement model; workflow durability, overload mechanics, and production acceptance remain owned by existing notes.

- [ ] Step 1: Confirm branch/base and inspect the target without clobbering concurrent work.

Use Task 1's commands with docs/agent-architecture/self-improving-agent-systems.md substituted.

- [ ] Step 2: Extract mechanisms before drafting.

Search for generate, execute, score, filter, learn, retest, memory, trajectory, synthetic data, verifier, human judgment, sandbox, promotion, canary, rollback, kill, reward hacking, drift, distribution shift, runaway, and self-confirming.

- [ ] Step 3: Create the note with apply_patch.

Write 1,100–1,600 words and all ten sections. Explain generate → execute → score → filter → learn → retest inside an isolated evaluation boundary; separate test-time search, configuration, memory, and weight changes; cover evidence quality, verifier coverage, trajectory lineage, memory admission/expiry, autonomy proportional to verifiability/reversibility/consequence, sandboxing, approval, canary, kill controls, and rollback; include the support-agent proposal scenario; and explicitly avoid claiming open-ended autonomous self-modification is production-ready. Link to Durable Workflows and Idempotency, Reliability and Failure Control, Production AI Assurance, Model Adaptation and Training, and Architecture Decision Method.

- [ ] Step 4: Validate the contract, trust-boundary links, unsafe-claim scan, and git diff --check.

### Task 5: Update README navigation

Files:
- Modify: README.md

Interfaces:
- Consumes: all four approved note paths and existing maintainable notes.
- Produces: grouped direct navigation, docs/agent-architecture/ as the Agent architecture domain, and direct Master Manual access.

- [ ] Step 1: Replace only the Maintainable notes and Domains blocks with apply_patch.

Preserve the description, Start here links, existing canonical notes, and scope sentence. Group Maintainable notes as:

    ## Maintainable notes
    ### Software architecture
    - [Architecture Decision Method](docs/software-architecture/architecture-decision-method.md)
    ### System design
    - [Reliability and Failure Control](docs/system-design/reliability-and-failure-control.md)
    ### Cross-cutting patterns
    - [Durable Workflows and Idempotency](docs/cross-cutting-patterns/durable-workflows-and-idempotency.md)
    ### AI architecture
    - [Production AI Assurance](docs/ai-architecture/production-ai-assurance.md)
    - [LLM Inference Systems](docs/ai-architecture/llm-inference-systems.md)
    - [Reasoning System Design](docs/ai-architecture/reasoning-system-design.md)
    - [Model Adaptation and Training](docs/ai-architecture/model-adaptation-and-training.md)
    ### Agent architecture
    - [Self-Improving Agent Systems](docs/agent-architecture/self-improving-agent-systems.md)
    - [Agent Engineering Master Manual](handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html)

Replace the Agent architecture domain item with:

    - [Agent architecture](docs/agent-architecture/)

- [ ] Step 2: Validate direct links and whitespace.

    for path in docs/ai-architecture/llm-inference-systems.md docs/ai-architecture/reasoning-system-design.md docs/ai-architecture/model-adaptation-and-training.md docs/agent-architecture/self-improving-agent-systems.md; do rg -Fq "]($path)" README.md; done
    rg -Fq '](docs/agent-architecture/)' README.md
    rg -Fq '](handbooks/agent-engineering/agent-engineering-master-manual-v2.7.html)' README.md
    test "$(rg -c '^## Maintainable notes$' README.md)" -eq 1
    git diff --check -- README.md

If a note is not yet present because another worker is creating it, retain the link and rerun existence checks after that note is published.

### Task 6: Update CATALOG

Files:
- Modify: CATALOG.md

Interfaces:
- Consumes: four stable note paths and all existing rows/status definitions.
- Produces: exactly sixteen unique rows and an accurate remaining-migrations state.

- [ ] Step 1: Append the exact rows with apply_patch and remove completed Later migrations.

Leave every existing handbook/note row and status definition unchanged, then append:

    | LLM Inference Systems | AI architecture | [docs/ai-architecture/llm-inference-systems.md](docs/ai-architecture/llm-inference-systems.md) | Markdown | Current | Living | 2026-09-06 |
    | Reasoning System Design | AI architecture | [docs/ai-architecture/reasoning-system-design.md](docs/ai-architecture/reasoning-system-design.md) | Markdown | Current | Living | 2026-09-06 |
    | Model Adaptation and Training | AI architecture | [docs/ai-architecture/model-adaptation-and-training.md](docs/ai-architecture/model-adaptation-and-training.md) | Markdown | Current | Living | 2026-09-06 |
    | Self-Improving Agent Systems | Agent architecture | [docs/agent-architecture/self-improving-agent-systems.md](docs/agent-architecture/self-improving-agent-systems.md) | Markdown | Current | Living | 2026-09-06 |

Delete the Later migrations heading and candidate text. After the unchanged status definitions, retain exactly:

    > Repository scope: Complete course notebooks and certification packs are not repository artifacts.

- [ ] Step 2: Validate row count, metadata, uniqueness, and concurrent path state.

    python3 - <<'PY'
    from pathlib import Path
    import re
    text = Path('CATALOG.md').read_text(encoding='utf-8')
    rows = [line for line in text.splitlines() if line.startswith('| ') and not line.startswith('| ---') and not line.startswith('| Title |')]
    assert len(rows) == 16, len(rows)
    required = {'LLM Inference Systems', 'Reasoning System Design', 'Model Adaptation and Training', 'Self-Improving Agent Systems'}
    for title in required:
        matches = [row for row in rows if row.startswith('| ' + title + ' |')]
        assert len(matches) == 1
        assert '| Markdown | Current | Living | 2026-09-06 |' in matches[0]
    paths = re.findall(r'\]\(([^)#]+)', text)
    assert len(paths) == len(set(paths)), 'duplicate catalogue paths'
    assert '## Later migrations' not in text
    assert text.count('Complete course notebooks and certification packs are not repository artifacts.') == 1
    allowed = {
        'docs/ai-architecture/llm-inference-systems.md',
        'docs/ai-architecture/reasoning-system-design.md',
        'docs/ai-architecture/model-adaptation-and-training.md',
        'docs/agent-architecture/self-improving-agent-systems.md',
    }
    missing = [path for path in paths if not Path(path).exists()]
    assert set(missing) <= allowed, missing
    print('catalogue rows:', len(rows), 'unique paths:', len(paths), 'pending:', len(missing))
    PY
    git diff --check -- CATALOG.md

The missing-path allowance is exact and temporary; once all note tasks finish, rerun with missing equal to an empty list.

### Task 7: Integrated validation, immutability, and delivery preparation

Files: Verify README.md, CATALOG.md, the four notes, and existing source artifacts; modify none during validation.

- [ ] Step 1: Validate all four note contracts.

For each note, assert all ten headings occur once and in order, word count is 1,100–1,600, and the three status markers occur once. Require all four files to exist at this stage.

- [ ] Step 2: Resolve local links.

Parse Markdown links in README.md, CATALOG.md, and the four notes; resolve relative targets from each source; skip only http://, https://, mailto:, and fragment-only links; fail on any missing path. Rerun after concurrent note creation and print local links: PASS.

- [ ] Step 3: Check ownership and public safety.

Confirm detailed definitions are only in their owner note and other notes link or apply them. Scan changed Markdown for credentials, private URLs, conversation/tool identifiers, HTML comments, copied source navigation, certification-pack imports, and claims that autonomous self-modification is inherently safe.

- [ ] Step 4: Verify existing artifacts remain unchanged.

    git diff --exit-code 59cf1fef630bb98d8aff1b08d44e6b3c9450bd3a -- handbooks learning-paths docs/software-architecture docs/system-design docs/cross-cutting-patterns

Expected: exit 0. The unrelated HTML modification in another checkout is outside this worktree and must not be touched.

- [ ] Step 5: Run final scope and whitespace checks.

    git diff --check
    git status --short
    git diff --name-only 59cf1fef630bb98d8aff1b08d44e6b3c9450bd3a

Read the output before claiming completion. Only the four focused notes, this plan, README.md, and CATALOG.md may be changed.

### Task 8: Independent review and review-only pull request

- [ ] Step 1: Review the complete diff against the approved design for ownership, source coverage, provenance, section contracts, note size, Mermaid readability, navigation, catalogue metadata, path uniqueness, and source immutability.

- [ ] Step 2: Apply only verified findings with apply_patch, then rerun every Task 7 check.

- [ ] Step 3: After owner authorisation, push docs/focused-architecture-notes without force and open a pull request titled docs: add focused architecture notes against main. Summarise the four notes, grouped navigation, sixteen catalogue rows, validation evidence, and the visible-provenance/scope constraints.

- [ ] Step 4: Stop before merge. Report the pull request link, four note paths, exact row count, resolved-path result, unchanged-source result, and git diff --check output.
