# Lab 02 · Production RAG — provider-agnostic, local-first ($0 on Ollama).
# `make help` lists targets. Choose backends in .env (see .env.example).

.PHONY: help env setup ingest ask eval clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template
	cp -n .env.example .env && echo "wrote .env — edit it to choose backends"

setup:  ## Install Python dependencies
	pip install -r requirements.txt

ingest:  ## Build the index from corpus/ (run once, and when docs change)
	python ingest.py

ask:  ## Ask a question, e.g. make ask Q="what is reranking?"
	python rag.py "$(Q)"

eval:  ## Run the groundedness eval over eval/qa.json
	python evaluate.py

clean:  ## Remove the local index and Python caches
	rm -rf .qdrant __pycache__
