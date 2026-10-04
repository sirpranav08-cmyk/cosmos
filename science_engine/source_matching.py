import math


class SourceMatcher:

    def __init__(self, max_distance=10.0):
        self.max_distance = max_distance

    def distance(self, source_a, source_b):

        dx = source_b["x"] - source_a["x"]
        dy = source_b["y"] - source_a["y"]

        return math.sqrt(
            dx * dx + dy * dy
        )

    def match(
        self,
        sources_a,
        sources_b
    ):

        matches = []

        used_b = set()

        for index_a, source_a in enumerate(sources_a):

            best_index = None
            best_distance = float("inf")

            for index_b, source_b in enumerate(sources_b):

                if index_b in used_b:
                    continue

                distance = self.distance(
                    source_a,
                    source_b
                )

                if (
                    distance <= self.max_distance
                    and distance < best_distance
                ):

                    best_distance = distance
                    best_index = index_b

            if best_index is not None:

                used_b.add(best_index)

                matches.append({

                    "source_a": source_a,

                    "source_b":
                        sources_b[best_index],

                    "distance":
                        best_distance
                })

        return matches