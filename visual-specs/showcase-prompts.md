# Showcase Image Prompt Pack

Hand-off file for generating the showcase image set (GPT Image, Midjourney, etc.).
Paste the **Global Style Block** plus one **Frame Prompt** at a time. Generate one
image per frame, then review against its EXACT LABEL LIST before shipping.

- System + review rules: [`VISUAL-PROMPT-STANDARD.md`](../VISUAL-PROMPT-STANDARD.md)
- Roadmap + priorities: [`IMAGERY-PLAN.md`](../IMAGERY-PLAN.md)
- Save output to `assets/diagrams/<slug>.png`.

**Wave 1 specs are filled and ready below.** Waves 2–3 have briefs in
`IMAGERY-PLAN.md`; promote them to full specs here when their pages come up.

---

## Global Style Block (paste before every frame)

```text
Create a clean modern technical system-architecture diagram in a flat vector
infographic style. It should look like a polished architecture handoff sheet:
crisp, calm, precise, readable. Generous whitespace, precise alignment, airy
layout, white background. Systems are soft rounded rectangles with thin borders
and very light fills. Group related systems inside labeled boundary containers.
Simple flat line icons only, one per major box at most. Connectors are clean thin
arrows with short labels; arrow direction is meaningful. Do not add arrows that
are not requested.

Palette (violet brand):
- Ink / text: deep navy (#0f1923)
- Primary path / accent: violet (#6d4aff)
- Control / reliability layer: deep indigo (#3b2d8c)
- Success / grounded: green (#1a6b35)
- Warning / degraded / low-confidence: amber (#b8860b)
- Failure / blocked: red (#8b1a1a)
- Soft fills: very light tints of the above on white

Typography: clean sans-serif, short bold labels in Title Case, high contrast,
legible at presentation size. No photorealism, 3D, heavy gradients, drop-shadow
clutter, decorative noise, fake screenshots, tiny text, or dense paragraphs.

Critical accuracy rule: render every text label EXACTLY as written below. Do not
add extra words, boxes, icons, or arrows. If a label is unclear, leave it blank
rather than guessing.
```

---

## Wave 1

### 1. Four-Layer Map  → `assets/diagrams/four-layer-map.png`

```text
TITLE: The Four-Layer Map
SUBTITLE: One AI system, four layers — the engineer's term and the exec's one-liner.
CANVAS: portrait or square.

Layout: four stacked horizontal layer bands, top to bottom, each a rounded
rectangle. A thin downward arrow labeled "depends on" connects each band to the
one below. Each band has a bold left label (engineer term) and a lighter right
label (exec one-liner), separated within the same band.

Bands (top to bottom):
1. "L4 · Architecture and Governance"  | right label: "What we are allowed to build"
2. "L1 · Apps and Agents"              | right label: "The thing the user touches"
3. "L2 · LLMOps and Infra"             | right label: "The engine room: fast and affordable"
4. "L3 · MLOps and Data"               | right label: "The discipline for what we train"

Arrows:
- L4 -- "depends on" --> L1
- L1 -- "depends on" --> L2
- L2 -- "depends on" --> L3

Color: use violet for the band borders/labels; keep fills very light. No status
colors needed here.

LEGEND: none needed (single concept).

EXACT LABEL LIST:
The Four-Layer Map
One AI system, four layers — the engineer's term and the exec's one-liner.
L4 · Architecture and Governance
What we are allowed to build
L1 · Apps and Agents
The thing the user touches
L2 · LLMOps and Infra
The engine room: fast and affordable
L3 · MLOps and Data
The discipline for what we train
depends on
```

---

### 2. RAG — The Two Loops  → `assets/diagrams/rag-two-loops.png`

```text
TITLE: Retrieval-Augmented Generation — The Two Loops
SUBTITLE: Indexing happens offline and occasionally; querying happens live, per question.
CANVAS: landscape 16:9.

Layout: two horizontal lanes inside labeled boundary containers.
Top lane boundary: "Indexing — offline, when docs change"
Bottom lane boundary: "Query — live, every question"

Top lane, left to right (use violet primary path):
- "Your Docs" (cylinder) -- "load" --> "Chunk" -- "split into passages" --> "Embed" -- "text to vectors" --> "Vector DB" (cylinder)

Bottom lane, left to right:
- "Question" -- "embed query" --> "Embed Query" -- "find nearest" --> "Search" -- "top passages" --> "Build Prompt" -- "question + passages" --> "LLM" -- "grounded answer + citations" --> "Answer"

Cross-link (dashed, indigo): "Vector DB" -- "search reads the index" --> "Search"

ANNOTATIONS (small callout, not a box):
- "The LLM only ever sees the retrieved passages, never the whole library." (verified)

LEGEND: violet = primary path; indigo dashed = index reused at query time.

EXACT LABEL LIST:
Retrieval-Augmented Generation — The Two Loops
Indexing happens offline and occasionally; querying happens live, per question.
Indexing — offline, when docs change
Query — live, every question
Your Docs
Chunk
Embed
Vector DB
Question
Embed Query
Search
Build Prompt
LLM
Answer
load
split into passages
text to vectors
embed query
find nearest
top passages
question + passages
grounded answer + citations
search reads the index
The LLM only ever sees the retrieved passages, never the whole library.
```

