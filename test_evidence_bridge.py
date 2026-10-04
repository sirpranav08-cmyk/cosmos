from science_engine.investigation_engine import (
    InvestigationEngine
)

from agi.evidence_bridge import (
    EvidenceBridge
)


print()
print("=" * 60)
print("COSMOS AGI EVIDENCE BRIDGE")
print("=" * 60)


# ----------------------------------------
# Epoch A
# ----------------------------------------

epoch_a = [

    {
        "x": 300.0,
        "y": 250.0,
        "signal": 0.8
    },

    {
        "x": 200.0,
        "y": 350.0,
        "signal": 0.6
    }
]


# ----------------------------------------
# Epoch B
# ----------------------------------------

epoch_b = [

    {
        "x": 304.0,
        "y": 253.0,
        "signal": 0.82
    },

    {
        "x": 200.0,
        "y": 350.0,
        "signal": 0.61
    }
]


# ----------------------------------------
# SCIENCE ENGINE
# ----------------------------------------

investigation_engine = InvestigationEngine()

investigations = investigation_engine.investigate(
    epoch_a,
    epoch_b,
    time_delta=10.0
)


print()
print("SCIENCE RESULTS")
print("-" * 60)

for result in investigations:

    print(
        f"Candidate {result['candidate_id']}: "
        f"motion = "
        f"{result['motion']['motion_detected']}"
    )


# ----------------------------------------
# AGI EVIDENCE BRIDGE
# ----------------------------------------

bridge = EvidenceBridge()

results = bridge.process_motion(
    investigations
)


print()
print("AGI EVIDENCE")
print("-" * 60)

for result in results:

    print(
        f"Candidate {result['candidate_id']}"
    )

    print(
        "Motion detected:",
        result["motion_detected"]
    )

    if result["evidence"]:

        print(
            "Evidence:",
            result["evidence"]["description"]
        )

        print(
            "Evidence value:",
            result["evidence"]["value"]
        )


# ----------------------------------------
# HYPOTHESIS REPORT
# ----------------------------------------

report = bridge.report()


print()
print("HYPOTHESIS ASSESSMENT")
print("-" * 60)

for name, confidence in report[
    "hypotheses"
].items():

    print(
        f"{name}: "
        f"{confidence:.2f}"
    )


print()
print(
    "Strongest hypothesis:",
    report["strongest"]
)

print(
    "Confidence:",
    f"{report['confidence']:.2f}"
)


print()
print("=" * 60)
print("AGI EVIDENCE BRIDGE COMPLETE")
print("=" * 60)