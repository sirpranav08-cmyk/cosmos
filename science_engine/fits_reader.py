from pathlib import Path

import numpy as np
from astropy.io import fits


class FITSReader:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

        if not self.filepath.exists():
            raise FileNotFoundError(
                f"FITS file not found: {self.filepath}"
            )

    def read(self):

        with fits.open(self.filepath) as hdul:

            print("\nFITS FILE")
            print("=" * 50)

            print("File:", self.filepath)

            print("\nHDU INFORMATION")

            for index, hdu in enumerate(hdul):

                print(
                    f"HDU {index}: "
                    f"{type(hdu).__name__}"
                )

                print(
                    "Shape:",
                    getattr(
                        hdu.data,
                        "shape",
                        None
                    )
                )

            primary = hdul[0]

            data = primary.data
            header = primary.header

            if data is None:

                raise ValueError(
                    "Primary HDU contains no image data."
                )

            data = np.asarray(
                data,
                dtype=np.float64
            )

            return data, header