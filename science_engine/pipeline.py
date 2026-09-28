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

    def compare(
        self,
        image_a,
        image_b,
        header
    ):

        # Align second observation
        alignment = self.aligner.estimate_shift(
            image_a,
            image_b
        )

        aligned_b = self.aligner.align(
            image_b,
            alignment["shift_x"],
            alignment["shift_y"]
        )

        # Difference image
        difference = self.difference.calculate(
            image_a,
            aligned_b
        )

        change = self.difference.detect_changes(
            difference["difference"],
            threshold=0.1
        )

        # Detect sources
        sources = self.detector.detect(
            difference["difference"],
            threshold=0.1
        )

        # WCS
        mapper = WCSMapper(header)

        for source in sources:

            sky = mapper.pixel_to_sky(
                source["x"],
                source["y"]
            )

            source["ra"] = sky["ra"]
            source["dec"] = sky["dec"]

        return {
            "alignment": alignment,
            "difference": difference,
            "change": change,
            "sources": sources
        }