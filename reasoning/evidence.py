class EvidenceEngine:

    def add(
        self,
        state,
        evidence
    ):

        if evidence is None:
            return

        state.evidence.append(evidence)

        for hypothesis in state.hypotheses:

            if hypothesis.name == evidence.supports:

                hypothesis.supporting_evidence.append(
                    evidence
                )

    def find_contradictions(
        self,
        state
    ):

        contradictions = []

        for hypothesis in state.hypotheses:

            if (
                hypothesis.supporting_evidence
                and hypothesis.contradicting_evidence
            ):

                contradictions.append(
                    hypothesis.name
                )

        return contradictions