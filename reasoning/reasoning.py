from core.state import Evidence, Hypothesis


class ReasoningEngine:

    def create_hypotheses(self):

        return [

            Hypothesis(
                name="Moving astronomical object",
                prior=0.30
            ),

            Hypothesis(
                name="Stationary astronomical source",
                prior=0.30
            ),

            Hypothesis(
                name="Measurement or imaging artifact",
                prior=0.20
            ),

            Hypothesis(
                name="Transient astronomical event",
                prior=0.20
            )
        ]

    def analyze_motion(
        self,
        motion_result
    ):

        if not motion_result:
            return None

        distance = motion_result[
            "angular_distance"
        ]

        if distance <= 0:

            return Evidence(
                description="No measurable positional change",
                value=0.20,
                source="motion_analysis",
                supports="Stationary astronomical source",
                reliability=0.95
            )

        if distance > 0:

            return Evidence(
                description=(
                    f"Positional change detected: "
                    f"{distance:.6f} degrees"
                ),
                value=0.35,
                source="motion_analysis",
                supports="Moving astronomical object",
                reliability=0.95
            )

    def analyze_spectrum(
        self,
        spectral_result
    ):

        if not spectral_result:
            return None

        if not spectral_result.get("available"):
            return None

        bands = spectral_result["bands"]

        if bands >= 3:

            return Evidence(
                description=(
                    f"Multi-band spectral detection "
                    f"across {bands} bands"
                ),
                value=0.15,
                source="spectral_analysis",
                supports="Moving astronomical object",
                reliability=0.85
            )

        return None

    def analyze_catalog(
        self,
        catalog_match
    ):

        if catalog_match is False:

            return Evidence(
                description="No known catalog match found",
                value=0.10,
                source="catalog_search",
                supports="Moving astronomical object",
                reliability=0.70
            )

        return Evidence(
            description="Known catalog object detected",
            value=0.20,
            source="catalog_search",
            supports="Stationary astronomical source",
            reliability=0.95
        )