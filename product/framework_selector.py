# product/framework_selector.py

class FrameworkSelector:
    """
    Phase 3 – Intelligent Framework Selection (v2.1)

    Uses problem severity and business context to select
    PM frameworks the way a senior PM would.
    """

    def select(self, problem_summary: str) -> str:
        text = problem_summary.lower()

        # --- Signal detection ---
        has_growth = any(k in text for k in ["growth", "revenue", "monetization"])
        has_onboarding = any(k in text for k in ["activation", "onboarding"])
        has_retention = any(k in text for k in ["retention", "churn"])
        has_performance = any(k in text for k in ["performance", "reliability", "latency"])
        has_delivery = any(k in text for k in ["delivery", "scope", "deadline"])
        has_value = any(k in text for k in ["value", "satisfaction", "experience"])

        # --- PM decision logic (priority-based) ---

        # 1️⃣ Business-impact & survival problems → RICE
        if has_growth or (has_onboarding and has_retention):
            return "RICE"

        # 2️⃣ Speed & execution problems → ICE
        if has_performance:
            return "ICE"

        # 3️⃣ Scope control & delivery planning → MoSCoW
        if has_delivery:
            return "MoSCoW"

        # 4️⃣ ONLY pure satisfaction / delight problems → Kano
        if has_value and not (has_onboarding or has_retention or has_growth):
            return "Kano"

        # 5️⃣ Safe PM default
        return "RICE"
