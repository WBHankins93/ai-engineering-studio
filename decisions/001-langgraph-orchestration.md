# ADR 001 — LangGraph as the orchestration standard

- **Status:** Accepted
- **Date:** 2026-06
- **Deciders:** Repo author (SE/SA lens)

## Context

Every lab that involves more than a single model call needs an orchestration
framework — the thing that wires steps, tools, and agents together. This site
needs *one* standard so labs read as a coherent body of work and a reader learns
transferable concepts, not five competing APIs. The choice is a teaching and
positioning decision, not a claim that one framework is universally best.

The candidates in 2026: **LangGraph**, **LlamaIndex Workflows**, **DSPy**, the
**OpenAI Agents SDK**, and "no framework" (raw API calls).

## Decision

**Standardize all labs on LangGraph**, while teaching the underlying concepts
(state, nodes, edges, hub-and-spoke orchestration) as framework-independent so the
knowledge survives a tool swap.

## Why

- **Most production mindshare.** It's the safe recommendation to a customer — you
  won't have to defend an exotic choice in a deal.
- **Its model matches the durable pattern.** Production multi-agent systems are
  overwhelmingly hub-and-spoke orchestrator-worker; LangGraph's graph-of-nodes
  with conditional edges expresses exactly that. Teaching the tool teaches the
  pattern.
- **Concepts transfer.** State/nodes/edges map onto every other framework, so a
  reader isn't stranded if their shop uses something else.

## Alternatives considered

| Option | Why not (as the standard) |
| --- | --- |
| **DSPy** | More research-forward and differentiated, but a steeper on-ramp and less customer-facing mindshare — wrong fit for a translation-first site. |
| **LlamaIndex Workflows** | Strong for RAG specifically; narrower than a general orchestration story. Used where it fits, not as the spine. |
| **OpenAI Agents SDK** | Ties the teaching to one model vendor; this site stays vendor-neutral and local-first. |
| **No framework (raw)** | Best for *learning the mechanics* once — used deliberately in early labs to show what the framework abstracts — but doesn't scale as the house standard. |

## Consequences

- **Positive:** coherent labs; a defensible answer to "what should we use?"; the
  hub-and-spoke pattern is taught by default.
- **Negative / cost:** LangGraph's API evolves, so lab code dates — mitigated by
  pinning versions in each lab and keeping tool names in `CANONICAL-CAST.md` for
  one-edit swaps. Concept-first teaching limits the blast radius of any future
  change to this decision.
- **Revisit if:** mindshare shifts materially, or a lab's needs are served far
  better by a different tool (record a superseding ADR rather than editing this).

<div class="ai-deeper">
  <span class="ai-label">Related</span>
  Beginner intro: <a href="/foundations/langgraph-how-to">LangGraph in 10 Minutes</a>.
  The "do we even need an agent at all?" question is a separate decision — see the
  <code>decision-frames/do-we-need-an-agent</code> frame.
</div>
