# Interview preparation

**Status:** Draft for owner review · **Last reviewed:** 13 October 2026

Start with the role you are interviewing for, choose relevant evidence, then add the vacancy context. The same career facts support different questions; the actual title, dates and results do not change with the role perspective.

## Choose your route

| Interview role | Main guide | Main decisions to demonstrate |
| --- | --- | --- |
| Delivery Lead | [Delivery Lead](roles/delivery-lead.md) | Delivery health, recovery, commercial choices, suppliers and leadership |
| Agile Delivery Lead | [Agile Delivery Lead](roles/agile-delivery-lead.md) | Flow, coaching, facilitation, cross-team dependencies and improvement |
| Product Owner | [Product Owner](roles/product-owner.md) | Product goals, backlog ordering, user evidence, acceptance and value |
| Product Manager | [Product Manager](roles/product-manager.md) | Discovery, strategy, segments, roadmaps, experiments and economics |
| Senior Project Manager | [Senior Project Manager](roles/senior-project-manager.md) | Business case, scope, schedule, budget, governance and benefits |
| Software or AI Architect | [Software & AI Architect](roles/software-ai-architect.md) | Requirements before technology, trade-offs, failure modes, AI governance and cost |
| AI Engineer | [AI Engineer](roles/ai-engineer.md) | Retrieval, agents and tools, evaluation, cost and latency, with your public projects |
| Forward Deployed Engineer | [Forward Deployed Engineer](roles/forward-deployed-engineer.md) | Decomposition, customer conversations, practical coding and production design |

Read the [shared handbook](shared/handbook.md) for answer structures and tools. Select examples from the [evidence bank](shared/evidence-bank.md). For the Accenture Product Owner (Associate Manager) interview, start with the [Accenture PO playbook](vacancies/accenture-product-owner.md): a night-before page, cost and scenario methods, 15 spoken answers and six scenario drills.

For opening and motivation practice, use [Present → Past → Future and Company → Role → Fit](shared/handbook.md#opening-and-motivation-answers). For question practice, start with [STAR and PEARL](shared/handbook.md#behavioural-answers), [question-type selection](shared/handbook.md#choose-the-question-type) and the [scenario answering sequence](shared/handbook.md#scenario-answers). Each delivery and product role guide adds two scenario drills with follow-up probes and weak-answer traps; the Accenture playbook adds six, using one five-step scenario method. The architect, AI engineer and FDE guides, and the 2026 question banks in the Product Owner and Senior Project Manager guides, give spoken model answers built from the evidence bank, with dated public sources for each question set.

The [Accenture extra questions page](vacancies/accenture-product-owner-questions.md) holds short answers to depth and quick-fire questions (Scrum, SAFe, API-first, cloud, AI risk, consulting situations) and the research register.

For engineering interviews, start with the [AI Engineer](roles/ai-engineer.md) or [Forward Deployed Engineer](roles/forward-deployed-engineer.md) guide; for the Accenture vacancy add the [Accenture Forward Deployed AI Engineer supplement](vacancies/accenture-fde.md) alongside the [FDE Handbook v1.5](../handbooks/fde/fde-handbook-v1.5.html). It maps vacancy R00345109 to evidence, adds eleven inferred technical/leadership drills and a synthetic programme/commercial case, and distinguishes practice from qualifying client deployment.

## Read the guides as HTML

Every guide has its own HTML page next to its Markdown file, and `index.html` is this page. Open [index.html](index.html) and use the left-hand menu to move between guides; [handbook.html](handbook.html) holds every guide in one tabbed page.

On the guide pages, **Practice mode** hides the model answers so you can answer out loud first; **Show model answer** reveals one at a time, **▶ Listen** reads a question and answer aloud in British English, and **Practised** ticks are remembered in your browser. Dark view and Print work on every page; your theme choice carries across guide pages and the tabbed view (it starts from your system setting), and print always shows the answers.

GitHub shows HTML files as source code. To read them as pages, download the repository (Code → Download ZIP) and open `interview-prep/index.html` in a browser, or use a static-file viewer such as `https://raw.githack.com/arvindsoni2/Architect/main/interview-prep/index.html`.

The HTML is generated from these Markdown files: edit the Markdown, then run `python3 scripts/render_interview_handbook.py` from the repository root.

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

Run `python3 scripts/render_interview_handbook.py --check` and the repository content checks. With Playwright and Chromium installed, run `node tests/interview-browser-smoke.cjs` to check route headings, cross-guide links, themes, mobile layout, print, the no-JavaScript fallback and, on every guide page, anchors, phone layout and practice mode. A custom browser path can be supplied with `INTERVIEW_CHROMIUM_EXECUTABLE`.

## Connect to the existing knowledge base

Technical preparation remains in the [architecture curriculum](../learning-paths/software-architect/software-architect-curriculum-guide-v3.md), [connected project guides](../learning-paths/software-architect/connected-learning/README.md) and [AI/ML Interview Resource Accelerator](../learning-paths/ai-ml-interview/interview-resource-accelerator-v4.4.html). Choose the depth the role requires. A delivery interview needs the consequence of a technical decision; an architecture interview may require defending the design itself.
