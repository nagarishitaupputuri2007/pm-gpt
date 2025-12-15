class RoadmapGenerator:
    """
    Generates a product roadmap based on prioritized features.
    """

    def generate(self, scored_features: list[dict]) -> dict:
        """
        Generate a simple time-based roadmap.

        Args:
            scored_features (list[dict]): Features with RICE scores

        Returns:
            dict: Roadmap grouped by timeline
        """
        roadmap = {
            "Now (0–1 month)": [],
            "Next (1–3 months)": [],
            "Later (3–6 months)": []
        }

        # Sort features by RICE score (descending)
        sorted_features = sorted(
            scored_features, key=lambda x: x["score"], reverse=True
        )

        for idx, feature in enumerate(sorted_features):
            if idx < 2:
                roadmap["Now (0–1 month)"].append(feature["feature"])
            elif idx < 4:
                roadmap["Next (1–3 months)"].append(feature["feature"])
            else:
                roadmap["Later (3–6 months)"].append(feature["feature"])

        return roadmap
