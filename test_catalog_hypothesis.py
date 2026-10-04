from agi import HypothesisManager


print()
print("=" * 60)
print("COSMOS CATALOG → HYPOTHESIS")
print("=" * 60)


manager = HypothesisManager()


print("\nINITIAL HYPOTHESES")
print("-" * 60)

for name, probability in manager.hypotheses.items():

    print(
        f"{name}: "
        f"{probability:.2f}"
    )


catalog_evidence = {

    "type":
        "catalog_match",

    "matched":
        True,

    "catalog_id":
        "STAR-001",

    "name":
        "Known Star A",

    "distance_arcsec":
        0.0
}


print("\nCATALOG EVIDENCE")
print("-" * 60)

print(
    "Matched:",
    catalog_evidence["matched"]
)

print(
    "Catalog ID:",
    catalog_evidence["catalog_id"]
)

print(
    "Name:",
    catalog_evidence["name"]
)

print(
    "Distance:",
    catalog_evidence["distance_arcsec"],
    "arcsec"
)


manager.update(
    catalog_evidence
)


print("\nUPDATED HYPOTHESES")
print("-" * 60)

for name, probability in manager.hypotheses.items():

    print(
        f"{name}: "
        f"{probability:.2f}"
    )


print("\nCURRENT ASSESSMENT")
print("-" * 60)

print(
    "Strongest hypothesis:",
    manager.strongest()
)

print(
    "Confidence:",
    f"{manager.confidence():.2f}"
)


print()
print("=" * 60)
print("CATALOG → HYPOTHESIS COMPLETE")
print("=" * 60)