"""Model-backend resolver for Lab 07 — the whole stack in one file.

Three roles, same provider-agnostic pattern as every earlier lab:
  - get_chat_model()  — a LangChain chat model for the LangGraph orchestrator
  - get_embedder()    — a raw OpenAI-compatible client for RAG ingest/retrieval
  - embed()           — turn text into vectors

See labs/model-backends.md. Pick a backend with MODEL_BACKEND in .env.
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI

load_dotenv()

_CHAT = {
    "ollama": {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "llama3.1:8b"},
    "groq": {"base_url": "https://api.groq.com/openai/v1", "api_key_env": "GROQ_API_KEY", "model": "llama-3.1-8b-instant"},
    "openai": {"base_url": "https://api.openai.com/v1", "api_key_env": "OPENAI_API_KEY", "model": "gpt-4o-mini"},
}

# Embeddings: Groq is chat-only, so it's intentionally not here.
_EMBED = {
    "ollama": {"base_url": "http://localhost:11434/v1", "api_key": "ollama", "model": "nomic-embed-text"},
    "openai": {"base_url": "https://api.openai.com/v1", "api_key_env": "OPENAI_API_KEY", "model": "text-embedding-3-small"},
}


def _cfg(table: dict, backend: str):
    cfg = table.get(backend)
    if cfg is None:
        raise SystemExit(f"Unknown backend {backend!r}. Options: {', '.join(table)}")
    api_key = cfg.get("api_key") or os.environ.get(cfg.get("api_key_env", ""), "")
    if not api_key:
        raise SystemExit(f"Backend {backend} needs {cfg['api_key_env']} set (put it in .env).")
    return cfg, api_key


def get_chat_model(temperature: float = 0.0) -> ChatOpenAI:
    """A LangChain chat model, for the LangGraph orchestrator.

    Honors OPENAI_BASE_URL as an override on top of MODEL_BACKEND=openai — this
    is the one line that lets the Cloud Track (see README) point at a rented-GPU
    serving endpoint instead of api.openai.com, since any OpenAI-compatible
    endpoint (vLLM/SGLang included) works the same way.
    """
    backend = os.environ.get("MODEL_BACKEND", "ollama").lower()
    cfg, api_key = _cfg(_CHAT, backend)
    base_url = os.environ.get("OPENAI_BASE_URL", cfg["base_url"])
    model = os.environ.get("MODEL", cfg["model"])
    return ChatOpenAI(base_url=base_url, api_key=api_key, model=model, temperature=temperature)


def get_embedder():
    """Return (client, model) for embeddings (defaults to local Ollama)."""
    backend = os.environ.get("EMBED_BACKEND", "ollama").lower()
    cfg, api_key = _cfg(_EMBED, backend)
    model = os.environ.get("EMBED_MODEL", cfg["model"])
    return OpenAI(base_url=cfg["base_url"], api_key=api_key), model


def embed(client, model, texts: list[str]) -> list[list[float]]:
    """Embed a batch of strings -> list of vectors."""
    resp = client.embeddings.create(model=model, input=texts)
    return [d.embedding for d in resp.data]
