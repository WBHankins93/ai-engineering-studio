# AI Engineering Studio — Full Build Plan

The complete implementation spec. `AGENTS.md` is the dense always-loaded context;
this file is the exhaustive marching orders. Read both before building content.

---

## 0. What this repo is, and the one rule that governs everything

A VitePress site teaching the AI engineering ecosystem **through a Solutions
Engineer / Solutions Architect lens.** The author is an SE/SA, not a deep AI
engineer — and that is the deliberate, defensible edge. The scarce skill in 2026
is the person who makes AI legible to a CTO and an engineer in the same meeting,
not the 500th deep-RAG tutorial.

**The governing rule for every page:** answer *what decision does this serve,
who is in the room, and how do I explain it.* Depth is in service of translation.

**The failure mode to avoid:** content that reads as "AI for people who can't be
bothered to learn AI." **The defense:** labs still build the real thing (you run
the RAG pipeline, write the eval, measure the latency); the translation layer is
*added on top*, never *substituted* for rigor.

Three reader goals, all in play: (1) share with SE/SA peers, (2) use at the
author's actual job, (3) portfolio showcase.

---

## 1. The four-layer ecosystem model

All content organizes under four layers the field has converged on:

| Layer | Name | Covers |
| --- | --- | --- |
| L1 | LLM apps & agents | RAG, agents, prompt/context engineering, evals, orchestration, MCP/A2A, multi-agent |
| L2 | LLMOps & inference infra | Serving (vLLM/SGLang), quantization, GPU, vector DBs, gateways, LLM observability, cost/latency |
| L3 | Classic MLOps & data | Training pipelines, feature stores, registries, experiment tracking, CI/CD for ML, drift |
| L4 | AI architecture & governance | Reference architectures, build-vs-buy, guardrails, evaluation strategy, NIST/EU AI Act/ISO 42001 |

Research-backed facts to use (cross-validated, 2026): agents are overwhelmingly
**hub-and-spoke orchestrator-worker** in production, not mesh/swarm; **MCP** (tools
for one agent) + **A2A** (agent-to-agent coordination) are the connective protocols;
RAG best practice is **hybrid search (BM25 + dense, RRF fusion) → rerank → top-5**;
**eval-as-a-production-gate** is the practice separating real work from demos;
inference standard is **vLLM/SGLang + quantization by default**; LLMOps is an
**extension of MLOps, not a replacement**; on architecture, **never build the model
layer, hybrid dominates** (buy foundation models + infra, build data layer +
task-specific agents). Mark all cost/latency/accuracy figures **illustrative**
unless verified against official docs.

---

## 2. The Depth Standard (apply per page, by tier)

Adapted from `solutions-playbook`'s DEPTH-STANDARD. The five moves:

1. **Worked scenario** — one concrete, named case end-to-end with a drawn mermaid flow.
2. **State the numbers** — real policy/values, or marked illustrative (`~1s`, `e.g. 1s→2s→4s`). Never invent an authoritative number.
3. **Failure path** — the flow shows happy path *and* failure, not just success.
4. **Talk track** — a `.sp-say` "Say it like this" box at each key decision: the literal sentence said on a call.
5. **Audience lens** — a "who sees what" view (eng / exec / customer) wherever relevant.

**Tiers** — what gets applied where:

| Tier | Folders | Moves |
| --- | --- | --- |
| A — Full | `lessons/`, `decision-frames/`, `visuals/` | All five |
| B — Partial | `poc-playbooks/`, `labs/`, `foundations/` | 1, 2, 4 (+3, +5 where relevant) |
| C — Lean (do not pad) | `talk-tracks/`, ADRs in `decisions/` | None — padding breaks their purpose |

---

## 3. The three-layer lab reading model (the defining lab convention)

Every lab is layered so three readers all get through it without one being lost
or the other being bored:

1. **Main track** — a generalist with general technical experience completes the
   lab front-to-back with no prior AI tooling knowledge. Gloss every new term in
   one plain line the first time it appears.
2. **`.ai-context` boxes** — inline notes explaining the *why* and customer
   relevance: what an SE would say about this step in a meeting.
3. **`.ai-deeper` anchors** — where engineering detail matters, link down to an
   "Under the hood" appendix or a linked lesson. Opt-in depth.
4. **`.ai-explain` close** — every lab ends not with "congratulations" but with
   *how you'd demo this to a customer* + the one-sentence non-technical version.

Example lab step (the texture to match):
> **Step 4 · Add a reranker.** Run `make rerank`. Your top-50 results get
> re-scored and cut to the best 5.
> `.ai-context`: "This is the cheapest quality win in RAG — to a customer it's
> 'we double-check the search results before the AI reads them.'"
> `.ai-deeper`: → Under the hood: cross-encoders vs bi-encoders · Lesson: RAG retrieval decisions

