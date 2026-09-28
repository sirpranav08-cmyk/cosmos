import numpy as np


class DifferenceEngine:

    def calculate(
        self,
        reference,
        target
    ):

        reference = np.asarray(
            reference,
            dtype=np.float64
        )

        target = np.asarray(
            target,
            dtype=np.float64
        )

        if reference.shape != target.shape:

            raise ValueError(
                "Images must have the same shape."
            )

        difference = target - reference

        absolute_difference = np.abs(
            difference
        )

        return {
            "difference": difference,
            "absolute": absolute_difference
        }

    def detect_changes(
        self,
        difference,
        threshold=0.1
    ):

        absolute_difference = np.abs(
            difference
        )

        mask = (
            absolute_difference > threshold
        )

        changed_pixels = int(
            np.sum(mask)
        )

        total_pixels = mask.size

        change_fraction = (
            changed_pixels /
            total_pixels
        )

        return {
            "mask": mask,
            "changed_pixels": changed_pixels,
            "total_pixels": total_pixels,
            "change_fraction": change_fraction
        }