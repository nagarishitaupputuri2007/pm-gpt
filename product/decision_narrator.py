class DecisionNarrator:
    """
    Generates human-readable PM-style reasoning
    for prioritization and roadmap decisions.
    """

    def explain_framework_choice(self, framework: str) -> str:
        explanations = {
            "RICE": (
                "RICE was selected because this decision involves roadmap planning "
                "where reach, impact, confidence, and effort can be reasonably estimated. "
                "This helps prioritize features with the highest overall value."
            ),
            "ICE": (
                "ICE was selected to enable fast prioritization when limited data is available. "
                "It focuses on impact, confidence, and ease to support quick decision-making."
            ),
            "MoSCoW": (
                "MoSCoW was selected to clearly separate must-have features from optional ones, "
                "helping align delivery expectations with stakeholders."
            ),
            "Kano": (
                "Kano was selected to understand which features are basic expectations versus "
                "those that can delight users and improve satisfaction."
            )
        }

        return explanations.get(
            framework,
            "A suitable prioritization framework was selected based on the problem context."
        )

    def explain_prioritization(self, scored_features: list[dict]) -> str:
        if not scored_features:
            return "No features were prioritized due to insufficient input."

        top_feature = scored_features[0]["feature"]

        return (
            f"The feature '{top_feature}' was prioritized first because it offers the highest "
            "combination of user impact and feasibility based on the selected framework. "
            "Lower-ranked features are scheduled later to balance delivery risk."
        )

    def explain_roadmap(self) -> str:
        return (
            "The roadmap is structured to address foundational issues first, "
            "followed by engagement improvements and long-term optimizations. "
            "This sequencing reduces risk and ensures each phase builds on the previous one."
        )
