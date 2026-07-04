# Lab 06 · Observability - provider-agnostic, local-first ($0 on Ollama +
# Langfuse's free tier). `make help` lists targets. Choose backends in .env.

MODEL ?= llama3.1:8b

.PHONY: help env setup pull ask clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template
	cp -n .env.example .env && echo "wrote .env — add your Langfuse keys to see traces in a dashboard"

setup:  ## Install Python dependencies
	python3 -m pip install -r requirements.txt

pull:  ## (Ollama backend only) download the chat + embedding models, one-time
	ollama pull $(MODEL)
	ollama pull nomic-embed-text

ask:  ## Ask a question, e.g. make ask Q="why do traces matter?"
	python3 app.py "$(Q)"

clean:  ## Remove Python caches
	rm -rf __pycache__
