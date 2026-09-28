from agi.autonomous_loop import (
    AutonomousInvestigator
)


print()
print("=" * 60)
print("COSMOS AUTONOMOUS INVESTIGATION")
print("=" * 60)


cosmos = AutonomousInvestigator(
    "candidate_1042"
)


print("\n1. ADD OBSERVATIONS")
print("-" * 60)


cosmos.add_observation({
    "epoch": "2026-05-01",
    "ra": 182.341,
    "dec": -12.552
})


cosmos.add_observation({
    "epoch": "2026-05-15",
    "ra": 182.342,
    "dec": -12.551
})


print("Two observations added.")


print("\n2. ADD MOTION EVIDENCE")
print("-" * 60)


cosmos.add_evidence({
    "type": "motion",
    "value": 0.001414,
    "source": "motion_analysis"
})


print("Motion evidence added.")


print("\n3. ADD SPECTRAL EVIDENCE")
print("-" * 60)


cosmos.add_evidence({
    "type": "spectrum",
    "bands": 3,
    "source": "spectral_analysis"
})


print("Spectral evidence added.")


print("\n4. COSMOS REFLECTION")
print("-" * 60)


thinking = cosmos.think()


for reason in thinking[
    "reflection"
]["reasoning"]:

    print(
        "->",
        reason
    )


print("\nMISSING EVIDENCE")

for item in thinking[
    "reflection"
]["missing_evidence"]:

    print(
        "->",
        item
    )


print("\n5. PLANNED ACTIONS")
print("-" * 60)


for action in thinking["actions"]:

    print(
        "->",
        action["name"]
    )


print("\n6. EXECUTION")
print("-" * 60)


results = cosmos.act(
    thinking["actions"]
)


for result in results:

    print(
        "->",
        result["action"],
        ":",
        result["success"]
    )


print("\n7. CURRENT COSMOS STATE")
print("-" * 60)


state = cosmos.state()


print(
    "Candidate:",
    state["candidate"]
)


print(
    "Strongest hypothesis:",
    state[
        "hypotheses"
    ]["strongest"]
)


print(
    "Internal confidence:",
    f"{state['hypotheses']['confidence']:.2f}"
)


print(
    "Investigation status:",
    state[
        "investigation"
    ]["status"]
)


print()
print("=" * 60)
print("AUTONOMOUS INVESTIGATION COMPLETE")
print("=" * 60)