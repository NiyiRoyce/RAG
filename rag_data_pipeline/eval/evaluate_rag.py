"""
Evaluate RAG performance
"""

import csv

def evaluate(query: str, expected_answer: str, rag_answer: str) -> dict:
    # TODO: implement real evaluation metrics (precision, recall, faithfulness, etc.)
    return {"query": query, "expected": expected_answer, "got": rag_answer, "score": 0.8}

def log_metrics(metrics: dict, file_path: str = "eval/metrics.csv"):
    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=metrics.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(metrics)

if __name__ == "__main__":
    m = evaluate("What is RAG?", "retrieval augmented generation", "retrieval augmented generation (approx)")
    log_metrics(m)
