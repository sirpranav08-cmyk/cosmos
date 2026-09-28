class Verifier:

    def verify(self, hypotheses, evidence):

        results = []

        for hypothesis in hypotheses:

            support = sum(
                e.value
                for e in hypothesis.supporting_evidence
            )

            contradiction = sum(
                e.value
                for e in hypothesis.contradicting_evidence
            )

            score = (
                hypothesis.confidence
                + support
                - contradiction
            )

            score = max(
                0.0,
                min(1.0, score)
            )

            results.append({
                "hypothesis": hypothesis.name,
                "confidence": score,
                "verified": score >= 0.70
            })

        return results