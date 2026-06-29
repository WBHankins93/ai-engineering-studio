# Retrieval in RAG

Retrieval is where a RAG system's quality is won or lost. The language model only
ever sees the passages retrieval hands it — garbage retrieval means a confident
wrong answer, no matter how good the model is.

## Dense vs sparse search

Dense (vector) search matches on meaning: "reset my password" and "recover account
access" land near each other even with no shared words. Sparse search (BM25) matches
on exact keywords, so it is strong on names, codes, and rare terms that vector search
often misses.

## Hybrid retrieval

Hybrid retrieval runs both dense and sparse search and combines their results. The
standard fusion method is Reciprocal Rank Fusion (RRF), which scores each document by
the sum of 1 / (k + rank) across the two rankings, where k is a small constant such
as 60. Hybrid retrieval is the 2026 production default because it covers both
meaning-based and keyword-based matches.

## Reranking

A reranker is a second, more careful model — usually a cross-encoder — that re-scores
the fused candidates for true relevance before they reach the language model. It is
often the single cheapest quality win in RAG: retrieve a few dozen candidates with
hybrid search, then rerank down to the best five. Cross-encoders are slower per pair
than embedding search, which is why you rerank only the top candidates, not the whole
corpus.
