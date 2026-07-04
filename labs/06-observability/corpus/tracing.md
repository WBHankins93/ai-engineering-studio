# Tracing

A trace is the full record of one request through a system — every step it took,
in order, with timing. For an LLM app, a trace typically has at least two child
spans: retrieval (if the app does RAG) and generation (the model call itself).

## Why traces matter more for LLM apps than typical web apps

A normal web request either works or throws an error. An LLM request can
"succeed" — return a 200, return text — and still be wrong: it retrieved the
wrong passage, or it ignored the passage it was given. A trace lets you see
which step actually went wrong, not just that the final answer was bad.

## What belongs in a trace

Input and output at each step, the model and parameters used, latency per step,
and enough metadata (user id, session id, environment) to reconstruct what
happened without re-running the request.
