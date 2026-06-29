"""Lab 01 · Step 1 — a streaming chat CLI, provider-agnostic.

Talks to whatever backend you selected (local Ollama by default, or a hosted
OpenAI-compatible endpoint like Groq). Run with `make chat`.

The whole point of this file: an LLM app is a loop that (1) collects a message,
(2) sends the running conversation to the model, (3) streams the reply back token
by token, and (4) remembers the reply so the next turn has context. That's it —
and it's identical whether the model is on your laptop or behind an API.
"""

import sys

from provider import get_client_and_model

client, MODEL = get_client_and_model()

SYSTEM = (
    "You are a concise, helpful assistant. If you are unsure or the answer is not "
    "something you can know, say so plainly instead of guessing."
)


def main() -> None:
    print(f"Chat with {MODEL}  —  type a message, Ctrl+C to exit\n")

    # `messages` IS the model's memory. The model has none of its own between
    # calls; we resend the running history every turn (see foundations: context window).
    messages = [{"role": "system", "content": SYSTEM}]

    while True:
        try:
            user = input("you ▸ ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye")
            return

        if not user:
            continue

        messages.append({"role": "user", "content": user})

        print("ai  ▸ ", end="", flush=True)
        reply = ""
        try:
            # stream=True yields the reply in chunks as the model generates it,
            # which is what makes the app feel responsive.
            stream = client.chat.completions.create(
                model=MODEL, messages=messages, stream=True
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                print(delta, end="", flush=True)
                reply += delta
        except Exception as exc:  # noqa: BLE001 — surface setup errors plainly
            print(f"\n[error talking to the model: {exc}]")
            print("Check your backend: is Ollama running / is your API key set? (.env)")
            sys.exit(1)

        print("\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
