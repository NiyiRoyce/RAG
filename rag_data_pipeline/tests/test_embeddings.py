from scripts.generate_embeddings import generate_embeddings

def test_embeddings_shape():
    docs = ["doc1", "doc2"]
    embeddings = generate_embeddings(docs)
    assert len(embeddings) == len(docs)
