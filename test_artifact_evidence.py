from astropy.io import fits

from agi.action_executor import ActionExecutor
from agi.science_adapter import ScienceEvidenceAdapter
from science_engine.pipeline import SciencePipeline


print()
print("=" * 60)
print("COSMOS ARTIFACT EVIDENCE")
print("=" * 60)


# ------------------------------------------------------------
# LOAD SCIENCE DATA
# ------------------------------------------------------------

pipeline = SciencePipeline()

image_a, header = pipeline.load(
    "data/wcs_test.fits"
)

image_b = image_a.copy()

# Artificial change
image_b[250, 300] += 0.8
image_b[350, 200] += 0.6


print()
print("SCIENCE DATA")
print("-" * 60)

print(
    "Image A:",
    image_a.shape
)

print(
    "Image B:",
    image_b.shape
)


# ------------------------------------------------------------
# CONNECT SCIENCE ADAPTER
# ------------------------------------------------------------

adapter = ScienceEvidenceAdapter()


executor = ActionExecutor(
    science_adapter=adapter,
    image_a=image_a,
    image_b=image_b,
    header=header
)


# ------------------------------------------------------------
# EXECUTE ARTIFACT CHECK
# ------------------------------------------------------------

result = executor.artifact_evidence()


print()
print("ARTIFACT EVIDENCE")
print("-" * 60)

print(
    "Success:",
    result["success"]
)

print(
    "Evidence:",
    result["evidence"]
)


print()
print("=" * 60)
print("ARTIFACT EVIDENCE COMPLETE")
print("=" * 60)