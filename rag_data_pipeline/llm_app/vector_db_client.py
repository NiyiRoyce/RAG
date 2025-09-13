import faiss
import numpy as np

class VectorDBClient:
    def __init__(self, dim: int):
        # L2 distance FAISS index
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []  # store raw docs for retrieval

    def add(self, embeddings: list, docs: list):
        # Convert embeddings to float32 numpy
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.docs.extend(docs)

    def search(self, query_embedding: list, top_k: int = 5):
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.docs):
                results.append({"doc": self.docs[idx], "score": float(dist)})
        return results
