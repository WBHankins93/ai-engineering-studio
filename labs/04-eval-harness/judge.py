"""LLM-as-judge — score an answer against per-case criteria.

The judge is itself an LLM, so it can be wrong in the same ways the system it's
grading is. Three techniques here reduce that noise:
  1. A strict, explicit rubric (grade against *criteria*, not vibes).
  2. A structured verdict (PASS/FAIL + one-line reason) that's easy to parse.
  3. The option to use a stronger judge model than the SUT (JUDGE_MODEL in .env).

This is still an approximation — calibrate it against a few human labels before you
trust it as a gate.
"""

import provider

_client, _model = provider.get_judge()

RUBRIC = (
    "You are a strict evaluator. Grade the CANDIDATE answer against the CRITERIA for "
    "the given INPUT. Judge only whether the candidate satisfies the criteria — not "
    "whether it is eloquent. Refusals are correct when the criteria require them.\n"
    "Respond on two lines exactly:\n"
    "VERDICT: PASS or FAIL\n"
    "REASON: <one short sentence>"
)


def grade(question: str, criteria: str, candidate: str) -> tuple[bool, str]:
    resp = _client.chat.completions.create(
        model=_model,
        temperature=0,
        messages=[
            {"role": "system", "content": RUBRIC},
            {
                "role": "user",
                "content": (
                    f"INPUT: {question}\nCRITERIA: {criteria}\nCANDIDATE: {candidate}"
                ),
            },
        ],
    )
    text = resp.choices[0].message.content
    verdict_line = next((l for l in text.splitlines() if "VERDICT" in l.upper()), "")
    reason_line = next((l for l in text.splitlines() if "REASON" in l.upper()), "")
    passed = "PASS" in verdict_line.upper()
    reason = reason_line.split(":", 1)[-1].strip() if ":" in reason_line else text.strip()
    return passed, reason
