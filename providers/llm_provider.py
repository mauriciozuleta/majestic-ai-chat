from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Sequence


class LLMProvider(ABC):
    """
    Interface for LLM providers used by the app.

    Conventions:
    - `question` is the user's natural-language question.
    - `context_chunks` is a list of retrieved chunks (dicts containing at least `content`,
      and ideally `id`, `title`, `source`).
    """

    @abstractmethod
    def generate(
        self,
        question: str,
        context_chunks: Sequence[Dict[str, Any]],
        stream: bool = False,
    ) -> str:
        """Generate an answer grounded in the provided context."""
        raise NotImplementedError

    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Optional: return embeddings for a list of texts.
        Providers that don't support embeddings can leave this unimplemented.
        """
        raise NotImplementedError("This provider does not support embeddings.")
