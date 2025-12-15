from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


class ProblemClusterer:
    """
    Clusters user feedback into product problem groups.
    """

    def __init__(self, num_clusters: int = 3):
        self.num_clusters = num_clusters
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.model = KMeans(n_clusters=self.num_clusters, random_state=42)

    def cluster(self, texts: list[str]) -> dict:
        """
        Cluster cleaned feedback texts into problem groups.

        Args:
            texts (list[str]): Cleaned user feedback texts

        Returns:
            dict: cluster_id -> list of feedback
        """
        if not texts:
            return {}

        vectors = self.vectorizer.fit_transform(texts)
        labels = self.model.fit_predict(vectors)

        clusters = {}
        for text, label in zip(texts, labels):
            clusters.setdefault(label, []).append(text)

        return clusters
