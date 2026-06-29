"""Lab 01 · Step 2 — function calling (tools), provider-agnostic.

A model on its own can only produce text. "Function calling" lets it ask *your*
code to do something — look up the weather, query a database, hit an API — and then
answer using the result. The model decides *when* to call; your code decides *what
the call actually does*.

The flow: send the question + a tool spec → the model replies with a tool call →
you run the real function → you send the result back → the model writes the final
answer. Run with `make tools`. Works on any backend that supports tool calling
(Ollama with a tool-capable model, Groq, OpenAI).
"""

import json

from provider import get_client_and_model

client, MODEL = get_client_and_model()


# --- The actual tool: ordinary Python the model is allowed to invoke. ----------
def get_weather(city: str) -> str:
    """Illustrative stub. A real tool would call a weather API here."""
    fake = {
        "paris": "18°C, clear",
        "london": "12°C, light rain",
        "tokyo": "24°C, humid",
    }
    return fake.get(city.lower(), f"No data for {city} (this is a demo stub).")


# --- The tool spec the model sees: name, description, and typed arguments. -----
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g. Paris"}
                },
                "required": ["city"],
            },
        },
    }
]

AVAILABLE = {"get_weather": get_weather}


def main() -> None:
    question = "What's the weather in Paris right now?"
    print(f"you ▸ {question}\n")

    messages = [{"role": "user", "content": question}]
    first = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
    msg = first.choices[0].message

    if not msg.tool_calls:
        # The model chose to answer directly without a tool.
        print("ai  ▸", msg.content)
        return

    # The model asked us to run one or more tools. Run them and feed results back.
    messages.append(msg)  # the assistant turn that contains the tool call(s)
    for call in msg.tool_calls:
        name = call.function.name
        args = json.loads(call.function.arguments or "{}")
        print(f"... model requested {name}({args})")
        result = AVAILABLE[name](**args) if name in AVAILABLE else "unknown tool"
        messages.append(
            {"role": "tool", "tool_call_id": call.id, "content": str(result)}
        )

    final = client.chat.completions.create(model=MODEL, messages=messages)
    print("ai  ▸", final.choices[0].message.content)


if __name__ == "__main__":
    main()
