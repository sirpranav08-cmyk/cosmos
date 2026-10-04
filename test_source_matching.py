from science_engine.source_matching import (
    SourceMatcher
)

from science_engine.motion_tracker import (
    MotionTracker
)


print()
print("=" * 60)
print("COSMOS SOURCE MATCHING + MOTION")
print("=" * 60)


# ----------------------------------------
# Epoch 1
# ----------------------------------------

sources_epoch_1 = [

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


# ----------------------------------------
# Epoch 2
# ----------------------------------------

sources_epoch_2 = [

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


print()
print("EPOCH 1")
print("-" * 60)

for source in sources_epoch_1:

    print(
        f"Source: "
        f"({source['x']}, {source['y']})"
    )


print()
print("EPOCH 2")
print("-" * 60)

for source in sources_epoch_2:

    print(
        f"Source: "
        f"({source['x']}, {source['y']})"
    )


# ----------------------------------------
# Matching
# ----------------------------------------

matcher = SourceMatcher(
    max_distance=10.0
)

matches = matcher.match(
    sources_epoch_1,
    sources_epoch_2
)


print()
print("SOURCE MATCHING")
print("-" * 60)

print(
    "Matches:",
    len(matches)
)


# ----------------------------------------
# Motion
# ----------------------------------------

tracker = MotionTracker()


print()
print("MOTION ANALYSIS")
print("-" * 60)


for index, match in enumerate(matches):

    source_a = match["source_a"]
    source_b = match["source_b"]

    motion = tracker.calculate(
        source_a,
        source_b
    )

    print()
    print(
        f"Candidate {index + 1}"
    )

    print(
        f"Epoch 1: "
        f"({source_a['x']}, {source_a['y']})"
    )

    print(
        f"Epoch 2: "
        f"({source_b['x']}, {source_b['y']})"
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
        "Motion detected:",
        motion["motion_detected"]
    )


print()
print("=" * 60)
print("SOURCE MATCHING + MOTION COMPLETE")
print("=" * 60)