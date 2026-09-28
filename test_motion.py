from science_engine.motion import MotionAnalyzer


print("\nMOTION ANALYSIS")
print("=" * 50)


# Observation 1
source_a = {
    "source_id": 1,
    "x": 300.0,
    "y": 250.0
}


# Observation 2
source_b = {
    "source_id": 1,
    "x": 304.0,
    "y": 253.0
}


analyzer = MotionAnalyzer()


result = analyzer.calculate_displacement(
    source_a,
    source_b
)


print(
    "Observation A:",
    source_a
)

print(
    "Observation B:",
    source_b
)

print(
    "\nDelta X:",
    result["dx"]
)

print(
    "Delta Y:",
    result["dy"]
)

print(
    "Pixel displacement:",
    result["pixel_distance"]
)


# Assume 10 units of time between observations
velocity = analyzer.calculate_velocity(
    source_a,
    source_b,
    time_difference=10
)


print(
    "Pixel velocity:",
    velocity["pixel_velocity"]
)


print(
    "\nMotion detected:",
    result["pixel_distance"] > 0
)