import math


class MotionAnalyzer:

    def calculate_displacement(
        self,
        source_a,
        source_b
    ):

        dx = (
            source_b["x"]
            - source_a["x"]
        )

        dy = (
            source_b["y"]
            - source_a["y"]
        )

        distance = math.sqrt(
            dx ** 2 +
            dy ** 2
        )

        return {
            "dx": dx,
            "dy": dy,
            "pixel_distance": distance
        }

    def calculate_velocity(
        self,
        source_a,
        source_b,
        time_difference
    ):

        displacement = (
            self.calculate_displacement(
                source_a,
                source_b
            )
        )

        distance = displacement[
            "pixel_distance"
        ]

        if time_difference <= 0:

            raise ValueError(
                "Time difference must be positive."
            )

        velocity = (
            distance /
            time_difference
        )

        return {
            **displacement,
            "pixel_velocity": velocity
        }