"""Tiny in-memory embedding retrieval for Lab 06.

Deliberately minimal — no vector DB, no reranking (that's Lab 02's job). This
lab is about *observing* a RAG pipeline, not building a better one, so
retrieval here is the simplest thing that's still real: embed the corpus,
embed the question, rank by cosine similarity.
"""

from pathlib import Path

from provider import embed, get_embedder

CORPUS_DIR = Path(__file__).with_name("corpus")


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


def _load_corpus() -> list[dict]:
    docs = []
    for path in sorted(CORPUS_DIR.glob("*.md")):
        docs.append({"source": path.name, "text": path.read_text()})
    return docs


def retrieve(question: str, top_k: int = 2) -> list[dict]:
    """Return the top_k most relevant corpus docs for the question."""
    docs = _load_corpus()
    client, model = get_embedder()
    vectors = embed(client, model, [d["text"] for d in docs] + [question])
    doc_vectors, query_vector = vectors[:-1], vectors[-1]

    scored = [
        {**doc, "score": _cosine(vec, query_vector)}
        for doc, vec in zip(docs, doc_vectors)
    ]
    scored.sort(key=lambda d: d["score"], reverse=True)
    return scored[:top_k]
