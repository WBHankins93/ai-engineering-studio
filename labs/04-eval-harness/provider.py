"""Model-backend resolver for Lab 04 — the app-under-test and the judge.

Provider-agnostic (see labs/model-backends.md). Two roles:
  - the SUT (system under test) uses the main chat backend
  - the JUDGE can point at a *different, stronger* model — a common technique to
    make LLM-as-judge more reliable. Defaults to the same backend/model as the SUT.
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


def _resolve(backend: str, model_env: str, default_model_backend: str):
    cfg = _CHAT.get(backend)
    if cfg is None:
        raise SystemExit(f"Unknown backend {backend!r}. Options: {', '.join(_CHAT)}")
    api_key = cfg.get("api_key") or os.environ.get(cfg.get("api_key_env", ""), "")
    if not api_key:
        raise SystemExit(f"Backend {backend} needs {cfg['api_key_env']} set (put it in .env).")
    model = os.environ.get(model_env, cfg["model"])
    return OpenAI(base_url=cfg["base_url"], api_key=api_key), model


def get_sut():
    """The system under test: (client, model)."""
    return _resolve(os.environ.get("MODEL_BACKEND", "ollama").lower(), "MODEL", "ollama")


def get_judge():
    """The judge: (client, model). Falls back to the SUT backend/model."""
    backend = os.environ.get("JUDGE_BACKEND", os.environ.get("MODEL_BACKEND", "ollama")).lower()
    # JUDGE_MODEL overrides; else fall back to MODEL, else the backend default.
    if "JUDGE_MODEL" not in os.environ and "MODEL" in os.environ:
        os.environ.setdefault("JUDGE_MODEL", os.environ["MODEL"])
    return _resolve(backend, "JUDGE_MODEL", "ollama")
