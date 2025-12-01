import json
import random
import re

# Map for project source to readable name (customize as needed)
PROJECT_NAMES = {
    "fresh 24 bp for rag": "Fresh 24",
    "majestic plt bp for rag": "Majestic P.L.T.",
    "majestic air cargo bp for rag": "Majestic Air Cargo"
}

def clean_title(title):
    # Remove numbering and extra whitespace
    return re.sub(r"^\d+(\.\d+)*\s*", "", title).strip()

def generate_prompt(title, project_name):
    title_clean = clean_title(title)
    # Heuristic prompt generation
    if not title_clean:
        return None
    if "objective" in title_clean.lower() or "problem" in title_clean.lower():
        return f"What problem will {project_name} solve? What are its objectives?"
    if "risk" in title_clean.lower():
        return f"What are the {title_clean.lower()} for {project_name}?"
    if "team" in title_clean.lower() or "governance" in title_clean.lower():
        return f"How is the {project_name} team structured and governed?"
    if "market" in title_clean.lower():
        return f"What is the market analysis for {project_name}?"
    if "financial" in title_clean.lower():
        return f"What are the financial risks for {project_name}?"
    # Default
    return f"Tell me about {title_clean} in {project_name}."

def main(chunk_file, out_file):
    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    if not chunks:
        print("No chunks found.")
        return
    project_source = chunks[0].get("source", "unknown")
    project_name = PROJECT_NAMES.get(project_source, project_source)
    prompts = []
    for chunk in chunks:
        title = chunk.get("title", "")
        if not title.strip():
            continue
        prompt = generate_prompt(title, project_name)
        if prompt:
            prompts.append({
                "section_id": chunk.get("id"),
                "title": title,
                "prompt": prompt
            })
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(prompts)} prompts to {out_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python generate_prompt_file.py <chunk_file.json> <out_file.json>")
        exit(1)
    main(sys.argv[1], sys.argv[2])
