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

## Waves 2–3

Briefs are in [`IMAGERY-PLAN.md`](../IMAGERY-PLAN.md) (Track A table). Promote each
to a full spec here — same format as Wave 1 — when its page is being built:

- `production-rag-pipeline` (Wave 2)
- `eval-as-a-gate` (Wave 2)
- `inference-serving-path` (Wave 3)
- `governance-stack` (Wave 3)
- `llm-observability` (Wave 3)
- `capstone-architecture` (Wave 3)
