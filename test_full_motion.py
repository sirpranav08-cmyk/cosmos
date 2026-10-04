from science_engine.investigation_engine import InvestigationEngine


print()
print("=" * 60)
print("COSMOS FULL MOTION INVESTIGATION")
print("=" * 60)


# ============================================================
# EPOCH 1
# ============================================================

sources_epoch_a = [

    {
        "source_id": 1,
        "x": 300.0,
        "y": 250.0
    },

    {
        "source_id": 2,
        "x": 200.0,
        "y": 350.0
    }
]


# ============================================================
# EPOCH 2
# ============================================================

sources_epoch_b = [

    {
        "source_id": 1,
        "x": 304.0,
        "y": 253.0
    },

    {
        "source_id": 2,
        "x": 200.0,
        "y": 350.0
    }
]


# ============================================================
# INVESTIGATION ENGINE
# ============================================================

engine = InvestigationEngine(
    max_match_distance=10.0
)


results = engine.investigate(
    sources_epoch_a,
    sources_epoch_b,
    time_delta=10.0
)


# ============================================================
# RESULTS
# ============================================================

print()
print("INVESTIGATION RESULTS")
print("-" * 60)


for result in results:

    motion = result["motion"]

    print()
    print(
        "Candidate:",
        result["candidate_id"]
    )

    print(
        "Epoch A:",
        result["epoch_a"]
    )

    print(
        "Epoch B:",
        result["epoch_b"]
    )

    print(
        "Match distance:",
        result["match_distance"]
    )

    print(
        "Delta X:",
        motion["delta_x"]
    )

    print(
        "Delta Y:",
        motion["delta_y"]
    )

    print(
        "Pixel displacement:",
        motion["pixel_displacement"]
    )

    print(
        "Pixel velocity:",
        motion["pixel_velocity"]
    )

    print(
        "Motion detected:",
        motion["motion_detected"]
    )


print()
print("=" * 60)
print("FULL MOTION INVESTIGATION COMPLETE")
print("=" * 60)