# Interview preparation

**Status:** Draft for owner review · **Last reviewed:** 5 October 2026

Start with the role you are interviewing for, choose relevant evidence, then add the vacancy context. The same career facts support different questions; the actual title, dates and results do not change with the role perspective.

## Choose your route

| Interview role | Main guide | Main decisions to demonstrate |
| --- | --- | --- |
| Delivery Lead | [Delivery Lead](roles/delivery-lead.md) | Delivery health, recovery, commercial choices, suppliers and leadership |
| Agile Delivery Lead | [Agile Delivery Lead](roles/agile-delivery-lead.md) | Flow, coaching, facilitation, cross-team dependencies and improvement |
| Product Owner | [Product Owner](roles/product-owner.md) | Product goals, backlog ordering, user evidence, acceptance and value |
| Product Manager | [Product Manager](roles/product-manager.md) | Discovery, strategy, segments, roadmaps, experiments and economics |
| Senior Project Manager | [Senior Project Manager](roles/senior-project-manager.md) | Business case, scope, schedule, budget, governance and benefits |

Read the [shared handbook](shared/handbook.md) for answer structures and tools. Select examples from the [evidence bank](shared/evidence-bank.md). The [Accenture Product Owner supplement](vacancies/accenture-product-owner.md) adds the supplied vacancy's requirements.

For question practice, start with [STAR and PEARL](shared/handbook.md#behavioural-answers), [question-type selection](shared/handbook.md#choose-the-question-type) and the [scenario answering sequence](shared/handbook.md#scenario-answers). Each role guide adds two scenario drills with follow-up probes and weak-answer traps; the Accenture supplement adds two consulting cases. These supplement the existing worked scenarios. Scenario preparation is relevant, but this collection does not claim that most interviews use scenarios or that their frequency has recently increased.

The [Accenture model question-and-answer bank](vacancies/accenture-product-owner-questions.md) adds researched question origins, 29 model answers, three personal-story scaffolds and follow-up probes. Its research register distinguishes reports, suggestions and vacancy-derived predictions.

[Open the tabbed reading view](handbook.html). It is generated from these Markdown files; edit the sources, then run `python3 scripts/render_interview_handbook.py` from the repository root.

## Prepare in three passes

1. **Match:** identify the five strongest requirements in the advert; match each to a story and a decision you actually made.
2. **Explain:** rehearse a 90-second answer; prepare the artefact, measurement and alternative for follow-up questions.
3. **Challenge:** practise a recovery or prioritisation scenario, a setback and a credibility probe. Ask what the panel could challenge in your wording.

If only two hours remain, spend 20 minutes decoding the advert, 50 minutes on three stories, 25 minutes on a scenario, 15 minutes on motivation and questions, and 10 minutes checking logistics.

## Ownership and maintenance

- Framework definitions belong in the shared handbook; role guides explain their use in context.
- Historical facts and headline metrics belong in the evidence bank. Role guides link to them rather than maintaining another version of the results.
- Vacancy supplements contain employer-specific motivation, advert mapping and interview questions. Refresh those facts before another application.
- Review dates describe this editorial review, not independent verification of employer accounting or operational data.
- Use stable paths and Git history. Replace an existing guide when improving it; do not add another dated copy.
- Keep private interview feedback, contact details, eligibility information and confidential employer material outside this public collection.

## Check a rendered update

Run `python3 scripts/render_interview_handbook.py --check` and the repository content checks. With Playwright and Chromium installed, run `node tests/interview-browser-smoke.cjs` to check route headings, cross-guide links, themes, mobile layout, print and the no-JavaScript fallback. A custom browser path can be supplied with `INTERVIEW_CHROMIUM_EXECUTABLE`.

## Connect to the existing knowledge base

Technical preparation remains in the [architecture curriculum](../learning-paths/software-architect/software-architect-curriculum-guide-v3.md), [connected project guides](../learning-paths/software-architect/connected-learning/README.md) and [AI/ML Interview Resource Accelerator](../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.4.html). Choose the depth the role requires. A delivery interview needs the consequence of a technical decision; an architecture interview may require defending the design itself.
