# rag_ollama_test.py
# Test script: retrieves top-k chunks using FAISS and sends them to Ollama for answer generation

import sys
import requests
from sentence_transformers import SentenceTransformer
from index_store import query_index

OLLAMA_URL = "http://localhost:11434/api/generate"  # Default Ollama endpoint
OLLAMA_MODEL = "mistral"  # Use the running model

def build_prompt(context_chunks, question):
    context = "\n\n".join(f"[{c['title']}]: {c['content']}" for c in context_chunks)
    prompt = f"You are an expert assistant. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    return prompt

def call_ollama(prompt, model=OLLAMA_MODEL):
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    response.raise_for_status()
    return response.json().get("response", "No response from model.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python rag_ollama_test.py <your question>")
        return
    question = sys.argv[1]
    print(f"Query: {question}")
    # Embed the question
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_emb = model.encode(question).tolist()
    # Retrieve top-3 chunks
    top_chunks = query_index(query_emb, top_k=3)
    print("Top retrieved chunks:")
    for c in top_chunks:
        print(f"- {c['title']}")
    # Build prompt and call Ollama
    prompt = build_prompt(top_chunks, question)
    print("\nSending prompt to Ollama...")
    answer = call_ollama(prompt)
    print("\nOllama Answer:\n", answer)

if __name__ == "__main__":
    main()
