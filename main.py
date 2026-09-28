from core.brain import CosmosBrain


data = [

    {
        "id": "candidate_1042",
        "timestamp": "2026-05-01",
        "ra": 182.3410,
        "dec": -12.5520,
        "brightness": 14.8,
        "spectrum": {
            "band_1": 0.42,
            "band_2": 0.51,
            "band_3": 0.63
        }
    },

    {
        "id": "candidate_1042",
        "timestamp": "2026-05-15",
        "ra": 182.3420,
        "dec": -12.5510,
        "brightness": 14.9,
        "spectrum": {
            "band_1": 0.44,
            "band_2": 0.53,
            "band_3": 0.61
        }
    }
]


brain = CosmosBrain()


report = brain.investigate(
    "Find unusual moving objects",
    data
)


print("\n")
print("=" * 60)
print(report)
print("=" * 60)