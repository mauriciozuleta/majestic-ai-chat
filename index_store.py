
# index_store.py
# Stores and retrieves embeddings and metadata using FAISS

import json
import numpy as np
import faiss
import os

EMBEDDINGS_PATH = "embeddings.json"
INDEX_PATH = "faiss.index"
META_PATH = "faiss_meta.json"

def load_embeddings():
	with open(EMBEDDINGS_PATH, "r", encoding="utf-8") as f:
		data = json.load(f)
	vectors = [item["embedding"] for item in data]
	meta = [{k: v for k, v in item.items() if k != "embedding"} for item in data]
	return np.array(vectors).astype('float32'), meta

def build_and_save_index():
	vectors, meta = load_embeddings()
	dim = vectors.shape[1]
	index = faiss.IndexFlatL2(dim)
	index.add(vectors)
	faiss.write_index(index, INDEX_PATH)
	with open(META_PATH, "w", encoding="utf-8") as f:
		json.dump(meta, f, indent=2, ensure_ascii=False)
	print(f"FAISS index built and saved to {INDEX_PATH}. Metadata saved to {META_PATH}.")

def load_index_and_meta():
	if not os.path.exists(INDEX_PATH) or not os.path.exists(META_PATH):
		raise FileNotFoundError("Index or metadata file not found. Run build_and_save_index() first.")
	index = faiss.read_index(INDEX_PATH)
	with open(META_PATH, "r", encoding="utf-8") as f:
		meta = json.load(f)
	return index, meta

def query_index(query_embedding, top_k=3):
	index, meta = load_index_and_meta()
	query_vec = np.array(query_embedding).astype('float32').reshape(1, -1)
	D, I = index.search(query_vec, top_k)
	results = []
	for idx, dist in zip(I[0], D[0]):
		if idx < 0 or idx >= len(meta):
			continue
		item = meta[idx].copy()
		item['score'] = float(dist)
		results.append(item)
	return results

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		build_and_save_index()
	elif len(sys.argv) > 2 and sys.argv[1] == "query":
		# Example: python index_store.py query "your query text"
		from sentence_transformers import SentenceTransformer
		model = SentenceTransformer('all-MiniLM-L6-v2')
		query_text = sys.argv[2]
		query_emb = model.encode(query_text).tolist()
		results = query_index(query_emb, top_k=3)
		print("Top results:")
		for r in results:
			print(f"Score: {r['score']:.4f} | Title: {r['title']}\nContent: {r['content'][:200]}...\n")
	else:
		print("Usage:")
		print("  python index_store.py build        # Build and save FAISS index")
		print("  python index_store.py query <text> # Query index with input text")
