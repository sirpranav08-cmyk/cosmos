import math


class MotionTracker:

    def calculate(
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

        displacement = math.sqrt(
            dx * dx + dy * dy
        )

        return {

            "delta_x": dx,

            "delta_y": dy,

            "pixel_displacement":
                displacement,

            "motion_detected":
                displacement > 0
        }

    def calculate_velocity(
        self,
        motion,
        time_delta
    ):

        if time_delta <= 0:

            raise ValueError(
                "time_delta must be greater than zero"
            )

        velocity = (
            motion["pixel_displacement"]
            / time_delta
        )

        return {

            **motion,

            "time_delta":
                time_delta,

            "pixel_velocity":
                velocity
        }