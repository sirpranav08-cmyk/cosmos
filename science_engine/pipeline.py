from science_engine.fits_reader import FITSReader
from science_engine.preprocessing import ImagePreprocessor
from science_engine.alignment import ImageAligner
from science_engine.difference import DifferenceEngine
from science_engine.source_detection import SourceDetector
from science_engine.motion import MotionAnalyzer
from science_engine.wcs_mapper import WCSMapper


class SciencePipeline:

    def __init__(self):

        self.preprocessor = ImagePreprocessor()
        self.aligner = ImageAligner()
        self.difference = DifferenceEngine()
        self.detector = SourceDetector()
        self.motion = MotionAnalyzer()

    def load(self, filepath):

        reader = FITSReader(filepath)

        data, header = reader.read()

        return data, header

    def preprocess(self, data):

        result = self.preprocessor.process(data)

        return result["normalized"]

    # ========================================================
    # ADD WCS COORDINATES
    # ========================================================

    def _add_wcs_coordinates(
        self,
        sources,
        header
    ):

        mapper = WCSMapper(header)

        for source in sources:

            sky = mapper.pixel_to_sky(
                source["x"],
                source["y"]
            )

            source["ra"] = sky["ra"]
            source["dec"] = sky["dec"]

        return sources

    # ========================================================
    # COMPARE TWO OBSERVATIONS
    # ========================================================

    def compare(
        self,
        image_a,
        image_b,
        header
    ):

        # ----------------------------------------------------
        # STEP 1: ALIGN SECOND OBSERVATION
        # ----------------------------------------------------

        alignment = self.aligner.estimate_shift(
            image_a,
            image_b
        )

        aligned_b = self.aligner.align(
            image_b,
            alignment["shift_x"],
            alignment["shift_y"]
        )

        # ----------------------------------------------------
        # STEP 2: DETECT SOURCES IN EPOCH A
        # ----------------------------------------------------

        sources_epoch_a = self.detector.detect(
            image_a,
            threshold=0.1
        )

        # ----------------------------------------------------
        # STEP 3: DETECT SOURCES IN EPOCH B
        # ----------------------------------------------------

        sources_epoch_b = self.detector.detect(
            aligned_b,
            threshold=0.1
        )

        # ----------------------------------------------------
        # STEP 4: WCS FOR EPOCH A
        # ----------------------------------------------------

        sources_epoch_a = (
            self._add_wcs_coordinates(
                sources_epoch_a,
                header
            )
        )

        # ----------------------------------------------------
        # STEP 5: WCS FOR EPOCH B
        # ----------------------------------------------------

        sources_epoch_b = (
            self._add_wcs_coordinates(
                sources_epoch_b,
                header
            )
        )

        # ----------------------------------------------------
        # STEP 6: DIFFERENCE IMAGE
        # ----------------------------------------------------

        difference = self.difference.calculate(
            image_a,
            aligned_b
        )

        # ----------------------------------------------------
        # STEP 7: CHANGE DETECTION
        # ----------------------------------------------------

        change = self.difference.detect_changes(
            difference["difference"],
            threshold=0.1
        )

        # ----------------------------------------------------
        # STEP 8: DIFFERENCE SOURCES
        # ----------------------------------------------------

        difference_sources = self.detector.detect(
            difference["difference"],
            threshold=0.1
        )

        difference_sources = (
            self._add_wcs_coordinates(
                difference_sources,
                header
            )
        )

        # ----------------------------------------------------
        # RETURN COMPLETE SCIENCE RESULT
        # ----------------------------------------------------

        return {

            "alignment":
                alignment,

            "difference":
                difference,

            "change":
                change,

            # Sources detected independently
            # in each observation.
            "sources_epoch_a":
                sources_epoch_a,

            "sources_epoch_b":
                sources_epoch_b,

            # Sources detected from the
            # difference image.
            "sources":
                difference_sources
        }