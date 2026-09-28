from agi.investigation import Investigation
from agi.reflection import ReflectionEngine


print()
print("=" * 60)
print("COSMOS REFLECTION ENGINE")
print("=" * 60)


investigation = Investigation(
    candidate_id="candidate_1042"
)


# Add current observations
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


# Add evidence
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


# Run reflection
engine = ReflectionEngine()

result = engine.reflect(
    investigation
)


print("\nREFLECTION")
print("-" * 60)

for reason in result["reasoning"]:

    print(
        "->",
        reason
    )


print("\nMISSING EVIDENCE")
print("-" * 60)

for item in result["missing_evidence"]:

    print(
        "->",
        item
    )


print("\nRECOMMENDED ACTIONS")
print("-" * 60)

for action in result["recommended_actions"]:

    print(
        "->",
        action
    )


print("\nSTATUS")
print("-" * 60)

print(
    result["status"]
)