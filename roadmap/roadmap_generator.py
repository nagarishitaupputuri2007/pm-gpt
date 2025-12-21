# roadmap/roadmap_generator.py

class RoadmapGenerator:
    """
    Generates a 6-month product roadmap from prioritized features.

    Accepts:
    - List[dict]  → [{"feature": "...", "score": ...}]
    - List[str]   → ["feature 1", "feature 2"]

    Never assumes pandas. Never crashes.
    """

    def generate(self, scored_features):
        # --------------------------------------------------
        # Normalize input to List[str]
        # --------------------------------------------------
        features = []

        # Case 1: List of dicts (RICE / ICE / Kano / MoSCoW)
        if isinstance(scored_features, list) and len(scored_features) > 0:
            first_item = scored_features[0]

            if isinstance(first_item, dict) and "feature" in first_item:
                features = [item["feature"] for item in scored_features]
            elif isinstance(first_item, str):
                features = scored_features
            else:
                raise ValueError("Unsupported feature structure in roadmap generator")

        # Empty case
        elif scored_features == []:
            features = []

        else:
            raise ValueError("Unsupported scored_features type passed to RoadmapGenerator")

        # --------------------------------------------------
        # Roadmap buckets
        # --------------------------------------------------
        foundations = []
        enablement = []
        expansion = []

        for feature in features:
            text = feature.lower()

            # Q1 — Stabilize & Activate
            if any(k in text for k in [
                "onboarding", "activation", "crash", "performance",
                "startup", "stability", "reliability", "value"
            ]):
                foundations.append(feature)

            # Still Q1 — enable usage
            elif any(k in text for k in [
                "guidance", "nudge", "progress", "engagement", "clarify"
            ]):
                enablement.append(feature)

            # Q2 — Growth & Scale
            else:
                expansion.append(feature)

        # --------------------------------------------------
        # Final roadmap (6 months)
        # --------------------------------------------------
        roadmap = {
            "Q1 (0–3 months) — Stabilize & Activate": foundations + enablement,
            "Q2 (3–6 months) — Optimize & Grow": expansion
        }

        return roadmap
