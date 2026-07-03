"""Turn bench.py's measured tokens/sec into a self-host vs hosted-API cost table.

Self-host cost is derived from what you actually measured (real, this machine).
Hosted prices below are published rates, checked against provider pricing pages
on 2026-07-03 — re-verify before quoting a customer; providers change prices
often and this file will drift.
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

GPU_HOURLY_USD = float(os.environ.get("GPU_HOURLY_USD", "0.50"))

# $ per 1M tokens. Sourced from provider pricing pages, 2026-07-03.
HOSTED_PRICING = {
    "Groq — Llama 3.1 8B Instant": {"input": 0.05, "output": 0.08},
    "Groq — Llama 3.3 70B Versatile": {"input": 0.59, "output": 0.79},
    "OpenAI — gpt-5.4-nano": {"input": 0.20, "output": 1.25},
    "OpenAI — gpt-5.4-mini": {"input": 0.75, "output": 4.50},
}


def self_host_cost_per_million(tok_per_s: float) -> float:
    """$ per 1M output tokens if this GPU/instance served this stream nonstop.

    Illustrative simplification: assumes one continuous stream at the measured
    throughput. Real serving batches concurrent requests, which raises
    effective tokens/sec per dollar — this is a conservative (worst-case)
    floor, not a batched-production estimate. See the lab's go-deeper note.
    """
    tokens_per_hour = tok_per_s * 3600
    return (GPU_HOURLY_USD / tokens_per_hour) * 1_000_000


def main():
    results_path = Path(__file__).with_name("results.json")
    if not results_path.exists():
        raise SystemExit("No results.json — run `make bench` first.")
    results = json.loads(results_path.read_text())

    print(f"Self-host assumption: ${GPU_HOURLY_USD:.2f}/hr GPU or instance (set GPU_HOURLY_USD in .env)\n")
    print(f"{'model':<34} {'tok/s':>8}  {'$/1M output tok (self-host)':>28}")
    for r in results:
        cost = self_host_cost_per_million(r["avg_tok_per_s"])
        print(f"{r['model']:<34} {r['avg_tok_per_s']:>8.1f}  {cost:>28.4f}")

    print(f"\n{'Hosted tier':<34} {'$/1M input':>12} {'$/1M output':>14}")
    for name, price in HOSTED_PRICING.items():
        print(f"{name:<34} {price['input']:>12.2f} {price['output']:>14.2f}")

    fastest = max(results, key=lambda r: r["avg_tok_per_s"])
    fastest_cost = self_host_cost_per_million(fastest["avg_tok_per_s"])
    cheapest_hosted_name = min(HOSTED_PRICING, key=lambda k: HOSTED_PRICING[k]["output"])
    cheapest_hosted = HOSTED_PRICING[cheapest_hosted_name]["output"]
    print(
        f"\nAt ${GPU_HOURLY_USD:.2f}/hr, your fastest local model "
        f"({fastest['model']}) costs ~${fastest_cost:.3f} per 1M output tokens "
        f"self-hosted — one continuous stream, no batching — versus "
        f"${cheapest_hosted:.2f} for the cheapest hosted tier above "
        f"({cheapest_hosted_name}). Batching concurrent requests is what makes "
        f"self-host competitive at real volume; see the cost-at-scale decision frame."
    )


if __name__ == "__main__":
    main()
