def chunk_text(docs, chunk_size=500):
    chunks = []
    for doc in docs:
        words = doc["text"].split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i+chunk_size])
            chunks.append({"filename": doc["filename"], "chunk": chunk})
    return chunks
