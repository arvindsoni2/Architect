# AI Engineer interview guide

**Status:** Draft for owner review · **Last reviewed:** 13 October 2026 · **Sources checked:** 13 October 2026

AI engineer interviews in 2026 test whether you can **build on foundation models** — retrieval, tools and agents, evaluation, cost and latency — rather than train them. Panels reward a working system with numbers more than definitions. Your position: a delivery and product leader who now builds hands-on, with one production AI rollout and three public projects. Say that plainly; do not present personal projects as employed engineering experience.

## What the 2026 loop looks like

Reported loops share five kinds of round. Confirm the actual format with the recruiter; these are patterns from public guides, not a promise. [1][2][3]

| Round | Typical prompt | What scores well |
| --- | --- | --- |
| Technical screen | "You have a 200-page PDF and a question. What happens between enter and the answer?" | Every stage named, chunk size and top-k justified, knowing when retrieval is the wrong tool |
| Take-home | "Here are 50 Markdown docs. Build Q&A, a 20-question eval set, and report recall@5 and faithfulness." | A working system plus numbers; a judge checked against human labels |
| Live coding or debugging | "This agent loops forever on some inputs. Find out why and fix it." | Tracing the failing step, capping calls and cost, replaying fixed cases |
| System design | "Design a support assistant. How do you know it is helping and not making things worse?" | Evaluation and serving designed around a model you do not control |
| Product sense | "A customer says the bot feels dumb. What do you change first?" | Turning a vague complaint into a measurable, prioritised fix |

Many teams now allow AI coding assistants in live rounds and judge how you direct, check and override them. [2] Expect lighter algorithm questions than a classic software loop, and a practical build instead. [3]

## Positioning and evidence

**Model opening (about 90 seconds):** "I'm a delivery and product leader who now builds AI systems hands-on. At Natoora I led the rollout of a GPT-4o-mini order-automation workflow in London and Paris that cut manual order-entry effort by about 90%, with exceptions routed to people. Since then I've built three open-source projects. IncidentPilot is an incident-triage agent where deterministic rules stay in control and the model only ranks evidence-grounded hypotheses. Hatch is a multi-agent job-search workspace on LangGraph that never takes an external action without me. ResearchOps ranks research items with mostly deterministic scoring and keeps model spend to pennies a day. The common thread is controls around the model, an evaluation that can say no, and cost as a design constraint."

