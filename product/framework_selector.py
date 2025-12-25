class FrameworkSelector:
    """
    Phase 4 – Decisive Framework Selection (v3.2)

    - Eliminates invalid frameworks per problem type
    - Prevents RICE overuse
    - Mimics senior PM judgment
    """

    def select(self, problem_type: str, summary: str) -> str:
        text = summary.lower()

        # --------------------------------------------------
        # HARD GATES (NO SCORING YET)
        # --------------------------------------------------

        # PERFORMANCE → ICE ONLY
        if problem_type == "performance":
            return "ICE"

        # DELIVERY → MOSCOW ONLY
        if problem_type == "delivery":
            return "MoSCoW"

        # ONBOARDING / RETENTION → KANO FIRST
        if problem_type in ["onboarding", "retention"]:
            return "Kano"

        # GROWTH → RICE (ONLY HERE)
        if problem_type == "growth":
            return "RICE"

        # --------------------------------------------------
        # FALLBACK LOGIC
        # --------------------------------------------------

        # If estimation language exists → RICE
        if any(k in text for k in [
            "reach", "impact", "confidence", "effort",
            "roi", "estimate", "forecast"
        ]):
            return "RICE"

        # Default → ICE (fast learning)
        return "ICE"