Lab anatomy (from `devops-studio`): one Makefile, quick start, detailed setup,
project structure, troubleshooting, cleanup, cost note (almost always `$0`),
next steps — **plus** the three-layer reading model on top.

---

## 4. Component classes (in `.vitepress/theme/custom.css` — already created)

Use these; never hardcode hex (breaks dark mode).

- `.sp-say` + `.sp-label` — talk-track box. `<div class="sp-say"><div class="sp-label">Say it like this</div><p>"..."</p></div>`
- `.sp-band` + `.sp-step` (`.sp-h`/`.sp-d`) — scenario step band.
- `.sp-pill` (`.ok`/`.warn`/`.bad`) — inline status tags, e.g. `<span class="sp-pill warn">429</span>`.
- `.ai-context` + `.ai-label` — SE relevance note (the lab's translation layer).
- `.ai-deeper` + `.ai-label` — go-deeper pointer to appendix/lesson.
- `.ai-explain` + `.ai-label` — the "explain it to a customer" lab close.

---

## 5. Canonical cast (reuse so the repo reads authored, not assembled)

Create `CANONICAL-CAST.md` documenting these. Vendor-neutral as *categories*,
concrete as *examples*. Keep tool names isolated here so a swap is one edit.

| Category | Example used |
| --- | --- |
| Local serving | Ollama + Llama 3.x 8B |
| Embeddings | bge / nomic-embed |
| Vector DB | Qdrant |
| Tracing / observability | Langfuse |
| Eval | promptfoo / DeepEval (+ RAGAS for RAG) |
| Orchestration | **LangGraph** (the standard — ADR 001) |
| Model gateway | LiteLLM |
| Production serving (lessons) | vLLM / SGLang |

---

## 6. Repo structure (target — build folders as you go)

```
ai-engineering-studio/
├── index.md                  # home (done)
├── START-HERE.md             # fastest-orientation entry (Phase 0)
├── DEPTH-STANDARD.md         # §2 of this file, as its own page (Phase 0)
├── CANONICAL-CAST.md         # §5 (Phase 0)
├── CONTRIBUTING.md           # git workflow note (Phase 0)
├── foundations/              # Tier B — the legible on-ramp
│   ├── how-llms-actually-work.md      (no-math mental models)
│   ├── the-four-layer-map.md
│   ├── ai-vocabulary-for-sas.md       (the glossary)
│   └── langgraph-how-to.md            ("LangGraph in 10 minutes")
├── decision-frames/          # Tier A — SIGNATURE: build-vs-buy, cost, "when X vs Y"
│   └── managed-vs-self-host.md
├── poc-playbooks/            # Tier B — SIGNATURE: scope, success criteria, demo, recovery
│   └── scoping-an-ai-poc.md
├── talk-tracks/              # Tier C — SIGNATURE: customer-safe "say it like this" cards
│   └── explaining-a-hallucination.md
├── lessons/                  # Tier A — concept + decision framing, by layer
│   ├── index.md  (overview)
│   ├── apps-agents/   llmops-infra/   mlops-data/   architecture-governance/
├── labs/                     # Tier B — hands-on, local-first, 3-layer reading model
│   ├── index.md  (overview + suggested order + difficulty/time table)
│   ├── 01-first-llm-app/   02-production-rag/   03-agent-system/
│   ├── 04-eval-harness/    05-serving-and-cost/  06-observability/  07-capstone/
├── visuals/                  # Tier A — SIGNATURE: translation diagrams, dual-labeled
│   └── four-layer-map.md
├── decisions/                # Tier C — ADRs in SE-readable language
│   └── 001-langgraph-orchestration.md
└── product/BUILD-PLAN.md     # this file
```

**Whenever you add a page, add its link to the sidebar/nav in
`.vitepress/config.mts`** or the build fails on the dead link. Conversely, the
config currently lists target pages that don't exist yet — create them (or
temporarily remove the link) so the build is green at each commit.

---

## 7. Phased build plan (PR-per-deliverable; squash; dead-link CI gate)

Each deliverable = one branch = one (eventual) squashed PR. Commit frequently
within a branch with plain imperative messages. Branch naming: `phase-N/slug`,
e.g. `phase-1/poc-playbook-first`. Keep `main` green after every merge.

