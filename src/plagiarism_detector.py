def detect_plagiarism(similarity_matrix, threshold=0.70):

    score = similarity_matrix[0][1]

    if score >= threshold:
        verdict = "Potential semantic plagiarism detected."
    else:
        verdict = "Low semantic similarity."

    return {
        "score": float(score),
        "verdict": verdict
    }
