"""Ingest embeddings into Pinecone vector index.

Batch upsert: 100 vectors per call.
Metadata: text truncated to 1000 chars (40KB limit).
"""

import json
import os
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from pinecone import Pinecone
from tqdm import tqdm

load_dotenv()

RAW_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "processed"

EMBEDDINGS_PATH = PROCESSED_DIR / "embeddings.npy"
IDS_PATH = PROCESSED_DIR / "embedding_ids.json"

BATCH_SIZE = 100
TEXT_LIMIT = 1000  # metadata text truncation


def ingest(progress_callback=None):
    """Batch upsert embeddings into Pinecone vector index.

    Args:
        progress_callback: Optional callback(current, total) for progress updates.

    Returns:
        int: Number of vectors upserted.

    Hints:
        - Load embeddings from PROCESSED_DIR / "embeddings.npy"
        - Load IDs from PROCESSED_DIR / "embedding_ids.json"
        - Load texts from RAW_DIR / "corpus.jsonl" for metadata
        - Connect: Pinecone(api_key=...) → pc.Index(index_name)
        - Upsert format: {"id": ..., "values": [...], "metadata": {"text": ...}}
        - Batch size: BATCH_SIZE (100), truncate text to TEXT_LIMIT (1000) chars
    """
    # TODO: Implement Pinecone upsert
    embeddings = np.load(EMBEDDINGS_PATH)
    ids = json.loads(IDS_PATH.read_text())
    
    texts = []
    with open(RAW_DIR / "corpus.jsonl", encoding="utf-8") as f:
        for line in f:
            texts.append(json.loads(line)["text"])

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = os.getenv("PINECONE_INDEX", "ragsession")
    index = pc.Index(index_name)

    total_count = len(ids)
    for i in range(0, total_count, BATCH_SIZE):
        batch_ids = ids[i : i + BATCH_SIZE]
        batch_vectors = embeddings[i : i + BATCH_SIZE].tolist()
        batch_metadatas = [
            {"text": texts[j][:TEXT_LIMIT]} 
            for j in range(i, i + len(batch_ids))
        ]

        vectors_to_upsert = list(zip(batch_ids, batch_vectors, batch_metadatas))
        
        index.upsert(vectors=vectors_to_upsert)
        
        if progress_callback:
            progress_callback(i + len(batch_ids), total_count)

    return total_count


if __name__ == "__main__":
    ingest()
