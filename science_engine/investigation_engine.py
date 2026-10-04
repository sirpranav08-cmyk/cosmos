from science_engine.source_matching import SourceMatcher
from science_engine.motion_tracker import MotionTracker


class InvestigationEngine:

    def __init__(self, max_match_distance=10.0):

        self.matcher = SourceMatcher(
            max_distance=max_match_distance
        )

        self.motion_tracker = MotionTracker()

    def investigate(
        self,
        sources_epoch_a,
        sources_epoch_b,
        time_delta
    ):

        matches = self.matcher.match(
            sources_epoch_a,
            sources_epoch_b
        )

        investigations = []

        for index, match in enumerate(matches):

            source_a = match["source_a"]
            source_b = match["source_b"]

            motion = self.motion_tracker.calculate(
                source_a,
                source_b
            )

            velocity = self.motion_tracker.calculate_velocity(
                motion,
                time_delta
            )

            investigations.append({

                "candidate_id":
                    index + 1,

                "epoch_a":
                    source_a,

                "epoch_b":
                    source_b,

                "match_distance":
                    match["distance"],

                "motion":
                    velocity
            })

        return investigations