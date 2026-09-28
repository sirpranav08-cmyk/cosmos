import numpy as np
from scipy.ndimage import label, center_of_mass


class SourceDetector:

    def detect(
        self,
        difference,
        threshold=0.1
    ):

        difference = np.asarray(
            difference,
            dtype=np.float64
        )

        # Absolute signal change
        signal = np.abs(difference)

        # Threshold
        mask = signal > threshold

        # Find connected regions
        labeled, num_sources = label(mask)

        sources = []

        if num_sources == 0:
            return sources

        centers = center_of_mass(
            signal,
            labeled,
            range(1, num_sources + 1)
        )

        for source_id, center in enumerate(
            centers,
            start=1
        ):

            y, x = center

            pixels = (
                labeled == source_id
            )

            values = signal[pixels]

            sources.append({

                "source_id": source_id,

                "x": float(x),

                "y": float(y),

                "peak_signal": float(
                    np.max(values)
                ),

                "total_signal": float(
                    np.sum(values)
                ),

                "pixel_count": int(
                    np.sum(pixels)
                )
            })

        return sources