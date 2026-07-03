# Lab 05 · Serving & Cost — provider-agnostic wrapper not needed here: this lab
# measures local Ollama directly (it's the point). $0, needs Ollama installed.
# `make help` lists targets. Choose models to compare in .env (see .env.example).

.PHONY: help env setup pull bench report clean

help:  ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

env:  ## Create .env from the template
	cp -n .env.example .env && echo "wrote .env — edit MODELS/GPU_HOURLY_USD to change the comparison"

setup:  ## Install Python dependencies
	python3 -m pip install -r requirements.txt

pull:  ## Download the two model variants being compared (a few GB, one-time)
	ollama pull llama3.2:3b
	ollama pull llama3.2:3b-instruct-fp16

bench:  ## Measure real tokens/sec and time-to-first-token for each model
	python3 bench.py

report:  ## Turn bench.py's results.json into a self-host vs hosted-API cost table
	python3 cost.py

clean:  ## Remove results and Python caches
	rm -rf __pycache__ results.json
