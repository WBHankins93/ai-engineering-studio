"""Model-backend resolver for Lab 02 — chat + embeddings, provider-agnostic.

Same idea as Lab 01: talk to an OpenAI-compatible API and point base_url wherever.
RAG needs two model types:

  - CHAT       — generates the grounded answer (MODEL_BACKEND: ollama | groq | openai)
  - EMBEDDINGS — turns text into vectors for retrieval (EMBED_BACKEND: ollama | openai)

Embeddings and chat are configured separately because some chat providers (Groq)
don't serve embeddings — so you can run chat on Groq while embeddings stay on local
Ollama. See labs/model-backends.md.
"""

import os

from dotenv import load_dotenv
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


def _resolve(table: dict, backend: str, model_env: str):
    cfg = table.get(backend)
    if cfg is None:
        raise SystemExit(f"Unknown backend {backend!r}. Options: {', '.join(table)}")
    api_key = cfg.get("api_key") or os.environ.get(cfg.get("api_key_env", ""), "")
    if not api_key:
        raise SystemExit(f"Backend {backend} needs {cfg['api_key_env']} set (put it in .env).")
    base_url = cfg["base_url"]
    model = os.environ.get(model_env, cfg["model"])
    return OpenAI(base_url=base_url, api_key=api_key), model


def get_chat():
    """Return (client, model) for generation."""
    return _resolve(_CHAT, os.environ.get("MODEL_BACKEND", "ollama").lower(), "MODEL")


def get_embedder():
    """Return (client, model) for embeddings (defaults to local Ollama)."""
    return _resolve(_EMBED, os.environ.get("EMBED_BACKEND", "ollama").lower(), "EMBED_MODEL")


def embed(client, model, texts: list[str]) -> list[list[float]]:
    """Embed a batch of strings -> list of vectors."""
    resp = client.embeddings.create(model=model, input=texts)
    return [d.embedding for d in resp.data]
