from science_engine.investigation_engine import (
    InvestigationEngine
)

from science_engine.catalog import (
    CatalogMatcher
)


class ActionExecutor:

    def __init__(
        self,
        science_adapter=None,
        image_a=None,
        image_b=None,
        header=None,
        time_delta=1.0,
        catalog_matcher=None
    ):

        self.science_adapter = science_adapter

        self.image_a = image_a
        self.image_b = image_b
        self.header = header

        self.time_delta = time_delta

        self.investigation_engine = (
            InvestigationEngine()
        )

        self.catalog_matcher = (
            catalog_matcher
            if catalog_matcher is not None
            else CatalogMatcher()
        )

    # ========================================================
    # MAIN ACTION DISPATCHER
    # ========================================================

    def execute(
        self,
        action,
        candidate=None,
        catalog=None
    ):

        action_name = action["name"]

        if action_name == "check_artifacts":

            return self.check_artifacts()

        if action_name == "calculate_motion":

            return self.calculate_motion()

        if action_name == "analyze_spectrum":

            return self.analyze_spectrum()

        if action_name == "request_additional_epoch":

            return self.request_additional_epoch()

        if action_name == "cross_match_catalog":

            return self.cross_match_catalog(
                candidate=candidate,
                catalog=catalog
            )

        return {
            "success": False,
            "action": action_name,
            "message": "Unknown action"
        }

    # ========================================================
    # ARTIFACT CHECK
    # ========================================================

    def check_artifacts(self):

        if (
            self.science_adapter is None
            or self.image_a is None
            or self.image_b is None
        ):

            return {
                "success": False,
                "action": "check_artifacts",
                "message":
                    "Science data not connected."
            }

        result = (
            self.science_adapter.analyze_images(
                self.image_a,
                self.image_b,
                self.header
            )
        )

        assessment = (
            self.science_adapter.artifact_assessment(
                result
            )
        )

        return {
            "success": True,
            "action": "check_artifacts",
            "result": assessment,
            "science_result": result
        }

    # ========================================================
    # ARTIFACT EVIDENCE
    # ========================================================

    def artifact_evidence(self):

        result = self.check_artifacts()

        if not result["success"]:

            return {
                "success": False,
                "evidence": None,
                "message":
                    result["message"]
            }

        assessment = result["result"]

        evidence = {

            "type":
                "artifact_check",

            "artifact_probability":
                assessment[
                    "artifact_probability"
                ],

            "change_fraction":
                assessment[
                    "change_fraction"
                ],

            "status":
                assessment[
                    "status"
                ],

            "source":
                "artifact_analysis"
        }

        return {
            "success": True,
            "evidence": evidence
        }

    # ========================================================
    # REAL MOTION ANALYSIS
    # ========================================================

    def calculate_motion(self):

        if (
            self.science_adapter is None
            or self.image_a is None
            or self.image_b is None
        ):

            return {
                "success": False,
                "action":
                    "calculate_motion",
                "message":
                    "Science data not connected."
            }

        # ----------------------------------------------------
        # Run science pipeline
        # ----------------------------------------------------

        result = (
            self.science_adapter.analyze_images(
                self.image_a,
                self.image_b,
                self.header
            )
        )

        # ----------------------------------------------------
        # Get source epochs
        # ----------------------------------------------------

        sources_a = result.get(
            "sources_epoch_a",
            []
        )

        sources_b = result.get(
            "sources_epoch_b",
            []
        )

        # Compatibility fallbacks

        if not sources_a:

            sources_a = result.get(
                "sources_a",
                []
            )

        if not sources_b:

            sources_b = result.get(
                "sources_b",
                []
            )

        # ----------------------------------------------------
        # Need two source epochs
        # ----------------------------------------------------

        if not sources_a or not sources_b:

            return {
                "success": False,
                "action":
                    "calculate_motion",
                "message":
                    "Two source epochs are required.",
                "science_result":
                    result
            }

        # ----------------------------------------------------
        # Investigation engine
        # ----------------------------------------------------

        investigations = (
            self.investigation_engine.investigate(
                sources_a,
                sources_b,
                self.time_delta
            )
        )

        motion_candidates = []

        for investigation in investigations:

            motion = investigation["motion"]

            displacement = (
                motion["pixel_displacement"]
            )

            velocity = (
                motion["pixel_velocity"]
            )

            motion_detected = (
                displacement > 0
            )

            motion_candidates.append({

                "candidate_id":
                    investigation[
                        "candidate_id"
                    ],

                "epoch_a":
                    investigation[
                        "epoch_a"
                    ],

                "epoch_b":
                    investigation[
                        "epoch_b"
                    ],

                "match_distance":
                    investigation[
                        "match_distance"
                    ],

                "delta_x":
                    motion[
                        "delta_x"
                    ],

                "delta_y":
                    motion[
                        "delta_y"
                    ],

                "pixel_displacement":
                    displacement,

                "pixel_velocity":
                    velocity,

                "motion_detected":
                    motion_detected
            })

        any_motion = any(
            candidate[
                "motion_detected"
            ]
            for candidate in motion_candidates
        )

        return {

            "success": True,

            "action":
                "calculate_motion",

            "result": {

                "motion_detected":
                    any_motion,

                "candidates":
                    motion_candidates
            },

            "science_result":
                result
        }

    # ========================================================
    # SPECTRUM
    # ========================================================

    def analyze_spectrum(self):

        return {

            "success": False,

            "action":
                "analyze_spectrum",

            "message":
                "Spectral engine not connected yet."
        }

    # ========================================================
    # ADDITIONAL EPOCH
    # ========================================================

    def request_additional_epoch(self):

        return {

            "success": True,

            "action":
                "request_additional_epoch",

            "result": {

                "status":
                    "REQUESTED"
            }
        }

    # ========================================================
    # CATALOG CROSS-MATCH
    # ========================================================

    # ========================================================
# CATALOG CROSS-MATCH
# ========================================================

    def cross_match_catalog(
    self,
    candidate=None,
    catalog=None
    ):

        if candidate is None:
            return {
            "success": False,
            "action": "cross_match_catalog",
            "matched": False,
            "matches": [],
            "result": {
                "matched": False,
                "matches": []
            },
            "message": "Candidate data not provided."
            }

        if catalog is None:
            return {
            "success": False,
            "action": "cross_match_catalog",
            "matched": False,
            "matches": [],
            "result": {
                "matched": False,
                "matches": []
            },
            "message": "Catalog data not provided."
            }

        # Import here to avoid unnecessary circular imports
        from science_engine.catalog import CatalogMatcher

        try:

            matcher = CatalogMatcher(
            max_distance_arcsec=5.0
            )

            matches = matcher.match(
            candidate,
            catalog
            )

            matched = len(matches) > 0

        # Best match
            best_match = (
            matches[0]
            if matched
            else None
            )

            return {

            "success": True,

            "action":
                "cross_match_catalog",

            # Top-level fields expected by tests
            "matched":
                matched,

            "matches":
                matches,

            # Keep a standard nested result too
            "result": {

                "matched":
                    matched,

                "matches":
                    matches,

                "best_match":
                    best_match
                }
            }

        except Exception as exc:

            return {

            "success": False,

            "action":
                "cross_match_catalog",

            "matched":
                False,

            "matches":
                [],

            "result": {

                "matched":
                    False,

                "matches":
                    []
            },

            "message":
                str(exc)
            }