class Planner:

    def create_plan(self, goal):

        goal = goal.lower()

        if "moving" in goal:

            return [
                "load_observations",
                "compare_epochs",
                "calculate_motion",
                "analyze_spectrum",
                "verify_candidate",
                "generate_report"
            ]

        if "unusual" in goal:

            return [
                "load_observations",
                "detect_changes",
                "calculate_motion",
                "analyze_spectrum",
                "search_catalog",
                "verify_candidate",
                "generate_report"
            ]

        return [
            "load_observations",
            "analyze_observations",
            "generate_report"
        ]