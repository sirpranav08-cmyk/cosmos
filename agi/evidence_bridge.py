from agi.hypothesis_manager import HypothesisManager


class EvidenceBridge:

    def __init__(self):

        self.hypothesis_manager = HypothesisManager()

    def process_motion(self, investigations):

        results = []

        for investigation in investigations:

            motion = investigation["motion"]

            candidate_id = investigation[
                "candidate_id"
            ]

            if motion["motion_detected"]:

                evidence = {

                    "type": "motion",

                    "description":
                        "Positional motion detected between observation epochs.",

                    "value":
                        motion["pixel_displacement"],

                    "reliability":
                        0.90,

                    "supports":
                        "Moving astronomical object"
                }

                updated = (
                    self.hypothesis_manager.update(
                        evidence
                    )
                )

                results.append({

                    "candidate_id":
                        candidate_id,

                    "motion_detected":
                        True,

                    "evidence":
                        evidence,

                    "hypotheses":
                        updated
                })

            else:

                results.append({

                    "candidate_id":
                        candidate_id,

                    "motion_detected":
                        False,

                    "evidence":
                        None,

                    "hypotheses":
                        self.hypothesis_manager.hypotheses.copy()
                })

        return results

    def report(self):

        return self.hypothesis_manager.report()