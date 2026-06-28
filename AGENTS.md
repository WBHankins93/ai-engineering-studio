# AI Engineering Studio

A VitePress documentation site teaching the AI engineering ecosystem through a
Solutions Engineer / Architect lens — making LLM apps, infrastructure, MLOps,
and governance legible to technical *and* non-technical audiences. Third repo in
the author's trilogy (siblings: `solutions-playbook`, `devops-studio`).
Last verified: 2026-06-28

## Reader & positioning (do not drift from this)
The author is an SE/SA, **not** a deep AI engineer, and that is the deliberate
edge. Every page answers: *what decision does this serve, who is in the room,
how do I explain it.* Depth is in service of translation, never depth for its
own sake. Failure mode to avoid: content that reads as "AI for people avoiding
AI." Defense: labs still build the real thing; translation is added, not
substituted. Full plan in `product/BUILD-PLAN.md` — read it before building content.

## Commands
- Install: `npm ci` (or `npm install` first time) — Node 20.
- Dev: `npm run docs:dev` (hot reload, host 0.0.0.0).
- Build / gate: `npm run docs:build` — compiles every page, **fails on dead
  internal links** (`ignoreDeadLinks: false`). This is the CI gate.
- Preview built site: `npm run docs:preview`.

## Architecture
- `.vitepress/config.mts` — site config + sidebar/nav. **Add a page's link here
  when you create the file**, or it won't appear; a link to a missing file fails
  the build. `base: '/ai-engineering-studio/'` (GitHub Pages subpath).
- `.vitepress/theme/` — `index.ts` (layout + mermaid in `securityLevel: 'strict'`),
  `custom.css` (violet brand + `.sp-*` and `.ai-*` component classes).
- `index.md` — VitePress home (hero + features).
- Content folders (created as built): `foundations/`, `decision-frames/`,
  `poc-playbooks/`, `talk-tracks/`, `lessons/` (l1–l4 subfolders),
  `labs/` (01–07), `visuals/`, `decisions/` (ADRs).
- `product/BUILD-PLAN.md` — the full phase-by-phase implementation spec.

## Conventions
- **Depth Standard** governs every content page — see `product/BUILD-PLAN.md`:
  worked scenario + drawn mermaid flow, real-or-illustrative numbers (never
  invent a number and present it as authoritative), failure path, talk track,
  audience lens.
- **Three-layer lab reading model** (the defining lab convention): a main track
  a generalist completes without prior AI knowledge; inline `.ai-context` boxes
  for customer relevance; `.ai-deeper` anchors to appendices/lessons for the
  engineering detail; an `.ai-explain` "explain it to a customer" close.
- **Component classes** (in `custom.css`, never hardcode hex): `.sp-say` (talk
  track), `.sp-band`/`.sp-step` (scenario steps), `.sp-pill` (status tags,
  `ok`/`warn`/`bad`); `.ai-context`, `.ai-deeper`, `.ai-explain`.
