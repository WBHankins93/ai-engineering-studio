"""Lab 02 · Indexing — turn a folder of documents into a searchable index.

This is the offline half of RAG (see the rag-two-loops visual): read docs, split
them into passages ("chunks"), embed each chunk into a vector, and store the vectors
+ text in Qdrant. Run once, and again whenever the documents change.

Run with `make ingest`.
"""

import glob
import os

from qdrant_client.models import Distance, PointStruct, VectorParams

import provider
from store import COLLECTION, get_store

CORPUS_GLOB = "corpus/*.md"
CHUNK_CHARS = 600       # rough target chunk size (illustrative — tune per corpus)
CHUNK_OVERLAP = 100     # carry a little context across boundaries


def chunk(text: str) -> list[str]:
    """Split on blank lines, then pack paragraphs up to ~CHUNK_CHARS with overlap.

    Chunking is the most underrated RAG decision: too big buries the answer in noise,
    too small severs the context that makes a sentence meaningful.
    """
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if cur and len(cur) + len(p) > CHUNK_CHARS:
            chunks.append(cur)
            cur = cur[-CHUNK_OVERLAP:] + "\n\n" + p  # keep a tail for continuity
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        chunks.append(cur)
    return chunks


def main() -> None:
    client, embed_model = provider.get_embedder()

    # Build the chunk list from every doc in the corpus.
    records = []  # (text, source)
    for path in sorted(glob.glob(CORPUS_GLOB)):
        with open(path, encoding="utf-8") as f:
            for c in chunk(f.read()):
                records.append((c, os.path.basename(path)))

    if not records:
        raise SystemExit(f"No documents found in {CORPUS_GLOB}.")

    print(f"Embedding {len(records)} chunks from {CORPUS_GLOB} via {embed_model} ...")
    vectors = provider.embed(client, embed_model, [t for t, _ in records])
    dim = len(vectors[0])

    store = get_store()
    if store.collection_exists(COLLECTION):
        store.delete_collection(COLLECTION)
    store.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )
    store.upsert(
        collection_name=COLLECTION,
        points=[
            PointStruct(id=i, vector=vectors[i], payload={"text": t, "source": s})
            for i, (t, s) in enumerate(records)
        ],
    )
    print(f"Indexed {len(records)} chunks (dim {dim}) into '{COLLECTION}'. Done.")


if __name__ == "__main__":
    main()
