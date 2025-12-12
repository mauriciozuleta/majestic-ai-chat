import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY. Set it in your environment or .env file.")

# Use a modern default; override via .env
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.2"))

# Retrieval
TOP_K = int(os.getenv("TOP_K", "3"))

# Safety / cost controls
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "350"))
MAX_CONTEXT_CHARS = int(os.getenv("MAX_CONTEXT_CHARS", "12000"))  # optional guardrail
MIN_SIMILARITY = float(os.getenv("MIN_SIMILARITY", "0.25"))       # for cosine thresholding

# Networking guardrails
OPENAI_TIMEOUT_SECONDS = int(os.getenv("OPENAI_TIMEOUT_SECONDS", "30"))
