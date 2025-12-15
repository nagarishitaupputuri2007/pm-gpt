class FeatureGenerator:
    """
    Generates feature ideas based on identified product problems.
    """

    def generate_features(self, problem_statement: str) -> list[str]:
        """
        Generate feature ideas for a given product problem.

        Args:
            problem_statement (str): Identified product problem

        Returns:
            list[str]: List of feature ideas
        """
        if "Payment" in problem_statement:
            return [
                "Payment retry mechanism",
                "Improved checkout error handling",
                "Payment failure notifications"
            ]

        if "Search" in problem_statement:
            return [
                "Search relevance tuning",
                "Auto-suggestions and filters",
                "Search result personalization"
            ]

        return [
            "UI performance improvements",
            "Bug fixes and stability enhancements"
        ]
