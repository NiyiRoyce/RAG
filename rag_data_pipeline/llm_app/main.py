from fastapi import FastAPI
from rag_pipeline import run_pipeline
from vector_db_client import VectorDBClient

app = FastAPI()
db_client: VectorDBClient = None  # global client

@app.on_event("startup")
def startup_event():
    global db_client
    db_client = run_pipeline("data/pdfs", {"db": "faiss"})  # load PDFs into FAISS

@app.get("/")
def root():
    return {"message": "RAG API is running 🚀"}

@app.post("/query")
def rag_query(query: str):
    # TODO: replace with real query embedding generation
    query_embedding = [0.1, 0.2, 0.3]
    results = db_client.search(query_embedding, top_k=3)
    return {"query": query, "results": results}