- **Mermaid** runs in `strict` mode: no HTML in node labels, no `<br>`, no click
  handlers, short single-line labels. Fence with ` ```mermaid `.
- **Tables** in markdown by default (dark-mode safe). Custom HTML only for the
  `.sp-*`/`.ai-*` classes above.
- **Canonical cast** (reuse so it reads authored): local serving `Ollama` +
  Llama 3.x 8B, embeddings `bge`/`nomic-embed`, vector DB `Qdrant`, tracing
  `Langfuse`, eval `promptfoo`/`DeepEval`, orchestration **LangGraph**, gateway
  `LiteLLM`. Vendor-neutral as categories, concrete as examples.
- **Labs are local-first / $0** on Ollama. Lab 07 has two tracks: a strictly-$0
  local path AND an optional rented-GPU cloud capstone — never force spend.
- **Git: plain single-author commits.** A `commit-msg` hook rejects
  `Co-Authored-By` / `Generated with` trailers. Imperative subject, no period,
  body only when the "why" isn't obvious.
- **Commit meaningfully and often.** Every logical unit of work — one page, one
  fix, one config change — is its own commit, made as soon as it builds green.
  Never batch a whole phase into one commit, and never leave finished work sitting
  uncommitted. If a change is done and the build passes, commit it before moving on.

## Decisions
- 2026-06 — LangGraph is the orchestration standard for all labs — most
  production mindshare, safe to standardize; recorded in ADR 001. Include a
  beginner "LangGraph in 10 minutes" page in foundations.
- 2026-06 — Two handoff files, not one: dense `AGENTS.md` + exhaustive
  `product/BUILD-PLAN.md` — keeps source-of-truth lean while giving full build
  instructions.
- 2026-06 — Own violet brand (siblings are teal) so the trilogy is visually
  distinct but structurally identical.
- 2026-06 — PR-per-deliverable (one lab/lesson/artifact), squash-merge to keep
  `main` clean, dead-link CI as required check. Build PR-per-deliverable groupings
  even while local-only, so they replay as real PRs once GitHub auth is connected.

## State
- Scaffold complete: VitePress config, violet theme with `.sp-*` + `.ai-*`
  classes, Node-20 dead-link CI, home page, git + commit-msg hook.
- **Phase 0 content closeout done (2026-06-27):** `START-HERE.md` + all four
  `foundations/` pages (`how-llms-actually-work`, `the-four-layer-map`,
  `ai-vocabulary-for-sas`, `langgraph-how-to`) written. `DEPTH-STANDARD.md`,
  `CANONICAL-CAST.md`, `CONTRIBUTING.md` already present.
- **Build runs green** (`npm ci && npm run docs:build`, no dead links). Required a
  clean `npm ci` first (shipped node_modules was incomplete). Added a `markdown.config`
  fence rule in `config.mts` so ` ```mermaid ` blocks render as `.mermaid` divs the
  theme picks up (the scaffolded theme rendered `.mermaid` divs but nothing produced
  them). `config.mts` sidebar/nav trimmed to live pages; Phase 1+ links are kept
  commented as the roadmap — uncomment each as its page lands. Home `index.md`
  feature links to unbuilt pages dropped (re-add in Phase 1/2).
- Working tree is **uncommitted** — repo has no commits yet. Awaiting user before
  committing/pushing.
- Repo created on GitHub (empty): https://github.com/WBHankins93/ai-engineering-studio
  Remote not yet pushed — needs authenticated GitHub connection (see Open questions).

## Roadmap
Next milestone — **Phase 0 closeout + Phase 1 (SE/SA spine)**. Definition of done:
foundations on-ramp (4 pages incl. LangGraph how-to), first POC playbook, 2–3
decision frames, first talk-track card, four-layer translation visual, ADR 001,
START-HERE.md — all building green. Then Phase 2 (labs 01–03), Phase 3
(evals + cost), Phase 4 (architecture + governance + MLOps bridge), Phase 5
(capstone + learning paths + trilogy cross-links). Full detail: `product/BUILD-PLAN.md`.

## Non-goals
- Do not build this as AI-Engineer-depth content competing on tooling mastery.
- Do not pad pages with depth that doesn't serve a decision (respect the tier
  system in the build plan — not every page gets all five depth moves).
- Do not invent specific numbers (costs, latencies, accuracy) as authoritative —
  mark illustrative or verify against official docs.
- Do not add CSS frameworks or per-page `<style>` blocks — classes live once in
  `custom.css`.
- Do not add co-authoring/generation trailers to commits.

## Open questions
- GitHub auth for push/PR: connect the `engineering` plugin's GitHub MCP, or the
  author runs an authenticated push? Remote is empty and waiting.
- GitHub Pages deploy workflow not yet added (only the build-gate CI exists) —
  add a Pages deploy job when ready to publish.

## Maintaining this file
You (the agent) update this file when state changes: decisions made, milestones
shipped, direction changed. Keep it under 150 lines — delete before you add.
Never rewrite Decisions/Roadmap/Non-goals without explicit user confirmation.
