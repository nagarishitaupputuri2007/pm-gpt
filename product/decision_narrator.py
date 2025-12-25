from typing import List, Dict


class DecisionNarrator:
    """
    Phase 4 – Framework + Problem Aware PM Narrative Engine (v3.1)

    - Aligns with StrategyResolver v3.1
    - Different frameworks = different PM reasoning
    - Drop-in replacement (NO app.py changes)
    """

    # --------------------------------------------------
    # FRAMEWORK CHOICE
    # --------------------------------------------------
    def explain_framework_choice(self, framework: str, problem_type: str) -> str:
        f = framework.lower()

        if f == "rice":
            return (
                f"The RICE framework was selected because this {problem_type} problem "
                f"requires explicit ROI trade-offs. Comparing reach, impact, confidence, "
                f"and effort ensures scarce capacity is invested where it delivers "
                f"the highest measurable return."
            )

        if f == "ice":
            return (
                f"The ICE framework was chosen to prioritize speed and confidence. "
                f"For this {problem_type} problem, learning quickly and shipping improvements "
                f"is more valuable than perfect estimation upfront."
            )

        if f == "moscow":
            return (
                f"The MoSCoW framework was selected to protect delivery focus. "
                f"This {problem_type} challenge benefits from clearly separating "
                f"must-have commitments from deferrable scope to reduce execution risk."
            )

        if f == "kano":
            return (
                f"The Kano framework was chosen because this {problem_type} problem "
                f"is driven by user expectations and satisfaction. The goal is to "
                f"prevent dissatisfaction while selectively introducing delight."
            )

        return (
            f"A structured prioritization framework was used to make trade-offs "
            f"explicit for this {problem_type} problem."
        )

    # --------------------------------------------------
    # PRIORITIZATION DEFENSE (🔥 KEY FIX)
    # --------------------------------------------------
    def explain_prioritization(self, scored_features: List[Dict], problem_type: str) -> str:
        if not scored_features:
            return "Features were prioritized based on qualitative impact and feasibility."

        top = scored_features[0]["feature"]
        score = scored_features[0]["score"]

        # Numeric frameworks (RICE / ICE)
        if isinstance(score, (int, float)):
            return (
                f"**{top}** emerged as the top priority because it offers the strongest "
                f"impact-to-effort trade-off under the selected framework. Prioritizing "
                f"this initiative maximizes outcomes while minimizing execution risk."
            )

        # Categorical frameworks (MoSCoW / Kano)
        return (
            f"**{top}** was prioritized because it falls into the highest-impact category "
            f"(**{score}**) under the selected framework. Addressing this first establishes "
            f"a stable foundation before lower-impact initiatives are considered."
        )

    # --------------------------------------------------
    # ROADMAP LOGIC
    # --------------------------------------------------
    def explain_roadmap(self, problem_type: str) -> str:
        if problem_type == "onboarding":
            return (
                "The roadmap is front-loaded with activation improvements to ensure users "
                "reach first value quickly before additional complexity is introduced."
            )

        if problem_type == "retention":
            return (
                "The roadmap prioritizes habit-forming and engagement initiatives "
                "before expanding new capabilities, allowing retention gains to compound."
            )

        if problem_type == "growth":
            return (
                "Revenue-impacting initiatives are sequenced early while deferring "
                "longer-term experiments until core growth levers are validated."
            )

        if problem_type == "performance":
            return (
                "Stability and reliability work is prioritized first to avoid scaling "
                "a fragile system and eroding user trust."
            )

        if problem_type == "delivery":
            return (
                "The roadmap protects delivery confidence by sequencing must-have work "
                "ahead of optional enhancements."
            )

        if problem_type == "satisfaction":
            return (
                "The roadmap focuses on reducing friction and improving usability "
                "before introducing delight-driven features."
            )

        return "The roadmap balances short-term impact with long-term scalability."

    # --------------------------------------------------
    # TRADE-OFF DEFENSE
    # --------------------------------------------------
    def explain_tradeoffs(self, problem_type: str) -> str:
        return (
            f"Lower-impact initiatives were intentionally deferred to protect focus "
            f"and reduce delivery risk for this {problem_type} problem."
        )

    # --------------------------------------------------
    # SUCCESS METRICS
    # --------------------------------------------------
    def explain_success_metrics(self, problem_type: str) -> str:
        if problem_type == "onboarding":
            return (
                "Success will be measured by activation rate, time-to-first-value, "
                "and onboarding-related support volume."
            )

        if problem_type == "retention":
            return (
                "Success will be measured through cohort retention, repeat usage frequency, "
                "and churn reduction."
            )

        if problem_type == "growth":
            return (
                "Success will be evaluated using conversion rate, ARPU uplift, "
                "and sustainable revenue growth."
            )

        if problem_type == "performance":
            return (
                "Success will be measured by latency reduction, error rates, "
                "and system reliability indicators."
            )

        if problem_type == "delivery":
            return (
                "Success will be measured by on-time delivery, scope adherence, "
                "and reduced execution risk."
            )

        if problem_type == "satisfaction":
            return (
                "Success will be measured through qualitative feedback, NPS trends, "
                "and sentiment improvement."
            )

        return "Success will be measured using primary business and user outcome metrics."