---

### 3. Hub-and-Spoke Agent  → `assets/diagrams/hub-and-spoke.png`

```text
TITLE: Hub-and-Spoke Orchestrator-Worker
SUBTITLE: The production default for agents — one coordinator, specialized workers.
CANVAS: landscape 16:9 or square.

Layout: a central "Orchestrator" rounded rectangle (violet, prominent). Three
worker boxes arranged around it, each connected by a labeled out-arrow and a
plain return arrow. One worker connects out to an external service (hexagon).

Center:
- "Orchestrator" — subtitle inside or below: "decompose and route"

Workers (around the hub):
- "Worker: Search"
- "Worker: Compute"
- "Worker: Write"

External service (hexagon, off the Search worker):
- "MCP Tool"

Flow:
- Orchestrator -- "needs a lookup" --> Worker: Search
- Orchestrator -- "needs a calculation" --> Worker: Compute
- Orchestrator -- "needs a draft" --> Worker: Write
- Worker: Search -- "tool call" --> MCP Tool
- Worker: Search -- "result" --> Orchestrator
- Worker: Compute -- "result" --> Orchestrator
- Worker: Write -- "result" --> Orchestrator
- Orchestrator -- "done" --> "Final Answer"

ANNOTATION (small callout): "The orchestrator's task decomposition is the #1 reliability decision." (verified)

LEGEND: violet = orchestrator/primary path; indigo = the control role of the hub.

EXACT LABEL LIST:
Hub-and-Spoke Orchestrator-Worker
The production default for agents — one coordinator, specialized workers.
Orchestrator
decompose and route
Worker: Search
Worker: Compute
Worker: Write
MCP Tool
Final Answer
needs a lookup
needs a calculation
needs a draft
tool call
result
done
The orchestrator's task decomposition is the #1 reliability decision.
```

---

## Wave 4 (Phase 4 — generated, done)

### 4. Three Reference Architecture Tiers  → `assets/diagrams/reference-architecture-tiers.png`

```text
TITLE: Three Reference Architecture Tiers
SUBTITLE: Match the architecture to the stage, not the ambition.
CANVAS: landscape 16:9.

Layout: three vertically stacked horizontal bands, top to bottom, each a rounded
rectangle boundary container labeled by tier. Each band shows a simplified
left-to-right mini-flow of just its own systems. A thin downward arrow labeled
"grows into" connects each band to the one below it.

Band 1 (top) — boundary label: "Pilot — RAG-Only"
  Mini-flow: "User" -- "asks" --> "Retrieval + LLM" -- "answer" --> "User"
  Small caption under the band: "Proving one use case"

Band 2 (middle) — boundary label: "Feature — Agentic"
  Mini-flow: "User" -- "asks" --> "Orchestrator" -- "routes" --> "RAG + Tools" -- "result" --> "User"
  Small caption under the band: "The feature that acts, not just answers"

Band 3 (bottom) — boundary label: "Platform — Enterprise AI Platform"
  Mini-flow: "Many Teams" -- "calls" --> "Gateway + Guardrails" -- "routes" --> "Orchestrator + Models" -- "governed answer" --> "Many Teams"
  Small caption under the band: "Shared infra across many use cases"

Arrows between bands (indigo, dashed):
- Pilot band -- "grows into" --> Feature band
- Feature band -- "grows into" --> Platform band

Color: violet for each band's primary mini-flow arrows; indigo dashed for the
"grows into" arrows between bands. Keep fills very light per tier (slightly
darker tint as tiers increase, top to bottom) to suggest increasing weight/scale.

LEGEND: violet = primary flow within a tier; indigo dashed = growth path between tiers.

EXACT LABEL LIST:
Three Reference Architecture Tiers
Match the architecture to the stage, not the ambition.
Pilot — RAG-Only
User
Retrieval + LLM
asks
answer
Proving one use case
Feature — Agentic
Orchestrator
RAG + Tools
routes
result
The feature that acts, not just answers
Platform — Enterprise AI Platform
Many Teams
Gateway + Guardrails
Orchestrator + Models
calls
governed answer
Shared infra across many use cases
grows into
```

