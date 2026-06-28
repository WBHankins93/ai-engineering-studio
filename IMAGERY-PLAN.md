# Imagery Plan

What needs a polished visual, what kind, what belongs *in* the image, and what
stays in page text. Two jobs:

1. Identify the diagrams worth creating as polished images (the showcase set).
2. Prevent visual drift as mermaid diagrams are promoted over time.

Use the sibling repos' images as the quality bar (`solutions-playbook/assets/diagrams`,
`devops-studio/assets/diagrams`): crisp flat-vector infographic, strong hierarchy,
short labels, lots of whitespace, consistent icon language, clear boundaries, no
decorative filler. **Consistency matters more than novelty.** Prompts and review
rules live in [`VISUAL-PROMPT-STANDARD.md`](VISUAL-PROMPT-STANDARD.md); filled,
ready-to-paste specs live in [`visual-specs/showcase-prompts.md`](visual-specs/showcase-prompts.md).

---

## Visual quality bar

Every image should pass these before it ships:

- **One job per image.** One architecture concept, one flow, or one decision surface.
- **Readable at a glance.** 10–18 in-image labels. Split anything denser into frames.
- **Boundaries first.** Show ownership/trust/environment/phase zones before arrows.
- **Short labels only.** Long explanations, caveats, numbers, talk tracks → caption or page text.
- **Directional arrows matter.** Label only arrows that clarify intent: request, response, retrieve, rerank, retry, escalate.
- **Status colors deliberately.** Violet = primary path, indigo = control/reliability layer, green = success/grounded, amber = degraded/manual/low-confidence, red = failure/blocked.
- **Consistent shapes.** Rounded rectangles = systems/steps, cylinders = data stores, dashed containers = boundaries, hexagons/side blocks = external services, numbered circles = ordered steps.
- **No fake specificity in-image.** Illustrative numbers go in the caption, marked illustrative — never as fact inside the diagram.

---

## Mermaid vs image policy

Mermaid stays the working layer (the renderer is fixed; diagrams render in strict
mode). **Promote a mermaid diagram to a polished image only when one is true:**

- The page is hard to understand without the diagram.
- The diagram is reused in interviews, customer calls, or portfolio material.
- It carries architecture boundaries, data flow, trust boundaries, or failure paths that benefit from visual hierarchy.
- It's already acting like a flagship, not a quick sketch.

**Keep as mermaid** (do not promote): decision trees, simple process flows, and
quick sketches — e.g. `do-we-need-an-agent` decision tree, `managed-vs-self-host`
decision flow, the POC lifecycle strip, the next-token loop. These render fine and
gain little as images.

---

## Track A — Showcase images (prioritized)

Each needs a filled content spec in `visual-specs/showcase-prompts.md` before
generation. Build **one end-to-end first** (the four-layer map) to lock the style,
then batch the rest. Status legend: 🔜 spec ready · 📝 brief only.

| Wave | Name / file slug | Used on | Image brief | Must show | Keep out of image | Status |
| --- | --- | --- | --- | --- | --- | --- |
| **1** | `four-layer-map` | `visuals/four-layer-map.md`, `foundations/the-four-layer-map.md` | The signature dual-labeled ecosystem stack. | L1–L4 layers, the engineer term **and** the exec one-liner per layer, "depends on" arrows down the stack. | The full audience-lens table; per-layer tool lists. | 🔜 |
| **1** | `rag-two-loops` | Lab 02, RAG lessons (Phase 2) | The canonical RAG diagram: offline indexing vs live query. | Indexing loop (docs → chunk → embed → vector DB) and query loop (question → embed → search → assemble prompt → LLM → grounded answer + citations); the "LLM only sees retrieved passages" insight. | Chunk-size guidance, pricing, framework names. | 🔜 |
| **1** | `hub-and-spoke` | `foundations/langgraph-how-to.md`, Lab 03 (Phase 2) | Orchestrator-worker agent pattern (the production default). | Orchestrator, specialized workers (search/compute/write), route-out and return arrows, final answer; one MCP tool. | "Why not a mesh" discussion; LangGraph code. | 🔜 |
| **2** | `production-rag-pipeline` | Lab 02, RAG retrieval lesson | Advanced retrieval path. | Hybrid retrieval (keyword + vector, RRF fusion) → top-50 → cross-encoder rerank → top-5 → LLM. | Exact recall/accuracy numbers (caption, illustrative). | 📝 |
| **2** | `eval-as-a-gate` | Lab 04, "how good is good enough" frame (Phase 3) | Evaluation as a CI deploy gate. | Prod-traffic sample → eval suite (LLM-as-judge + metrics) → pass/regress decision → block or ship; version traceability. | Specific metric thresholds (caption, illustrative). | 📝 |
| **3** | `inference-serving-path` | L2 lessons, Lab 05 (serving + cost) | How an open model is served efficiently. | Request → gateway (LiteLLM) → serving engine (vLLM/SGLang) with batching → quantized model on GPU → response; cost/latency callouts. | Exact \$/latency figures (caption, illustrative). | 📝 |
| **3** | `governance-stack` | L4 governance lesson (Phase 4) | The three-instrument governance stack + runtime guardrails. | NIST AI RMF (method), EU AI Act (law), ISO 42001 (certifiable evidence); guardrails enforced at the gateway; audit trail. | Clause-level detail; per-framework checklists. | 📝 |
| **3** | `llm-observability` | Lab 06 (Phase 5) | Tracing and cost across an LLM pipeline. | Instrumented calls → trace store (Langfuse) → latency/cost/quality dashboards; the boundary between retrieval and generation. | Dashboard screenshots; exact cost numbers. | 📝 |
| **3** | `capstone-architecture` | Lab 07 (Phase 5) | End-to-end RAG-agent app. | The whole stack: app → agent (LangGraph) → RAG tool + other tools → serving → vector DB → observability; optional cloud-deploy boundary. | Step-by-step build instructions. | 📝 |

> **Bounded scope:** ~8 showcase images for the full project. Wave 1 (three
> images) anchors what's live now and in Phase 2. Don't batch ahead of need —
> generate a wave as its pages come up.

---

## Track B — Stay mermaid (candidate promotion later)

These render fine as mermaid and only get promoted if they become recurring
teaching/interview artifacts:

- `do-we-need-an-agent` — decision tree
- `managed-vs-self-host` — decision flow
- `rag-tco` — cost-component breakdown
- `scoping-an-ai-poc` — POC lifecycle strip
- `how-llms-actually-work` — next-token loop

---

## File conventions

- Save images to `assets/diagrams/<slug>.png` (mirrors the sibling repos).
- Embed with descriptive alt text: `![<what it shows>](../assets/diagrams/<slug>.png)`.
- Keep the filled content spec for each in `visual-specs/showcase-prompts.md` — the
  spec is the durable record; the PNG is regenerable from it.
- Put illustrative numbers in the page caption under the image, marked illustrative.
