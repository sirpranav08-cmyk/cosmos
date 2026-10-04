import numpy as np
from scipy.ndimage import label, center_of_mass


class SourceDetector:

    def detect(
        self,
        image,
        threshold=0.1,
        min_pixels=1,
        max_pixels=1000
    ):

        image = np.asarray(
            image,
            dtype=np.float64
        )

        # --------------------------------------------------
        # 1. Remove large-scale background
        # --------------------------------------------------

        background = np.median(image)

        signal = image - background

        # We are interested in positive sources
        signal = np.maximum(signal, 0.0)

        # --------------------------------------------------
        # 2. Threshold
        # --------------------------------------------------

        mask = signal > threshold

        # --------------------------------------------------
        # 3. Connected components
        # --------------------------------------------------

        labeled, num_sources = label(mask)

        sources = []

        if num_sources == 0:
            return sources

        # --------------------------------------------------
        # 4. Analyze each component
        # --------------------------------------------------

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

            pixel_count = int(
                np.sum(pixels)
            )

            # Ignore extremely large background regions
            if pixel_count < min_pixels:
                continue

            if pixel_count > max_pixels:
                continue

            values = signal[pixels]

            sources.append({

                "source_id":
                    len(sources) + 1,

                "x":
                    float(x),

                "y":
                    float(y),

                "peak_signal":
                    float(np.max(values)),

                "total_signal":
                    float(np.sum(values)),

                "pixel_count":
                    pixel_count
            })

        return sources