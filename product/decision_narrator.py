class DecisionNarrator:
    """
    Generates PM-style reasoning for framework choice,
    prioritization, roadmap sequencing, trade-offs, and success metrics.

    IMPORTANT:
    - Works ONLY with list-based scored features
    - Never assumes pandas / iloc
    """

    def explain_framework_choice(self, framework: str) -> str:
        return (
            f"The {framework} framework was selected because it enables structured "
            "decision-making under limited engineering capacity. It helps balance "
            "impact, effort, and confidence while making trade-offs explicit."
        )

    def explain_prioritization(self, scored_features) -> str:
        if not scored_features or not isinstance(scored_features, list):
            return (
                "Features were prioritized based on qualitative impact and feasibility, "
                "focusing first on solving core user problems."
            )

        # Sort safely by score (descending)
        sorted_features = sorted(
            scored_features,
            key=lambda x: x.get("score", 0),
            reverse=True
        )

        top_feature = sorted_features[0]["feature"]

        return (
            f"The highest-priority item is **{top_feature}**, as it directly addresses "
            "the most critical user and business pain points. Features with lower scores "
            "were sequenced later to reduce delivery risk and ensure early wins."
        )

    def explain_roadmap(self) -> str:
        return (
            "The roadmap is intentionally sequenced to first stabilize the product and "
            "improve early value realization. Once activation and reliability improve, "
            "the focus shifts toward optimization and scalable growth initiatives."
        )

    def explain_tradeoffs(self) -> str:
        return (
            "Short-term feature expansion was deprioritized in favor of fixing foundational "
            "issues such as onboarding clarity and performance. This trade-off reduces the "
            "risk of building new features on an unstable product experience."
        )

    def explain_success_metrics(self) -> str:
        return (
            "Success will be measured through activation rate, time-to-first-value, "
            "retention cohorts, onboarding-related support tickets, and engagement among "
            "power users. These metrics directly reflect whether the core problems are resolved."
        )
