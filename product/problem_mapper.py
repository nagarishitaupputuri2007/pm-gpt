class ProblemMapper:
    def map(self, problem_text: str) -> dict:
        text = problem_text.lower()

        # -------------------------
        # PROBLEM TYPE DETECTION
        # -------------------------
        if any(k in text for k in ["onboarding", "signup", "activation", "kyc"]):
            problem_type = "activation"

        elif any(k in text for k in [
            # Explicit retention terms
            "churn",
            "retention",
            "downgrade",

            # Trial-related retention
            "trial",
            "free trial",
            "trial ends",
            "users leave after trial",
            "not converting after trial",
            "post-trial",

            # Behavioral retention (PM language)
            "repeat order",
            "repeat orders",
            "low repeat",
            "second order",
            "come back",
            "not returning",
            "after first",
            "week 1",
        ]):
            problem_type = "retention"

        elif any(k in text for k in ["slow", "performance", "latency", "reliability"]):
            problem_type = "performance"

        else:
            problem_type = "general"

        # -------------------------
        # CORE PROBLEM
        # -------------------------
        core_problem = (
            "Users are failing to reach product value efficiently."
            if problem_type == "activation"
            else "Users are disengaging due to unmet product expectations."
            if problem_type == "retention"
            else "Product reliability and performance issues are impacting trust."
            if problem_type == "performance"
            else "The product is not meeting user or business expectations."
        )

        # -------------------------
        # USER FAILURE POINT
        # -------------------------
        user_failure_point = (
            "Users drop off before completing first-time setup."
            if problem_type == "activation"
            else "Power users abandon workflows or downgrade plans."
            if problem_type == "retention"
            else "Users experience slow or unreliable behavior during key actions."
            if problem_type == "performance"
            else "Users encounter friction that blocks success."
        )

        # -------------------------
        # BUSINESS IMPACT
        # -------------------------
        if problem_type == "activation":
            business_impact = [
                "Lower activation and conversion rates",
                "Higher customer acquisition cost due to drop-offs",
                "Reduced downstream retention and monetization",
            ]
        elif problem_type == "retention":
            business_impact = [
                "Increased churn among high-value users",
                "Revenue loss from reduced repeat usage or downgrades",
                "Negative impact on lifetime value (LTV)",
            ]
        elif problem_type == "performance":
            business_impact = [
                "Loss of trust among power users",
                "Higher support and operational costs",
                "Revenue risk from churn and reduced expansion",
            ]
        else:
            business_impact = [
                "Negative impact on key product KPIs",
                "Reduced user satisfaction",
                "Long-term business risk if unresolved",
            ]

        # -------------------------
        # EXECUTION CONSTRAINTS
        # -------------------------
        if problem_type == "activation":
            constraints = [
                "Onboarding changes must not increase compliance or fraud risk",
                "Engineering capacity is limited for major flow rewrites",
                "Experiments must avoid harming existing conversion funnels",
            ]
        elif problem_type == "retention":
            constraints = [
                "Must prioritize high-value user segments",
                "Behavioral changes require time to validate impact",
                "Engineering focus is split across multiple roadmap initiatives",
            ]
        elif problem_type == "performance":
            constraints = [
                "System changes must avoid downtime or regressions",
                "Improvements must be shipped incrementally",
                "Observability and monitoring coverage is limited",
            ]
        else:
            constraints = [
                "Limited engineering capacity",
                "Need to balance speed with quality",
                "Execution risk must be carefully managed",
            ]

        # -------------------------
        # SUCCESS DEFINITION
        # -------------------------
        success_definition = (
            "Improve activation and time-to-first-value."
            if problem_type == "activation"
            else "Reduce churn and increase retention of high-value users."
            if problem_type == "retention"
            else "Improve reliability, latency, and user trust."
            if problem_type == "performance"
            else "Improve overall product outcomes."
        )

        # -------------------------
        # PM-GRADE SUMMARY
        # -------------------------
        if problem_type == "activation":
            summary = (
                "This is a critical activation problem occurring at a high-leverage moment "
                "in the user journey. Users are dropping off before reaching first value, "
                "which directly reduces conversion efficiency and inflates acquisition costs. "
                "If left unresolved, this bottleneck compounds downstream retention and monetization losses."
            )
        elif problem_type == "retention":
            summary = (
                "This is a high-impact retention problem affecting the most valuable segment "
                "of the user base. Users disengage after initial value realization, leading "
                "to reduced repeat usage and revenue contraction. If left unaddressed, this erosion "
                "compounds over time and weakens long-term growth."
            )
        elif problem_type == "performance":
            summary = (
                "This problem undermines trust in the product during critical usage moments. "
                "Reliability and performance issues disproportionately affect core workflows, "
                "increasing churn risk and operational cost."
            )
        else:
            summary = (
                "This problem negatively impacts both user experience and business outcomes "
                "at a critical point in the product journey."
            )

        return {
            "problem_type": problem_type,
            "core_problem": core_problem,
            "user_failure_point": user_failure_point,
            "business_impact": business_impact,
            "constraints": constraints,
            "success_definition": success_definition,
            "summary": summary,
        }
