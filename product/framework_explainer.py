class FrameworkExplainer:
    """
    Thin wrapper.
    Real explanation is handled by DecisionNarrator.
    This exists only for backward compatibility.
    """

    def explain(self, framework: str, context: dict) -> str:
        return (
            "Framework explanation is provided in the PM Reasoning section "
            "with full context and trade-off rationale."
        )
