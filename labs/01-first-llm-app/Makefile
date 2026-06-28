# Lab 01 · First LLM App — local-first, $0 on Ollama.
# `make help` lists targets. Override the model with: make chat MODEL=qwen2.5:7b

MODEL ?= llama3.1:8b

.PHONY: help setup pull chat tools clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

setup:  ## Install Python dependencies
	pip install -r requirements.txt

pull:  ## Download the local model via Ollama (one-time, a few GB)
	ollama pull $(MODEL)

chat:  ## Run the streaming chat CLI (Step 1)
	python chat.py

tools:  ## Run the function-calling example (Step 2)
	python tools.py

clean:  ## Remove Python caches
	rm -rf __pycache__ .pytest_cache
