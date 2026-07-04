"""Lab 06 - a small RAG app instrumented with Langfuse tracing + cost.

Two spans per question: retrieve (a "retriever" observation) and generate (a
"generation" observation), both nested under one trace. Works with or without
real Langfuse credentials - the SDK logs an auth warning and skips the upload
rather than crashing the app, so the chat still works if you haven't set up
Langfuse yet; you just won't see traces in a dashboard.
"""

import os
import sys
import time

from dotenv import load_dotenv
from langfuse import Langfuse

from provider import get_chat
from retrieve import retrieve

load_dotenv()

langfuse = Langfuse()  # reads LANGFUSE_PUBLIC_KEY / LANGFUSE_SECRET_KEY / LANGFUSE_HOST from env

# $ per 1M tokens, illustrative (see Lab 05's cost.py for the same pattern).
# Local Ollama is $0; hosted backends get an approximate published rate.
_COST_PER_M = {
    "ollama": {"input": 0.0, "output": 0.0},
    "groq": {"input": 0.05, "output": 0.08},
    "openai": {"input": 0.20, "output": 1.25},
}


def ask(question: str) -> tuple[str, str | None]:
    backend = os.environ.get("MODEL_BACKEND", "ollama").lower()

    with langfuse.start_as_current_observation(name="lab06-ask", as_type="span", input=question) as trace:
        trace_id = trace.trace_id

        with langfuse.start_as_current_observation(name="retrieve", as_type="retriever", input=question) as retrieval:
            passages = retrieve(question)
            retrieval.update(output=[p["source"] for p in passages])

        context = "\n\n".join(p["text"] for p in passages)
        prompt = (
            "Answer the question using only the context below. If the answer "
            "isn't in the context, say you don't know.\n\n"
            f"Context:\n{context}\n\nQuestion: {question}"
        )

        client, model = get_chat()
        with langfuse.start_as_current_observation(
            name="generate", as_type="generation", input=question, model=model
        ) as generation:
            t0 = time.time()
            resp = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
            latency_s = time.time() - t0
            answer = resp.choices[0].message.content
            usage = resp.usage
            rate = _COST_PER_M.get(backend, {"input": 0.0, "output": 0.0})
            cost = (usage.prompt_tokens * rate["input"] + usage.completion_tokens * rate["output"]) / 1_000_000
            generation.update(
                output=answer,
                usage_details={"input": usage.prompt_tokens, "output": usage.completion_tokens},
                cost_details={"total": cost},
                metadata={"latency_s": round(latency_s, 2)},
            )

        trace.update(output=answer)

    langfuse.flush()
    try:
        trace_url = langfuse.get_trace_url(trace_id=trace_id)
    except Exception:
        # No Langfuse keys configured (or invalid ones) - the client disables
        # itself rather than raising when you *start* a span, but asking a
        # disabled client for a trace URL raises. The app should still work.
        trace_url = None
    return answer, trace_url


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "Why do traces matter for LLM apps?"
    answer, trace_url = ask(q)
    print(f"\nQ: {q}\nA: {answer}\n")
    if trace_url:
        print(f"Trace: {trace_url}")
    else:
        print("Trace: not available (set LANGFUSE_PUBLIC_KEY/SECRET_KEY in .env to see it in a dashboard)")
