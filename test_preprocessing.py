from science_engine.fits_reader import FITSReader
from science_engine.preprocessing import ImagePreprocessor


reader = FITSReader("data/sample.fits")

data, header = reader.read()


processor = ImagePreprocessor()

result = processor.process(data)

cleaned = result["cleaned"]
normalized = result["normalized"]


print("\nPREPROCESSING")
print("=" * 50)

print("Original shape:", data.shape)

print("Cleaned minimum:", cleaned.min())
print("Cleaned maximum:", cleaned.max())

print("Normalized minimum:", normalized.min())
print("Normalized maximum:", normalized.max())

print("NaN values:", normalized[~__import__("numpy").isfinite(normalized)].size)