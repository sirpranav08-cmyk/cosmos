from science_engine.catalog import CatalogMatcher


print()
print("=" * 60)
print("COSMOS CATALOG CROSS-MATCH")
print("=" * 60)


catalog = [

    {
        "catalog_id": "STAR-001",
        "name": "Known Star A",
        "ra": 179.9955,
        "dec": -0.0005
    },

    {
        "catalog_id": "STAR-002",
        "name": "Known Star B",
        "ra": 180.0055,
        "dec": 0.0095
    },

    {
        "catalog_id": "STAR-003",
        "name": "Known Star C",
        "ra": 181.0000,
        "dec": 2.0000
    }
]


candidate = {

    "source_id": 1,

    "ra":
        179.9955,

    "dec":
        -0.0005
}


matcher = CatalogMatcher(
    max_distance_arcsec=5.0
)


matches = matcher.match(
    candidate,
    catalog
)


print()
print("CANDIDATE")
print("-" * 60)

print(
    "RA:",
    candidate["ra"]
)

print(
    "Dec:",
    candidate["dec"]
)


print()
print("CATALOG MATCHES")
print("-" * 60)

if not matches:

    print(
        "No catalog matches found."
    )

else:

    for match in matches:

        print(
            "Catalog ID:",
            match["catalog_id"]
        )

        print(
            "Name:",
            match["name"]
        )

        print(
            "Distance:",
            match["distance_arcsec"],
            "arcsec"
        )


print()
print("=" * 60)
print("CATALOG CROSS-MATCH COMPLETE")
print("=" * 60)