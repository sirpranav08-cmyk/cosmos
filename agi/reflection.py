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

        # ====================================================
        # CHECK OBSERVATION COUNT
        # ====================================================

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

        # ====================================================
        # CHECK MOTION EVIDENCE
        # ====================================================

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

        # ====================================================
        # CHECK SPECTRAL EVIDENCE
        # ====================================================

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

        # ====================================================
        # CHECK ARTIFACT EVIDENCE
        # ====================================================

        has_artifact_check = any(
            e.get("type") == "artifact_check"
            for e in evidence
            if isinstance(e, dict)
        )

        if has_artifact_check:

            reflection["reasoning"].append(
                "Artifact verification has been performed."
            )

        else:

            reflection["missing_evidence"].append(
                "Imaging artifact verification"
            )

            reflection["recommended_actions"].append(
                "check_artifacts"
            )

        # ====================================================
        # CHECK CATALOG EVIDENCE
        # ====================================================

        has_catalog_match = any(
            e.get("type") == "catalog_match"
            for e in evidence
            if isinstance(e, dict)
        )

        if has_catalog_match:

            reflection["reasoning"].append(
                "Astronomical catalog cross-match "
                "has been performed."
            )

        else:

            reflection["missing_evidence"].append(
                "Astronomical catalog cross-match"
            )

            reflection["recommended_actions"].append(
                "cross_match_catalog"
            )

        # ====================================================
        # DETERMINE STATUS
        # ====================================================

        if not reflection["missing_evidence"]:

            reflection["status"] = (
                "READY_FOR_VERIFICATION"
            )

        else:

            reflection["status"] = (
                "MORE_EVIDENCE_REQUIRED"
            )

        # ====================================================
        # STORE REFLECTION
        # ====================================================

        investigation.reflect(
            reflection
        )

        return reflection