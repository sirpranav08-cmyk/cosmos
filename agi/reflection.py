class ReflectionEngine:

    def reflect(self, investigation):

        evidence = investigation.evidence
        observations = investigation.observations

        reflection = {
            "reasoning": [],
            "missing_evidence": [],
            "recommended_actions": [],
            "status": "UNCERTAIN"
        }

        # --------------------------------
        # Check observation count
        # --------------------------------

        if len(observations) < 3:

            reflection["reasoning"].append(
                "Only a small number of observations "
                "are available."
            )

            reflection["missing_evidence"].append(
                "Additional observation epoch"
            )

            reflection["recommended_actions"].append(
                "request_additional_epoch"
            )

        else:

            reflection["reasoning"].append(
                "Multiple observation epochs are available."
            )

        # --------------------------------
        # Check motion evidence
        # --------------------------------

        has_motion = any(
            e.get("type") == "motion"
            for e in evidence
            if isinstance(e, dict)
        )

        if has_motion:

            reflection["reasoning"].append(
                "Positional motion has been detected."
            )

        else:

            reflection["missing_evidence"].append(
                "Motion measurement"
            )

            reflection["recommended_actions"].append(
                "calculate_motion"
            )

        # --------------------------------
        # Check spectral evidence
        # --------------------------------

        has_spectrum = any(
            e.get("type") == "spectrum"
            for e in evidence
            if isinstance(e, dict)
        )

        if has_spectrum:

            reflection["reasoning"].append(
                "Spectral evidence is available."
            )

        else:

            reflection["missing_evidence"].append(
                "Spectral analysis"
            )

            reflection["recommended_actions"].append(
                "analyze_spectrum"
            )

        # --------------------------------
        # Check artifact analysis
        # --------------------------------

        has_artifact_check = any(
            e.get("type") == "artifact_check"
            for e in evidence
            if isinstance(e, dict)
        )

        if not has_artifact_check:

            reflection["missing_evidence"].append(
                "Imaging artifact verification"
            )

            reflection["recommended_actions"].append(
                "check_artifacts"
            )

        else:

            reflection["reasoning"].append(
                "Artifact verification has been performed."
            )

        # --------------------------------
        # Determine status
        # --------------------------------

        if not reflection["missing_evidence"]:

            reflection["status"] = "READY_FOR_VERIFICATION"

        else:

            reflection["status"] = "MORE_EVIDENCE_REQUIRED"

        investigation.reflect(
            reflection
        )

        return reflection