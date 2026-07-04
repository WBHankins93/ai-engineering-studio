# Lab 07 · Capstone - the whole stack, provider-agnostic, $0 on Ollama.
# `make help` lists targets. Choose backends in .env (see .env.example).

MODEL ?= llama3.1:8b

.PHONY: help env setup pull ingest run clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template
	cp -n .env.example .env && echo "wrote .env — edit it to choose backends"

setup:  ## Install Python dependencies
	python3 -m pip install -r requirements.txt

pull:  ## (Ollama backend only) download the chat + embedding models, one-time
	ollama pull $(MODEL)
	ollama pull nomic-embed-text

ingest:  ## Build the RAG index from corpus/ (run once, and when docs change)
	python3 ingest.py

run:  ## Ask the agent, e.g. make run Q="what's your return policy?"
	python3 agent.py "$(Q)"

clean:  ## Remove the local index and Python caches
	rm -rf .qdrant __pycache__
