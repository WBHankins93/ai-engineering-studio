# Lab 03 · Agent System — provider-agnostic, local-first ($0 on Ollama).
# `make help` lists targets. Choose a backend in .env (see .env.example).

.PHONY: help env setup run mcp-check clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template
	cp -n .env.example .env && echo "wrote .env — edit it to choose a backend"

setup:  ## Install Python dependencies
	pip install -r requirements.txt

run:  ## Run the agent, e.g. make run Q="status of order C300?"
	python agent.py "$(Q)"

mcp-check:  ## List the tools the MCP server exposes (no LLM needed)
	python mcp_check.py

clean:  ## Remove Python caches
	rm -rf __pycache__
