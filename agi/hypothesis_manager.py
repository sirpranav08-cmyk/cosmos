class HypothesisManager:

    def __init__(self):

        self.hypotheses = {
            "Moving astronomical object": 0.50,
            "Stationary astronomical source": 0.20,
            "Measurement or imaging artifact": 0.20,
            "Transient astronomical event": 0.10
        }

    def update(self, evidence):

        evidence_type = evidence.get("type")

        if evidence_type == "motion":

            self.hypotheses[
                "Moving astronomical object"
            ] += 0.25

            self.hypotheses[
                "Stationary astronomical source"
            ] -= 0.10

        elif evidence_type == "artifact_check":

            probability = evidence.get(
                "artifact_probability",
                0.5
            )

            if probability < 0.2:

                self.hypotheses[
                    "Measurement or imaging artifact"
                ] -= 0.15

                self.hypotheses[
                    "Moving astronomical object"
                ] += 0.10

            elif probability > 0.7:

                self.hypotheses[
                    "Measurement or imaging artifact"
                ] += 0.20

        elif evidence_type == "spectrum":

            self.hypotheses[
                "Moving astronomical object"
            ] += 0.10

        self._normalize()

        return self.hypotheses

    def _normalize(self):

        # Prevent negative probabilities
        for name in self.hypotheses:

            self.hypotheses[name] = max(
                0.0,
                self.hypotheses[name]
            )

        total = sum(
            self.hypotheses.values()
        )

        if total == 0:
            return

        for name in self.hypotheses:

            self.hypotheses[name] /= total

    def strongest(self):

        return max(
            self.hypotheses,
            key=self.hypotheses.get
        )

    def confidence(self):

        strongest = self.strongest()

        return self.hypotheses[
            strongest
        ]

    def report(self):

        return {
            "hypotheses": self.hypotheses.copy(),
            "strongest": self.strongest(),
            "confidence": self.confidence()
        }