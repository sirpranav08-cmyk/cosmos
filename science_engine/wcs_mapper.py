from astropy.wcs import WCS


class WCSMapper:

    def __init__(self, header):

        self.wcs = WCS(header)

    def pixel_to_sky(
        self,
        x,
        y
    ):

        ra, dec = self.wcs.pixel_to_world_values(
            x,
            y
        )

        return {
            "ra": float(ra),
            "dec": float(dec)
        }

    def sky_to_pixel(
        self,
        ra,
        dec
    ):

        x, y = self.wcs.world_to_pixel_values(
            ra,
            dec
        )

        return {
            "x": float(x),
            "y": float(y)
        }