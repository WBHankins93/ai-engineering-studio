"""Lab 02 · Evaluation — a lightweight groundedness/correctness gate.

A demo RAG that "kind of works" takes an afternoon; one you trust takes a way to
measure it. This is the minimal version: for each question in eval/qa.json, run the
RAG pipeline and let an LLM judge whether the answer matches the reference. Prints a
pass rate.

This is intentionally light — Lab 04 builds a real eval harness (LLM-as-judge +
regression gate in CI). Run with `make eval`.
"""

import json

import provider
from rag import answer

JUDGE_SYSTEM = (
    "You are a strict grader. Given a QUESTION, a REFERENCE answer, and a CANDIDATE "
    "answer, reply with exactly 'PASS' if the candidate is consistent with the "
    "reference (including correctly declining when the reference declines), or 'FAIL' "
    "otherwise. Reply with only PASS or FAIL."
)


def judge(client, model, question, reference, candidate) -> bool:
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": JUDGE_SYSTEM},
            {
                "role": "user",
                "content": (
                    f"QUESTION: {question}\nREFERENCE: {reference}\n"
                    f"CANDIDATE: {candidate}"
                ),
            },
        ],
    )
    return "PASS" in resp.choices[0].message.content.strip().upper()


def main() -> None:
    with open("eval/qa.json", encoding="utf-8") as f:
        cases = json.load(f)

    judge_client, judge_model = provider.get_chat()
    passed = 0
    for case in cases:
        cand, _sources = answer(case["question"])
        ok = judge(judge_client, judge_model, case["question"], case["reference"], cand)
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {case['question']}")

    total = len(cases)
    pct = round(100 * passed / total) if total else 0
    print(f"\nGrounded/correct on {passed}/{total} ({pct}%).")
    print("Illustrative gate: a real pipeline sets an agreed bar (see the POC playbook).")


if __name__ == "__main__":
    main()
