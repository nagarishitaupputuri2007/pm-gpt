class FrameworkExplainer:
    """
    Provides human-readable explanations for
    why a prioritization framework is used.
    """

    def explain(self, framework: str, context: dict) -> str:
        if framework == "RICE":
            return (
                "RICE was selected because this decision involves roadmap planning "
                "where reach, impact, confidence, and effort can be reasonably estimated."
            )

        if framework == "ICE":
            return (
                "ICE was selected because this decision needs a fast prioritization "
                "based on impact, confidence, and ease."
            )

        if framework == "MoSCoW":
            return (
                "MoSCoW was selected to clearly separate must-have features "
                "from optional ones for delivery planning."
            )

        if framework == "Kano":
            return (
                "Kano was selected to understand which features are basic expectations "
                "versus those that can delight users."
            )

        return "No explanation available for the selected framework."
