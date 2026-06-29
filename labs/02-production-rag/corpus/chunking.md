# Chunking

Chunking is splitting documents into passages, because a RAG system retrieves and
injects passages, not whole files. It is the most underrated decision in the
pipeline.

## Why chunk size matters

Chunk too big and you waste prompt space and bury the relevant sentence in noise.
Chunk too small and you sever the context that makes a sentence meaningful. There is
no universal best size — it depends on the documents.

## Strategies

Fixed-size chunking splits on a character or token count. Semantic chunking splits on
topic boundaries. Structure-aware chunking respects headings, paragraphs, and code
blocks. A common starting point is roughly 300 to 800 tokens per chunk with a small
overlap, so a sentence cut at a boundary still appears whole in a neighboring chunk.
Tune by inspecting what retrieval actually returns.
