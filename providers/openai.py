from __future__ import annotations
from typing import Any, Dict, Sequence
import logging, time

from openai import OpenAI
from config import (
    OPENAI_API_KEY, OPENAI_MODEL, TEMPERATURE,
    MAX_OUTPUT_TOKENS, MAX_CONTEXT_CHARS, OPENAI_TIMEOUT_SECONDS
)

RETRY_ATTEMPTS = 3
RETRY_DELAY = 2

try:
    client = OpenAI(api_key=OPENAI_API_KEY, timeout=OPENAI_TIMEOUT_SECONDS)
except TypeError:
    client = OpenAI(api_key=OPENAI_API_KEY)

MAX_CHUNK_CHARS = 1500

def _build_context(context_chunks: Sequence[Dict[str, Any]]) -> str:
    parts = []
    for c in context_chunks:
        cid = c.get("id", "?")
        title = c.get("title", "Untitled")
        content = (c.get("content", "") or "")[:MAX_CHUNK_CHARS]
        parts.append(f"CHUNK {cid} — {title}:\n{content}")
    context = "\n\n".join(parts)
    return context[:MAX_CONTEXT_CHARS]

class OpenAIProvider:
    def generate(self, question: str, context_chunks, stream: bool = False) -> str:
        if stream:
            logging.warning("stream=True requested but streaming is not implemented; using non-stream.")
        context_text = _build_context(context_chunks)

        system_prompt = (
            "You are a business-plan Q&A assistant.\n"
            "Answer ONLY using the provided CONTEXT.\n"
            "Do NOT add external facts, assumptions, or general knowledge.\n"
            "If the answer is not clearly found in the CONTEXT, say:\n"
            "\"I couldn't find that in the provided business plan.\"\n"
            "Return your response in EXACTLY this format:\n"
            "Answer: <answer>\n"
            "Sources: CHUNK <id>, CHUNK <id>\n"
        )

        user_prompt = f"CONTEXT:\n{context_text}\n\nQUESTION:\n{question}\n"

        for attempt in range(RETRY_ATTEMPTS):
            try:
                resp = client.responses.create(
                    model=OPENAI_MODEL,
                    input=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=TEMPERATURE,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                )
                return resp.output_text or "No response."
            except Exception as e:
                logging.error(f"OpenAI error (attempt {attempt+1}/{RETRY_ATTEMPTS}): {e}")
                if attempt < RETRY_ATTEMPTS - 1:
                    time.sleep(RETRY_DELAY)
                else:
                    return "Sorry — I couldn't generate an answer right now. Please try again."
