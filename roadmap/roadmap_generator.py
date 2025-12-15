# roadmap/roadmap_generator.py

class RoadmapGenerator:
    """
    Generates a product roadmap from prioritized features
    (framework-agnostic).
    """

    def generate(self, prioritized_features: list[dict]) -> dict:
        """
        Generate a simple time-based roadmap.

        Args:
            prioritized_features (list[dict]): Output from any strategy

        Returns:
            dict: Roadmap grouped by timeline
        """

        roadmap = {
            "Now (0–1 month)": [],
            "Next (1–3 months)": [],
            "Later (3–6 months)": []
        }

        if not prioritized_features:
            return roadmap

        # We ONLY care about order, not score
        features = [item["feature"] for item in prioritized_features]

        for idx, feature in enumerate(features):
            if idx < 2:
                roadmap["Now (0–1 month)"].append(feature)
            elif idx < 4:
                roadmap["Next (1–3 months)"].append(feature)
            else:
                roadmap["Later (3–6 months)"].append(feature)

        return roadmap
