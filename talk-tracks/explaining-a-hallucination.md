---
tags:
  - talk-track
  - apps-agents
  - customer-facing
---
# Explaining a Hallucination

## 📝 Context

Battle cards for the moment the model says something confidently wrong — often in a
live demo. The goal is to keep trust intact and redirect to the fix. Keep these to
one clean line each; don't over-explain in the room.

Reach for this when the model just produced a confident, wrong answer in front of a
customer, **or** someone asks "how do we know it won't just make things up?" The
*why* behind these lines is in
[How LLMs Actually Work](/foundations/how-llms-actually-work).

> **The core move:** don't defend the model and don't panic. *Name it plainly,
> reframe it as expected, point at the fix.* Honesty here builds more trust than a
> save attempt.

## 🗣️ The Cards

### It just hallucinated, live, in the demo

<div class="sp-say">
  <div class="sp-label">Say it like this</div>
  <p>"That's a hallucination — and it's exactly what we design against. The model
  predicts fluent text, so when it isn't grounded in your documents it can sound
  certain and be wrong. In production we constrain it to answer only from your sources
  and say 'I don't know' otherwise. Let me show you that guardrail."</p>
</div>

### "How do we know it won't just make things up?"

<div class="sp-say">
  <div class="sp-label">Say it like this</div>
  <p>"You don't take it on faith — you measure it. We ground every answer in your
  approved content with citations you can click, and we run an eval suite that scores
  how often it stays grounded. 'Trust me' isn't the answer; 'here's the score and here
  are the receipts' is."</p>
</div>

### "Can't you just use a smarter / bigger model?"

<div class="sp-say">
  <div class="sp-label">Say it like this</div>
  <p>"A bigger model helps with reasoning, but it doesn't fix this — an ungrounded
  question gets a confident guess from any model. The fix is retrieval and guardrails,
  not horsepower. It's usually cheaper and more reliable than upgrading the model."</p>
</div>

### "So it's unreliable and we can't use it?" (the over-correction)

<div class="sp-say">
  <div class="sp-label">Say it like this</div>
  <p>"It's reliable *within a design that accounts for this.* We don't deploy a raw
  model and hope — we ground it, cite sources, and set it to defer when it's unsure.
  Used that way, it's dependable; the failure mode is using it naked, which we don't
  do."</p>
</div>

## ⚠️ What Not to Say

| Don't | Why |
| --- | --- |
| "That's weird, it usually works." | Sounds like you don't understand your own system. |
| "The model is just wrong sometimes." | True but fatalistic — gives no path forward. |
| Silently move on and hope they missed it. | They didn't. Unaddressed, it's the thing they remember. |
| Over-explain transformers/attention. | Wrong altitude; you lose the room defending instead of redirecting. |

## 🔗 Links

- [How LLMs Actually Work](/foundations/how-llms-actually-work) — why hallucination happens
- [Scoping an AI POC](/poc-playbooks/scoping-an-ai-poc) — de-risking the demo where this bites
