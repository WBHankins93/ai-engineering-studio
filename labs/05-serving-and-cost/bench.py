"""Benchmark local Ollama models: real latency + throughput, no manual stopwatch.

Hits Ollama's native /api/generate (not the OpenAI-compatible endpoint) because
only the native API returns per-call timing — eval_count/eval_duration give
exact tokens/sec straight from the server, and prompt_eval_duration +
load_duration approximate time-to-first-token.
"""

import json
import os
import statistics
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELS = [m.strip() for m in os.environ.get("MODELS", "llama3.2:3b,llama3.2:3b-instruct-fp16").split(",")]
RUNS = int(os.environ.get("RUNS", "3"))
PROMPTS = json.loads(Path(__file__).with_name("prompts.json").read_text())


def call(model: str, prompt: str) -> dict:
    resp = requests.post(
        OLLAMA_URL,
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()


def bench_model(model: str) -> dict:
    print(f"\n== {model} ==")
    per_prompt = []
    for case in PROMPTS:
        runs = []
        for i in range(RUNS):
            data = call(model, case["prompt"])
            eval_count = data.get("eval_count", 0)
            eval_ns = data.get("eval_duration", 1) or 1
            prompt_ns = data.get("prompt_eval_duration", 0)
            load_ns = data.get("load_duration", 0)
            tok_per_s = eval_count / (eval_ns / 1e9)
            ttft_s = (load_ns + prompt_ns) / 1e9
            runs.append({"tok_per_s": tok_per_s, "ttft_s": ttft_s, "eval_count": eval_count})
            print(f"  {case['id']} run {i + 1}/{RUNS}: {tok_per_s:.1f} tok/s, ttft {ttft_s:.2f}s")
        per_prompt.append(
            {
                "id": case["id"],
                "avg_tok_per_s": statistics.mean(r["tok_per_s"] for r in runs),
                "avg_ttft_s": statistics.mean(r["ttft_s"] for r in runs),
                "avg_eval_count": statistics.mean(r["eval_count"] for r in runs),
            }
        )
    return {
        "model": model,
        "cases": per_prompt,
        "avg_tok_per_s": statistics.mean(c["avg_tok_per_s"] for c in per_prompt),
        "avg_ttft_s": statistics.mean(c["avg_ttft_s"] for c in per_prompt),
    }


def main():
    results = [bench_model(m) for m in MODELS]
    out = Path(__file__).with_name("results.json")
    out.write_text(json.dumps(results, indent=2))
    print(f"\nWrote {out}")
    print("\nSummary (avg across prompts, first run per model includes load time):")
    print(f"{'model':<34} {'tok/s':>8} {'ttft (s)':>10}")
    for r in results:
        print(f"{r['model']:<34} {r['avg_tok_per_s']:>8.1f} {r['avg_ttft_s']:>10.2f}")
    print("\nNext: make report")


if __name__ == "__main__":
    main()
