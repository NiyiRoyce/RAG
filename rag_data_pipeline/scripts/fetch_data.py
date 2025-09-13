import os
import fitz  # PyMuPDF

def fetch_pdfs(pdf_dir="data/pdfs/"):
    texts = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(pdf_dir, file))
            text = ""
            for page in doc:
                text += page.get_text()
            texts.append({"filename": file, "text": text})
    return texts

if __name__ == "__main__":
    docs = fetch_pdfs()
    print(f"Loaded {len(docs)} PDF(s)")
