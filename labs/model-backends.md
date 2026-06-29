---
tags:
  - lab
  - llmops-infra
---
# Choosing a Model Backend

Every lab here is **provider-agnostic**. The code talks to an OpenAI-compatible API,
so the *same* lab runs against a model on your laptop (Ollama) **or** a hosted
endpoint (Groq, OpenAI, …) — you just change a couple of environment variables. This
page is the one-time setup; each lab links back here.

> **Why this exists.** The labs shouldn't assume specific hardware. Apple-Silicon
> users get a great $0 local experience; everyone else — Intel Macs, Windows/Linux,
> locked-down corp laptops — gets an identical lab through a free hosted tier.

## Which backend should I use?

| You're on… | Use | Why |
| --- | --- | --- |
| Apple Silicon (M1–M4) | **Ollama** (default) | Fast enough locally, $0, fully private |
| Intel Mac (e.g. 2019 i9) | **Groq free tier**, or Ollama with a small model | CPU inference is slow for 8B; hosted is instant and free |
| Windows / Linux, no GPU | **Groq free tier** | No local serving needed |
| Locked-down / corp laptop | **Groq or OpenAI** | No install rights required |
| Want fully offline / private | **Ollama** | Nothing leaves the machine |

All paths are **$0 to a few dollars**: Ollama is free; Groq has a free tier; OpenAI
is pennies at lab volume.

## Option A · Ollama (local, default)

Best on Apple Silicon. Free and private.

1. Install [Ollama](https://ollama.com) and make sure it's running (`ollama --version`).
2. Pull a model: `make pull` (downloads `llama3.1:8b`, a few GB, one-time).
3. Leave `MODEL_BACKEND=ollama` in your `.env` (the default).

On a slower CPU (e.g. an Intel i9), use a smaller model: set `MODEL=llama3.2:3b`.

## Option B · Groq (hosted, free tier)

Best for Intel/older Macs and anyone who can't run a model locally. Very fast,
OpenAI-compatible, free tier.

1. Get a free API key at [console.groq.com](https://console.groq.com).
2. `make env` to create `.env`, then set:
   ```
   MODEL_BACKEND=groq
   GROQ_API_KEY=gsk_your_key_here
   ```
3. Run the lab normally (`make chat`, `make tools`).

## Option C · OpenAI (hosted, paid)

Set `MODEL_BACKEND=openai` and `OPENAI_API_KEY=sk-...` in `.env`. Cheap at lab
volume; defaults to `gpt-4o-mini`. Any other OpenAI-compatible provider works too —
set `OPENAI_BASE_URL` to its endpoint.

## How it works under the hood

`provider.py` reads `MODEL_BACKEND` and returns an `openai` client pointed at the
right `base_url` with the right key and default model. Ollama exposes an
OpenAI-compatible API (`/v1`), so one code path covers local and hosted — no
if/else littered through the lab.

## ⚠️ Gotchas

- **Tool calling needs a capable model.** `tools.py` requires a tool-capable model — Llama 3.1+, Qwen 2.5, Groq's Llama models, or any OpenAI model. Very small/old models may ignore tools.
- **Keep `.env` out of git.** It holds API keys; it's already gitignored. Commit `.env.example`, never `.env`.
- **Intel CPU + 8B = slow.** It works, but expect a few tokens/sec. Use `llama3.2:3b` locally, or switch to Groq.

## 🔗 Links

- [Labs overview](/labs/)
- [Lab 01 · First LLM App](/labs/01-first-llm-app/) — the first lab to use this
- [Managed API vs Self-Host](/decision-frames/managed-vs-self-host) — the same choice, at production scale
