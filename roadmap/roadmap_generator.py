# roadmap/roadmap_generator.py

class RoadmapGenerator:
    """
    Phase 3.3 – Dependency-Aware 6-Month Product Roadmap

    Produces a realistic PM-style roadmap:
    - Q1 (0–3 months): Foundations & risk reduction
    - Q2 (3–6 months): Growth & leverage
    """

    def generate(self, scored_features):
        """
        Expects scored_features as a list of dicts or a DataFrame-like structure
        with a 'feature' or similar field.
        """

        # Normalize feature names
        features = []
        for item in scored_features:
            if isinstance(item, dict):
                features.append(item.get("feature") or item.get("name"))
            else:
                features.append(str(item))

        # --- Dependency buckets ---
        foundations = []
        enablement = []
        expansion = []

        for feature in features:
            f = feature.lower()

            # Foundational work (must come first)
            if any(k in f for k in [
                "onboarding", "activation", "performance", "reliability",
                "bug", "stability", "error", "latency"
            ]):
                foundations.append(feature)

            # Enable measurement & learning
            elif any(k in f for k in [
                "analytics", "telemetry", "tracking", "feedback",
                "monitoring", "metrics"
            ]):
                enablement.append(feature)

            # Growth & advanced capabilities
            else:
                expansion.append(feature)

        # --- Build 6-month roadmap ---
        roadmap = {
            "Q1 (0–3 months) — Stabilize & Activate": [],
            "Q2 (3–6 months) — Optimize & Grow": []
        }

        # Q1 priorities
        roadmap["Q1 (0–3 months) — Stabilize & Activate"].extend(foundations)
        roadmap["Q1 (0–3 months) — Stabilize & Activate"].extend(enablement)

        # Q2 priorities
        roadmap["Q2 (3–6 months) — Optimize & Grow"].extend(expansion)

        return roadmap
