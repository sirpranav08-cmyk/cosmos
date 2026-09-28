from astropy.io import fits

from science_engine.wcs_mapper import WCSMapper


print("\nWCS COORDINATE TEST")
print("=" * 50)


# Load FITS
with fits.open(
    "data/wcs_test.fits"
) as hdul:

    header = hdul[0].header


# Create mapper
mapper = WCSMapper(header)


# Candidate detected by COSMOS
x = 304.0
y = 253.0


sky = mapper.pixel_to_sky(
    x,
    y
)


print(
    "Pixel X:",
    x
)

print(
    "Pixel Y:",
    y
)

print(
    "\nRA:",
    sky["ra"]
)

print(
    "Dec:",
    sky["dec"]
)


# Convert back
pixel = mapper.sky_to_pixel(
    sky["ra"],
    sky["dec"]
)


print(
    "\nReverse conversion"
)

print(
    "X:",
    pixel["x"]
)

print(
    "Y:",
    pixel["y"]
)