from science_engine.fits_reader import FITSReader
from science_engine.preprocessing import ImagePreprocessor
from science_engine.difference import DifferenceEngine
from science_engine.source_detection import SourceDetector


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

image_b = image_a.copy()

# Simulated astronomical changes
image_b[250, 300] += 0.8
image_b[350, 200] += 0.6

print("Second observation created")


print("\nSTEP 4: DIFFERENCE IMAGING")

difference_engine = DifferenceEngine()

result = difference_engine.calculate(
    image_a,
    image_b
)

difference = result["difference"]


print("\nSTEP 5: SOURCE DETECTION")

detector = SourceDetector()

sources = detector.detect(
    difference,
    threshold=0.1
)


print("\nCANDIDATE SOURCES")
print("=" * 50)

print(
    "Number of candidates:",
    len(sources)
)


for source in sources:

    print(
        f"\nCandidate {source['source_id']}"
    )

    print(
        "X:",
        source["x"]
    )

    print(
        "Y:",
        source["y"]
    )

    print(
        "Peak signal:",
        source["peak_signal"]
    )

    print(
        "Total signal:",
        source["total_signal"]
    )

    print(
        "Pixels:",
        source["pixel_count"]
    )