# product/framework_selector.py

class FrameworkSelector:
    """
    Selects the most appropriate prioritization framework
    based on the given problem context.
    """

    def select(self, problem: str) -> str:
        problem = problem.lower()

        if "user" in problem or "experience" in problem:
            return "Kano"

        if "quick" in problem or "fast" in problem:
            return "ICE"

        if "stakeholder" in problem or "requirement" in problem:
            return "MoSCoW"

        # Default framework
        return "RICE"
