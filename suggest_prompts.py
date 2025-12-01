import json

# Map for project source to readable name (customize as needed)
PROJECT_NAMES = {
    "fresh 24 bp for rag": "Fresh 24",
    "majestic plt bp for rag": "Majestic P.L.T.",
    "majestic air cargo bp for rag": "Majestic Air Cargo"
}

def generate_prompt(title, project_name):
    # Simple rules for prompt generation
    title_lower = title.lower()
    if "risk" in title_lower:
        return f"What are the {title_lower} for {project_name}?"
    if "team" in title_lower or "governance" in title_lower:
        return f"How is the {project_name} team structured and governed?"
    if "objective" in title_lower or "problem" in title_lower:
        return f"What problem will {project_name} solve? What are its objectives?"
    if "market" in title_lower:
        return f"What is the market analysis for {project_name}?"
    if "financial" in title_lower:
        return f"What are the financial risks for {project_name}?"
    # Default
    return f"Tell me about {title_lower} in {project_name}."

def main(chunk_file):
    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    if not chunks:
        print("No chunks found.")
        return
    project_source = chunks[0].get("source", "unknown")
    project_name = PROJECT_NAMES.get(project_source, project_source)
    print(f"Prompt suggestions for {project_name} (source: {project_source}):\n")
    for chunk in chunks:
        title = chunk.get("title", "")
        if not title.strip():
            continue
        prompt = generate_prompt(title, project_name)
        print(f"- {prompt}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python suggest_prompts.py <chunk_file.json>")
        exit(1)
    main(sys.argv[1])
