class Reporter:

    def generate(
        self,
        candidate_id,
        hypotheses,
        verification
    ):

        report = []

        report.append(
            f"COSMOS Investigation: {candidate_id}"
        )

        report.append(
            "\nHypotheses:"
        )

        for h in hypotheses:

            report.append(
                f"- {h.name}: "
                f"{h.confidence:.2f}"
            )

        report.append(
            "\nVerification:"
        )

        for result in verification:

            status = (
                "SUPPORTED"
                if result["verified"]
                else "UNCONFIRMED"
            )

            report.append(
                f"- {result['hypothesis']}: "
                f"{result['confidence']:.2f} "
                f"({status})"
            )

        report.append(
            "\nCOSMOS does not classify this "
            "as a confirmed astronomical discovery "
            "without sufficient scientific evidence."
        )

        return "\n".join(report)