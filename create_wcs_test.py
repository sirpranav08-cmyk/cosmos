from pathlib import Path

import numpy as np

from astropy.io import fits


data_dir = Path("data")
data_dir.mkdir(exist_ok=True)


# Create image
image = np.random.normal(
    100,
    5,
    (512, 512)
)


header = fits.Header()

# Basic image information
header["NAXIS"] = 2
header["NAXIS1"] = 512
header["NAXIS2"] = 512

# WCS
header["CTYPE1"] = "RA---TAN"
header["CTYPE2"] = "DEC--TAN"

# Reference sky position
header["CRVAL1"] = 180.0
header["CRVAL2"] = 0.0

# Reference pixel
header["CRPIX1"] = 256.0
header["CRPIX2"] = 256.0

# Pixel scale
header["CDELT1"] = -0.0001
header["CDELT2"] = 0.0001

header["CUNIT1"] = "deg"
header["CUNIT2"] = "deg"


hdu = fits.PrimaryHDU(
    data=image,
    header=header
)


output = data_dir / "wcs_test.fits"

hdu.writeto(
    output,
    overwrite=True
)

print(
    "Created:",
    output.resolve()
)