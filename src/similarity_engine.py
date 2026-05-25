from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(embeddings):

    similarity_matrix = cosine_similarity(
        embeddings
    )

    return similarity_matrix
