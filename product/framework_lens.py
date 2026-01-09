class FrameworkLens:
    @staticmethod
    def explain(framework: str) -> str:
        framework = (framework or "").lower()

        if framework == "rice":
            return "RICE helps compare multiple options objectively using reach, impact, confidence, and effort."

        if framework == "moscow":
            return "MoSCoW helps prioritize must-haves over nice-to-haves when scope or timelines are tight."

        if framework == "kano":
            return "Kano helps distinguish basic expectations from performance drivers and delighters."

        if framework == "ice":
            return "ICE enables fast decisions under uncertainty by balancing impact, confidence, and ease."

        return "This framework provides a structured decision lens."
