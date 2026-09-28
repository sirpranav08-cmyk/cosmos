from agi import ActionPlanner
from agi import ActionExecutor
from agi import Investigation
from agi import ReflectionEngine


print()
print("=" * 60)
print("COSMOS ACTION EXECUTOR")
print("=" * 60)


investigation = Investigation(
    candidate_id="candidate_1042"
)


investigation.add_observation({
    "epoch": "2026-05-01",
    "ra": 182.341,
    "dec": -12.552
})


investigation.add_observation({
    "epoch": "2026-05-15",
    "ra": 182.342,
    "dec": -12.551
})


investigation.add_evidence({
    "type": "motion",
    "value": 0.001414,
    "source": "motion_analysis"
})


investigation.add_evidence({
    "type": "spectrum",
    "value": 3,
    "source": "spectral_analysis"
})


# Reflection
reflection_engine = ReflectionEngine()

reflection = reflection_engine.reflect(
    investigation
)


# Planning
planner = ActionPlanner()

actions = planner.plan(
    reflection
)


# Execution
executor = ActionExecutor()


print("\nEXECUTING ACTIONS")
print("-" * 60)


for action in actions:

    print(
        f"\nACTION: {action['name']}"
    )

    result = executor.execute(
        action
    )

    print(
        "SUCCESS:",
        result["success"]
    )

    print(
        "RESULT:",
        result["result"]
    )