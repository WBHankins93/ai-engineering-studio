# AI Engineering Studio

A VitePress documentation site teaching the AI engineering ecosystem through a
customer-facing engineer's lens, making LLM apps, infrastructure, MLOps, and
governance legible to technical *and* non-technical audiences. Third repo in the
author's trilogy (siblings: `solutions-playbook`, `devops-studio`).
Last verified: 2026-09-17

## Reader & positioning (do not drift from this)
The author is a customer-facing engineer, **not** a model-training researcher, and
that is the deliberate edge. Every page answers: *what decision does this serve,
who is in the room, how do I explain it.* Depth serves translation, never itself.
Failure mode to avoid: content that reads as "AI for people avoiding AI." Defense:
labs still build the real thing; translation is added, not substituted. Full plan
in `product/BUILD-PLAN.md` — read it before building content.

## Commands
- Install `npm ci` (Node 20) · dev `npm run docs:dev` · preview `npm run docs:preview`.
- Build / gate: `npm run docs:build` — compiles every page, **fails on dead
  internal links** (`ignoreDeadLinks: false`). This is the CI gate.

## Architecture
- `.vitepress/config.mts` — site config + sidebar/nav + social meta. **Add a
  page's link here when you create the file**, or it won't appear; a link to a
  missing file fails the build. `base: '/ai-engineering-studio/'` (Pages subpath).
- `.vitepress/theme/` — `index.ts` (layout + mermaid `securityLevel: 'strict'`),
  `custom.css` (violet brand + `.sp-*`/`.ai-*` classes).
- `index.md` home · `foundations/` `decision-frames/` `poc-playbooks/`
  `talk-tracks/` `lessons/` `labs/` (01–07) `visuals/` `decisions/` (ADRs).
- `product/BUILD-PLAN.md` — the full phase-by-phase implementation spec.

## Conventions
- **Depth Standard** governs every content page — see `product/BUILD-PLAN.md`:
  worked scenario + drawn mermaid flow, real-or-illustrative numbers (never invent
  one and present it as authoritative), failure path, talk track, audience lens.
- **Three-layer lab reading model** (the defining lab convention): a main track a
  generalist completes without prior AI knowledge; inline `.ai-context` boxes for
  customer relevance; `.ai-deeper` anchors to appendices/lessons for engineering
  detail; an `.ai-explain` "explain it to a customer" close.
- **Component classes** (in `custom.css`, never hardcode hex): `.sp-say` (talk
  track), `.sp-band`/`.sp-step` (scenario steps), `.sp-pill` (status tags,
  `ok`/`warn`/`bad`); `.ai-context`, `.ai-deeper`, `.ai-explain`.
