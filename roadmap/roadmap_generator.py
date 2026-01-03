# roadmap/roadmap_generator.py

class RoadmapGenerator:
    """
    Framework-aware 6-month Product Roadmap Generator

    Accepts:
    - List[dict]  → [{"feature": "...", "score": ...}]
    - List[str]   → ["feature 1", "feature 2"]

    Never crashes. Backward compatible.
    """

    def generate(self, scored_features, framework="RICE"):
        # --------------------------------------------------
        # Normalize input to List[str]
        # --------------------------------------------------
        features = []

        if isinstance(scored_features, list) and len(scored_features) > 0:
            first_item = scored_features[0]

            if isinstance(first_item, dict) and "feature" in first_item:
                features = [item["feature"] for item in scored_features]
            elif isinstance(first_item, str):
                features = scored_features
            else:
                raise ValueError("Unsupported feature structure in roadmap generator")

        elif scored_features == []:
            features = []

        else:
            raise ValueError("Unsupported scored_features type passed to RoadmapGenerator")

        # --------------------------------------------------
        # Bucket features (semantic grouping)
        # --------------------------------------------------
        foundations = []
        enablement = []
        experimentation = []
        expansion = []

        for feature in features:
            text = feature.lower()

            if any(k in text for k in [
                "onboarding", "activation", "crash", "performance",
                "startup", "stability", "reliability", "value", "bug"
            ]):
                foundations.append(feature)

            elif any(k in text for k in [
                "guidance", "nudge", "progress", "engagement",
                "clarify", "education", "tooltip", "feedback"
            ]):
                enablement.append(feature)

            elif any(k in text for k in [
                "experiment", "test", "pilot", "mvp",
                "hypothesis", "trial", "validate"
            ]):
                experimentation.append(feature)

            else:
                expansion.append(feature)

        # --------------------------------------------------
        # Framework-specific roadmap shaping
        # --------------------------------------------------
        if framework == "ICE":
            return {
                "Q1 (0–3 months) — Learn & Validate": (
                    experimentation + enablement + foundations
                ),
                "Q2 (3–6 months) — Scale What Works": (
                    expansion
                )
            }

        if framework == "Kano":
            return {
                "Q1 (0–3 months) — Fix Basics": (
                    foundations + enablement
                ),
                "Q2 (3–6 months) — Delight & Differentiate": (
                    expansion
                )
            }

        if framework == "MoSCoW":
            return {
                "Q1 (0–3 months) — Deliver Must-Haves": (
                    foundations
                ),
                "Q2 (3–6 months) — Expand Scope": (
                    enablement + expansion
                )
            }

        # --------------------------------------------------
        # Default: RICE
        # --------------------------------------------------
        return {
            "Q1 (0–3 months) — Highest Impact First": (
                foundations + enablement
            ),
            "Q2 (3–6 months) — Compound Impact": (
                expansion
            )
        }
