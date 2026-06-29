# Grounding and citations

Grounding means constraining the model to answer only from the retrieved passages,
cite its sources, and say it does not know when the answer is not present. It is what
turns a demo that "kind of works" into a system you can trust.

## How grounding is enforced

Grounding lives in the prompt and the system instruction: tell the model to answer
only from the supplied context, to quote sources, and to refuse to invent. A grounded
answer can be traced back to the passage that produced it.

## What grounding does and does not do

Grounding reduces hallucination — the model answers from supplied text rather than
memory — but it does not eliminate it. A model can still misread good context. That is
why evaluation is not optional: you measure how often answers stay grounded rather
than trusting vibes. Knowing whether a RAG system is good requires deliberate testing,
not a quick look at a few examples.
