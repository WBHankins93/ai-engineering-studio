"""Shared model-backend resolver — provider-agnostic labs.

The same lab code runs against a local model (Ollama) or any OpenAI-compatible
hosted endpoint (Groq, OpenAI, Together, ...). They all speak the OpenAI API, so we
use the `openai` client and just point `base_url` somewhere different.

Pick a backend with the MODEL_BACKEND env var (default: ollama). For hosted
backends, set the matching API key. See `.env.example` and the lab's
"Choose your model backend" section.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # read a local .env if present (gitignored)

# base_url + default model per backend. `api_key` is fixed for local Ollama
# (it ignores the value but the client requires one); hosted backends read a key
# from the named env var.
BACKENDS = {
    "ollama": {
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "model": "llama3.1:8b",
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "api_key_env": "GROQ_API_KEY",
        "model": "llama-3.1-8b-instant",
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4o-mini",
    },
}


def get_client_and_model() -> tuple[OpenAI, str]:
    """Return an (OpenAI client, model name) pair for the selected backend."""
    backend = os.environ.get("MODEL_BACKEND", "ollama").lower()
    cfg = BACKENDS.get(backend)
    if cfg is None:
        raise SystemExit(
            f"Unknown MODEL_BACKEND={backend!r}. Options: {', '.join(BACKENDS)}"
        )

    api_key = cfg.get("api_key") or os.environ.get(cfg.get("api_key_env", ""), "")
    if not api_key:
        raise SystemExit(
            f"MODEL_BACKEND={backend} needs {cfg['api_key_env']} set "
            f"(put it in .env). Get a free key from the provider."
        )

    base_url = os.environ.get("OPENAI_BASE_URL", cfg["base_url"])
    model = os.environ.get("MODEL", cfg["model"])
    return OpenAI(base_url=base_url, api_key=api_key), model
