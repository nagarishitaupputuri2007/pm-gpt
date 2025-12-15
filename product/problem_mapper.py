class ProblemMapper:
    """
    Maps clustered feedback into human-readable product problems.
    """

    def map_problem(self, cluster_texts) -> str:
        if isinstance(cluster_texts, str):
            cluster_texts = [cluster_texts.lower()]

        if not cluster_texts:
            return "Unknown product problem"

        if any("payment" in text or "checkout" in text for text in cluster_texts):
            return "Payment and Checkout Reliability Issues"

        if any("search" in text for text in cluster_texts):
            return "Search Accuracy and Discoverability Issues"

        return "General User Experience Issues"
