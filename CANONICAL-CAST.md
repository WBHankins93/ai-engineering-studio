# Canonical Cast

Reuse these systems across pages so the repo reads authored, not assembled.
Vendor-neutral as *categories*, concrete as *examples*. Keep tool names isolated
here — a swap should be one edit.

| Category | Example used |
| --- | --- |
| Local serving | Ollama + Llama 3.x 8B |
| Embeddings | bge / nomic-embed |
| Vector DB | Qdrant |
| Tracing / observability | Langfuse |
| Eval | promptfoo / DeepEval (+ RAGAS for RAG) |
| Orchestration | LangGraph (the standard — see ADR 001) |
| Model gateway | LiteLLM |
| Production serving (lessons) | vLLM / SGLang |

Names illustrate a *category*, not an endorsement. Pages stay vendor-neutral; the
example stays concrete.
