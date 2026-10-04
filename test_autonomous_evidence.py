from science_engine.investigation_engine import InvestigationEngine
from agi.science_adapter import ScienceEvidenceAdapter
from agi.action_executor import ActionExecutor
from agi.hypothesis_manager import HypothesisManager
from science_engine.pipeline import SciencePipeline


print()
print("=" * 60)
print("COSMOS AUTONOMOUS EVIDENCE LOOP")
print("=" * 60)


# ============================================================
# 1. SCIENCE OBSERVATIONS
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
# 2. MOTION INVESTIGATION
# ============================================================

engine = InvestigationEngine(
    max_match_distance=10.0
)

investigations = engine.investigate(
    epoch_a,
    epoch_b,
    time_delta=10.0
)


# ============================================================
# 3. MOTION → EVIDENCE
# ============================================================

adapter = ScienceEvidenceAdapter()

motion_evidence = adapter.motion_evidence(
    investigations
)


print()
print("MOTION EVIDENCE")
print("-" * 60)

for item in motion_evidence:

    print(
        "Candidate:",
        item["candidate_id"]
    )

    print(
        "Displacement:",
        item["pixel_displacement"]
    )

    print(
        "Velocity:",
        item["pixel_velocity"]
    )


# ============================================================
# 4. LOAD REAL SCIENCE DATA
# ============================================================

pipeline = SciencePipeline()

image_a, header = pipeline.load(
    "data/wcs_test.fits"
)

image_b = image_a.copy()

image_b[250, 300] += 0.8
image_b[350, 200] += 0.6


# ============================================================
# 5. ARTIFACT ACTION
# ============================================================

executor = ActionExecutor(
    science_adapter=adapter,
    image_a=image_a,
    image_b=image_b,
    header=header
)

artifact_result = executor.artifact_evidence()


print()
print("ARTIFACT EVIDENCE")
print("-" * 60)

print(
    artifact_result["evidence"]
)


# ============================================================
# 6. HYPOTHESIS MANAGER
# ============================================================

manager = HypothesisManager()


print()
print("INITIAL HYPOTHESIS")
print("-" * 60)

for name, probability in manager.hypotheses.items():

    print(
        f"{name}: {probability:.2f}"
    )


# ============================================================
# 7. APPLY MOTION EVIDENCE
# ============================================================

for evidence in motion_evidence:

    manager.update(
        evidence
    )


# ============================================================
# 8. APPLY ARTIFACT EVIDENCE
# ============================================================

if artifact_result["success"]:

    manager.update(
        artifact_result["evidence"]
    )


# ============================================================
# 9. FINAL ASSESSMENT
# ============================================================

report = manager.report()


print()
print("FINAL HYPOTHESIS")
print("-" * 60)

for name, probability in report["hypotheses"].items():

    print(
        f"{name}: {probability:.2f}"
    )


print()
print("STRONGEST HYPOTHESIS:")
print(
    report["strongest"]
)

print()

print("CONFIDENCE:")
print(
    f"{report['confidence']:.2f}"
)


print()
print("=" * 60)
print("AUTONOMOUS EVIDENCE LOOP COMPLETE")
print("=" * 60)