### Phase 0 — Scaffold + standards + on-ramp  (mostly DONE)
Done: VitePress config, violet theme + classes, Node-20 dead-link CI, `.gitignore`,
home `index.md`, git + commit-msg hook, `AGENTS.md`, this file.
Remaining: `START-HERE.md`, `DEPTH-STANDARD.md`, `CANONICAL-CAST.md`,
`CONTRIBUTING.md`, and the 4 `foundations/` pages incl. `langgraph-how-to.md`.
Exit: a non-AI reader can orient; build green.

### Phase 1 — The SE/SA spine  (~2 wk)
The differentiators, front-loaded (most work-usable, proves positioning fastest):
first POC playbook (`poc-playbooks/scoping-an-ai-poc.md`), 2–3 decision frames
(start `decision-frames/managed-vs-self-host.md`; add RAG TCO, "do we even need an
agent?"), first talk-track (`talk-tracks/explaining-a-hallucination.md`), the
four-layer translation visual (`visuals/four-layer-map.md`), ADR 001
(`decisions/001-langgraph-orchestration.md`). Exit: usable at work day one.

### Phase 2 — Apps & agents, hands-on & anchored  (~2–3 wk)
Labs 01–03 on the three-layer reading model + apps-agents lessons. Lab 01: first
LLM app (streaming CLI, function calling, Ollama). Lab 02: production RAG (hybrid
search + rerank + RAGAS evals). Lab 03: agent system (hub-and-spoke
orchestrator-worker with LangGraph + one MCP tool). Each lab's `.ai-explain`
close links to a talk track. Exit: credible hands-on proof, legible to a generalist.

### Phase 3 — Evals + cost made legible  (~1–2 wk)
Lab 04 (eval harness: LLM-as-judge + regression gate in CI) paired with a
"how do we know it's good enough?" decision frame. Lab 05 (serving + cost:
Ollama/quantization tradeoffs, measured latency/cost) paired with a "what will
this cost at scale?" frame. The two questions every customer asks.

### Phase 4 — Architecture, governance & the MLOps bridge  (~1–2 wk)
Mostly lessons + visuals. L4: reference architectures, guardrails, the
NIST / EU AI Act / ISO 42001 stack in plain English. L3: MLOps↔LLMOps bridge
lesson that cross-links to `devops-studio`. Author's DevOps depth carries this fast.

### Phase 5 — Capstone, observability & trilogy polish  (~1–2 wk)
Lab 06 (Langfuse observability). Lab 07 (capstone, end-to-end RAG-agent app) with
**two tracks: strictly-$0 local AND optional rented-GPU cloud deploy** — never
force spend. Role-based learning paths page, cross-links into the other two repos,
full depth-standard QA pass. Exit: portfolio-ready, link-clean, trilogy complete.

---

## 8. Learning paths (build as a page in Phase 5)

| Path | For | Sequence |
| --- | --- | --- |
| SE/SA entering AI (flagship) | People like the author | foundations → decision-frames → POC playbook → Labs 01–02 → talk tracks |
| In a live AI deal | Work, right now | START-HERE → talk track → matching decision frame → demo script |
| Get hands dirty | Build credibility | Labs 01 → 02 → 04 → 03, anchors followed as desired |
| From DevOps to AI | The crossover | MLOps↔LLMOps bridge → infra lessons → governance (links to devops-studio) |

---

## 9. Git & PR workflow

- Plain single-author commits; `commit-msg` hook rejects co-author/generation
  trailers. Imperative subject, no trailing period, body only when "why" is non-obvious.
- PR-per-deliverable. Squash-merge to `main`. Invest polish in PR titles — they
  become the permanent history (e.g. "Lab 02 · Production RAG", "POC Playbook · Scoping an AI POC").
- Dead-link CI (`npm run docs:build`) is a required check.
- Phase 0's first scaffold can land directly on `main`; everything after branches.
- Remote `origin` = https://github.com/WBHankins93/ai-engineering-studio (empty).
  Push needs authenticated GitHub access — connect the engineering GitHub MCP or
  run an authenticated push manually. Build PR-groupings locally meanwhile.

## 10. Before finishing any content page — checklist
- [ ] Correct tier identified; only the required depth moves applied (don't pad Tier C).
- [ ] Page link added to `.vitepress/config.mts` sidebar/nav.
- [ ] `npm run docs:build` passes (no dead links).
- [ ] Numbers stated or marked illustrative — none invented as authoritative.
- [ ] Talk tracks in the author's voice (warm, direct, outcome-first, one clean line).
- [ ] Mermaid labels short, single-line, strict-mode safe.
- [ ] Canonical cast used for any tool reference.
- [ ] For labs: main track is generalist-completable; `.ai-context`/`.ai-deeper`/`.ai-explain` present.
