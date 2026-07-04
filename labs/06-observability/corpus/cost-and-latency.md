# Cost and Latency

Every LLM call has two numbers worth tracking per request: tokens (input and
output, which drive cost) and time-to-first-token plus total duration (which
drive perceived speed).

## Why track them per-request, not just in aggregate

An average cost or average latency hides the requests that actually hurt —
the one user question that triggered a 10x-longer retrieval, or the one
session that burned through most of a day's token budget. Per-request
tracking is what lets you find those outliers instead of averaging them away.

## Where the numbers come from

Most providers return usage (input/output token counts) on every response.
Cost is usage multiplied by the provider's published per-token price. Latency
is just wall-clock time around the call, split into time-to-first-token and
total completion time if the response is streamed.
