# Dashboards

A dashboard turns individual traces into a trend: pass rate over time, p50/p95
latency, cost per day, which prompts or users generate the most tokens. The
trace is the record of one request; the dashboard is what tells you whether
today looks different from last week.

## What a useful LLM dashboard shows

Volume (requests per day), cost per day, latency percentiles (not just an
average — p95 catches the slow tail an average hides), and a quality signal
(pass rate from an eval gate, or a sampled human/LLM-judge score) trended over
time so a regression is visible before a customer reports it.

## The link back to the eval gate

A dashboard answers "is something wrong right now"; an eval gate (see Lab 04)
answers "does this specific change make it worse." Production observability
and pre-merge evaluation are complementary — one watches live traffic, the
other blocks a regression before it ships.
