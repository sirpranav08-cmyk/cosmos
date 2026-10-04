import numpy as np
from reasoning import evidence
from science_engine.catalog import CatalogMatcher
from science_engine.investigation_engine import InvestigationEngine
from science_engine.pipeline import SciencePipeline


class ScienceEvidenceAdapter:

    def __init__(self):

        self.pipeline = SciencePipeline()

        self.investigation_engine = (
            InvestigationEngine(
                max_match_distance=10.0
            )
        )
    def analyze_images(
        self,
        image_a,
        image_b,
        header,
        preprocessed=False
    ):

        image_a = np.asarray(
            image_a,
            dtype=np.float64
        )

        image_b = np.asarray(
            image_b,
            dtype=np.float64
        )

        if preprocessed:

            processed_a = image_a
            processed_b = image_b

        else:

            processed_a = self.pipeline.preprocess(
                image_a
            )

            processed_b = self.pipeline.preprocess(
                image_b
            )

        result = self.pipeline.compare(
            processed_a,
            processed_b,
            header
        )

        return result

    def create_evidence(
        self,
        result
    ):

        evidence = []

        # ----------------------------------------
        # Change detection
        # ----------------------------------------

        change = result["change"]

        if change["changed_pixels"] > 0:

            evidence.append({

                "type":
                    "change_detection",

                "changed_pixels":
                    change["changed_pixels"],

                "change_fraction":
                    change["change_fraction"],

                "source":
                    "difference_imaging"
            })

        # ----------------------------------------
        # Source detection
        # ----------------------------------------

        sources = result["sources"]

        if sources:

            evidence.append({

                "type":
                    "source_detection",

                "source_count":
                    len(sources),

                "sources":
                    sources,

                "source":
                    "source_detection"
            })

        # ----------------------------------------
        # Alignment evidence
        # ----------------------------------------

        alignment = result["alignment"]

        evidence.append({

            "type":
                "alignment",

            "shift_x":
                alignment["shift_x"],

            "shift_y":
                alignment["shift_y"],

            "correlation_peak":
                alignment["correlation_peak"],

            "source":
                "image_alignment"
        })

        return evidence

    def artifact_assessment(
        self,
        result
    ):

        change = result["change"]

        changed_pixels = (
            change["changed_pixels"]
        )

        total_pixels = (
            change["total_pixels"]
        )

        if total_pixels == 0:

            return {

                "artifact_probability":
                    1.0,

                "status":
                    "INVALID"
            }

        fraction = (
            changed_pixels /
            total_pixels
        )

        # Engineering heuristic only.
        # This is NOT a scientific probability.

        if fraction < 0.00001:

            probability = 0.30

        elif fraction < 0.001:

            probability = 0.10

        else:

            probability = 0.40

        return {

            "artifact_probability":
                probability,

            "change_fraction":
                fraction,

            "status":
                (
                    "LOW"
                    if probability < 0.2
                    else "MODERATE"
                )
        }
    def investigate_motion(
    self,
    result,
    time_delta
    ):

        sources_a = result.get(
        "sources_epoch_a",
        []
        )

        sources_b = result.get(
        "sources_epoch_b",
        []
        )

        investigations = (
            self.investigation_engine.investigate(
                sources_a,
                sources_b,
                time_delta
            )
        )

        return investigations
    
    def motion_evidence(
        self,
        investigations
    ):

        evidence = []

        for investigation in investigations:

            motion = investigation["motion"]

            if not motion["motion_detected"]:
                continue

            evidence.append({

                "type":
                    "motion",

                "candidate_id":
                    investigation["candidate_id"],

                "delta_x":
                    motion["delta_x"],

                "delta_y":
                    motion["delta_y"],

                "pixel_displacement":
                    motion["pixel_displacement"],

                "pixel_velocity":
                    motion["pixel_velocity"],

                "value":
                    motion["pixel_displacement"],

                "source":
                    "motion_tracking"
            })

        return evidence
    def cross_match_catalog(self, candidate=None, catalog=None):

        from science_engine.catalog import CatalogMatcher

        matcher = CatalogMatcher(
        max_distance_arcsec=5.0
        )

        if candidate is None:
            candidate = {
            "ra": 179.9955,
            "dec": -0.0005
        }

        if catalog is None:
            catalog = [
            {
                "catalog_id": "STAR-001",
                "name": "Known Star A",
                "ra": 179.9955,
                "dec": -0.0005
            }
        ]

        matches = matcher.match(
        candidate,
        catalog
        )

        return {
        "matched": len(matches) > 0,
        "matches": matches
        }