Used on: [`lessons/architecture-governance/reference-architectures.md`](../lessons/architecture-governance/reference-architectures.md). Generated and shipped 2026-07-03; passed self-review on first pass.

---

### 5. The Enterprise AI Platform Reference Architecture  → `assets/diagrams/enterprise-ai-platform.png`

```text
TITLE: The Enterprise AI Platform Reference Architecture
SUBTITLE: The ceiling, not the floor — most engagements scope down from this.
CANVAS: landscape 16:9.

Layout: left-to-right pipeline with one boundary container grouping the
governance layer, and a small side branch down to observability.

Systems, left to right:
- "User / App" (rounded rectangle, start)
- "Gateway (LiteLLM)" (rounded rectangle)
- "Guardrails" (rounded rectangle) — group "Gateway (LiteLLM)" and "Guardrails"
  together inside a labeled boundary container: "Governance Layer"
- "Orchestrator" (rounded rectangle, violet, prominent — this is the primary path hub)
- "RAG Tool" (rounded rectangle, below-right of Orchestrator)
- "Other Tools (MCP)" (rounded rectangle, below-right of Orchestrator, next to RAG Tool)
- "Vector DB" (cylinder, connected only from RAG Tool)
- "Model Layer (Hosted + Self-Hosted)" (rounded rectangle, right of Orchestrator)
- "Eval Gate" (diamond/decision shape, right of Model Layer)
- "Ship" (small rounded rectangle, success green, right of Eval Gate)
- "Block" (small rounded rectangle, failure red, below Eval Gate)
- "Observability (Langfuse)" (rounded rectangle, below Model Layer, connected by a
  thin indigo line — this is a side branch, not the main left-to-right path)

Flow (ordered, primary path in violet):
- User / App -- "request" --> Gateway (LiteLLM)
- Gateway (LiteLLM) -- "checked" --> Guardrails
- Guardrails -- "cleared" --> Orchestrator
- Orchestrator -- "needs context" --> RAG Tool
- Orchestrator -- "needs an action" --> Other Tools (MCP)
- RAG Tool -- "search" --> Vector DB
- Orchestrator -- "generate" --> Model Layer (Hosted + Self-Hosted)
- Model Layer (Hosted + Self-Hosted) -- "candidate answer" --> Eval Gate

Error / alt path (dashed):
- Eval Gate -- "pass" --> Ship
- Eval Gate -- "fail" --> Block

Side branch (thin indigo line, not part of primary flow):
- Model Layer (Hosted + Self-Hosted) -- "traced" --> Observability (Langfuse)

ANNOTATION (small callout, not a box): "Every layer here is a lab on this site, assembled." (verified)

LEGEND: violet = primary request path; indigo = governance/control and
observability; green = pass/ship; red = fail/block.

EXACT LABEL LIST:
The Enterprise AI Platform Reference Architecture
The ceiling, not the floor — most engagements scope down from this.
User / App
Gateway (LiteLLM)
Guardrails
Governance Layer
Orchestrator
RAG Tool
Other Tools (MCP)
Vector DB
Model Layer (Hosted + Self-Hosted)
Eval Gate
Ship
Block
Observability (Langfuse)
request
checked
cleared
needs context
needs an action
search
generate
candidate answer
pass
fail
traced
Every layer here is a lab on this site, assembled.
```

Used on: [`lessons/architecture-governance/reference-architectures.md`](../lessons/architecture-governance/reference-architectures.md). Generated and shipped 2026-07-03; dense (21 labels, over the usual 10–18 guideline) as the deliberate flagship "put it all together" shot — passed self-review on first pass, no relabeling needed.

---

### 6. The Governance Stack  → `assets/diagrams/governance-stack.png`

