from core.state import Observation


class Perception:

    def observe(self, raw_data: list[dict]) -> list[Observation]:

        observations = []

        for item in raw_data:

            observation = Observation(
                observation_id=item["id"],
                timestamp=item["timestamp"],
                ra=float(item["ra"]),
                dec=float(item["dec"]),
                brightness=item.get("brightness"),
                spectral_data=item.get("spectrum", {}),
                metadata=item.get("metadata", {})
            )

            observations.append(observation)

        return observations