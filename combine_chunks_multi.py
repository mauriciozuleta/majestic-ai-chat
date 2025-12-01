# combine_chunks_multi.py
# Combine multiple .docx chunk files and Excel chunks for unified embedding

import json
import glob
import os

# Find all *_chunks.json and excel_chunks.json in the root folder
chunk_files = glob.glob("*_chunks.json")
if os.path.exists("excel_chunks.json"):
    chunk_files.append("excel_chunks.json")

COMBINED_CHUNKS = "all_chunks.json"
all_chunks = []
for fname in chunk_files:
    try:
        with open(fname, "r", encoding="utf-8") as f:
            chunks = json.load(f)
            # Ensure 'source' field is preserved for filtering
            for chunk in chunks:
                if 'source' not in chunk:
                    # Try to infer from filename if missing
                    chunk['source'] = os.path.splitext(os.path.basename(fname))[0].replace('_chunks','')
                all_chunks.append(chunk)
            print(f"Loaded {len(chunks)} chunks from {fname}")
    except Exception as e:
        print(f"Warning: Could not load {fname}: {e}")

with open(COMBINED_CHUNKS, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=2, ensure_ascii=False)

print(f"Combined {len(all_chunks)} chunks into {COMBINED_CHUNKS}")
