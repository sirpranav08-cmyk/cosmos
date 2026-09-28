from science_engine.pipeline import SciencePipeline


print("\n")
print("=" * 60)
print("COSMOS SCIENCE PIPELINE")
print("=" * 60)


pipeline = SciencePipeline()


print("\nSTEP 1: LOAD")

image_a, header = pipeline.load(
    "data/wcs_test.fits"
)

image_b, _ = pipeline.load(
    "data/wcs_test.fits"
)


print("\nSTEP 2: PREPROCESS")

image_a = pipeline.preprocess(
    image_a
)

image_b = pipeline.preprocess(
    image_b
)


print("\nSTEP 3: CREATE TEST CHANGE")

# Simulate a changed astronomical source
image_b[250, 300] += 0.8

image_b[350, 200] += 0.6


print("\nSTEP 4: RUN SCIENCE PIPELINE")

result = pipeline.compare(
    image_a,
    image_b,
    header
)


print("\nALIGNMENT")
print("-" * 40)

print(
    result["alignment"]
)


print("\nCHANGE ANALYSIS")
print("-" * 40)

print(
    "Changed pixels:",
    result["change"]["changed_pixels"]
)

print(
    "Change fraction:",
    result["change"]["change_fraction"]
)


print("\nCANDIDATES")
print("-" * 40)

for candidate in result["sources"]:

    print(
        f"Candidate {candidate['source_id']}"
    )

    print(
        f"Pixel: "
        f"({candidate['x']:.2f}, "
        f"{candidate['y']:.2f})"
    )

    print(
        f"RA: {candidate['ra']:.8f}"
    )

    print(
        f"Dec: {candidate['dec']:.8f}"
    )

    print(
        f"Signal: "
        f"{candidate['peak_signal']:.4f}"
    )


print("\n")
print("=" * 60)
print("SCIENCE PIPELINE COMPLETE")
print("=" * 60)