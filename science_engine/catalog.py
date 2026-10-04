import math


class CatalogMatcher:

    def __init__(self, max_distance_arcsec=5.0):

        self.max_distance_arcsec = (
            max_distance_arcsec
        )

    def angular_distance(
        self,
        ra1,
        dec1,
        ra2,
        dec2
    ):

        ra_difference = (
            (ra2 - ra1)
            * math.cos(
                math.radians(dec1)
            )
        )

        dec_difference = (
            dec2 - dec1
        )

        distance_degrees = math.sqrt(
            ra_difference ** 2
            + dec_difference ** 2
        )

        return (
            distance_degrees * 3600.0
        )

    def match(
        self,
        candidate,
        catalog
    ):

        matches = []

        candidate_ra = candidate["ra"]
        candidate_dec = candidate["dec"]

        for entry in catalog:

            distance = self.angular_distance(
                candidate_ra,
                candidate_dec,
                entry["ra"],
                entry["dec"]
            )

            if (
                distance
                <= self.max_distance_arcsec
            ):

                matches.append({

                    "catalog_id":
                        entry["catalog_id"],

                    "name":
                        entry["name"],

                    "ra":
                        entry["ra"],

                    "dec":
                        entry["dec"],

                    "distance_arcsec":
                        distance
                })

        matches.sort(
            key=lambda item:
                item["distance_arcsec"]
        )

        return matches