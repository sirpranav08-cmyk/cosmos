from science_engine.investigation_engine import (
    InvestigationEngine
)


print()
print("=" * 60)
print("COSMOS INVESTIGATION ENGINE")
print("=" * 60)


epoch_a = [

    {
        "x": 300.0,
        "y": 250.0,
        "signal": 0.8
    },

    {
        "x": 200.0,
        "y": 350.0,
        "signal": 0.6
    }
]


epoch_b = [

    {
        "x": 304.0,
        "y": 253.0,
        "signal": 0.82
    },

    {
        "x": 200.0,
        "y": 350.0,
        "signal": 0.61
    }
]


engine = InvestigationEngine()

results = engine.investigate(
    epoch_a,
    epoch_b,
    time_delta=10.0
)


for result in results:

    print()
    print(
        f"Candidate {result['candidate_id']}"
    )

    print(
        "Match distance:",
        result["match_distance"]
    )

    motion = result["motion"]

    print(
        "Delta X:",
        motion["delta_x"]
    )

    print(
        "Delta Y:",
        motion["delta_y"]
    )

    print(
        "Displacement:",
        motion["pixel_displacement"]
    )

    print(
        "Velocity:",
        motion["pixel_velocity"]
    )

    print(
        "Motion detected:",
        motion["motion_detected"]
    )


print()
print("=" * 60)
print("INVESTIGATION COMPLETE")
print("=" * 60)