import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "vectorstore/faiss_index/index.faiss"
METADATA_PATH = "vectorstore/faiss_index/chunks_metadata.json"

def load_resources():
    index = faiss.read_index(INDEX_PATH)

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    return index, metadata, model


def retrieve(query, top_k=3):
    index, metadata, model = load_resources()

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(metadata[idx]["chunk"])

    return results


if __name__ == "__main__":
    question = input("Ask a question: ")

    results = retrieve(question)

    print("\nTop relevant chunks:\n")

    for i, chunk in enumerate(results):
        print(f"Result {i+1}:")
        print(chunk)
        print("\n------------------\n")