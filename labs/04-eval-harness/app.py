"""The system under test (SUT) — a tiny assistant we want to evaluate.

In a real project this would be your RAG pipeline or agent. Here it's a concise
support-style answerer, kept simple so the lab focuses on the *evaluation*, not the
app. The one interesting behavior: it's told to decline when it doesn't know, which
the eval checks for.
"""

import provider

_client, _model = provider.get_sut()

SYSTEM = (
    "You are a concise customer-support assistant for an online store. Answer in one "
    "or two sentences. If the question is outside store support or you cannot know the "
    "answer, reply exactly: 'I can't help with that.'"
)


def answer(question: str) -> str:
    resp = _client.chat.completions.create(
        model=_model,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": question},
        ],
    )
    return resp.choices[0].message.content.strip()
