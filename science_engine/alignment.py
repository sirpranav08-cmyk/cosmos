import numpy as np


class ImageAligner:

    def estimate_shift(self, reference, target):

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
                "Reference and target images "
                "must have the same shape."
            )

        # Remove average brightness
        reference_centered = (
            reference - np.mean(reference)
        )

        target_centered = (
            target - np.mean(target)
        )

        # FFT-based cross correlation
        reference_fft = np.fft.fft2(
            reference_centered
        )

        target_fft = np.fft.fft2(
            target_centered
        )

        correlation = np.fft.ifft2(
            reference_fft *
            np.conj(target_fft)
        )

        correlation = np.abs(
            np.fft.fftshift(correlation)
        )

        # Find correlation peak
        peak = np.unravel_index(
            np.argmax(correlation),
            correlation.shape
        )

        center_y = correlation.shape[0] // 2
        center_x = correlation.shape[1] // 2

        shift_y = peak[0] - center_y
        shift_x = peak[1] - center_x

        return {
            "shift_x": int(shift_x),
            "shift_y": int(shift_y),
            "correlation_peak": float(
                correlation[peak]
            )
        }

    def align(
        self,
        target,
        shift_x,
        shift_y
    ):

        aligned = np.roll(
            target,
            shift=(shift_y, shift_x),
            axis=(0, 1)
        )

        return aligned