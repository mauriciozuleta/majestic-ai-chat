# combine_chunks.py
# Combine .docx and Excel chunks for unified embedding

import json

DOCX_CHUNKS = "chunks.json"
EXCEL_CHUNKS = "excel_chunks.json"
COMBINED_CHUNKS = "all_chunks.json"

with open(DOCX_CHUNKS, "r", encoding="utf-8") as f:
    docx_chunks = json.load(f)
with open(EXCEL_CHUNKS, "r", encoding="utf-8") as f:
    excel_chunks = json.load(f)

all_chunks = docx_chunks + excel_chunks

with open(COMBINED_CHUNKS, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=2, ensure_ascii=False)

print(f"Combined {len(docx_chunks)} docx chunks and {len(excel_chunks)} excel chunks into {COMBINED_CHUNKS}")
