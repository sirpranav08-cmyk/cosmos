from science_engine.investigation_engine import InvestigationEngine
from agi.science_adapter import ScienceEvidenceAdapter


print()
print("=" * 60)
print("COSMOS SCIENCE → AGI EVIDENCE")
print("=" * 60)


# ============================================================
# EPOCH DATA
# ============================================================

epoch_a = [

    {
        "source_id": 1,
        "x": 300.0,
        "y": 250.0
    },

    {
        "source_id": 2,
        "x": 200.0,
        "y": 350.0
    }
]


epoch_b = [

    {
        "source_id": 1,
        "x": 304.0,
        "y": 253.0
    },

    {
        "source_id": 2,
        "x": 200.0,
        "y": 350.0
    }
]


# ============================================================
# SCIENCE INVESTIGATION
# ============================================================

engine = InvestigationEngine(
    max_match_distance=10.0
)

investigations = engine.investigate(
    epoch_a,
    epoch_b,
    time_delta=10.0
)


print()
print("SCIENCE INVESTIGATION")
print("-" * 60)

for item in investigations:

    print(
        "Candidate:",
        item["candidate_id"]
    )

    print(
        "Motion:",
        item["motion"]["motion_detected"]
    )

    print(
        "Displacement:",
        item["motion"]["pixel_displacement"]
    )


# ============================================================
# AGI EVIDENCE BRIDGE
# ============================================================

adapter = ScienceEvidenceAdapter()

evidence = adapter.motion_evidence(
    investigations
)


print()
print("AGI EVIDENCE")
print("-" * 60)

for item in evidence:

    print(
        "Evidence type:",
        item["type"]
    )

    print(
        "Candidate:",
        item["candidate_id"]
    )

    print(
        "Delta X:",
        item["delta_x"]
    )

    print(
        "Delta Y:",
        item["delta_y"]
    )

    print(
        "Displacement:",
        item["pixel_displacement"]
    )

    print(
        "Velocity:",
        item["pixel_velocity"]
    )

    print(
        "Source:",
        item["source"]
    )


print()
print("=" * 60)
print("SCIENCE → AGI BRIDGE COMPLETE")
print("=" * 60)