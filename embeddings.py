

import json
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = "all_chunks.json"
EMBEDDINGS_PATH = "embeddings.json"

def get_embedding(model, text):
	try:
		return model.encode(text).tolist()
	except Exception as e:
		print(f"Error embedding text: {e}")
		return None

def main():
	print("Loading sentence-transformers model (all-MiniLM-L6-v2)...")
	try:
		model = SentenceTransformer('all-MiniLM-L6-v2')
	except Exception as e:
		print(f"Failed to load model: {e}")
		return
	try:
		with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
			chunks = json.load(f)
	except Exception as e:
		print(f"Failed to load {CHUNKS_PATH}: {e}")
		return
	results = []
	for chunk in chunks:
		text = chunk.get("content", "")
		if not text.strip():
			print(f"Skipping empty chunk: {chunk.get('title')}")
			continue
		print(f"Embedding chunk: {chunk.get('title')}")
		embedding = get_embedding(model, text)
		if embedding is None:
			print(f"Failed to embed chunk: {chunk.get('title')}")
			continue
		# Preserve 'source' for filtering
		results.append({
			"id": chunk["id"],
			"title": chunk["title"],
			"content": text,
			"path": chunk["path"],
			"source": chunk.get("source", "unknown"),
			"embedding": embedding
		})
	try:
		with open(EMBEDDINGS_PATH, "w", encoding="utf-8") as f:
			json.dump(results, f, indent=2, ensure_ascii=False)
		print(f"Saved {len(results)} embeddings to {EMBEDDINGS_PATH}")
	except Exception as e:
		print(f"Failed to save embeddings: {e}")

if __name__ == "__main__":
	main()
# embeddings.py
# Generates embeddings for text chunks using sentence-transformers
