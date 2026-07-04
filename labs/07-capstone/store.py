"""Local Qdrant vector store — embedded mode, no server, no Docker.

Same pattern as Lab 02: `QdrantClient(path=...)` runs Qdrant in-process against a
folder on disk, keeping this $0 and local.
"""

from qdrant_client import QdrantClient

QDRANT_PATH = ".qdrant"   # gitignored local data dir
COLLECTION = "docs"


def get_store() -> QdrantClient:
    return QdrantClient(path=QDRANT_PATH)
