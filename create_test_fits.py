from pathlib import Path

import numpy as np
from astropy.io import fits


data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Create a small synthetic astronomical image
image = np.random.normal(
    loc=100,
    scale=5,
    size=(512, 512)
)

# Add a few artificial sources
image[200, 250] += 500
image[300, 350] += 800
image[150, 400] += 300

header = fits.Header()

header["OBJECT"] = "COSMOS_TEST"
header["TELESCOP"] = "SIMULATED"
header["INSTRUME"] = "COSMOS"
header["BUNIT"] = "arbitrary"

hdu = fits.PrimaryHDU(
    data=image,
    header=header
)

output = data_dir / "sample.fits"

hdu.writeto(
    output,
    overwrite=True
)

print("Created:")
print(output.resolve())