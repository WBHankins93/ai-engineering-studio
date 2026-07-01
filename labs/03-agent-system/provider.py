"""Model-backend resolver for Lab 03 — returns a LangChain chat model.

Same provider-agnostic idea as Labs 01–02, but LangGraph wants a LangChain chat
model. `ChatOpenAI` speaks the OpenAI API, and every backend here is OpenAI-
compatible (Ollama included), so one builder covers local + hosted. Pick a backend
with MODEL_BACKEND in .env. See labs/model-backends.md.
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

_CHAT = {
    "ollama": {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "llama3.1:8b"},
    "groq": {"base_url": "https://api.groq.com/openai/v1", "api_key_env": "GROQ_API_KEY", "model": "llama-3.1-8b-instant"},
    "openai": {"base_url": "https://api.openai.com/v1", "api_key_env": "OPENAI_API_KEY", "model": "gpt-4o-mini"},
}


def get_chat_model(temperature: float = 0.0) -> ChatOpenAI:
    """Return a LangChain ChatOpenAI wired to the selected backend."""
    backend = os.environ.get("MODEL_BACKEND", "ollama").lower()
    cfg = _CHAT.get(backend)
    if cfg is None:
        raise SystemExit(f"Unknown MODEL_BACKEND={backend!r}. Options: {', '.join(_CHAT)}")
    api_key = cfg.get("api_key") or os.environ.get(cfg.get("api_key_env", ""), "")
    if not api_key:
        raise SystemExit(f"MODEL_BACKEND={backend} needs {cfg['api_key_env']} set (put it in .env).")
    model = os.environ.get("MODEL", cfg["model"])
    return ChatOpenAI(base_url=cfg["base_url"], api_key=api_key, model=model, temperature=temperature)
