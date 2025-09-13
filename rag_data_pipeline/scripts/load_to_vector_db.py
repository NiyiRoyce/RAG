from llm_app.vector_db_client import VectorDBClient

def load_to_vector_db(embeddings: list, docs: list, config: dict = None):
    dim = len(embeddings[0])  # embedding size
    client = VectorDBClient(dim)
    client.add(embeddings, docs)
    print(f"Loaded {len(docs)} documents into FAISS index")
    return client
