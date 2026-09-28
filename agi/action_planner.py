class ActionPlanner:

    ACTIONS = {
        "request_additional_epoch":
            "Acquire another observation epoch",

        "calculate_motion":
            "Calculate positional motion",

        "analyze_spectrum":
            "Analyze spectral characteristics",

        "check_artifacts":
            "Check for imaging or measurement artifacts",

        "cross_match_catalog":
            "Cross-match candidate with astronomical catalogs"
    }

    def plan(self, reflection):

        actions = []

        for action_name in reflection[
            "recommended_actions"
        ]:

            description = self.ACTIONS.get(
                action_name,
                "Unknown scientific action"
            )

            actions.append({
                "name": action_name,
                "description": description
            })

        return actions