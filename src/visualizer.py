import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(similarity_matrix):

    plt.figure(figsize=(6,5))

    sns.heatmap(
        similarity_matrix,
        annot=True,
        cmap="Blues"
    )

    plt.title("Semantic Similarity Heatmap")

    plt.savefig(
        "outputs/similarity_heatmap.png"
    )

    plt.show()
