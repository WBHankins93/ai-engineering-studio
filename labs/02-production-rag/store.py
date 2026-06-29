"""Local Qdrant vector store — embedded mode, no server, no Docker.

`QdrantClient(path=...)` runs Qdrant in-process against a folder on disk. That keeps
the lab $0 and local. Only one process can open the path at a time, which is why you
run `ingest.py` and `rag.py` separately.
"""

from qdrant_client import QdrantClient

QDRANT_PATH = ".qdrant"   # gitignored local data dir
COLLECTION = "docs"


def get_store() -> QdrantClient:
    return QdrantClient(path=QDRANT_PATH)
