from science_engine.fits_reader import FITSReader


file_path = "data/sample.fits"

reader = FITSReader(file_path)

data, header = reader.read()

print("\nIMAGE DATA")
print("=" * 50)

print("Shape:", data.shape)
print("Minimum:", data.min())
print("Maximum:", data.max())
print("Mean:", data.mean())
print("NaN values:", data.size - data[~__import__("numpy").isnan(data)].size)