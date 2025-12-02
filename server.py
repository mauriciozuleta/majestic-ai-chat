# server.py
# FastAPI backend for RAG pipeline with Ollama

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import uvicorn
import requests
from index_store import query_index

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama2"  # Use 'llama2' for Llama 2 7B compatibility

app = FastAPI()

# Allow CORS for local UI testing
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

class QueryRequest(BaseModel):
	question: str
	top_k: int = 3
	filter_source: str = None  # e.g. 'majestic plt bp for rag', 'fresh 24 bp for rag'
	id_range: list = None      # e.g. [2, 13] for Majestic Air Cargo

model = None

def get_model():
	global model
	if model is None:
		model = SentenceTransformer('all-MiniLM-L6-v2')
	return model

def build_prompt(context_chunks, question):
	context = "\n\n".join(f"[{c['title']}]: {c['content']}" for c in context_chunks)
	prompt = (
		"You have full access to the Majestic P.L.T. project information below. "
		"Answer the user's question naturally and directly, as an informed project insider. "
		"Do not introduce yourself or use formulaic phrases—just provide the answer as if you are sharing knowledge with a colleague. "
		"Be very concise, clear, and simple. Avoid unnecessary detail and complexity. If the answer involves a list (such as sponsors, aircraft, or team members), mention all items, but keep the answer short and easy to understand—ideally in one or two plain sentences.\n\n"
		f"Project Information:\n{context}\n\nQuestion: {question}\nAnswer:"
	)
	return prompt

def call_ollama(prompt, model_name=OLLAMA_MODEL, num_predict=128):
	response = requests.post(OLLAMA_URL, json={
		"model": model_name,
		"prompt": prompt,
		"num_predict": num_predict,
		"stream": False
	})
	response.raise_for_status()
	return response.json().get("response", "No response from model.")

@app.post("/rag")
async def rag_query(req: QueryRequest):
	question = req.question
	top_k = req.top_k
	filter_source = req.filter_source
	id_range = req.id_range
	embedder = get_model()
	query_emb = embedder.encode(question).tolist()

	# Load all embeddings and metadata for filtering
	import json
	with open("embeddings.json", "r", encoding="utf-8") as f:
		all_chunks = json.load(f)
	filtered_chunks = all_chunks
	if filter_source:
		filtered_chunks = [c for c in filtered_chunks if c.get('source') == filter_source]
	if id_range and len(id_range) == 2:
		start, end = id_range
		filtered_chunks = [c for c in filtered_chunks if c.get('id') and start <= int(str(c['id'])) <= end]
	# If filtering, run similarity search only on filtered chunks
	if filter_source or (id_range and len(id_range) == 2):
		# Compute embedding similarity manually
		import numpy as np
		vectors = [c['embedding'] for c in filtered_chunks]
		vectors = np.array(vectors).astype('float32')
		query_vec = np.array(query_emb).astype('float32').reshape(1, -1)
		D = np.sum((vectors - query_vec) ** 2, axis=1)
		top_indices = np.argsort(D)[:top_k]
		top_chunks = [filtered_chunks[i] for i in top_indices]
	else:
		# Default: use FAISS index
		from index_store import query_index
		top_chunks = query_index(query_emb, top_k=top_k)
	# Concatenate all top chunks' content for a larger context window (no truncation)
	prompt = build_prompt(top_chunks, question)
	answer = call_ollama(prompt, num_predict=256)
	return {
		"question": question,
		"answer": answer,
		"chunks": top_chunks
	}

@app.get("/")
async def root():
	return {"message": "RAG API is running."}

if __name__ == "__main__":
	uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
