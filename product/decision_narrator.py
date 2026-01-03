from typing import List, Dict


class DecisionNarrator:
    """
    Phase 4 – FAANG-Grade PM Decision Narrative Engine (v4.0)

    Design goals:
    - Framework-aware (RICE / ICE / MoSCoW / Kano)
    - Problem-aware (growth, onboarding, retention, delivery, etc.)
    - Decision-first (not feature-first)
    - Drop-in replacement (NO app.py changes)
    """

    # --------------------------------------------------
    # FRAMEWORK CHOICE — DECISION LENS
    # --------------------------------------------------
    def explain_framework_choice(self, framework: str, problem_type: str) -> str:
        f = framework.lower()

        if f == "rice":
            return (
                f"For this {problem_type} problem, the core risk is misallocating limited capacity "
                f"across competing opportunities. RICE was selected to impose a quantitative lens "
                f"on reach, impact, confidence, and effort, enabling objective comparison of bets "
                f"and prioritization based on expected return."
            )

        if f == "ice":
            return (
                f"This {problem_type} problem is characterized by uncertainty rather than execution failure. "
                f"ICE was chosen to prioritize speed of learning, allowing the team to validate assumptions "
                f"quickly and avoid over-investing before signal strength is established."
            )

        if f == "moscow":
            return (
                f"The dominant risk in this {problem_type} problem is delivery slippage. "
                f"MoSCoW was applied to enforce scope discipline, ensuring must-have commitments "
                f"are protected while lower-criticality work remains intentionally flexible."
            )

        if f == "kano":
            return (
                f"This {problem_type} problem is driven by user expectations rather than raw functionality. "
                f"Kano was selected to distinguish baseline requirements from performance drivers "
                f"and delighters, ensuring effort translates into perceived value."
            )

        return (
            f"A structured prioritization framework was used to make trade-offs explicit "
            f"and reduce decision ambiguity for this {problem_type} problem."
        )

    # --------------------------------------------------
    # PRIORITIZATION — WHY THIS BET
    # --------------------------------------------------
    def explain_prioritization(self, scored_features: List[Dict], problem_type: str) -> str:
        if not scored_features:
            return (
                "Features were prioritized using qualitative impact assessment and feasibility, "
                "with an emphasis on minimizing execution risk."
            )

        top_feature = scored_features[0]["feature"]
        score = scored_features[0]["score"]

        # Numeric scoring (RICE / ICE)
        if isinstance(score, (int, float)):
            return (
                f"**{top_feature}** represents the highest-leverage opportunity under the selected framework. "
                f"It was prioritized because it offers a strong impact-to-effort ratio while maintaining "
                f"acceptable confidence, making it the most defensible near-term bet for this {problem_type} context."
            )

        # Categorical scoring (MoSCoW / Kano)
        return (
            f"**{top_feature}** was prioritized because it falls into the highest-priority category "
            f"(**{score}**). Addressing this first reduces downstream risk and establishes a stable "
            f"foundation before investing in lower-impact initiatives."
        )

    # --------------------------------------------------
    # ROADMAP — WHY THIS SEQUENCE
    # --------------------------------------------------
    def explain_roadmap(self, problem_type: str) -> str:
        if problem_type == "onboarding":
            return (
                "The roadmap is intentionally front-loaded with activation improvements. "
                "Reducing early friction increases the likelihood that subsequent investments "
                "compound rather than leak value."
            )

        if problem_type == "retention":
            return (
                "The roadmap prioritizes habit-forming and engagement drivers first, "
                "allowing retention gains to compound before expanding scope."
            )

        if problem_type == "growth":
            return (
                "High-confidence growth levers are sequenced early, while longer-horizon experiments "
                "are deferred until core drivers demonstrate consistent signal."
            )

        if problem_type == "performance":
            return (
                "Stability and reliability work is prioritized before scale. "
                "This avoids amplifying systemic risk and protects user trust."
            )

        if problem_type == "delivery":
            return (
                "The roadmap sequence protects delivery confidence by ensuring "
                "critical commitments are met before optional enhancements."
            )

        if problem_type == "satisfaction":
            return (
                "The roadmap focuses on eliminating sources of dissatisfaction "
                "before layering in delight-driven improvements."
            )

        return (
            "The roadmap balances near-term impact with long-term optionality, "
            "sequencing work to minimize compounding risk."
        )

    # --------------------------------------------------
    # TRADE-OFFS — WHAT WE SAID NO TO
    # --------------------------------------------------
    def explain_tradeoffs(self, problem_type: str) -> str:
        return (
            f"Lower-impact or higher-uncertainty initiatives were intentionally deprioritized. "
            f"This trade-off favors depth of impact over breadth of execution for this {problem_type} problem."
        )

    # --------------------------------------------------
    # SUCCESS METRICS — HOW WE KNOW IT WORKED
    # --------------------------------------------------
    def explain_success_metrics(self, problem_type: str) -> str:
        if problem_type == "onboarding":
            return (
                "Success will be measured through activation rate improvement, "
                "reduced time-to-first-value, and lower onboarding-related support volume."
            )

        if problem_type == "retention":
            return (
                "Success will be evaluated using cohort retention curves, "
                "repeat usage frequency, and churn reduction."
            )

        if problem_type == "growth":
            return (
                "Success will be measured by conversion uplift, ARPU growth, "
                "and the sustainability of revenue gains over time."
            )

        if problem_type == "performance":
            return (
                "Success will be measured via latency reduction, error rate improvements, "
                "and overall system reliability."
            )

        if problem_type == "delivery":
            return (
                "Success will be measured by on-time delivery, scope adherence, "
                "and reduced execution risk."
            )

        if problem_type == "satisfaction":
            return (
                "Success will be evaluated using qualitative feedback, NPS movement, "
                "and sentiment trends."
            )

        return (
            "Success will be measured using a combination of primary business outcomes "
            "and leading user behavior indicators."
        )
