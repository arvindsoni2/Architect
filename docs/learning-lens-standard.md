# Learning Lens Standard

**Status:** Current · **Introduced:** 21 October 2026 · **Applies to:** HTML handbooks and learning paths

The learning lens is a small, repeatable layer that helps a reader turn a handbook chapter into something they can explain and use. It adds four things to the existing content: first principles, a Pareto cut, a visual, and a Feynman loop. It never replaces the chapter. It sits in front of it, inside it and after it.

## 1. The four lenses

| Lens | Question it answers | Where it goes |
| --- | --- | --- |
| **First principles** | What problem does this exist to solve, and which truths would still hold with different tools? | Top of the unit |
| **Pareto** | What is the 20% to learn now, and what can wait for a second pass? | Top of the unit, after first principles |
| **Visual** | Can I see the mechanism, one numbered arrow at a time? | After the concept text |
| **Feynman loop** | Can I redraw it, explain it without jargon, find my gaps and check myself? | End of the unit |

## 2. Block rules

### First principles

- One sentence naming the problem the concept exists to solve.
- Two to four irreducible truths, each paired with a "so what" for the design.
- A truth must survive a change of technology. If it names a product, it belongs in the body, not here.
- Optionally tag what it acts on (compute, data, communication) or which spine truths it builds on.

### Pareto

- At most **three** "learn now" items. If you need more, the unit is two units.
- A defer list that says when to come back ("after chapter 11", "when a role asks for it").
- A handbook may also mark a core path (for example the System Design "Core path only" toggle). Dim non-core content; never hide it.

### Visual

- One main diagram per unit with no more than about nine boxes.
- Arrows are numbered in the order things happen; the numbered list under the diagram says what each arrow means.
- Colour encodes role, the same way in every handbook:

| Role | Colour | Use for |
| --- | --- | --- |
| client | blue | users, callers, requests |
| compute | green | services, workers, processing steps |
| data | amber | stores, records, evidence |
| async | violet | queues, streams, events |
| model | pink | model calls and AI components |
| control | teal | policy, validation, gates, approvals |
| risk | red | failure, rejection, untrusted input |
| external | grey, dashed | third parties and results |

- Dashed arrows mean replies, asynchronous paths or stop paths; the legend says which.
- The diagram must work without JavaScript and in print: all arrows and steps are visible at rest. *Next step*, *Back* and *Show all* only add highlighting.
- Inline SVG with `role="img"`, `aria-label`, `<title>` and `<desc>`. Colours come from the page's tokens so both themes work. The SVG keeps a 600 px minimum width inside its own scrolling frame, so the page never scrolls sideways on a phone.
- An existing figure can serve as the unit's visual: mark it with `data-lens-block="visual"`.

### Feynman loop

- **Blank page:** redraw the unit's diagram from memory; tie it to the unit's exercise or whiteboard challenge where one exists.
- **Explain it to a junior:** one concrete prompt with three banned jargon words.
- **Gap hunt:** each gap points to the exact part to reread.
- **Model answer:** hidden in a `<details>` until the reader has tried; written in plain words.
- Prompts are written for each unit. The validator rejects identical Feynman blocks in one file.
- Sections that are not full units (FDE and Evaluation guide sections, Grooming units) may use the single-prompt *explain it back* form: one prompt, banned words, hidden model answer.

### Watch links

Link to a verified lesson page (for example a numbered Mark Richards lesson) or to a search within a verified creator channel. Never invent a video ID or a URL you have not opened.

## 3. Markup

Every block carries `data-lens-block` with one of `fp`, `pareto`, `visual` or `feynman`. A unit is marked with `data-lens-unit`:

- `data-lens-unit=""` on the element that contains the whole unit (for example an `<article>` chapter);
- `data-lens-unit="until-next"` on the first block of a unit in a flat, heading-based document. The unit then runs until the next unit starts.

```html
<article class="chapter" data-lens-unit="" id="c05">
  <section class="lens-block lens-fp" data-lens-block="fp">…problem + truths table…</section>
  <section class="lens-block lens-pareto" data-lens-block="pareto">
    <ul class="lens-learn"><li>…</li><li>…</li><li>…</li></ul>
    <ul class="lens-defer"><li>…</li></ul>
  </section>
  …existing concept text…
  <figure class="lens-block lens-visual" data-lens-block="visual" data-steps="9" id="c05-lens">
    <div class="lens-controls" hidden>…Back · Next step · Show all…</div>
    <svg class="lens-svg" role="img" aria-label="…" aria-labelledby="c05-lens-t c05-lens-d">…</svg>
    <ol class="lens-steps"><li>…</li></ol>
  </figure>
  <section class="lens-block lens-feynman" data-lens-block="feynman">…loop + model answer…</section>
</article>
```

Each handbook carries one copy of the lens stylesheet and the small step-through script, mapped onto its own colour tokens (`--lens-ink`, `--lens-muted`, `--lens-line`, `--lens-surface`, `--lens-surface2`). The script opens model answers and sketches before printing. Handbooks stay single, offline files.

## 4. Validation

`scripts/validate_repository.py` checks every HTML file that uses the lens:

- each `data-lens-unit` contains all four blocks;
- no Pareto `lens-learn` list has more than three items;
- no two Feynman blocks in a file have identical text;
- every `lens-svg` diagram has `role="img"`, a `<title>` and a `<desc>`;
- `data-lens-block` uses only the four known values.

`tests/handbook-browser-smoke.cjs` steps through the first diagram on each audited page, toggles the System Design core path, checks that printing opens every model answer, and asserts there is no horizontal scroll at 390 px.

## 5. Where it is applied

| Handbook | Units | What it carries |
| --- | --- | --- |
| System Design Concept Handbook v6 | 18 concept chapters | Opening first-principles page, core-path toggle, all four blocks per chapter, 15 new step-through diagrams, reference sketches for 8 labs and 11 cases |
| AI Architect's Handbook v1.3 | 14 chapters (`until-next`) | AI first-principles spine, chapter on a page, 7 new step-through diagrams, Feynman loop before Key Takeaways |
| Software Architect Grooming Programme v6 | 10 units | First principles and Pareto per unit, recall check per unit, free video curriculum in Pareto order |
| FDE Handbook v1.6 | Sections | What the role reduces to, core path, 4 diagrams, 17 explain-it-back prompts |
| AI Evaluation Field Guide | Sections | Principle spine, minimum viable evaluation, 2 diagrams, 15 explain-it-back prompts |
| AI Engineering Handbook v3.3 | Weeks | Why-this-works block per week, 3 new diagrams |
| Agent Engineering Master Manual v2.9 | 49 lessons | A first-principles truths table per lesson |
| AWS SAA-C03 Visual Handbook | Decision lens | First-principles opener tied to the decision trees |
| PM & Product Field Guide v1 | 2 tracks (project, product) plus the Evaluation section | First principles and Pareto per track, 3 step-through diagrams, 2 Feynman loops and 1 explain-it-back prompt |
