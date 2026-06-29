# Lab 01 · First LLM App — provider-agnostic (local Ollama or hosted).
# `make help` lists targets. Choose a backend in .env (see .env.example).

MODEL ?= llama3.1:8b

.PHONY: help env setup pull chat tools clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template (then edit to pick a backend)
	cp -n .env.example .env && echo "wrote .env — edit it to choose a backend"

setup:  ## Install Python dependencies
	pip install -r requirements.txt

pull:  ## (Ollama backend only) download the local model, one-time
	ollama pull $(MODEL)

chat:  ## Run the streaming chat CLI (Step 1)
	python chat.py

tools:  ## Run the function-calling example (Step 2)
	python tools.py

clean:  ## Remove Python caches
	rm -rf __pycache__ .pytest_cache
