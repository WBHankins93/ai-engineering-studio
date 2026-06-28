# Depth Standard

How a generic page becomes a concrete, worked, talk-track-equipped page. Apply
per file, by tier. (Canonical source: `product/BUILD-PLAN.md` §2 — this page is
the reader-facing version.)

## The five moves
1. **Worked scenario** — one concrete, named case end-to-end with a drawn mermaid flow.
2. **State the numbers** — real values, or marked illustrative (`~1s`, `e.g. 1s→2s→4s`). Never invent an authoritative number.
3. **Failure path** — show happy path *and* failure, not just success.
4. **Talk track** — a `.sp-say` "Say it like this" box at each key decision.
5. **Audience lens** — a "who sees what" view (eng / exec / customer) where relevant.

## Tiers
| Tier | Folders | Moves |
| --- | --- | --- |
| A — Full | `lessons/`, `decision-frames/`, `visuals/` | All five |
| B — Partial | `poc-playbooks/`, `labs/`, `foundations/` | 1, 2, 4 (+3, +5 where relevant) |
| C — Lean (do not pad) | `talk-tracks/`, ADRs | None |

## Accuracy rule
Reputation artifact — wrong specifics are worse than vague ones. Universal facts
(HTTP semantics, "backoff doubles each attempt") state directly. Context-dependent
values (costs, latencies, accuracy, retry counts) mark illustrative or verify
against official docs first.

## Lab-specific: the three-layer reading model
Main track (generalist-completable) · `.ai-context` boxes (customer relevance) ·
`.ai-deeper` anchors (opt-in engineering detail) · `.ai-explain` close
("explain it to a customer"). Full detail in `product/BUILD-PLAN.md` §3.

## Component markup
`.sp-say` (talk track), `.sp-band`/`.sp-step` (scenario), `.sp-pill` (status:
`ok`/`warn`/`bad`), `.ai-context`, `.ai-deeper`, `.ai-explain`. Defined once in
`.vitepress/theme/custom.css` — never hardcode hex, never per-page `<style>`.
