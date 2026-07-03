# Lab 04 · Eval Harness — provider-agnostic, local-first ($0 on Ollama).
# `make help` lists targets. Choose backends in .env (see .env.example).

.PHONY: help env setup eval clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template
	cp -n .env.example .env && echo "wrote .env — edit it to choose backends"

setup:  ## Install Python dependencies
	python3 -m pip install -r requirements.txt

eval:  ## Run the eval + gate (exits non-zero on failure — this is the CI gate)
	python3 run_eval.py

clean:  ## Remove Python caches
	rm -rf __pycache__
