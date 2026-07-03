"""Lab 04 · The eval harness + regression gate.

Runs every case in dataset.json through the app, grades each with the LLM judge,
prints a report, and **exits non-zero if the pass rate falls below the baseline
threshold** — which is what lets it gate a CI pipeline (a failing exit blocks a merge).

Run with `make eval`. Tune the bar in baseline.json.
"""

import json
import sys

from app import answer
from judge import grade


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    cases = load("dataset.json")
    baseline = load("baseline.json")
    threshold = baseline["pass_rate_threshold"]

    passed = 0
    print(f"Running {len(cases)} cases...\n")
    for case in cases:
        out = answer(case["input"])
        ok, reason = grade(case["input"], case["criteria"], out)
        passed += ok
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] {case['id']}: {out[:70]!r}")
        if not ok:
            print(f"       ↳ judge: {reason}")

    rate = passed / len(cases) if cases else 0.0
    print(f"\nPass rate: {passed}/{len(cases)} = {rate:.0%}  (gate: >= {threshold:.0%})")

    if rate < threshold:
        print("GATE: FAIL — below threshold. (In CI this exit code blocks the merge.)")
        sys.exit(1)
    print("GATE: PASS")


if __name__ == "__main__":
    main()
