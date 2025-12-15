class FrameworkSelector:
    """
    Automatically selects a PM prioritization framework
    based on decision context.
    """

    def select(self, context: dict) -> str:
        goal = context.get("goal")
        time_pressure = context.get("time_pressure")
        delivery_commitment = context.get("delivery_commitment")
        focus = context.get("focus")

        # Fast decisions
        if time_pressure == "high":
            return "ICE"

        # Delivery planning
        if delivery_commitment:
            return "MoSCoW"

        # Customer satisfaction analysis
        if focus == "satisfaction":
            return "Kano"

        # Default
        return "RICE"