- **Mermaid** runs in `strict` mode: no HTML in node labels, no `<br>`, no HTML
  entities, no bare `&`, short single-line labels. Fence with ` ```mermaid `.
  **Renderer gotcha:** the `config.mts` fence rule must emit
  `<pre class="mermaid" v-pre>` with HTML-escaped content — a plain `<div>` lets
  Vue's template compiler condense the diagram's newlines to spaces, which mermaid
  rejects as a syntax error. Don't "simplify" that rule.
- **Showcase visuals** are polished PNGs (flat-vector, violet brand) in
  `assets/diagrams/`, promoted from mermaid only when flagship — see
  `IMAGERY-PLAN.md` (what), `VISUAL-PROMPT-STANDARD.md` (how),
  `visual-specs/showcase-prompts.md` (specs), `visual-specs/og-image.html` (the
  social card's source). Spec first, image second; simple flows stay mermaid.
- **Tables** in markdown by default (dark-mode safe). Custom HTML only for the
  `.sp-*`/`.ai-*` classes above.
- **Canonical cast** (reuse so it reads authored): `Ollama` + Llama 3.x 8B,
  embeddings `bge`/`nomic-embed`, `Qdrant`, `Langfuse`, `promptfoo`/`DeepEval`,
  **LangGraph**, `LiteLLM`. Vendor-neutral categories, concrete examples.
- **Labs are local-first / $0** on Ollama. Lab 07 has two tracks: strictly-$0
  local, plus an optional rented-GPU cloud capstone — never force spend.
- **Git: plain single-author commits.** A `commit-msg` hook rejects
  `Co-Authored-By` / `Generated with` trailers. Imperative subject, no period,
  body only when the "why" isn't obvious.
- **Commit meaningfully and often.** Every logical unit — one page, one fix, one
  config change — is its own commit, made as soon as it builds green. Never batch a
  phase into one commit, and never leave finished work uncommitted.

## Decisions
- 2026-06 — LangGraph is the orchestration standard for all labs — most
  production mindshare, safe to standardize; recorded in ADR 001. Include a
  beginner "LangGraph in 10 minutes" page in foundations.
- 2026-06 — Two handoff files, not one: dense `AGENTS.md` + exhaustive
  `product/BUILD-PLAN.md` — keeps source-of-truth lean while giving full build
  instructions.
- 2026-06 — Own violet brand (siblings are teal) so the trilogy is visually
  distinct but structurally identical.
- 2026-06 — Labs are **provider-agnostic** (decided w/ user 2026-06-28): OpenAI-
  compatible code, backend chosen in `.env` via `provider.py` — default local Ollama,
  first-class hosted fallback (Groq free tier / OpenAI) for Intel/older/locked-down
  machines. Audience assumes Apple Silicon, but no one is excluded. Shared setup in
  `labs/model-backends.md`. Aligns with the RAG reference doc's API-first stance.
- 2026-06 — PR **per deliverable** (revised per user 2026-06-28): a lab is always
  its own `phase-N/<slug>` branch + PR; signature artifacts are too, unless a few
  are small and tightly related (then they may share one PR, as the Phase 1 spine
  did). "Phase" is a roadmap label, not a PR unit. Commit often inside the branch
  (one logical unit each), preserve commits on merge (no squashing a deliverable),
  dead-link CI required, keep every commit green. Phase 0 → `main` (scaffold
  exception). Supersedes the earlier per-phase and per-deliverable-only decisions.
- 2026-09 — Positioning is a **customer-facing engineer's** lens, not an SE/SA
  one and not a model-training researcher's (user decision, published PR #38 +
  the site-wide reframe). The differentiator is translating LLM applications,
  infrastructure, evaluation, cost, and governance into decisions, demos, and
  production plans. Public studios teach the reasoning; the paid Pre-Sales Field
  Kit packages the editable tools — do not hide the studio to protect it. Keep
  "SE/SA spine" only where it names build history (phase labels, done lists).

## State
- **Phases 0–2 done:** scaffold + foundations on-ramp (direct to `main`, scaffold
  exception); SE/SA spine — POC playbook, 3 decision frames, talk track, four-layer
  visual, ADR 001 (PR #3); visuals system + mermaid `<pre v-pre>` fix + visual
  prompt system; Labs 01–03 + apps-agents lessons, provider-agnostic and
  smoke-tested against local Ollama.
- **Phase 3 complete (2026-07-03):** Lab 04 Eval Harness (PR #14),
  `frame-good-enough.md` (PR #16), Lab 05 Serving & Cost (PR #18 — smoke-tested
  CPU-only: quantization ~4.7x faster, single-stream self-host ~200x pricier per
  token than the cheapest hosted tier), `frame-cost-at-scale.md` (PR #19).
- **Phase 4 complete (2026-07-04):** reference architectures (three tiers, two
  showcase images), guardrails/governance (NIST AI RMF / EU AI Act / ISO 42001),
  MLOps-LLMOps bridge, `governance-stack` image — through PR #27. Watch for
  sidebar/list merge-conflict casualties when two PRs touch
  `.vitepress/config.mts`; CI catches dead links, not missing nav entries.
- **Phase 5 complete and merged (closeout PR #34, 2026-07-12):** Lab 06
  Observability (PR #28), OG social preview (PR #29), Lab 07 Capstone (PR #30),
  Learning Paths (PR #31), plus site author/published meta, Lab 07's restored
  sidebar entry, real Lab 06↔07 cross-links, and the `phase-5/qa-pass` sweep.
- **Published and post-launch (2026-08 → 2026-09):** `context-window-assembly`
  visual (PR #35), README interim note dropped (PR #36), MIT licence (PR #37),
  customer-facing positioning in `README.md`/`AGENTS.md` (PR #38), then the
  site-wide reframe — home hero, site/OG/Twitter meta, regenerated `og-image.png`
  (source now committed at `visual-specs/og-image.html`), `START-HERE.md`,
  `learning-paths.md`, `product/BUILD-PLAN.md` §0. All deployed to Pages.

## Roadmap
No open milestone — Phases 0–5 are merged and live. Remaining work is optional
post-launch polish, tracked in `IMAGERY-PLAN.md`: the flagship `four-layer-map`
showcase image still has to replace the placeholder mermaid on
`visuals/four-layer-map.md`. Full detail: `product/BUILD-PLAN.md`.

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
- **CI** (`ci.yml`) — `Build docs` on every PR and push to `main`; the dead-link
  build is the gate. **CD** (`deploy.yml`) — push to `main` rebuilds and publishes
  to Pages. Live: https://wbhankins93.github.io/ai-engineering-studio/.
- **`main` is protected**: required status check `Build docs` (strict/up-to-date),
  no force-push/delete. Reviews are *not* required (solo maintainer can't
  self-approve) — agent may self-review and merge once CI is green (user-authorized
  2026-06-27). `enforce_admins` off so the owner is never locked out.
- Non-fatal annotation: GitHub is deprecating Node-20 action *wrappers* —
  unrelated to our pinned build Node 20; no action needed.

## Open questions
- None blocking.

## Maintaining this file
You (the agent) update this file when state changes: decisions made, milestones
shipped, direction changed. Keep it under 150 lines — delete before you add.
Never rewrite Decisions/Roadmap/Non-goals without explicit user confirmation.
