"""Lab 01 · Step 1 — a streaming chat CLI against a local model.

Talks to Ollama running on your machine. Nothing leaves your laptop and it costs
$0. Run with `make chat` (or `python chat.py`).

The whole point of this file: an LLM app is a loop that (1) collects a message,
(2) sends the running conversation to the model, (3) streams the reply back token
by token, and (4) remembers the reply so the next turn has context. That's it.
"""

import os
import sys

from ollama import chat

# Canonical cast: a small local model served by Ollama. Override with MODEL=...
MODEL = os.environ.get("MODEL", "llama3.1:8b")

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
            for part in chat(model=MODEL, messages=messages, stream=True):
                chunk = part["message"]["content"]
                print(chunk, end="", flush=True)
                reply += chunk
        except Exception as exc:  # noqa: BLE001 — surface setup errors plainly
            print(f"\n[error talking to Ollama: {exc}]")
            print("Is Ollama running, and have you pulled the model? (make pull)")
            sys.exit(1)

        print("\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
