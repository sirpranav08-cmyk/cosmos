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

        self.reflection_engine = ReflectionEngine()
        self.planner = ActionPlanner()
        self.executor = ActionExecutor()
        self.hypothesis_manager = HypothesisManager()

        self.investigation.status = "INVESTIGATING"

    # ============================================================
    # OBSERVATION
    # ============================================================

    def add_observation(self, observation):

        self.investigation.add_observation(
            observation
        )

    # ============================================================
    # EVIDENCE
    # ============================================================

    def add_evidence(self, evidence):

        self.investigation.add_evidence(
            evidence
        )

        self.hypothesis_manager.update(
            evidence
        )

    # ============================================================
    # THINK
    # ============================================================

    def think(self):

        reflection = self.reflection_engine.reflect(
            self.investigation
        )

        if reflection["status"] == "READY_FOR_VERIFICATION":

            self.investigation.status = "VERIFYING"

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

    # ============================================================
    # ACT
    # ============================================================

    def act(
        self,
        actions,
        candidate=None,
        catalog=None
    ):

        results = []

        for action in actions:

            print(
                f"Executing action: {action['name']}"
            )

            result = self.executor.execute(
                action,
                candidate=candidate,
                catalog=catalog
            )

            results.append(result)

            self._process_result(
                result
            )

        return results

    # ============================================================
    # PROCESS EXECUTOR RESULT
    # ============================================================

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

        if output is None:

            output = {}

        # ========================================================
        # ARTIFACT
        # ========================================================

        if action == "check_artifacts":

            evidence = {

                "type":
                    "artifact_check",

                "artifact_probability":
                    output.get(
                        "artifact_probability",
                        0.5
                    ),

                "change_fraction":
                    output.get(
                        "change_fraction",
                        0.0
                    ),

                "status":
                    output.get(
                        "status",
                        "UNKNOWN"
                    ),

                "source":
                    "artifact_analysis"
            }

            self.add_evidence(
                evidence
            )

        # ========================================================
        # MOTION
        # ========================================================

        elif action == "calculate_motion":

            evidence = {

                "type":
                    "motion",

                "motion_detected":
                    output.get(
                        "motion_detected",
                        False
                    ),

                "source":
                    "motion_analysis"
            }

            self.add_evidence(
                evidence
            )

        # ========================================================
        # SPECTRUM
        # ========================================================

        elif action == "analyze_spectrum":

            evidence = {

                "type":
                    "spectrum",

                "available":
                    output.get(
                        "spectrum_available",
                        False
                    ),

                "source":
                    "spectral_analysis"
            }

            self.add_evidence(
                evidence
            )

        # ========================================================
        # ADDITIONAL OBSERVATION
        # ========================================================

        elif action == "request_additional_epoch":

            evidence = {

                "type":
                    "observation_request",

                "status":
                    output.get(
                        "status",
                        "UNKNOWN"
                    ),

                "source":
                    "observation_manager"
            }

            self.add_evidence(
                evidence
            )

        # ========================================================
        # CATALOG CROSS-MATCH
        # ========================================================

        elif action == "cross_match_catalog":

            matches = output.get(
                "matches",
                []
            )

            matched = output.get(
                "matched",
                len(matches) > 0
            )

            evidence = {

                "type":
                    "catalog_match",

                "matched":
                    matched,

                "matches":
                    matches,

                "source":
                    "catalog_search"
            }

            self.add_evidence(
                evidence
            )

    # ============================================================
    # STATE
    # ============================================================

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