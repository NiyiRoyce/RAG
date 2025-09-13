"""
Generate embeddings using chosen model
"""

def generate_embeddings(docs: list) -> list:
    # TODO: connect to LLM/embedding model
    print("Generating embeddings...")
    return [[0.1, 0.2, 0.3] for _ in docs]

if __name__ == "__main__":
    docs = ["doc1", "doc2"]
    print(generate_embeddings(docs))
