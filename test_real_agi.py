import numpy as np
from astropy.io import fits

from agi.science_adapter import (
    ScienceEvidenceAdapter
)

from agi.action_executor import (
    ActionExecutor
)


print()
print("=" * 60)
print("COSMOS REAL SCIENCE ↔ AGI TEST")
print("=" * 60)


# --------------------------------
# STEP 1
# Load real FITS image
# --------------------------------

print("\nSTEP 1: LOAD FITS")
print("-" * 60)

with fits.open(
    "data/wcs_test.fits"
) as hdul:

    image_a = np.asarray(
        hdul[0].data,
        dtype=np.float64
    )

    header = hdul[0].header.copy()


print(
    "Image shape:",
    image_a.shape
)


# --------------------------------
# STEP 2
# Create second observation
# --------------------------------

print("\nSTEP 2: CREATE SECOND OBSERVATION")
print("-" * 60)

# First observation is raw FITS data
raw_image = image_a.copy()

# Preprocess the first observation
from science_engine.preprocessing import ImagePreprocessor

processor = ImagePreprocessor()

processed = processor.process(raw_image)

image_a = processed["normalized"]

# Create second observation from the NORMALIZED image.
# This matches the way our standalone difference test works.
image_b = image_a.copy()

# Simulate new/changed astronomical sources
image_b[250, 300] += 0.8
image_b[350, 200] += 0.6


print(
    "Artificial changes inserted:"
)

print(
    "Source 1: (300, 250)"
)

print(
    "Source 2: (200, 350)"
)


# --------------------------------
# STEP 3
# Create adapter
# --------------------------------

print("\nSTEP 3: CONNECT SCIENCE ENGINE")
print("-" * 60)

adapter = ScienceEvidenceAdapter()

print(
    "Science adapter connected."
)


# --------------------------------
# STEP 4
# Analyze real images
# --------------------------------

print("\nSTEP 4: RUN REAL ANALYSIS")
print("-" * 60)

result = adapter.analyze_images(
    image_a,
    image_b,
    header,
    preprocessed=True
)


print(
    "Changed pixels:",
    result["change"]["changed_pixels"]
)

print(
    "Detected sources:",
    len(result["sources"])
)


# --------------------------------
# STEP 5
# Generate evidence
# --------------------------------

print("\nSTEP 5: GENERATE AGI EVIDENCE")
print("-" * 60)

evidence = adapter.create_evidence(
    result
)


for item in evidence:

    print(
        "Evidence:",
        item["type"]
    )


# --------------------------------
# STEP 6
# Artifact assessment
# --------------------------------

print("\nSTEP 6: ARTIFACT ASSESSMENT")
print("-" * 60)

artifact = adapter.artifact_assessment(
    result
)


print(
    "Artifact probability:",
    artifact["artifact_probability"]
)

print(
    "Status:",
    artifact["status"]
)


# --------------------------------
# STEP 7
# Action Executor
# --------------------------------

print("\nSTEP 7: AGI ACTION EXECUTOR")
print("-" * 60)

executor = ActionExecutor(
    science_adapter=adapter,
    image_a=image_a,
    image_b=image_b,
    header=header
)


action_result = executor.execute({
    "name": "check_artifacts"
})


print(
    "Action:",
    action_result["action"]
)

print(
    "Success:",
    action_result["success"]
)

print(
    "Result:",
    action_result["result"]
)


print()
print("=" * 60)
print("REAL SCIENCE ↔ AGI CONNECTION COMPLETE")
print("=" * 60)