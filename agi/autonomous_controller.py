from agi.autonomous_loop import AutonomousInvestigator


class AutonomousController:

    def __init__(
        self,
        candidate_id,
        candidate=None,
        catalog=None,
        max_cycles=5
    ):

        self.cosmos = AutonomousInvestigator(
            candidate_id=candidate_id
        )

        self.candidate = candidate
        self.catalog = catalog
        self.max_cycles = max_cycles

        self.history = []

    def add_observation(self, observation):

        self.cosmos.add_observation(
            observation
        )

    def add_evidence(self, evidence):

        self.cosmos.add_evidence(
            evidence
        )

    def run(self):

        for cycle in range(
            1,
            self.max_cycles + 1
        ):

            print()
            print("=" * 60)
            print(
                f"COSMOS AUTONOMOUS CYCLE {cycle}"
            )
            print("=" * 60)

            # ----------------------------------------
            # THINK
            # ----------------------------------------

            thinking = self.cosmos.think()

            reflection = thinking[
                "reflection"
            ]

            actions = thinking[
                "actions"
            ]

            print()
            print("REFLECTION")
            print("-" * 60)

            for reason in reflection[
                "reasoning"
            ]:

                print(
                    "->",
                    reason
                )

            print()
            print("MISSING EVIDENCE")

            for missing in reflection[
                "missing_evidence"
            ]:

                print(
                    "->",
                    missing
                )

            print()
            print(
                "STATUS:",
                reflection["status"]
            )

            # ----------------------------------------
            # STOP CONDITION
            # ----------------------------------------

            if (
                reflection["status"]
                == "READY_FOR_VERIFICATION"
            ):

                print()
                print(
                    "COSMOS HAS ENOUGH EVIDENCE "
                    "FOR VERIFICATION."
                )

                break

            # ----------------------------------------
            # NO ACTIONS
            # ----------------------------------------

            if not actions:

                print()
                print(
                    "No actions available."
                )

                break

            # ----------------------------------------
            # ACT
            # ----------------------------------------

            print()
            print("ACTIONS")
            print("-" * 60)

            for action in actions:

                print(
                    "->",
                    action["name"]
                )

            results = self.cosmos.act(
                actions,
                candidate=self.candidate,
                catalog=self.catalog
            )

            # ----------------------------------------
            # RECORD RESULTS
            # ----------------------------------------

            self.history.append({

                "cycle": cycle,

                "reflection": reflection,

                "actions": actions,

                "results": results
            })

            print()
            print("ACTION RESULTS")
            print("-" * 60)

            for result in results:

                print(
                    "Action:",
                    result.get("action")
                )

                print(
                    "Success:",
                    result.get(
                        "success"
                    )
                )

                if "matched" in result:

                    print(
                        "Matched:",
                        result["matched"]
                    )

            # ----------------------------------------
            # STATE
            # ----------------------------------------

            state = self.cosmos.state()

            print()
            print("CURRENT HYPOTHESIS")
            print("-" * 60)

            print(
                "Strongest:",
                state[
                    "hypotheses"
                ]["strongest"]
            )

            print(
                "Confidence:",
                f"{state['hypotheses']['confidence']:.2f}"
            )

        return self.cosmos.state()