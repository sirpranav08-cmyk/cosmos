import numpy as np

from science_engine.fits_reader import FITSReader
from science_engine.preprocessing import ImagePreprocessor
from science_engine.alignment import ImageAligner


print("\nSTEP 1: READING FITS")

reader = FITSReader("data/sample.fits")

data, header = reader.read()

print("FITS loaded successfully")


print("\nSTEP 2: PREPROCESSING")

processor = ImagePreprocessor()

result = processor.process(data)

image = result["normalized"]

print("Preprocessing complete")
print("Image shape:", image.shape)


print("\nSTEP 3: CREATING TEST SHIFT")

target = np.roll(
    image,
    shift=(5, 8),
    axis=(0, 1)
)

print("Test image created")


print("\nSTEP 4: ALIGNMENT")

aligner = ImageAligner()

alignment = aligner.estimate_shift(
    image,
    target
)

print("Alignment calculation complete")


print("\nIMAGE ALIGNMENT")
print("=" * 50)

print(
    "Detected X shift:",
    alignment["shift_x"]
)

print(
    "Detected Y shift:",
    alignment["shift_y"]
)

print(
    "Correlation peak:",
    alignment["correlation_peak"]
)


print("\nSTEP 5: APPLYING ALIGNMENT")

aligned = aligner.align(
    target,
    alignment["shift_x"],
    alignment["shift_y"]
)

print("Alignment applied")


print("\nSTEP 6: COMPARING IMAGES")

difference_before = np.mean(
    np.abs(image - target)
)

difference_after = np.mean(
    np.abs(image - aligned)
)


print("\nRESULT")
print("=" * 50)

print(
    "Difference before alignment:",
    difference_before
)

print(
    "Difference after alignment:",
    difference_after
)

if difference_after < difference_before:

    print("\nSUCCESS: Alignment improved the image match.")

else:

    print("\nWARNING: Alignment did not improve the image match.")