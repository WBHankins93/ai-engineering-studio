---
tags:
  - start-here
---
# Start Here

Welcome. This is a working reference for **making AI engineering legible** — built
by and for Solutions Engineers and Architects who have to stand between a CTO and
an engineer and make sure they're solving the same problem.

## 📝 What This Is (and What It Isn't)

This is **not** another deep-RAG tutorial competing on tooling mastery. The
internet has a glut of those. The scarce skill in 2026 is translation: scoping an
AI POC that won't embarrass anyone, framing build-vs-buy in dollars, explaining
why the demo hallucinated without losing the room. That's the SE/SA job, and
almost nobody publishes it well.

> The thesis, in one line: *"I can't out-engineer a Staff ML Engineer. But I can
> stand in front of your exec team and your engineers in the same meeting and make
> sure they're solving the same problem — here's how."*

The defense against this being shallow is non-negotiable: **the labs still build
the real thing.** You run the RAG pipeline, write the eval, measure the latency.
The translation layer is *added on top* of rigor, never *substituted* for it.

## 🔥 If You're in a Live AI Deal Right Now

Jump straight to what you need:

- **The model hallucinated / "won't it make things up?"** → [Explaining a Hallucination](/talk-tracks/explaining-a-hallucination) — the lines that hold the room.
- **Scoping a POC or a demo?** → [Scoping an AI POC](/poc-playbooks/scoping-an-ai-poc) — criteria and recovery that survive a live model.
- **"Should we build or buy / what'll it cost / do we need an agent?"** → the [Decision Frames](/decision-frames/managed-vs-self-host) — [managed vs self-host](/decision-frames/managed-vs-self-host), [RAG cost](/decision-frames/rag-tco), [agent or not](/decision-frames/do-we-need-an-agent).
- **Need to place a vague customer ask?** → [The Four-Layer Map](/visuals/four-layer-map) — the whiteboard you draw in a kickoff.
- **Blanking on a term mid-call?** → [AI Vocabulary for SAs](/foundations/ai-vocabulary-for-sas) — `Ctrl+F` it before you dial in.

## 🧭 If You're Orienting for the First Time

Read the foundations on-ramp in order — it assumes no prior AI knowledge and gets
you fluent fast:

1. [How LLMs Actually Work (no math)](/foundations/how-llms-actually-work) — the one idea everything hangs on, plus why models hallucinate.
2. [The Four-Layer Map](/foundations/the-four-layer-map) — the mental model the whole site is organized around.
3. [AI Vocabulary for SAs](/foundations/ai-vocabulary-for-sas) — the glossary you wish you'd had.
4. [LangGraph in 10 Minutes](/foundations/langgraph-how-to) — how agent workflows are wired.

## 🗺️ How the Site Is Built

Everything here is organized under the four-layer map (L1 apps & agents → L2
LLMOps & infra → L3 MLOps & data → L4 architecture & governance) and split into
content types that each do one job well:

| Type | Teaches by | Status |
| --- | --- | --- |
| **[Foundations](/foundations/how-llms-actually-work)** | orienting | ✅ available now |
| **[Decision frames](/decision-frames/managed-vs-self-host)** | deciding (build-vs-buy, cost, "when X vs Y") | ✅ available now |
| **[POC playbooks](/poc-playbooks/scoping-an-ai-poc)** | scoping & de-risking an engagement | ✅ available now |
| **[Talk tracks](/talk-tracks/explaining-a-hallucination)** | the customer-safe "say it like this" card | ✅ available now |
| **[Visuals](/visuals/four-layer-map)** | seeing — translation diagrams | ✅ available now |
| **Labs** | doing — hands-on, local-first, mostly $0 | 🔜 Phase 2 |
| **Lessons** | the concept + the decision behind it | 🔜 Phase 2+ |

The build is phased so the SE/SA spine — the differentiators — comes first. See
`product/BUILD-PLAN.md` for the full plan and `AGENTS.md` for the project's
source of truth.

## 📋 The Conventions That Keep It Consistent

- **Depth Standard** — how a generic page becomes a worked, talk-track-equipped one. See [DEPTH-STANDARD.md](/DEPTH-STANDARD).
- **Canonical Cast** — the reused tool examples (Ollama, Qdrant, Langfuse, LangGraph…) that make the site read authored, not assembled. See [CANONICAL-CAST.md](/CANONICAL-CAST).
- **Contributing** — git workflow and the dead-link CI gate. See [CONTRIBUTING.md](/CONTRIBUTING).

## 🔗 The Trilogy

This is the third repo in a set with one through-line — *a Solutions Architect who
makes hard technical domains understandable.* `solutions-playbook` (how I run
engagements) → `devops-studio` (the infra I can speak to) → **ai-engineering-studio**
(making the newest, least-understood domain legible). Each stands alone; together
they tell a single story.

---

*This site is under active build. The foundations on-ramp is complete; the SE/SA
spine and labs are filling in phase by phase.*
