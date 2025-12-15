class RiceScorer:
    """
    Scores features using the RICE prioritization framework.
    """

    def score(self, feature: str, metrics: dict) -> float:
        """
        Calculate RICE score.

        Args:
            feature (str): Feature name
            metrics (dict): Reach, Impact, Confidence, Effort

        Returns:
            float: RICE score
        """
        reach = metrics.get("reach", 0)
        impact = metrics.get("impact", 0)
        confidence = metrics.get("confidence", 0)
        effort = metrics.get("effort", 1)

        if effort == 0:
            return 0

        return round((reach * impact * confidence) / effort, 2)
