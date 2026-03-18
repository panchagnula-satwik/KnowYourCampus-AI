import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

CHUNKS_FILE = "data/processed/chunks.json"
INDEX_DIR = "vectorstore/faiss_index"

def load_chunks():
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_embeddings(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [chunk["chunk"] for chunk in chunks]
    embeddings = model.encode(texts)

    return embeddings

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index

def save_index(index, chunks):
    os.makedirs(INDEX_DIR, exist_ok=True)

    faiss.write_index(index, f"{INDEX_DIR}/index.faiss")

    with open(f"{INDEX_DIR}/chunks_metadata.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print("FAISS index saved successfully")

if __name__ == "__main__":
    chunks = load_chunks()
    embeddings = generate_embeddings(chunks)

    embeddings = np.array(embeddings).astype("float32")

    index = create_faiss_index(embeddings)

    save_index(index, chunks)