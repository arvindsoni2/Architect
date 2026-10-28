# Connect the dots

**Status:** Owner-approved · **Last reviewed:** 28 October 2026

Many interviews include questions that connect a story to the system behind it and to who decided what. A Product Owner panel once asked: “On the timesheet project, how did you handle the AWS architecture, what did you decide and what did the architect decide, and how did you present it to the ARB?” This page is the method for answering that kind of question. The [decision lists](decision-ledger.md) apply it to every story in the [evidence bank](evidence-bank.md), [Architecture review](architecture-review.md) covers governance boards, and the [dot drill](../dot-drill.html) lets you practise.

## One question, three layers

A boundary question cuts through three layers at once and scores how smoothly you move between them.

| Layer | What it covers | Where it lives |
| --- | --- | --- |
| Story | What happened, for whom, and what changed | The [evidence bank](evidence-bank.md) |
| System | What it ran on and where it could break | The handbooks, linked from each story's “One level down” |
| Decision rights | Who decided each thing, what you decided and how you influenced the rest | The [decision lists](decision-ledger.md) |

A Product Owner panel isn't asking you to be the architect. It's checking three things: that you understand the architecture well enough to make good product calls, that you know exactly where your authority stopped, and that you can work inside governance without being slowed by it. The weak answer either overclaims the architecture or retreats with “that was the architect's job”.

## Five beats for any boundary question

STAR still works for behavioural questions. Boundary questions need a different spine, because the panel wants the split of decisions and a picture of the system, not just a sequence of events. Each beat starts with an English keyword you can anchor on.

| Beat | What to say | Time |
| --- | --- | --- |
| Stakes | One line on what was at risk and for whom. Lead with stakes, not setup. | About 10 seconds |
| Split | Which decisions were yours and which belonged to the architect, engineering or the client. Name the owners. | About 15 seconds |
| Sketch | The system in three boxes and the one risky arrow. Say it as if you were drawing it. | About 15 seconds |
| Shape | How your decisions shaped the technical ones: requirements, risk ordering, rollout. This is where you claim the decisions you made. | About 30 seconds |
| Show | The governance moment and the result: the review, the conditions, the number and what it measured. | About 20 seconds |

Frameworks to name inside the beats, two or three per answer: RACI or decision rights (Split), the C4 context and container views (Sketch), non-functional requirements and the AWS Well-Architected pillars (Shape), an ADR and the review board's conditions (Show).

## The same story, four levels deep

You don't need different stories for different roles. You need to know which level each role expects you to start on: a delivery interview needs the consequence of a technical decision, and an architecture interview needs the defence of the design.

| Level | What you say | Smart Timesheet at this level |
| --- | --- | --- |
| 1 · Outcome | What changed and how it was measured | Around £500k a year; half the admin office visits |
| 2 · Decision | Options, the trade-off, who decided | An alpha at one depot before scaling; TCS chose the platform |
| 3 · Mechanism | Components, data flow, failure modes, quality needs | App → .NET → Oracle; only three fields leave Northern Powergrid; offline-first on the phone |
| 4 · Build and proof | Code, tests, evaluation, operations | You weren't at this level on S3. Use Hatch or IncidentPilot |

**The rule:** start at your role's level. Go one level down to prove you understand the mechanism, and one level up to show business sense. Go two levels down only where you actually did the work, and say so.

## Where each role starts

| Role | Starting level | How to answer |
| --- | --- | --- |
| Product Owner | 2 · Decision | Start with the decision, the trade-off and who owned it. Go one level down to show you understood the mechanism. |
| Product Manager | 2 · Decision | Start with the decision and keep the business case in view: segment, economics, and why this bet over others. |
| Delivery Lead | 1 · Outcome | Start with the consequence, the risk and the plan. Then show the decision behind it. |
| Architect | 3 · Mechanism | Start with constraints, options, the trade-off and failure modes. Say who signed off. |
| AI Engineer | 4 · Build and proof | Start with how it works and how you measured it. Use a personal project for code-level detail. |
| FDE | 4 · Build and proof | Start with the customer's problem, then what you built and how it was adopted. |

## Pair a work story with a personal project

Your work stories are strong on decisions, users and value. Your personal projects are strong on architecture, cost, AI and governance, because you made every decision yourself. Use a work story for the why and a personal project for the how. In a Product Owner interview, Smart Timesheet carries the answer on its own. In an architect or AI engineer interview, add: “and where I make these calls myself, in Hatch…”. Always say “personal project” when you use one.

## Story and lens grid

Strong means the story answers the lens on its own; usable means it works with care; thin means pair it with a stronger story.

| Story | Decisions | Architecture | Cloud and cost | Data and AI | Governance | Users | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 GenAI orders | strong | usable | usable | strong | usable | strong | usable |
| S2 SaaS launch | strong | usable | strong | thin | usable | strong | strong |
| S3 Smart Timesheet | strong | usable | usable | usable | strong | strong | strong |
| S4 Infrastructure | usable | strong | strong | thin | strong | usable | strong |
| S5 Nationwide GDPR | strong | thin | thin | usable | strong | thin | usable |
| S7 Agile and Jira | strong | usable | usable | thin | usable | usable | strong |
| S8 Hatch | strong | strong | strong | strong | strong | usable | thin |
| S9 IncidentPilot | strong | strong | usable | strong | strong | thin | thin |
| S10 ResearchOps | strong | strong | strong | strong | usable | thin | thin |

## Lens prompts

Each lens has one question a panel tends to ask. Replace “this story” with the story's name.

| Lens | Question |
| --- | --- |
| Decisions | In this story, which decisions were yours, which belonged to someone else, and how did you influence the ones that weren't yours? |
| Architecture | Sketch the system in this story in three boxes. Which arrow carried the most risk, and what did you do about it? |
| Cloud and cost | In this story, what did the solution cost to build and to run, and which design choice drove that cost? |
| Data and AI | In this story, where did data or a model make a decision, and how did you know it was good enough? |
| Governance | In this story, who had to approve the work, what did they challenge, and which condition did you carry afterwards? |
| Users | In this story, who were the users, what did you learn from them that changed the design, and how did you measure adoption? |
| Value | In this story, how was the value calculated, and what would a finance director challenge in that number? |

## Practise

Open the [dot drill](../dot-drill.html), pick a role, choose a story and a lens, and answer out loud in 90 seconds using the five beats. Each role guide also ends with bridge questions built from the [decision lists](decision-ledger.md).
