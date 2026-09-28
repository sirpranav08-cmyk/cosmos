from agi import (
    Investigation,
    ReflectionEngine,
    ActionPlanner,
    ActionExecutor,
    HypothesisManager
)


class AutonomousInvestigator:

    def __init__(self, candidate_id):

        self.investigation = Investigation(
            candidate_id=candidate_id
        )

        self.reflection_engine = (
            ReflectionEngine()
        )

        self.planner = ActionPlanner()

        self.executor = ActionExecutor()

        self.hypothesis_manager = (
            HypothesisManager()
        )

        self.investigation.status = (
            "INVESTIGATING"
        )

    def add_observation(
        self,
        observation
    ):

        self.investigation.add_observation(
            observation
        )

    def add_evidence(
        self,
        evidence
    ):

        self.investigation.add_evidence(
            evidence
        )

        self.hypothesis_manager.update(
            evidence
        )

    def think(self):

        reflection = (
            self.reflection_engine.reflect(
                self.investigation
            )
        )

        if reflection["status"] == (
            "READY_FOR_VERIFICATION"
        ):

            self.investigation.status = (
                "VERIFYING"
            )

        else:

            self.investigation.status = (
                "MORE_EVIDENCE_REQUIRED"
            )

        actions = self.planner.plan(
            reflection
        )

        return {
            "reflection": reflection,
            "actions": actions
        }

    def act(self, actions):

        results = []

        for action in actions:

            result = self.executor.execute(
                action
            )

            results.append(result)

            self._process_result(
                result
            )

        return results

    def _process_result(self, result):

        if not result.get("success"):
            return

        action = result.get(
            "action"
        )

        output = result.get(
            "result",
            {}
        )

        # --------------------------------
        # Convert executor result
        # into scientific evidence
        # --------------------------------

        if action == "check_artifacts":

            evidence = {
                "type": "artifact_check",
                "artifact_probability":
                    output.get(
                        "artifact_probability",
                        0.5
                    ),
                "source": "artifact_analysis"
            }

            self.add_evidence(
                evidence
            )

        elif action == "calculate_motion":

            evidence = {
                "type": "motion",
                "motion_detected":
                    output.get(
                        "motion_detected",
                        False
                    ),
                "source": "motion_analysis"
            }

            self.add_evidence(
                evidence
            )

        elif action == "analyze_spectrum":

            evidence = {
                "type": "spectrum",
                "available":
                    output.get(
                        "spectrum_available",
                        False
                    ),
                "source": "spectral_analysis"
            }

            self.add_evidence(
                evidence
            )

        elif action == "request_additional_epoch":

            evidence = {
                "type": "observation_request",
                "status":
                    output.get(
                        "status",
                        "UNKNOWN"
                    ),
                "source": "observation_manager"
            }

            self.add_evidence(
                evidence
            )

        elif action == "cross_match_catalog":

            evidence = {
                "type": "catalog_match",
                "matches":
                    output.get(
                        "matches",
                        []
                    ),
                "source": "catalog_search"
            }

            self.add_evidence(
                evidence
            )

    def state(self):

        hypothesis_report = (
            self.hypothesis_manager.report()
        )

        return {

            "candidate":
                self.investigation.candidate_id,

            "hypotheses":
                hypothesis_report,

            "investigation":
                self.investigation.summary()
        }