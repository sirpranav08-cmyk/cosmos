from agi import HypothesisManager


print()
print("=" * 60)
print("COSMOS HYPOTHESIS MANAGER")
print("=" * 60)


manager = HypothesisManager()


print("\nINITIAL HYPOTHESES")
print("-" * 60)

for name, value in manager.hypotheses.items():

    print(
        f"{name}: {value:.2f}"
    )


print("\nEVIDENCE 1: MOTION")
print("-" * 60)

result = manager.update({
    "type": "motion",
    "value": 5.0
})

for name, value in result.items():

    print(
        f"{name}: {value:.2f}"
    )


print("\nEVIDENCE 2: SPECTRUM")
print("-" * 60)

result = manager.update({
    "type": "spectrum",
    "bands": 3
})

for name, value in result.items():

    print(
        f"{name}: {value:.2f}"
    )


print("\nEVIDENCE 3: ARTIFACT CHECK")
print("-" * 60)

result = manager.update({
    "type": "artifact_check",
    "artifact_probability": 0.10
})

for name, value in result.items():

    print(
        f"{name}: {value:.2f}"
    )


print("\nCURRENT ASSESSMENT")
print("-" * 60)

report = manager.report()

print(
    "Strongest hypothesis:",
    report["strongest"]
)

print(
    "Confidence:",
    f"{report['confidence']:.2f}"
)