| What the panel tests | Best evidence | What to show |
| --- | --- | --- |
| Agents with safe tool boundaries | [S9 IncidentPilot](../shared/evidence-bank.md#s9-incidentpilot--personal-open-source-project) | Read-only MVP, model with no tools, rules-only fallback |
| Evaluation that drives decisions | [S8 Hatch](../shared/evidence-bank.md#s8-hatch--personal-open-source-project) | Hard gates; the baseline was retained when no challenger passed |
| Cost and grounding by design | [S10 ResearchOps v2](../shared/evidence-bank.md#s10-researchops-v2--personal-open-source-project) | Deterministic sub-scores, narrow model role, hard cost caps |
| Production rollout and exceptions | [S1 order automation](../shared/evidence-bank.md#s1-genai-order-automation) | Pilot scope, exception handling, measured manual effort |
| Learning | [Credentials and learning](../shared/evidence-bank.md#credentials-and-learning) | GeeksforGeeks Generative AI & Agentic AI course, AWS AI Practitioner, plus what you built with it |

## Fundamentals

Model answers are written in your voice from the evidence bank. Where one describes a habit rather than a recorded fact, keep only what you actually do.


### Q1. A user asks a question about a 200-page PDF. What happens between enter and the answer?

**Model answer:** "Two phases. Offline, I parse the PDF keeping its structure, split it into chunks along sections with a little overlap, embed each chunk and also index it for keyword search, storing page and section metadata. At query time I may rewrite the question, run hybrid retrieval, rerank the top candidates and pass only the best few chunks, with IDs, into a prompt that tells the model to answer from them and cite them. I check the citations point at real chunks before returning, and I stream the answer. Most latency is the generated tokens, not reading the prompt. If the question needs a live number, such as an account balance, retrieval is the wrong tool and I call an API instead."

### Q2. Is a bigger context window always better?

**Model answer:** "No. A longer prompt costs more, takes longer to process, and models use information in the middle of long contexts less reliably. I retrieve less but better, put the most relevant evidence first, and measure answer quality as I change top-k rather than assuming more context helps." [4]

### Q3. What does temperature change, and when do you set it to zero?

**Model answer:** "It reshapes the probability distribution the next token is sampled from: higher spreads it out, lower sharpens it. I use low or zero for extraction and tool calls, but zero is not a determinism guarantee, so I still validate output against a schema and retry on failure. Reliability comes from schemas, validators and evaluation, not from the sampling setting."

### Q4. Why is generating the answer slower than reading the prompt?

**Model answer:** "The prompt is processed in parallel in one prefill pass; the output is produced one token at a time, each step reading the cached keys and values of everything before it. So time to first token mostly tracks prompt length, and total time mostly tracks output length. That is why shorter outputs, streaming and prefix caching matter."

### Q5. When would you fine-tune instead of improving the prompt or adding retrieval?

**Model answer:** "Last, and only with evidence. I start with prompt structure and examples, measured on an evaluation set. If the gap is knowledge that changes or must be cited, that is retrieval. Fine-tuning fits stable behaviour the prompt cannot reliably produce — a strict format, a narrow classification — or moving a proven task to a smaller, cheaper model. It adds a data pipeline, versioning and a rollback path, so it has to beat the cheaper options on the same evaluation set."

### Q6. Your embedding search returns results that look related but are not what the user meant. What is happening?

**Model answer:** "Similarity is not relevance. Embeddings capture topic, so a question about cancelling an order can match an article about placing one, and they are weak on exact identifiers like error codes. I'd measure recall on a small labelled set first, then try hybrid search with keyword matching, a reranker, metadata filters and better chunk boundaries before paying to swap the embedding model."

## Retrieval

### Q7. How do you choose a chunk size?

**Model answer:** "From the documents and the questions, not a default. Small chunks are precise but lose context; large ones dilute the signal and cost tokens. I split on document structure — headings, sections, table rows — test two or three sizes against retrieval recall and answer quality on real questions, and keep parent-section metadata so I can expand context when needed."

### Q8. Why hybrid search and a reranker?

**Model answer:** "Keyword search catches exact terms and identifiers; vector search catches paraphrases. Combining them, usually with reciprocal rank fusion, improves recall. A cross-encoder reranker then scores each query–passage pair more accurately but is too slow for the whole corpus, so I retrieve broadly, rerank, and keep the top few."

### Q9. What happens when the documents do not answer the question?

**Model answer:** "The system should say so. I set a relevance threshold, tell the model it may answer 'I don't know', and log the unanswered question so the content owner can fill the gap. In evaluation I include unanswerable questions and score a confident wrong answer as worse than an honest abstention."

### Q10. How do you keep the index fresh and permission-safe?

**Model answer:** "Incremental ingestion keyed on content hashes, so changed documents are re-embedded and deleted ones are removed — deletes are the step teams forget. I store access-control metadata on every chunk and filter before anything reaches the model; the prompt is never the permission boundary. If I change embedding model, I re-embed everything and re-run the retrieval evaluation."

### Q11. How does agentic RAG differ from a single retrieval pass?

**Model answer:** "The model decides whether the evidence is enough and, if not, searches again with a better query, which helps multi-part questions. It costs latency, tokens and loop logic, so I cap iterations and keep it only for the question types where evaluation shows it beats a fixed pipeline."

## Agents and tools

### Q12. How does tool calling actually work?

**Model answer:** "I describe each tool with a schema. The model returns a structured request — a tool name and arguments — instead of prose. My code validates the arguments, checks permissions, runs the tool and appends the result to the conversation. The model never executes anything itself; every safety control lives in that code."

### Q13. When would you not use an agent?

**Model answer:** "When the steps are known in advance, a fixed workflow is cheaper, faster and easier to test. In IncidentPilot I used deterministic rules for the diagnosis that can be known, and gave the model one narrow job — ranking hypotheses from validated evidence — with no tools at all. If the model times out, the rules-only diagnosis still works."

### Q14. An agent loops forever on some inputs. How do you find and fix it?

**Model answer:** "I open the trace for a failing run and find the step that repeats. Common causes are a tool error the agent cannot see because it was swallowed, an ambiguous tool result, or no stop condition. I fix the cause — return a structured error, tighten the tool description, add an explicit 'done' state — and add guards: a maximum number of steps and tokens, a timeout, detection of the same call with the same arguments, and a partial result instead of silence. Then I replay the failing inputs as fixed test cases before shipping."

### Q15. How do you make tools safe to give an agent?

**Model answer:** "Least privilege, an allow-list of actions, arguments validated on the server, idempotency keys on anything that writes, and human confirmation for anything irreversible or expensive. Hatch is a good example: it prepares CV packs and tracks applications, but it never submits an application — a person always does that step."

### Q16. What is MCP, and how is it different from function calling?

**Model answer:** "Function calling is a model API feature: your application describes tools and handles the calls. MCP is an open protocol for exposing tools, resources and prompts from a server so that any compatible host can use them without a bespoke integration. The current specification, 2026-07-28, makes requests stateless and adds server discovery. MCP standardises the connection; it does not decide who may call a tool or whether a call is safe — authorisation and approval remain my job." [5]

### Q17. How do you build an agent that runs for days?

**Model answer:** "Keep state outside the conversation: a durable store with checkpoints, so a crash or restart resumes rather than repeats. Make external actions idempotent, because a checkpoint does not prove a side effect did not already happen. Hatch uses LangGraph with a SQLite checkpointer for this. Add human approval points and an expiry for stale approvals."

### Q18. When are multiple agents worth it?

**Model answer:** "When the work splits into parts that genuinely need different instructions, tools or models, or an independent check. In Hatch, Scout, Scorer, Tailor and Coach do different jobs with different context, and a human review sits between tailoring and applying. If one agent with good tools meets the target, more agents just add coordination cost and new failure modes."

## Evaluation

### Q19. How do you know your AI feature is good — not your gut, your number?

**Model answer:** "I define the task and what good means with the people who own it, build a labelled evaluation set from real cases including hard and unanswerable ones, and grade with deterministic checks first and a calibrated judge only where meaning needs interpretation. I set pass thresholds from the cost of failure and look at results by slice, not just the average. In IncidentPilot an evaluation passes only if all ten checks pass, including that the right cause ranked first and that no action was executed."

### Q20. How do you know a prompt change made the whole product better, not just one example?

**Model answer:** "Run the versioned evaluation set before and after, compare per-slice results and inspect the cases that changed, then gate the change in CI so a regression blocks the merge. After release I watch online signals such as escalations and user corrections. One improved example is an anecdote."

### Q21. When do you trust an LLM as a judge?

**Model answer:** "After checking it. I label a representative sample myself or with a domain expert, measure agreement, look at where the judge and humans disagree, and re-check after any model or rubric change. I use deterministic checks — schema, exact match, citation exists — wherever they can answer the question, because they do not drift."

### Q22. How do you evaluate a RAG system?

**Model answer:** "Separately for retrieval and generation, so I know which layer failed. Retrieval: recall@k and precision on labelled question–passage pairs. Generation: faithfulness to the retrieved text, answer relevance and citation validity. End to end: task success on real questions, including ones the corpus cannot answer."

### Q23. How do you evaluate an agent?

**Model answer:** "Task success on fixed scenarios with known end states, checked by inspecting the resulting state rather than the agent's description of it. Then the trajectory — tool choice, wasted steps, loops — and cost per task. Agents vary run to run, so I repeat trials and report how often every attempt succeeds, not just the best run."

### Q24. A customer says the bot feels dumb. What do you change first?

**Model answer:** "I'd collect twenty or thirty of the conversations they mean and sort the failures — wrong answer, refusal, slow, missing context, tone. Then I'd find the first failing layer: often retrieval missing the right document, not the model. I fix the cheapest layer that explains most failures, add those cases to the evaluation set and agree a measure with the customer so 'better' is visible."

## Production, cost and reliability

### Q25. The token bill tripled last month and nobody changed the code. What happened?

**Model answer:** "Something changed outside the code. I'd check traffic, then tokens per request: retrieval returning more or longer chunks, conversation history growing, retries or agent loops, a lower prompt-cache hit rate because the prompt prefix changed, or a provider model or price change. A per-request cost breakdown by feature answers this in minutes; without one it takes days."

### Q26. Your feature is too slow and too expensive. What do you do?

**Model answer:** "Measure where time and tokens go first. Then route easy requests to a smaller model, cache repeated prefixes and answers, send fewer chunks, cap output length, stream, and run independent tool calls in parallel — keeping each change only if quality holds on the evaluation set. ResearchOps shows the pattern: local scoring, the paid model only for the top items, and a hard daily cost ceiling."

### Q27. What do you log for an LLM feature?

**Model answer:** "Request and prompt-template version, model and parameters, retrieved document IDs, tool calls and results, the output, latency split into time to first token and total, tokens, cost, and any evaluation or user-feedback signal — linked by one trace ID. I minimise sensitive content: Hatch's optional traces deliberately exclude prompts, responses and CV text."

### Q28. How do you reduce hallucinations?

**Model answer:** "In layers: ground answers in retrieved evidence with citations, allow and reward abstention, constrain the output format, verify claims or citations automatically where possible, and measure the unsupported-claim rate on an evaluation set so I know whether a change helped."

### Q29. Your model provider has an outage. What happens?

**Model answer:** "A tested fallback, not any model that accepts the same request — a fallback changes behaviour, so it must pass the same evaluation. Where no fallback is safe, the system degrades gracefully. IncidentPilot falls back to rules-only diagnosis; it never silently returns a worse answer as if nothing happened."

### Q30. Local or hosted models?

**Model answer:** "It depends on data sensitivity, volume, latency and who will operate it. Hosted models are faster to start and stronger; local models keep data on the machine and cost nothing per call but bring hardware, updates and monitoring. Hatch supports both: a small local triage model filters roles quickly and a larger one does detailed work, or a cloud provider handles both."

## Security and safety

### Q31. How do you defend an agent against prompt injection?

**Model answer:** "Assume it will happen, because there is no complete fix. Treat retrieved text and tool results as data, keep secrets out of the model's context, give tools least privilege, validate actions outside the model, and require approval for anything consequential. The strongest control is limiting what injected text could make the system do — in IncidentPilot the model has no tools at all."

### Q32. How do you handle personal data in an LLM application?

**Model answer:** "Minimise what reaches the model, redact where possible, choose a provider and region that meet the data requirements, set retention for logs and traces, and support deletion across derived copies such as embeddings and caches."

## Projects and behavioural

### Q33. Walk me through a project you built end to end.

**Model answer (STAR):** "**Situation:** I wanted a triage assistant for containerised services, and to test how far an LLM should be trusted in that loop. **Task:** Build a triage agent that is useful and safe enough to run on real services. **Action:** I made the MVP read-only. A collector gathers runtime status, bounded logs, health checks and deployment data; deterministic rules diagnose the known failure patterns; an optional local model ranks hypotheses from validated evidence and has no tools; rules keep control of severity and recommended actions. I built golden-file evaluations for two injected failures with ten checks each, including 'no action executed', and a CI job that injects both failures into a live demo stack. **Result:** It produces JSON and SRE-style reports with or without the model, and every change has to keep both scenarios passing. **Next:** more scenarios, and approval-gated actions only once evaluation supports them."

### Q34. Tell me about a time your evaluation said no.

**Model answer:** "In July I ran a staged benchmark to see whether a newer local model should replace Hatch's writing baseline. All 27 runs completed with valid output and no unsupported claims, but no challenger passed the hard quality gates, so I kept the baseline. The point of the gates is that a newer model does not ship just because it is newer."

### Q35. Why did you rebuild ResearchOps rather than extend it?

**Model answer:** "Version one used CrewAI with hard-coded sources, so it only worked for AI topics. I wrote requirements for version two: any topic as a file, sources discovered and vetted at run time, ranking I could audit, no hard-coded credentials and a cost ceiling. Four of five ranking scores are now deterministic and only relevance is model-judged. Extending v1 would have kept its narrow design."

### Q36. How do you use coding agents in your own work?

**Model answer:** "As fast contributors working from a specification I write. I give them bounded context and a test that must pass, review every diff and keep decisions in the repository rather than chat history. I've used IncidentPilot as a benchmark project to compare Claude Code, Codex, OpenCode and Cline on the same tasks." Add one finding from that comparison that you can defend.

### Q37. You've been a delivery lead. Why AI engineering, and what is your gap?

**Model answer:** "I've spent years making sure systems create value in production, and the hardest problems in AI products now are exactly that: evaluation, safe integration, rollout and cost. I've backed that with hands-on work. My honest gap is operating an AI system at high scale as the engineer on call; I've built the evaluation, tracing and fallback patterns that scale needs, and I'd expect to close that gap quickly in a team that already runs at scale."

## Practice exercises

**Build in 40 minutes:** a FastAPI endpoint that answers questions over a folder of Markdown files with keyword plus vector retrieval, cites chunk IDs and abstains below a threshold. Get it working end to end before optimising. [3]

**Take-home rehearsal:** 50 documents, 20 questions with labelled answers including three unanswerable ones. Report recall@5, faithfulness and abstention accuracy, and one change you made because of the numbers.

**Debugging rehearsal:** an agent that repeats a tool call. Find the swallowed error, add a step cap and a repeated-call guard, and replay the failing input as a test.

## Bridge questions

These questions cross from your story into the system behind it and back. Each answer follows the five beats in [Connect the dots](../shared/connect-the-dots.md) (Stakes, Split, Sketch, Shape, Show); the decisions behind them are in the [decision lists](../shared/decision-ledger.md).

### Q38. How would you build the GenAI order automation today, and how would you evaluate it?

**Model answer:** “I'd keep what worked at Natoora: strip people's names and addresses before anything reaches the model, ask for structured JSON, validate customers and products against the warehouse system, block duplicates on the order reference and items, and send anything uncertain to human review. What I'd add is a fixed evaluation set: a labelled sample of real emails from each procurement system, scored field by field, plus the exception rate and handling time per system. Every prompt or model change would run against that set before release. It's the same gate I use in Hatch, my personal project, where a staged evaluation kept the baseline model because no challenger passed the quality gates.”

### Q39. What did production teach you that a demo didn't?

**Model answer:** “Three things on the GenAI order tool. Format variety was the real problem: Marketman in London and Lightspeed in Paris sent orders differently, so each procurement system needed its own experiments over two to three months. Exception rules can't be designed up front; ours grew out of what those experiments showed. And trust came from visibility: the human review screen let customer service see exactly how each order was handled. That's also why I measured effort released, about ninety per cent, rather than claiming a model accuracy figure.”

## Credibility probes

Which parts did you write and which did a coding agent write? How was the 90% order-automation figure measured? What does your evaluation set not cover? What would break first at a thousand users? Have you been on call for an AI system? Answer each directly; "personal project" is a respectable answer when it is true.

## Questions to ask the panel

How do you evaluate model or prompt changes before release? Who owns an AI feature's quality after launch? What does your observability show for an LLM call today? Which failure in production taught the team the most?

## Sources and freshness

Checked 13 October 2026. Interview patterns are synthesised from public guides; employer loops vary.

1. [What applied-AI engineer interviews test in 2026](https://www.techinterview.org/post/3233476824/ai-engineer-interview-rag-agents-evals/) — techinterview.org, 23 July 2026.
2. [AI Engineer Interview Questions 2026](https://www.kore1.com/ai-engineer-interview-questions-2026/) — KORE1, 23 June 2026 (a recruiting firm's view).
3. [AI Engineer Interview Questions 2026: LLM, RAG and Agents](https://techscreen.app/articles/ai-engineer-llm-interview-questions-2026) — TechScreen, 21 September 2026.
4. [50 LLM and AI Engineer Interview Questions for 2026](https://letsdatascience.com/blog/50-llm-and-ai-engineer-interview-questions-for-2026) — Let's Data Science, updated 6 September 2026 (deeper model-internals questions for research-leaning roles).
5. [Model Context Protocol versioning](https://modelcontextprotocol.io/specification/versioning) — current revision 2026-07-28.
6. LinkedIn's [AI Engineer interview question guide](https://business.linkedin.com/talent-solutions/resources/how-to-hire-guides/artificial-intelligence-engineer/interview-questions) for hiring managers — generic behavioural questions only.

Posts on X (for example a widely shared "real interview question" on running LLM evals) could not be opened for verification; they were used only as signals that evaluation questions are now standard, not as sources.
