---
tags:
  - lab
---
# Labs

Hands-on, **mostly $0** labs that build the real thing — RAG, agents, evals. They're
**provider-agnostic**: run them on a local model via [Ollama](https://ollama.com) (the
default — private, $0, great on Apple Silicon) or a free hosted tier (ideal on an
Intel/older Mac or a locked-down laptop). Set this up once in
[Choosing a Model Backend](/labs/model-backends). Each lab uses the three-layer
reading model: a main track any technically-literate reader can complete, inline
context boxes for SE relevance, go-deeper anchors for the engineering detail, and an
"explain it to a customer" close.

> The labs are where this site earns its credibility: the translation layer is
> *added on top* of real work, never substituted for it.

## The labs

| Lab | Focus | Stack | Time | Difficulty |
| --- | --- | --- | --- | --- |
| [01 · First LLM App](/labs/01-first-llm-app/) | The core app loop + function calling | Ollama/hosted, Python | ~1 h | Beginner |
| [02 · Production RAG](/labs/02-production-rag/) | Hybrid retrieval + RRF + rerank + grounding + eval | Qdrant, BM25, fastembed | ~2–3 h | Intermediate |
| [03 · Agent System](/labs/03-agent-system/) | Hub-and-spoke orchestrator-worker + one MCP tool | LangGraph, MCP | ~2–3 h | Intermediate |
| [04 · Eval Harness](/labs/04-eval-harness/) | LLM-as-judge + a regression gate in CI | openai-compatible | ~2 h | Intermediate |
| 05 · Serving & Cost *(Phase 3)* | Quantization tradeoffs, measured latency/cost | Ollama, vLLM | ~2 h | Advanced |
| 06 · Observability *(Phase 5)* | Tracing + cost dashboards | Langfuse | ~1–2 h | Intermediate |
| 07 · Capstone *(Phase 5)* | End-to-end RAG-agent app; $0 local **or** optional cloud | full stack | ~4 h | Advanced |

## Before you start

Two one-time steps, then every lab is just `make` commands.

**1 · A Python virtual environment** (keeps lab deps off your system Python and
avoids "externally-managed-environment" errors).

Requires **Python 3.10+** (Lab 03's MCP adapter needs it). Check first:

```bash
python3 --version
```

⚠️ macOS ships an older `python3` (often 3.9). If yours is below 3.10, install a
newer one — `brew install python@3.12`, or use [pyenv](https://github.com/pyenv/pyenv) —
and substitute it (e.g. `python3.12`) in the command below.

```bash
python3 -m venv .venv        # from the repo root, once (use python3.12 if needed)
source .venv/bin/activate    # macOS/Linux — each new terminal
# .venv\Scripts\activate     # Windows PowerShell
```

You'll know it's active when your prompt shows `(.venv)`. The labs call `python3`
throughout, so the venv's `python3` is all you need.

**2 · [Choose a model backend](/labs/model-backends)** — a ~2-minute decision:
run locally (Ollama) or on a free hosted tier. Every lab uses it.

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
