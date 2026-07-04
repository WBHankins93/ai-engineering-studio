"""The RAG tool — hybrid retrieval + rerank, wrapped as a tool the orchestrator calls.

Same hybrid (dense + BM25, RRF fusion) + cross-encoder rerank pipeline as Lab 02,
pointed at this lab's own corpus/index. The tool returns retrieved passages with
citations as text — it does NOT generate a final answer itself; the orchestrator
composes the final response from this tool's output (and the order-lookup tool's,
if it also calls that), so one answer can cite both a policy doc and an order
status in the same reply.
"""

import sys

from langchain_core.tools import tool
from rank_bm25 import BM25Okapi

import provider
from store import COLLECTION, get_store

DENSE_N = 20
RRF_K = 60
FUSED_K = 10
TOP_K = 5


def _load_all(store):
    points, _ = store.scroll(collection_name=COLLECTION, limit=10000, with_payload=True)
    return {p.id: (p.payload["text"], p.payload["source"]) for p in points}


def _dense(store, qvec):
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
    fused = {}
    for ranking in rankings:
        for rank, _id in enumerate(ranking):
            fused[_id] = fused.get(_id, 0.0) + 1.0 / (RRF_K + rank)
    return [i for i, _ in sorted(fused.items(), key=lambda x: x[1], reverse=True)]


_ENCODER = None


def _get_encoder():
    global _ENCODER
    if _ENCODER is None:
        from fastembed.rerank.cross_encoder import TextCrossEncoder

        _ENCODER = TextCrossEncoder("Xenova/ms-marco-MiniLM-L-6-v2")
    return _ENCODER


def _rerank(query, candidates):
    try:
        encoder = _get_encoder()
        docs = [c[1] for c in candidates]
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

    dense_ids = _dense(store, qvec)
    bm25_ids = _bm25(by_id, query)
    fused_ids = _rrf(dense_ids, bm25_ids)[:FUSED_K]

    candidates = [(i, by_id[i][0], by_id[i][1]) for i in fused_ids if i in by_id]
    return _rerank(query, candidates)[:TOP_K]


@tool
def search_docs(query: str) -> str:
    """Search shipping, returns, and product FAQ docs. Returns cited passages, not a final answer."""
    passages = retrieve(query)
    if not passages:
        return "No matching passages found."
    return "\n\n".join(
        f"[{n + 1}] (source: {src}) {text}" for n, (_id, text, src) in enumerate(passages)
    )
