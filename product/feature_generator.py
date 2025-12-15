# product/feature_generator.py

class FeatureGenerator:
    """
    Generates feature ideas from a product problem statement.
    """

    def generate(self, problem_statement: str) -> list[str]:
        """
        Generate a list of feature ideas based on the problem.

        Args:
            problem_statement (str): Human-readable product problem

        Returns:
            list[str]: Feature ideas
        """

        if not problem_statement:
            return []

        # Simple rule-based generation (stable & predictable)
        features = []

        problem_lower = problem_statement.lower()

        if "onboarding" in problem_lower:
            features.extend([
                "Simplify onboarding flow",
                "Add progress indicators to onboarding",
                "Provide contextual tooltips during onboarding"
            ])

        if "payment" in problem_lower or "checkout" in problem_lower:
            features.extend([
                "Improve payment retry mechanism",
                "Add clearer payment error messages",
                "Optimize checkout performance"
            ])

        if "search" in problem_lower:
            features.extend([
                "Improve search relevance ranking",
                "Add search filters",
                "Enable typo-tolerant search"
            ])

        if not features:
            features.extend([
                "Improve in-app guidance",
                "Enhance overall app performance",
                "Add user feedback collection"
            ])

        return features
