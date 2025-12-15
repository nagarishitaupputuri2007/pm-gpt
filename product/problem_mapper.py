class ProblemMapper:
    """
    Maps clustered feedback into human-readable product problems.
    """

    def map_problem(self, cluster_texts: list[str]) -> str:
        """
        Generate a concise problem statement from clustered feedback.

        Args:
            cluster_texts (list[str]): Feedback texts in a cluster

        Returns:
            str: Product problem statement
        """
        if not cluster_texts:
            return "Unknown product problem"

        # Very simple heuristic for now (explainable & safe)
        if any("payment" in text or "checkout" in text for text in cluster_texts):
            return "Payment and Checkout Reliability Issues"

        if any("search" in text for text in cluster_texts):
            return "Search Accuracy and Discoverability Issues"

        return "General User Experience Issues"
