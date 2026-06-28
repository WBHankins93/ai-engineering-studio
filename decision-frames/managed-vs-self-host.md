# Decision Frame · Managed API vs Self-Host

> The first build-vs-buy question in almost every AI deal: do we call a hosted
> model over an API, or run an open model on our own infrastructure? Here's the
> frame that gets a customer to the right answer — and the numbers conversation
> that goes with it.

::: tip The short version
For **most** teams starting out, **managed API wins** — you're buying speed and
zero ops. Self-hosting earns its keep at **high, steady volume**, under **hard
data-residency rules**, or when you need **deep customization**. The crossover is
about economics and constraints, not ideology.
:::

## The two options

| | Managed API | Self-host (open model) |
| --- | --- | --- |
| **What it is** | Call a hosted model (per-token billing) | Run an open model on your own / rented GPUs |
| **You're buying** | Speed, no ops, frontier quality | Control, privacy boundary, fixed-cost economics at scale |
| **Cost shape** | Variable, per-token — scales with usage | Mostly fixed — GPU capacity whether busy or idle |
| **Ops burden** | Near zero | Real: serving, scaling, upgrades, on-call |
| **Data boundary** | Leaves your environment (mitigable by enterprise terms) | Stays in your environment |
| **Time to first value** | Hours | Days to weeks |

## The decision flow

```mermaid
flowchart TD
  Q1{"Hard data-residency rule? (data cannot leave your environment)"}
  Q1 -->|yes| SH["Self-host the constraint decides it"]
  Q1 -->|no| Q2{"High steady volume? (over ~1M calls/yr, illustrative)"}
  Q2 -->|no| API["Managed API: speed and zero ops"]
  Q2 -->|yes| Q3{"Do you have ops capacity to run GPU serving?"}
  Q3 -->|no| API
  Q3 -->|yes| Q4{"Need deep customization or fixed-cost economics?"}
  Q4 -->|yes| SH
  Q4 -->|no| API
```

<div class="ai-context">
  <div class="ai-label">What an SE watches for</div>
  <p>The order matters: a hard data rule (L4 governance) ends the conversation
  before economics ever come up. Don't model TCO for a customer who legally can't
  send data to a hosted model — confirm the constraint first, then talk numbers.</p>
</div>

## State the numbers (illustrative — verify against their volume)

The economics hinge on **utilization**. A managed API costs you only when you use
it; a GPU costs you whether it's busy or not. So self-hosting wins when you'd keep
the hardware busy.

| Scenario | Managed API | Self-host | Who wins |
| --- | --- | --- | --- |
| Pilot / spiky traffic | pennies–low \$\$ per day, pay-as-you-go | a GPU billed 24/7, mostly idle | **Managed** |
| High, steady traffic | per-token cost adds up linearly | fixed GPU cost amortized across heavy use | **Self-host** |

::: warning Accuracy note
The "~1M calls/year" crossover is a **directional, workload-dependent** figure
from 2026 enterprise sources — not a constant. Real crossover depends on model
size, token lengths, GPU price, and utilization. Use it to frame the *shape* of
the decision; compute the actual break-even against the customer's real numbers
before putting a figure in writing.
:::

## The failure path

The classic mistake is **self-hosting too early** — a team stands up GPU
infrastructure for a pilot doing a few thousand calls a day, then spends months on
serving and on-call while paying for idle hardware.

<div class="sp-band">
  <div class="sp-step"><div class="sp-h">Symptom</div><div class="sp-d">"We're running our own model" — for a workload a managed API would serve for a few dollars a day.</div></div>
  <div class="sp-step"><div class="sp-h">Root cause</div><div class="sp-d">Treated self-hosting as the "serious" choice rather than an economics/constraints decision.</div></div>
  <div class="sp-step"><div class="sp-h">Cost</div><div class="sp-d">Idle GPU spend + ops time that should have gone into the product. The model was never the bottleneck.</div></div>
  <div class="sp-step"><div class="sp-h">Fix</div><div class="sp-d">Start managed, instrument usage, revisit self-host when real volume and a constraint justify it.</div></div>
</div>

The mirror-image failure is **ignoring a data constraint** until late — building on
a managed API, then discovering in security review the data can't leave. That's the
Q1 box; ask it first.

## Audience lens

| | Engineer hears | Exec hears | Security/legal hears |
| --- | --- | --- | --- |
| **Managed** | no infra to run, fast iteration | variable cost, scales with use | data leaves our boundary — need enterprise terms |
| **Self-host** | we own the serving stack | capex-like fixed cost, ops headcount | data stays in our environment |

## Talk track

<div class="sp-say">
  <div class="sp-label">Say it like this — to an exec</div>
  <p>"Two paths. We can call a hosted model — fastest to value, you pay per use, and
  it scales with you. Or we run an open model ourselves — more control and it gets
  cheaper at high volume, but it's real infrastructure and headcount. My
  recommendation for where you are: start hosted, measure real usage, and only move
  in-house if the volume and your data rules justify it. We won't pay for an engine
  room you don't need yet."</p>
</div>

<div class="sp-say">
  <div class="sp-label">Say it like this — when data residency comes up</div>
  <p>"If your policy is that this data can't leave your environment, that decides
  it — we self-host, and I'll size the infrastructure to your volume. Let's confirm
  that rule with your security team before we talk cost, because it changes the
  whole architecture."</p>
</div>

<div class="ai-deeper">
  <span class="ai-label">Go deeper</span>
  Total cost of a RAG system specifically (not just the model call) is worked in
  the <a href="/decision-frames/rag-tco">RAG TCO</a> frame. The hosted-data-handling
  question maps to the governance terms in
  <a href="/foundations/ai-vocabulary-for-sas">AI Vocabulary for SAs</a>.
</div>
