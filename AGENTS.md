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
- **Mermaid** runs in `strict` mode: no HTML in node labels, no `<br>`, no HTML
  entities (`&amp;`/`&gt;`), no bare `&`, short single-line labels. Fence with
  ` ```mermaid `. **Renderer gotcha:** the `config.mts` fence rule must emit
  `<pre class="mermaid" v-pre>` with HTML-escaped content — a plain `<div>` lets
  Vue's template compiler condense the diagram's newlines to spaces, which mermaid
  rejects as a syntax error. Don't "simplify" that rule.
- **Showcase visuals** are polished PNGs (flat-vector, violet brand) in
  `assets/diagrams/`, promoted from mermaid only when flagship — see
  `IMAGERY-PLAN.md` (what + priority), `VISUAL-PROMPT-STANDARD.md` (how), and
  `visual-specs/showcase-prompts.md` (ready-to-paste specs). Spec first, image
  second. Decision trees / simple flows stay mermaid.
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
- 2026-06 — PR **per deliverable** (revised per user 2026-06-28): a lab is always
  its own `phase-N/<slug>` branch + PR; signature artifacts are too, unless a few
  are small and tightly related (then they may share one PR, as the Phase 1 spine
  did). "Phase" is a roadmap label, not a PR unit. Commit often inside the branch
  (one logical unit each), preserve commits on merge (no squashing a deliverable),
  dead-link CI required, keep every commit green. Phase 0 → `main` (scaffold
  exception). Supersedes the earlier per-phase and per-deliverable-only decisions.

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
- **Phase 0 committed and pushed to `main`** (2026-06-27): 7 plain commits
  (scaffold → docs → one per foundations page → START-HERE). `origin` connected
  via authenticated `gh` (WBHankins93); https://github.com/WBHankins93/ai-engineering-studio
  is now populated.
- **Phase 1 (SE/SA spine) built on `phase-1/se-sa-spine`** (2026-06-27): POC
  playbook (`poc-playbooks/scoping-an-ai-poc`), three decision frames
  (`managed-vs-self-host`, `rag-tco`, `do-we-need-an-agent`), talk track
  (`explaining-a-hallucination`), signature visual (`visuals/four-layer-map`), ADR
  001 (`decisions/001-langgraph-orchestration`). All wired into nav/sidebar; home +
  START-HERE updated to surface them; build green per commit. Merged via PR #3.
- **Visuals system + mermaid fix on `visuals/diagram-system`** (2026-06-28): found
  mermaid diagrams rendered as syntax errors — root cause was the `<div>` fence
  rule letting Vue collapse newlines (now `<pre v-pre>` + escaped); also stripped
  `<br>`/entities from all diagram labels. Added the visual prompt system
  (`VISUAL-PROMPT-STANDARD.md`, `IMAGERY-PLAN.md`, `visual-specs/showcase-prompts.md`)
  modeled on the sibling repos, violet-adapted, with Wave 1 specs ready
  (four-layer-map, rag-two-loops, hub-and-spoke). Next: Phase 2 (labs 01–03 +
  apps-agents lessons).

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

## CI/CD
- **CI** (`.github/workflows/ci.yml`) — `Build docs` job runs on every PR and push
  to `main`; the dead-link build is the gate.
- **CD** (`.github/workflows/deploy.yml`) — on push to `main`, rebuilds and
  publishes to GitHub Pages (Actions build source). Live:
  https://wbhankins93.github.io/ai-engineering-studio/ (matches `base`).
- **`main` is protected**: required status check `Build docs` (strict/up-to-date),
  no force-push/delete. Reviews are *not* required (solo maintainer can't
  self-approve) — agent may self-review and merge once CI is green (user-authorized
  2026-06-27). `enforce_admins` off so the owner is never locked out.
- Non-fatal annotation: GitHub is deprecating Node-20 action *wrappers* (runs on
  Node 24 anyway) — unrelated to our pinned build Node 20; no action needed.

## Open questions
- Cloud-capstone-vs-strictly-$0 for Lab 07 still open (per BUILD-PLAN §7) — decide
  before Phase 5.

## Maintaining this file
You (the agent) update this file when state changes: decisions made, milestones
shipped, direction changed. Keep it under 150 lines — delete before you add.
Never rewrite Decisions/Roadmap/Non-goals without explicit user confirmation.
