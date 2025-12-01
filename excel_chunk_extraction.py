# excel_chunk_extraction.py
# Extracts chunks from an Excel file for RAG

import pandas as pd
import json
import os

EXCEL_PATH = "majestic finncial simulation.xlsx"
CHUNKS_OUT = "excel_chunks.json"

# You can customize this function to extract specific sheets or ranges

def extract_excel_chunks(excel_path):
    xls = pd.ExcelFile(excel_path)
    chunks = []
    chunk_id = 1
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        # Convert the whole sheet to a string table
        table_str = df.to_csv(index=False)
        chunk = {
            "id": f"excel-{chunk_id}",
            "title": f"Excel Sheet: {sheet_name}",
            "content": table_str,
            "path": [f"excel", sheet_name]
        }
        chunks.append(chunk)
        chunk_id += 1
    return chunks

if __name__ == "__main__":
    if not os.path.exists(EXCEL_PATH):
        print(f"Excel file not found: {EXCEL_PATH}")
        exit(1)
    chunks = extract_excel_chunks(EXCEL_PATH)
    with open(CHUNKS_OUT, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    print(f"Extracted {len(chunks)} chunks from Excel and saved to {CHUNKS_OUT}")
