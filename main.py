from src.text_cleaner import clean_text
from src.embedding_engine import Embedder
from src.similarity_engine import compute_similarity
from src.plagiarism_detector import detect_plagiarism
from src.visualizer import plot_heatmap

def load_document(path):

    with open(path, "r") as f:
        return f.read()

def main():

    print("\n🧬 Semantic Plagiarism Detector\n")

    doc_a = load_document(
        "data/document_a.txt"
    )

    doc_b = load_document(
        "data/document_b.txt"
    )

    clean_a = clean_text(doc_a)
    clean_b = clean_text(doc_b)

    embedder = Embedder()

    embeddings = embedder.encode([
        clean_a,
        clean_b
    ])

    similarity_matrix = compute_similarity(
        embeddings
    )

    results = detect_plagiarism(
        similarity_matrix
    )

    print("\nSimilarity Score:")
    print(round(results["score"], 3))

    print("\nVerdict:")
    print(results["verdict"])

    plot_heatmap(similarity_matrix)

if __name__ == "__main__":
    main()
