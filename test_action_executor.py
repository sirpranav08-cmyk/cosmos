from agi import ActionPlanner
from agi import ActionExecutor
from agi import Investigation
from agi import ReflectionEngine

from agi.science_adapter import ScienceEvidenceAdapter
from astropy.io import fits


print()
print("=" * 60)
print("COSMOS ACTION EXECUTOR")
print("=" * 60)


# ============================================================
# CREATE INVESTIGATION
# ============================================================

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


# ============================================================
# REFLECTION
# ============================================================

reflection_engine = ReflectionEngine()

reflection = reflection_engine.reflect(
    investigation
)


# ============================================================
# ACTION PLANNING
# ============================================================

planner = ActionPlanner()

actions = planner.plan(
    reflection
)


# ============================================================
# LOAD REAL FITS DATA
# ============================================================

print()
print("LOADING SCIENCE DATA")
print("-" * 60)

with fits.open(
    "data/wcs_test.fits"
) as hdul:

    image_a = hdul[0].data.copy()
    header = hdul[0].header.copy()


# Create second observation

image_b = image_a.copy()

image_b[250, 300] += 0.8
image_b[350, 200] += 0.6


print(
    "Image A shape:",
    image_a.shape
)

print(
    "Image B shape:",
    image_b.shape
)


# ============================================================
# CONNECT SCIENCE ADAPTER
# ============================================================

science_adapter = ScienceEvidenceAdapter()


executor = ActionExecutor(
    science_adapter=science_adapter,
    image_a=image_a,
    image_b=image_b,
    header=header
)


# ============================================================
# EXECUTE
# ============================================================

print()
print("EXECUTING ACTIONS")
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
        result.get("success")
    )

    print(
        "RESULT:",
        result.get(
            "result",
            result.get(
                "message",
                "No result"
            )
        )
    )


print()
print("=" * 60)
print("ACTION EXECUTOR TEST COMPLETE")
print("=" * 60)