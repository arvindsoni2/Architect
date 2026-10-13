# Repository review — 13 October 2026

A whole-repository review of accuracy, recency and quality, eight days after the [5 October freshness review](handbook-freshness-review-2026-10-05.md). It corrects drift since then and records recommendations that were not applied.

## What was checked

| Check | Result |
| --- | --- |
| Catalogue and local links (`validate_repository.py`) | Pass |
| Generated interview reading view | Matches Markdown sources |
| Python tests (repository, AWS, programme) | Pass (54) |
| Node tests (storage, programme) | Pass |
| Internal anchors and local links in all 11 HTML files | 0 broken |
| Spot-checks of technical claims | Little's Law, quorum caveats, exactly-once boundaries, cache sensitivity arithmetic and SAA-C03 domain weights (30/26/24/20) are correct |
| Time-sensitive vendor, framework and standards claims | Four items out of date; corrected below |

## Corrections applied

| Publication | Change |
| --- | --- |
| Agent Engineering Master Manual v2.8 | Claude Haiku 5.5 replaces Haiku 4.5 in the model snapshot and routing example; the example now totals about $577/month (78.6% reduction) instead of $1,119; LangGraph 1.2.14; OWASP 2026 name "improper output handling" |
| AI Engineering Handbook v3.2 | Claude Haiku 5.5 (ID, 1M/128K context, tiered pricing); LangGraph 1.2.14 in all three places |
| AI Evaluation Field Guide | OWASP reference moved from the 2025 to the 2026 LLM Top 10 |
| Catalogue | Review dates updated for refreshed files and for interview files edited on 13 October; the grooming programme now shows its visible page title too |
| Accenture PO playbook | Private recruitment feedback removed from public text, per `CONTRIBUTING.md` |

Editions and filenames were kept (v2.8, v3.2) and dated data-check notes were added, because a version bump would rename files and update links and test paths in about 15 places for a data-only change.

## Recommendations not applied

- **Process records in `docs/superpowers/`.** About 130 KB of agent implementation plans and design specs are uncatalogued and are process records rather than knowledge. Move them to a labelled maintenance area or out of the public knowledge base.
- **Filename drift.** `saa-c03-visual-handbook-2026.09.html` now carries edition v2026.10.08.2. Keep the filename (links and saved progress depend on it) but avoid dates in future filenames.
- **Outbound links.** About 430 external links were not exhaustively checked in this review; only the sources below were verified.
- **Git history.** The removed recruitment feedback remains in the public history of commit `88177d3`. Removing it from history would require a force-push to `main`; that is the owner's decision.

## Addendum — AI Architect's Handbook v1.2 full review

The handbook was last fully reviewed on 4 September 2026 and missed the 5 October pass, so it was reviewed end to end on 13 October: front matter, Chapters 0–13 and Appendices A–E. The architecture content, case studies and citations held up; corrections were limited to time-sensitive statements and small wording faults.

| Area | Change |
| --- | --- |
| Figures | The 11 PNG figures are now inline SVG that follow the light and dark themes and carry a title and description for screen readers. The file shrank from about 2.4 MB to 1.1 MB. |
| Freshness Register | Redated to 13 October 2026. OpenAI Evals dates confirmed (read-only 31 October, shutdown 30 November 2026) with an export prompt. The EU AI Act row now names Regulation (EU) 2026/1744 and records the simplified AI-literacy duty, the new non-consensual intimate imagery prohibition and the reported Article 50 marking transition. The NIST row notes the AI RMF revision under the AI Action Plan and the April 2026 critical-infrastructure profile concept note. MCP 2026-07-28, OpenTelemetry GenAI (Development) and ICO "under review" were confirmed unchanged. |
| Chapter 4 | Platform freshness note re-verified. |
| Chapter 9 | EU AI Act landscape redated and aligned with the AI Omnibus; AI-literacy paragraph notes the simplification. |
| Chapter 11 | ICO status redated; "privacy- engineering" conversion artefact fixed. |
| Chapter 1 | "Insecure output handling" renamed "improper output handling" (current OWASP naming). |
| Front matter | "Jev and Laya" now explained as typed decision models; edition line and date updated. |

The Article 50 marking transition comes from secondary analyses; the handbook says so and asks readers to confirm it in the official text.

## Primary sources checked on 13 October 2026

- [Anthropic models overview](https://platform.claude.com/docs/en/about-claude/models/overview) and [pricing](https://platform.claude.com/docs/en/about-claude/pricing): Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5; Haiku 5.5 at $0.10/$0.50 per million tokens for prompts up to 100K tokens and $0.50/$2.50 above.
- [LangGraph on PyPI](https://pypi.org/project/langgraph/): 1.2.14, released 6 October 2026.
- [MCP specification](https://modelcontextprotocol.io/specification/latest): 2026-07-28 remains the latest revision.
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/): published 3 August 2026.
- [AWS SAA-C03](https://aws.amazon.com/certification/certified-solutions-architect-associate/): still the current exam; no successor announced.
- [AWS MLA exam page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/): beta delivery from 29 September 2026; GA dates still TBD; the roadmap's code-discrepancy caution still applies.
- [European Commission: AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) and [Regulation (EU) 2026/1744 on EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744): in force 27 July 2026; Annex III high-risk from 2 December 2027, Annex I products from 2 August 2028.
- [OpenAI Evals guide](https://developers.openai.com/api/docs/guides/evals): read-only 31 October 2026, shutdown 30 November 2026.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework): 1.0 under revision; critical-infrastructure profile concept note, 7 April 2026.
- [ICO guidance on AI and data protection](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/): still marked under review because of the Data (Use and Access) Act.
- [Scrum Guide](https://scrumguides.org/scrum-guide.html): the 2020 edition remains the current official version.
