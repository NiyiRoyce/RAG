import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.fetch_data import fetch_pdfs
from scripts.transform_data import chunk_text
from scripts.generate_embeddings import generate_embeddings
from scripts.load_to_vector_db import load_to_vector_db

def run_pipeline():
    docs = fetch_pdfs("data/pdfs/")
    chunks = chunk_text(docs, chunk_size=500)
    embeddings = generate_embeddings(chunks)
    client = load_to_vector_db(embeddings, chunks, config={})
    return client

if __name__ == "__main__":
    client = run_pipeline()
    print("✅ Pipeline finished. FAISS index ready.")
