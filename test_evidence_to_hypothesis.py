from science_engine.investigation_engine import InvestigationEngine
from agi.science_adapter import ScienceEvidenceAdapter
from agi.hypothesis_manager import HypothesisManager


print()
print("=" * 60)
print("COSMOS EVIDENCE → HYPOTHESIS")
print("=" * 60)


# ============================================================
# OBSERVATIONS
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
# SCIENCE
# ============================================================

investigation_engine = InvestigationEngine(
    max_match_distance=10.0
)

investigations = investigation_engine.investigate(
    epoch_a,
    epoch_b,
    time_delta=10.0
)


# ============================================================
# SCIENCE → AGI
# ============================================================

adapter = ScienceEvidenceAdapter()

evidence = adapter.motion_evidence(
    investigations
)


print()
print("SCIENCE EVIDENCE")
print("-" * 60)

for item in evidence:

    print(
        f"Candidate {item['candidate_id']}: "
        f"motion = {item['pixel_displacement']}"
    )


# ============================================================
# HYPOTHESIS MANAGER
# ============================================================

manager = HypothesisManager()


print()
print("INITIAL HYPOTHESES")
print("-" * 60)

for name, probability in manager.hypotheses.items():

    print(
        f"{name}: {probability:.2f}"
    )


# ============================================================
# APPLY EVIDENCE
# ============================================================

for item in evidence:

    manager.update(item)


print()
print("UPDATED HYPOTHESES")
print("-" * 60)

report = manager.report()

for name, probability in report["hypotheses"].items():

    print(
        f"{name}: {probability:.2f}"
    )


print()
print("CURRENT ASSESSMENT")
print("-" * 60)

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
print("EVIDENCE → HYPOTHESIS COMPLETE")
print("=" * 60)