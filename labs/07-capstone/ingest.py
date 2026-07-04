"""Lab 07 · Indexing — turn corpus/*.md into a searchable index.

Same pattern as Lab 02's ingest.py, pointed at this lab's own corpus. Run once,
and again whenever the docs change: `make ingest`.
"""

import glob
import os

from qdrant_client.models import Distance, PointStruct, VectorParams

import provider
from store import COLLECTION, get_store

CORPUS_GLOB = "corpus/*.md"
CHUNK_CHARS = 600
CHUNK_OVERLAP = 100


def chunk(text: str) -> list[str]:
    """Split on blank lines, then pack paragraphs up to ~CHUNK_CHARS with overlap."""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if cur and len(cur) + len(p) > CHUNK_CHARS:
            chunks.append(cur)
            cur = cur[-CHUNK_OVERLAP:] + "\n\n" + p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        chunks.append(cur)
    return chunks


def main() -> None:
    client, embed_model = provider.get_embedder()

    records = []
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
