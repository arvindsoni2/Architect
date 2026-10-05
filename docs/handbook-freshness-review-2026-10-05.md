# Handbook freshness review — 5 October 2026

The owner approved the six updates identified by the quarterly freshness audit. This revision changes dated vendor, security, role and certification guidance and reconciles publication metadata. It preserves architectural principles and existing learning-progress identifiers. Original lesson and exam-content review dates remain distinguishable from this freshness check.

| Publication | Result |
| --- | --- |
| Agent Engineering Master Manual | v2.8: current Claude IDs/base prices, recalculated Sonnet example, Evals retirement warning and OWASP 2026 references |
| AI Engineering Handbook | v3.2: current Claude selection/cost snapshot and OWASP 2026 learning resource |
| Forward Deployed AI Engineer Handbook | v1.4: OWASP 2026 and stable careers discovery alongside dated role evidence |
| Interview Resource Accelerator | v4.4: OWASP 2026 anchor and edition-specific threat-table exercise |
| Architecture and Applied AI Certification Roadmap | Living update: active English MLA beta and unresolved official exam-code discrepancy |
| The $170 Cloud Lab Manual | v2.2: current naming and account-plan/credit assumptions |

System Design retains v5; its original content review and this freshness review are separately labelled. The AWS visual handbook retains v2026.09.25.1; the catalogue now matches its visible edition. Unaffected publications retain their editions and prior full-review dates. The interview-prep draft collection receives navigation-link updates only; its substantive content and Draft status remain.

## Primary-source evidence

All links below were checked on **5 October 2026**.

- [Anthropic model overview](https://platform.claude.com/docs/en/models/overview) and [API pricing](https://platform.claude.com/docs/en/about-claude/pricing): current model IDs and base token rates. Model promotion still requires task-specific quality, latency, cost and safety evaluation.
- [OpenAI API deprecations](https://developers.openai.com/api/docs/deprecations): legacy Evals deprecation announced 3 June 2026; read-only 31 October; dashboard/API shutdown scheduled 30 November. [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) supplies reusable evaluation guidance; it does not establish a new managed-platform replacement.
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/), published 3 August 2026: use this edition's risk names and identifiers. The older `/llm-top-10/` route is a 2025 archive.
- [OpenAI careers](https://openai.com/careers/), [Anthropic careers](https://www.anthropic.com/careers), [Anthropic FDE example](https://job-boards.greenhouse.io/anthropic/jobs/5391016008) and [Technical Deployment Lead example](https://job-boards.greenhouse.io/anthropic/jobs/5391108008): stable discovery links complement dated vacancies. The former London Applied AI Engineer URL now redirects to general careers search and no longer supports a vacancy-specific assertion.
- [AWS Machine Learning Engineer Associate page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/): English beta delivery began 29 September 2026; English MLA-C01 ended 28 September. GA dates remain TBD. Its headings identify MLA-C02 while its exam-code table displays ME1-C02; verify the booking record before scheduling rather than silently treating either display as authoritative.
- [AWS Free Tier](https://aws.amazon.com/free/): current new-customer offer and Free/Paid plan boundaries. These do not establish the owner's remaining credit, expiry or eligible services.
- [Amazon Quick documentation](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html): Quick Sight is the BI feature within Amazon Quick; existing QuickSight APIs/SDKs/integrations continue to work. [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) supplies current stream-delivery naming; CLI/API namespaces are retained.

## Validation scope

The catalogue validator and generated interview-view check pass. All **54 Python tests** and **14 Node tests** pass. Chromium smoke checks pass for navigation, print visibility, storage fallback, export and reset; focused desktop/mobile checks cover the five updated publications, including lab naming, budget assumptions, preserved storage namespaces and print-all output. Selected screenshots and affected print pages were visually inspected. An independent review found no functional regressions; its date-scope and edition-label findings were corrected. Long source URLs in the FDE register now wrap on narrow screens. Offline code checks do not establish successful AWS deployment or account eligibility. Source checks cover the approved findings and new links; they are not a claim that every outbound handbook URL was exhaustively checked.
