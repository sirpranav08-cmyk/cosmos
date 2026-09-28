import numpy as np

from science_engine.fits_reader import FITSReader
from science_engine.preprocessing import ImagePreprocessor
from science_engine.difference import DifferenceEngine


print("\nSTEP 1: READING FITS")

reader = FITSReader(
    "data/sample.fits"
)

data, header = reader.read()


print("\nSTEP 2: PREPROCESSING")

processor = ImagePreprocessor()

result = processor.process(data)

image_a = result["normalized"]


print("\nSTEP 3: CREATING SECOND OBSERVATION")

# Copy the first observation
image_b = image_a.copy()

# Simulate a new astronomical source
image_b[250, 300] += 0.8

# Simulate another changed source
image_b[350, 200] += 0.6

print("Second observation created")


print("\nSTEP 4: DIFFERENCE IMAGING")

engine = DifferenceEngine()

result = engine.calculate(
    image_a,
    image_b
)

difference = result["difference"]

print("Difference image calculated")


print("\nSTEP 5: CHANGE DETECTION")

changes = engine.detect_changes(
    difference,
    threshold=0.1
)


print("\nDIFFERENCE ANALYSIS")
print("=" * 50)

print(
    "Changed pixels:",
    changes["changed_pixels"]
)

print(
    "Total pixels:",
    changes["total_pixels"]
)

print(
    "Change fraction:",
    changes["change_fraction"]
)

print(
    "Maximum change:",
    np.max(
        np.abs(difference)
    )
)

print(
    "Mean change:",
    np.mean(
        np.abs(difference)
    )
)


if changes["changed_pixels"] > 0:

    print(
        "\nCHANGE DETECTED!"
    )

else:

    print(
        "\nNo significant change detected."
    )