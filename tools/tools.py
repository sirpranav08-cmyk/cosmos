import math


class ScientificTools:

    def calculate_motion(
        self,
        observation_a,
        observation_b
    ):

        delta_ra = observation_b.ra - observation_a.ra
        delta_dec = observation_b.dec - observation_a.dec

        distance = math.sqrt(
            delta_ra ** 2 +
            delta_dec ** 2
        )

        return {
            "delta_ra": delta_ra,
            "delta_dec": delta_dec,
            "angular_distance": distance
        }

    def compare_brightness(
        self,
        observation_a,
        observation_b
    ):

        if (
            observation_a.brightness is None
            or observation_b.brightness is None
        ):
            return None

        return (
            observation_b.brightness
            - observation_a.brightness
        )

    def analyze_spectrum(self, observation):

        if not observation.spectral_data:
            return {
                "available": False
            }

        values = list(
            observation.spectral_data.values()
        )

        return {
            "available": True,
            "bands": len(values),
            "minimum": min(values),
            "maximum": max(values),
            "average": sum(values) / len(values)
        }