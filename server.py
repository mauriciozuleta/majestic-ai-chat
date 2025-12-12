# server.py
from __future__ import annotations

import json
import numpy as np
from typing import Any, Dict, List, Optional, Tuple

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

from index_store import query_index
from providers.openai import OpenAIProvider
from config import TOP_K, MIN_SIMILARITY, ALLOWED_ORIGINS, MAX_QUESTION_CHARS

app = FastAPI()

# CORS: allow your website(s) only in production
origins = ALLOWED_ORIGINS or ["http://localhost:3000", "http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str
    top_k: int = TOP_K
    filter_source: Optional[str] = None  # e.g. 'majestic plt bp for rag', 'fresh 24 bp for rag'
    id_range: Optional[List[int]] = None # e.g. [2, 13]

llm = OpenAIProvider()

# Load embedding model once (important for performance)
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def load_chunks() -> List[Dict[str, Any]]:
    with open("embeddings.json", "r", encoding="utf-8") as f:
        return json.load(f)

ALL_CHUNKS: List[Dict[str, Any]] = load_chunks()


def brute_force_top_k(
    question_emb: np.ndarray,
    chunks: List[Dict[str, Any]],
    top_k: int,
) -> Tuple[List[Dict[str, Any]], List[float]]:
    """
    Cosine similarity search over an in-memory filtered chunk list.
    Handles cases where some chunks may not have embeddings.
    Returns (top_chunks, top_similarities).
    """
    valid = [(i, c) for i, c in enumerate(chunks) if c.get("embedding") is not None]
    if not valid:
        return [], []

    idx_map = [i for i, _ in valid]
    vectors = np.array([c["embedding"] for _, c in valid], dtype=np.float32)
    q = np.array(question_emb, dtype=np.float32)

    sims = util.cos_sim(q, vectors)[0].cpu().numpy()
    top_idx = np.argsort(sims)[::-1][:top_k]
    top_sims = sims[top_idx].tolist()

    top_chunks = [chunks[idx_map[i]] for i in top_idx]
    return top_chunks, top_sims


def strip_chunk(c: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove large/internal fields (like embeddings) before returning to browser.
    """
    return {
        "id": c.get("id"),
        "title": c.get("title"),
        "source": c.get("source"),
        "content": c.get("content"),
    }


@app.post("/rag")
async def rag_query(req: QueryRequest):
    question = (req.question or "").strip()

    if not question:
        return {"question": "", "answer": "Please enter a question.", "chunks": [], "citations": []}

    if len(question) > MAX_QUESTION_CHARS:
        return {
            "question": question[:MAX_QUESTION_CHARS],
            "answer": "Your question is a bit long. Please shorten it and try again.",
            "chunks": [],
            "citations": [],
        }

    top_k = req.top_k or TOP_K
    filter_source = req.filter_source
    id_range = req.id_range

    # Embed question once
    q_emb = embedder.encode(question)

    # Apply filters (if any)
    filtered_chunks = ALL_CHUNKS
    if filter_source:
        filtered_chunks = [c for c in filtered_chunks if c.get("source") == filter_source]

    if id_range and len(id_range) == 2:
        start, end = id_range
        filtered_chunks = [
            c
            for c in filtered_chunks
            if c.get("id") is not None and start <= int(str(c["id"])) <= end
        ]

    # Retrieval strategy:
    # - If filters are applied -> brute force cosine over filtered set
    # - Else -> use FAISS (query_index)
    best_sim: Optional[float] = None
    if filter_source or (id_range and len(id_range) == 2):
        top_chunks, top_sims = brute_force_top_k(q_emb, filtered_chunks, top_k=top_k)
        best_sim = top_sims[0] if top_sims else 0.0
    else:
        # Use FAISS index (faster / scalable)
        # NOTE: best_sim will be None unless query_index returns scores.
        top_chunks = query_index(q_emb.tolist(), top_k=top_k)

    # If no chunks retrieved
    if not top_chunks:
        return {
            "question": question,
            "answer": "I couldn’t find that in the provided document.",
            "chunks": [],
            "citations": [],
        }

    # Similarity guardrail (only reliable for brute-force path unless query_index returns distances)
    if best_sim is not None and best_sim < MIN_SIMILARITY:
        return {
            "question": question,
            "answer": "I couldn’t find that in the provided document.",
            "chunks": [],
            "citations": [],
        }

    citations = [c.get("id") for c in top_chunks if c.get("id") is not None]
    safe_chunks = [strip_chunk(c) for c in top_chunks]

    # IMPORTANT: pass question + chunks (provider builds grounded prompt)
    answer = llm.generate(question, top_chunks)

    return {
        "question": question,
        "answer": answer,
        "chunks": safe_chunks,
        "citations": citations,
    }


@app.get("/")
async def root():
    return {"message": "RAG API is running."}


@app.get("/health")
async def health():
    return {"ok": True}
