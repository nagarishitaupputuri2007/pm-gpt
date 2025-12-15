class FrameworkSelector:
    """
    Decides which prioritization framework to use
    based on decision context.
    """

    def select(self, context: dict) -> str:
        goal = context.get("goal")
        time_pressure = context.get("time_pressure")
        delivery_commitment = context.get("delivery_commitment")
        focus = context.get("focus")

        if time_pressure == "high":
            return "ICE"

        if delivery_commitment:
            return "MoSCoW"

        if focus == "satisfaction":
            return "Kano"

        return "RICE"
