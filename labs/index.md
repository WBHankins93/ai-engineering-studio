---
tags:
  - lab
---
# Labs

Hands-on, **local-first, mostly $0** labs that build the real thing — RAG, agents,
evals — on your own machine via [Ollama](https://ollama.com). Each lab uses the
three-layer reading model: a main track any technically-literate reader can
complete, inline context boxes for SE relevance, go-deeper anchors for the
engineering detail, and an "explain it to a customer" close.

> The labs are where this site earns its credibility: the translation layer is
> *added on top* of real work, never substituted for it.

## The labs

| Lab | Focus | Stack | Time | Difficulty |
| --- | --- | --- | --- | --- |
| [01 · First LLM App](/labs/01-first-llm-app/) | The core app loop + function calling | Ollama, Python | ~1 h | Beginner |
| 02 · Production RAG *(Phase 2)* | Hybrid retrieval + rerank + evals | Ollama, Qdrant, RAGAS | ~2–3 h | Intermediate |
| 03 · Agent System *(Phase 2)* | Hub-and-spoke orchestrator-worker + one MCP tool | LangGraph, Ollama | ~2–3 h | Intermediate |
| 04 · Eval Harness *(Phase 3)* | LLM-as-judge + a regression gate in CI | promptfoo / DeepEval | ~2 h | Intermediate |
| 05 · Serving & Cost *(Phase 3)* | Quantization tradeoffs, measured latency/cost | Ollama, vLLM | ~2 h | Advanced |
| 06 · Observability *(Phase 5)* | Tracing + cost dashboards | Langfuse | ~1–2 h | Intermediate |
| 07 · Capstone *(Phase 5)* | End-to-end RAG-agent app; $0 local **or** optional cloud | full stack | ~4 h | Advanced |

## Suggested order

Start with **[Lab 01](/labs/01-first-llm-app/)** — it stands up the app loop every
later lab builds on. From there, 01 → 02 → 04 (evals early, on purpose) → 03 is the
fastest path to credible, measured hands-on proof.

## What each lab gives you

- A `Makefile` with one-command setup, run, and cleanup.
- A clear cost note — almost always **$0** on local models.
- Troubleshooting for the things that actually break.
- The SE translation layer: how you'd demo it and explain it to a non-technical
  stakeholder.
