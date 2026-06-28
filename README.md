# AI Engineering Studio

**The AI engineering ecosystem, made legible — through a Solutions Engineer /
Architect lens.** LLM apps, infrastructure, MLOps, and governance, explained so a
CTO and an engineer can follow the same conversation.

🔗 **Live site:** https://wbhankins93.github.io/ai-engineering-studio/

> ℹ️ This README is an interim placeholder — enough context to orient a visitor. A
> full overhaul comes later. For the complete picture see
> [`AGENTS.md`](./AGENTS.md) (source of truth) and
> [`product/BUILD-PLAN.md`](./product/BUILD-PLAN.md) (the build plan).

## What this is

A VitePress documentation site, not another deep-RAG tutorial. The scarce, valuable
skill in 2026 is **translation** — scoping an AI POC that survives a live demo,
framing build-vs-buy in dollars, explaining why a model hallucinated without losing
the room. Every page answers: *what decision does this serve, who's in the room,
how do I explain it.* The labs still build the real thing (RAG, agents, evals,
local-first on Ollama); the translation layer is added on top, never substituted
for rigor.

It's the third repo in a trilogy with one through-line — *a Solutions Architect who
makes hard technical domains understandable*: **solutions-playbook** (how I run
engagements) → **devops-studio** (the infra I can speak to) → **ai-engineering-studio**
(making the newest, least-understood domain legible).

## How it's organized

Everything sits under a four-layer model (L1 apps & agents → L2 LLMOps & infra →
L3 MLOps & data → L4 architecture & governance), split into content types that each
do one job:

| Type | Teaches by | Status |
| --- | --- | --- |
| [Foundations](./foundations/how-llms-actually-work.md) | orienting (no-math mental models, the map, a glossary, LangGraph) | ✅ available |
| [Decision frames](./decision-frames/managed-vs-self-host.md) | deciding (build-vs-buy, cost, "when X vs Y") | ✅ available |
| [POC playbooks](./poc-playbooks/scoping-an-ai-poc.md) | scoping & de-risking an engagement | ✅ available |
| [Talk tracks](./talk-tracks/explaining-a-hallucination.md) | the customer-safe "say it like this" card | ✅ available |
| [Visuals](./visuals/four-layer-map.md) | seeing — translation diagrams | ✅ available |
| Labs | doing — hands-on, local-first, mostly $0 | 🔜 Phase 2 |
| Lessons | the concept + the decision behind it | 🔜 Phase 2+ |

## Status

- ✅ **Phase 0** — scaffold, standards, foundations on-ramp.
- ✅ **Phase 1** — the SE/SA spine (POC playbook, decision frames, talk track, four-layer visual, ADR 001).
- 🔜 **Phase 2** — hands-on labs (first LLM app, production RAG, agent system) + apps-agents lessons.

Full sequence and per-deliverable breakdown: [`product/BUILD-PLAN.md`](./product/BUILD-PLAN.md).

## Run it locally

Requires Node 20.

```bash
npm install        # first time
npm run docs:dev   # hot-reload dev server
```

Open the printed URL (note the `/ai-engineering-studio/` base path):
`http://localhost:5173/ai-engineering-studio/`. `npm run docs:build` runs the
production build, which fails on dead links — the CI gate.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). In short: PR per deliverable (a lab is
its own branch + PR), plain single-author commits, keep every commit green. CI
builds the site on every PR; merges to `main` auto-deploy to GitHub Pages.

Authoring conventions: [`DEPTH-STANDARD.md`](./DEPTH-STANDARD.md),
[`CANONICAL-CAST.md`](./CANONICAL-CAST.md),
[`VISUAL-PROMPT-STANDARD.md`](./VISUAL-PROMPT-STANDARD.md).
