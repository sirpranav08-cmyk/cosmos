from agi import ActionExecutor


print()
print("=" * 60)
print("COSMOS ACTION EXECUTOR → CATALOG")
print("=" * 60)


candidate = {
    "candidate_id": 1,
    "ra": 179.9955,
    "dec": -0.0005
}


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
        "ra": 180.1000,
        "dec": 0.1000
    }
]


executor = ActionExecutor()


action = {
    "name":
        "cross_match_catalog"
}


result = executor.cross_match_catalog(
    candidate=candidate,
    catalog=catalog
)


print("\nCATALOG RESULT")
print("-" * 60)

print("Success:", result["success"])

print("Matched:",
      result["result"]["matched"])

print("Catalog ID:",
      result["result"]["catalog_id"])

print("Name:",
      result["result"]["name"])

print("Distance:",
      result["result"]["distance_arcsec"],
      "arcsec")


print()
print("=" * 60)
print("CATALOG ACTION COMPLETE")
print("=" * 60)