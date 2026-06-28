# AI Vocabulary for SAs

> The glossary you wish you'd had in your first AI deal. Each term gets a plain
> definition and, where it helps, a "say it like this" line for a non-technical
> stakeholder. Organized by the [four-layer map](/foundations/the-four-layer-map)
> so you can see where each piece lives.

::: tip How to use this page
You don't read a glossary front to back — you `Ctrl+F` it before a call. The terms
most likely to come up in a live deal are in **L1** and **L4**. If you only skim
two sections, skim those.
:::

## L1 — LLM apps & agents

| Term | Plain definition | Say it like this |
| --- | --- | --- |
| **Token** | The unit a model reads and bills in — ~¾ of a word on average *(illustrative)*. | "Think of it as a syllable the AI is charged by." |
| **Context window** | The text the model can "see" in one request; its only working memory. | "However much it can hold in its head at once." |
| **Prompt** | The full input you send — instructions plus any context. | — |
| **Prompt engineering** | Wording the input to get reliable output. | "Asking the question the right way." |
| **Context engineering** | Deciding *what information* to put in the window, and in what order — the bigger lever than wording. | "Giving it the right briefing before it answers." |
| **RAG** | Retrieval-Augmented Generation: search your documents, paste the relevant bits into the prompt, then answer from them. | "It reads your docs before it answers, so it's grounded — not guessing." |
| **Chunking** | Splitting documents into passages so you can retrieve the relevant ones, not whole files. | "Cutting the manual into searchable pieces." |
| **Embedding** | A list of numbers representing a text's *meaning*; similar meanings sit near each other. | "It turns text into coordinates so we can find things by meaning, not keywords." |
| **Reranking** | A second, more careful pass that re-scores retrieved passages before the model reads them. | "Double-checking the search results before the AI uses them." |
| **Hallucination** | Confident, fluent output that isn't grounded in fact. | "When the most natural-sounding answer happens not to be true." |
| **Agent** | An LLM given tools and a goal, allowed to take steps and decide what to do next. | "It doesn't just answer — it can take actions to get the job done." |
| **Orchestration** | Coordinating the steps/agents/tools in a workflow. | "The conductor that decides what runs when." |
| **MCP** | Model Context Protocol — an open standard for giving *one* agent access to tools and data. | "A universal plug for connecting the AI to your systems." |
| **A2A** | Agent-to-Agent — an open protocol for *multiple* agents coordinating with each other. | "How the AIs talk to each other when one isn't enough." |
| **Eval** | A repeatable test of output quality — the thing that separates production from a demo. | "Our scorecard for whether it's actually good enough." |
| **LLM-as-judge** | Using a model to grade another model's output against criteria. | "Having one AI grade the other's homework, on rules we set." |

## L2 — LLMOps & inference infra

| Term | Plain definition | Say it like this |
| --- | --- | --- |
| **Inference** | Running a trained model to get an answer (as opposed to training it). | "The AI actually answering — the part you pay for per use." |
| **Serving** | The infrastructure that runs a model and answers requests at scale. | "The engine room that keeps it responding fast." |
| **vLLM / SGLang** | The standard high-throughput engines for serving open models in production. | "The proven way to run an open model efficiently." |
| **Quantization** | Shrinking a model's numbers to lower precision so it needs less memory and runs cheaper, with modest quality cost. | "Compressing the model so it runs on cheaper hardware." |
| **Vector DB** | A database that stores embeddings and finds nearest matches fast — the retrieval engine behind RAG. | "Where the searchable meaning of your docs lives." |
| **Gateway** | A single front door for model calls — routing, rate limits, logging, guardrails in one place. | "One controlled doorway for every AI call we make." |
| **Observability / tracing** | Logging inputs, outputs, latency, and cost through a pipeline so you can see what happened. | "The flight recorder — so when something's off, we know where." |
| **Latency** | Time to get an answer back. | "How long the user waits." |
| **Token cost** | What you pay per million tokens in/out — the main variable cost of an LLM app. | "The metered bill for using the AI." |

## L3 — Classic MLOps & data

| Term | Plain definition | Say it like this |
| --- | --- | --- |
| **Fine-tuning** | Further-training a model on your data to shift its *style or behavior* — not a reliable way to teach it new facts. | "Teaching it your house style — not stuffing it with your facts." |
| **MLOps** | The discipline of shipping and operating ML reliably: versioning, registries, CI/CD, monitoring. | "DevOps, but for models." |
| **LLMOps** | MLOps extended for LLMs — prompts become versioned, tested, A/B'd artifacts. | "The same operational rigor, applied to prompts and models." |
| **Feature store** | A central, versioned source of model inputs that kills training-vs-serving skew. | "One source of truth for what the model sees." |
| **Model registry** | The catalog tracing every deployed model back to the run that produced it. | "The paper trail for what's running and why." |
| **Drift** | When live data or model behavior shifts away from what you tested. | "The world changed and the model didn't — so quality quietly slips." |

## L4 — AI architecture & governance

| Term | Plain definition | Say it like this |
| --- | --- | --- |
| **Build-vs-buy** | Deciding what to build yourself vs. buy. Rule of thumb: never build the model layer; hybrid dominates. | "Buy the foundation, build what's actually yours." |
| **Guardrails** | Runtime checks that filter unsafe or off-policy input/output, best enforced at the gateway. | "The safety rails — what it's not allowed to say or do." |
| **Grounding** | Constraining answers to supplied sources, with citations and "I don't know" when absent. | "It only answers from your approved material, with receipts." |
| **NIST AI RMF** | A voluntary US risk-management framework, with a GenAI profile covering risk categories. | "A recognized checklist for managing AI risk." |
| **EU AI Act** | EU law setting obligations by risk tier, with high-risk requirements phasing in through 2026 and beyond. | "The EU's legal rulebook for AI, tiered by how risky the use is." |
| **ISO/IEC 42001** | A certifiable management-system standard — auditable evidence of AI governance. | "The certification that proves we govern AI properly." |

<div class="sp-say">
  <div class="sp-label">Say it like this — when someone asks "is our data training their model?"</div>
  <p>"With the setup we're proposing, your documents stay in your environment.
  When you ask a question, only the relevant snippet plus your question go to the
  model to generate an answer — and with an enterprise agreement that data isn't
  used for training. I'll get you the specific data-handling terms in writing so
  legal can sign off on the exact wording, not my paraphrase."</p>
</div>

::: warning Accuracy note
The "say it like this" lines are deliberately simplified for a non-technical
listener — they trade precision for clarity *on purpose*. For anything that goes
in a contract (data handling, compliance claims), point to the official terms, not
this glossary. Numbers marked *illustrative* vary by provider and workload.
:::

<div class="ai-deeper">
  <span class="ai-label">Go deeper</span>
  Tool-specific choices (which vector DB, which serving engine, which
  orchestrator) live in <code>CANONICAL-CAST.md</code> and the ADRs under
  <code>decisions/</code>. This glossary stays vendor-neutral on purpose.
</div>
