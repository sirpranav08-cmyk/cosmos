import numpy as np


class ImagePreprocessor:

    def clean(self, data):

        data = np.asarray(data, dtype=np.float64)

        # Replace invalid values
        data = np.nan_to_num(
            data,
            nan=0.0,
            posinf=0.0,
            neginf=0.0
        )

        # Remove extreme outliers
        median = np.median(data)
        std = np.std(data)

        lower = median - 5 * std
        upper = median + 5 * std

        cleaned = np.clip(
            data,
            lower,
            upper
        )

        return cleaned

    def normalize(self, data):

        minimum = data.min()
        maximum = data.max()

        if maximum == minimum:
            return np.zeros_like(data)

        normalized = (
            data - minimum
        ) / (
            maximum - minimum
        )

        return normalized

    def process(self, data):

        cleaned = self.clean(data)

        normalized = self.normalize(cleaned)

        return {
            "cleaned": cleaned,
            "normalized": normalized
        }
def normalize_with_reference(
    self,
    data,
    reference
):

    data = np.asarray(
        data,
        dtype=np.float64
    )

    reference = np.asarray(
        reference,
        dtype=np.float64
    )

    minimum = reference.min()
    maximum = reference.max()

    if maximum == minimum:

        return np.zeros_like(data)

    normalized = (
        data - minimum
    ) / (
        maximum - minimum
    )

    return normalized