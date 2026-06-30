"""Lab 02 · Query — hybrid retrieval, rerank, grounded generation.

The live half of RAG. For a question we:
  1. Retrieve with BOTH dense (vector) and sparse (BM25 keyword) search.
  2. Fuse the two rankings with Reciprocal Rank Fusion (RRF).
  3. Rerank the fused top results with a cross-encoder (the cheapest quality win).
  4. Generate an answer grounded ONLY in the top passages, with citations.

Why hybrid + rerank: pure vector search is weak on exact terms/names/codes; BM25 is
weak on meaning. Fusing them, then reranking, is the 2026 production default. Run
with `make ask` or `python rag.py "your question"`.
"""

import sys

from rank_bm25 import BM25Okapi

import provider
from store import COLLECTION, get_store

DENSE_N = 20      # candidates from each retriever
RRF_K = 60        # RRF constant (standard)
FUSED_K = 10      # how many fused candidates to rerank
TOP_K = 5         # passages handed to the model


def _load_all(store):
    """Pull every chunk (id, text, source) — small corpus, fine to hold in memory."""
    points, _ = store.scroll(collection_name=COLLECTION, limit=10000, with_payload=True)
    return {p.id: (p.payload["text"], p.payload["source"]) for p in points}


def _dense(store, qvec, ids_order):
    res = store.query_points(collection_name=COLLECTION, query=qvec, limit=DENSE_N)
    return [p.id for p in res.points]


def _bm25(by_id, query):
    ids = list(by_id)
    corpus = [by_id[i][0].lower().split() for i in ids]
    bm = BM25Okapi(corpus)
    scores = bm.get_scores(query.lower().split())
    ranked = sorted(zip(ids, scores), key=lambda x: x[1], reverse=True)
    return [i for i, _ in ranked[:DENSE_N]]


def _rrf(*rankings):
    """Reciprocal Rank Fusion: combine ranked id lists into one score per id."""
    fused = {}
    for ranking in rankings:
        for rank, _id in enumerate(ranking):
            fused[_id] = fused.get(_id, 0.0) + 1.0 / (RRF_K + rank)
    return [i for i, _ in sorted(fused.items(), key=lambda x: x[1], reverse=True)]


_ENCODER = None


def _get_encoder():
    """Load the cross-encoder once and reuse it (loading per query is slow)."""
    global _ENCODER
    if _ENCODER is None:
        from fastembed.rerank.cross_encoder import TextCrossEncoder

        _ENCODER = TextCrossEncoder("Xenova/ms-marco-MiniLM-L-6-v2")
    return _ENCODER


def _rerank(query, candidates):
    """Cross-encoder rerank (fastembed, ONNX/CPU). Falls back to fused order."""
    try:
        encoder = _get_encoder()
        docs = [c[1] for c in candidates]  # (id, text, source)
        scores = list(encoder.rerank(query, docs))
        order = sorted(range(len(candidates)), key=lambda i: scores[i], reverse=True)
        return [candidates[i] for i in order]
    except Exception as exc:  # noqa: BLE001 — rerank is an optimization, not required
        print(f"[rerank skipped: {exc}]", file=sys.stderr)
        return candidates


def retrieve(query: str):
    """Return the top-K (id, text, source) passages for a query."""
    store = get_store()
    by_id = _load_all(store)

    embed_client, embed_model = provider.get_embedder()
    qvec = provider.embed(embed_client, embed_model, [query])[0]

    dense_ids = _dense(store, qvec, by_id)
    bm25_ids = _bm25(by_id, query)
    fused_ids = _rrf(dense_ids, bm25_ids)[:FUSED_K]

    candidates = [(i, by_id[i][0], by_id[i][1]) for i in fused_ids if i in by_id]
    return _rerank(query, candidates)[:TOP_K]


def answer(query: str):
    """Retrieve, then generate a grounded answer. Returns (text, sources)."""
    passages = retrieve(query)
    context = "\n\n".join(
        f"[{n + 1}] (source: {src}) {text}" for n, (_id, text, src) in enumerate(passages)
    )
    system = (
        "You answer strictly from the provided context. Cite sources inline like "
        "[1], [2]. If the answer is not in the context, say 'I don't know based on "
        "the provided documents.' Do not use outside knowledge."
    )
    chat_client, chat_model = provider.get_chat()
    resp = chat_client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
        ],
    )
    sources = sorted({src for _id, _text, src in passages})
    return resp.choices[0].message.content, sources


def main() -> None:
    query = " ".join(sys.argv[1:]) or "What is hybrid retrieval and why use it?"
    print(f"you ▸ {query}\n")
    text, sources = answer(query)
    print("ai  ▸", text)
    print("\nsources:", ", ".join(sources))


if __name__ == "__main__":
    main()
