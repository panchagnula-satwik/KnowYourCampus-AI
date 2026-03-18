import json
import os

INPUT_FILE = "data/processed/extracted_text.json"
OUTPUT_FILE = "data/processed/chunks.json"

CHUNK_SIZE = 500
OVERLAP = 100


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def create_chunks():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        documents = json.load(f)

    chunked_data = []

    for doc in documents:
        source = doc["source"]
        text = doc["text"]

        chunks = chunk_text(text)

        for chunk in chunks:
            chunked_data.append({
                "source": source,
                "chunk": chunk
            })

    return chunked_data


def save_chunks(chunks):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Chunks saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    chunks = create_chunks()
    save_chunks(chunks)