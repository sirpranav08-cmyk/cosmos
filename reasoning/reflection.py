class ReflectionEngine:

    def reflect(self, state):

        state.reflection_count += 1

        reflections = []

        if not state.evidence:

            reflections.append(
                "No evidence has been collected."
            )

            state.status = "NEEDS_EVIDENCE"

            return reflections

        for hypothesis in state.hypotheses:

            confidence = hypothesis.confidence

            if confidence >= 0.70:

                reflections.append(
                    f"{hypothesis.name} has "
                    f"strong supporting evidence."
                )

            elif confidence >= 0.40:

                reflections.append(
                    f"{hypothesis.name} remains "
                    f"plausible but requires more evidence."
                )

            else:

                reflections.append(
                    f"{hypothesis.name} currently "
                    f"has weak support."
                )

        strongest = max(
            state.hypotheses,
            key=lambda h: h.confidence
        )

        if strongest.confidence >= 0.70:

            state.status = "SUPPORTED"

        else:

            state.status = "UNCERTAIN"

        return reflections