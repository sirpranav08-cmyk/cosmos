from agi.reflection import ReflectionEngine
from agi.action_planner import ActionPlanner


class AutonomousInvestigator:

    def __init__(self, action_executor):

        self.reflection_engine = ReflectionEngine()
        self.action_planner = ActionPlanner()
        self.action_executor = action_executor

    def investigate(self, investigation):

        print()
        print("=" * 60)
        print("COSMOS AUTONOMOUS INVESTIGATION")
        print("=" * 60)

        # --------------------------------
        # STEP 1: REFLECTION
        # --------------------------------

        print()
        print("STEP 1: REFLECTION")
        print("-" * 60)

        reflection = self.reflection_engine.reflect(
            investigation
        )

        for reasoning in reflection["reasoning"]:
            print("->", reasoning)

        # --------------------------------
        # STEP 2: MISSING EVIDENCE
        # --------------------------------

        print()
        print("MISSING EVIDENCE")
        print("-" * 60)

        for evidence in reflection[
            "missing_evidence"
        ]:

            print("->", evidence)

        # --------------------------------
        # STEP 3: ACTION PLANNING
        # --------------------------------

        print()
        print("STEP 2: ACTION PLANNING")
        print("-" * 60)

        actions = self.action_planner.plan(
            reflection
        )

        for action in actions:

            print(
                f"-> {action['name']}: "
                f"{action['description']}"
            )

        # --------------------------------
        # STEP 4: ACTION EXECUTION
        # --------------------------------

        print()
        print("STEP 3: ACTION EXECUTION")
        print("-" * 60)

        execution_results = []

        for action in actions:

            # IMPORTANT:
            # ActionExecutor.execute()
            # expects the complete dictionary.
            result = self.action_executor.execute(
                action
            )

            execution_results.append({
                "action": action["name"],
                "result": result
            })

            print(
                f"-> {action['name']}: "
                f"{result}"
            )

        # --------------------------------
        # STEP 5: STATUS
        # --------------------------------

        print()
        print("INVESTIGATION STATUS")
        print("-" * 60)

        print(
            "Status:",
            reflection["status"]
        )

        return {
            "reflection": reflection,
            "actions": actions,
            "execution": execution_results
        }