```text
TITLE: The Governance Stack
SUBTITLE: A method, a law, a certification — and the guardrails that enforce them.
CANVAS: portrait or landscape 16:9, whichever fits a top-to-bottom flow best.

Layout: a single top-to-bottom flow with one decision diamond partway down.

Systems, top to bottom:
- "NIST AI RMF" (rounded rectangle, violet, top)
- "EU Exposure?" (diamond, decision node)
- "EU AI Act" (rounded rectangle, violet, branch off the diamond's "yes" path)
- "Org Risk Program" (rounded rectangle, violet — where both paths converge)
- "ISO 42001 Certified AIMS" (rounded rectangle, violet)
- "Runtime Guardrails at Gateway" (rounded rectangle, indigo — this is the control/enforcement layer, visually distinct from the violet instruments above it)
- "Audit Trail" (small rounded rectangle, indigo, bottom)

Flow (ordered):
- NIST AI RMF -- "informs" --> Org Risk Program
- EU Exposure? -- "yes" --> EU AI Act
- EU Exposure? -- "no" --> Org Risk Program
- EU AI Act -- "binding rules by tier" --> Org Risk Program
- Org Risk Program -- "certified against" --> ISO 42001 Certified AIMS
- ISO 42001 Certified AIMS -- "enforced by" --> Runtime Guardrails at Gateway
- Runtime Guardrails at Gateway -- "logs" --> Audit Trail

ANNOTATION (small callout, not a box): "A method, a law, and a certification are not the same thing." (verified)

LEGEND: violet = risk-management instruments (method, law, certification); indigo = enforcement and audit — the layer that turns policy into something real.

EXACT LABEL LIST:
The Governance Stack
A method, a law, a certification — and the guardrails that enforce them.
NIST AI RMF
EU Exposure?
EU AI Act
Org Risk Program
ISO 42001 Certified AIMS
Runtime Guardrails at Gateway
Audit Trail
informs
yes
no
binding rules by tier
certified against
enforced by
logs
A method, a law, and a certification are not the same thing.
```

Used on: [`lessons/architecture-governance/guardrails-and-governance.md`](../lessons/architecture-governance/guardrails-and-governance.md). Generated and shipped 2026-07-03; took two generation attempts — the first correctly matched every label but rendered the enforcement-layer boxes (`Runtime Guardrails at Gateway`, `Audit Trail`) in the same violet tint as the risk-instrument boxes instead of the specced indigo. Fixed on the second attempt via a fresh generation (an in-place "edit this image" instruction reproduced the same unfixed image rather than actually changing the color).

---

## Waves 2–3

Briefs are in [`IMAGERY-PLAN.md`](../IMAGERY-PLAN.md) (Track A table). Promote each
to a full spec here — same format as Wave 1 — when its page is being built:

- `production-rag-pipeline` (Wave 2)
- `eval-as-a-gate` (Wave 2)
- `inference-serving-path` (Wave 3)
- `llm-observability` (Wave 3)
- `capstone-architecture` (Wave 3)

`governance-stack` (Wave 3) is done — see Wave 4, below.

---

## Wave 4 (Phase 5 polish — generated as deterministic SVG, done)

### 7. Context Window Assembly  → `assets/diagrams/context-window-assembly.png`

```text
TITLE: Context Window Assembly
SUBTITLE: The model answers from the briefing you assemble for this call.
CANVAS: landscape 16:9.

Layout: three left-to-right boundary containers:
- "INPUTS"
- "ASSEMBLY"
- "DECISION AND RECOVERY"

Inputs boundary, stacked top to bottom:
- "System Instruction" (indigo control box)
- "Question" (violet input box)
- "Retrieved Passages" (violet input box)
- "Conversation History" (violet input box)

Assembly boundary:
- "Assemble Context" (violet primary box)
- small subtitle inside the box: "order and fit the briefing"

Decision and recovery boundary:
- "Fits Window?" (amber decision diamond)
- small subtitle inside the diamond: "finite context check"
- "Model Answers" (green success box, above the diamond)
- "Compact and Retry" (amber recovery box, below the diamond)

Flow:
- System Instruction -- input arrow --> Assemble Context
- Question -- input arrow --> Assemble Context
- Retrieved Passages -- input arrow --> Assemble Context
- Conversation History -- input arrow --> Assemble Context
- Assemble Context -- "assembled prompt" --> Fits Window?
- Fits Window? -- "yes" --> Model Answers
- Fits Window? -- "no" --> Compact and Retry
- Compact and Retry -- "summarize / trim / re-retrieve" --> Assemble Context

LEGEND:
violet = context ingredients and primary path
indigo = instruction/control
green = answer path
amber = overflow recovery loop

EXACT LABEL LIST:
Context Window Assembly
The model answers from the briefing you assemble for this call.
INPUTS
ASSEMBLY
DECISION AND RECOVERY
System Instruction
Question
Retrieved Passages
Conversation History
Assemble Context
order and fit the briefing
Fits Window?
finite context check
Model Answers
Compact and Retry
assembled prompt
yes
no
summarize / trim / re-retrieve
violet = context ingredients and primary path
indigo = instruction/control
green = answer path
amber = overflow recovery loop
```

Used on: [`lessons/apps-agents/context-engineering.md`](../lessons/apps-agents/context-engineering.md). Shipped as a deterministic SVG-to-PNG asset rather than an image-model generation because the diagram's value depends on exact labels and clean arrow direction. Source retained at `assets/diagrams/context-window-assembly.svg`; PNG rendered at 1672×941 to match the other landscape showcase images.
