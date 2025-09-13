import os
from dotenv import load_dotenv 

load_dotenv()  

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_embeddings(docs: list) -> list:
    embeddings = []
    for doc in docs:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=doc[:1000]  # truncate long docs
        )
        vector = response.data[0].embedding
        embeddings.append(vector)
    return embeddings

if __name__ == "__main__":
    docs = ["RAG is retrieval augmented generation.", "FAISS stores embeddings."]
    print(len(generate_embeddings(docs)[0]))  # should print 1536
