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

## Page structure & formatting (house style — matches the trilogy)

Every content page follows the same skeleton so all three repos read as one body
of work. Match it exactly.

```
---
tags:
  - <type>        # decision-frame | poc-playbook | talk-track | foundations | visual | adr | lab | lesson
  - <layer/topic> # apps-agents | llmops-infra | mlops-data | architecture-governance | rag | agents | evals ...
  - <audience>    # customer-facing | internal   (optional)
---
# Plain Topic Title            ← H1, no "Decision Frame · " prefix; the section tells the type

## 📝 Context                  ← always the opener: what this serves, who's in the room. A one-line
                               recommendation may follow as a > blockquote.
## 🎯 …                        ← core content (options, selection, considerations)
## 🧭 …                        ← decision flow / framework (often the mermaid)
## 🧩 Worked Scenario: …       ← the named end-to-end case
## 📊 …                        ← numbers/tables (mark illustrative; accuracy notes as > blockquotes)
## 🚨 Failure Path / Common Failure Modes
## 👁️ Audience Lens — Who Hears What   ← the eng/exec/customer table where relevant
## 🗣️ Talk Track               ← `.sp-say` boxes
## ✅ Validation Checklist      ← where a checklist fits (e.g. POC playbook)
## ⚠️ Gotchas                  ← standard closer: bullet pitfalls
## 🔗 Links                    ← standard closer: related pages (markdown links)
```

Rules:
- **Emoji-prefixed section headings, from this fixed palette only** (reuse the
  trilogy's set, do not invent): `📝 🎯 🧭 🧩 📊 🏗️ 🛡️ 🚨 👁️ 🗣️ ✅ 📋 🔁 ⚠️ 🔗`.
- **No VitePress `:::` containers** (`::: tip/warning/info`). The siblings don't use
  them. Use an emoji section, a `>` blockquote, or a `.sp-*` component instead.
- **Frontmatter `tags:` on every content page.** Plain H1 = the topic, not the type.
- **Lean markdown-native.** Prefer bold-label bullet lists, tables, and `- [ ]`
  checklists over HTML boxes. Reserve `.sp-say` for talk tracks, `.ai-context`/
  `.ai-deeper`/`.ai-explain` for the lab three-layer model — use sparingly elsewhere.
- **Mermaid** uses the global theme config (no per-diagram `%%{init}%%` theme
  override — it would break dark mode); keep labels short and single-line.
