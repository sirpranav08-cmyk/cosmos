from agi.autonomous_loop import AutonomousInvestigator


print()
print("=" * 60)
print("COSMOS AUTONOMOUS CATALOG REASONING")
print("=" * 60)


# ============================================================
# CREATE AUTONOMOUS INVESTIGATOR
# ============================================================

cosmos = AutonomousInvestigator(
    candidate_id="candidate_1042"
)


# ============================================================
# OBSERVATIONS
# ============================================================

epoch_a = {
    "epoch": "A",
    "x": 300.0,
    "y": 250.0
}

epoch_b = {
    "epoch": "B",
    "x": 304.0,
    "y": 253.0
}

cosmos.add_observation(epoch_a)
cosmos.add_observation(epoch_b)


# ============================================================
# MOTION EVIDENCE
# ============================================================

cosmos.add_evidence({

    "type": "motion",

    "delta_x": 4.0,

    "delta_y": 3.0,

    "pixel_displacement": 5.0,

    "pixel_velocity": 0.5,

    "source": "motion_tracking"
})


# ============================================================
# SPECTRAL EVIDENCE
# ============================================================

cosmos.add_evidence({

    "type": "spectrum",

    "available": True,

    "source": "spectral_analysis"
})


# ============================================================
# FIRST THINK
# ============================================================

thinking = cosmos.think()


print()
print("INITIAL REFLECTION")
print("-" * 60)

for reason in thinking["reflection"]["reasoning"]:

    print("->", reason)


print()
print("MISSING EVIDENCE")

for item in thinking["reflection"]["missing_evidence"]:

    print("->", item)


print()
print("PLANNED ACTIONS")

for action in thinking["actions"]:

    print(
        "->",
        action["name"]
    )


# ============================================================
# CATALOG DATA
# ============================================================

candidate = {

    "ra": 179.9955,

    "dec": -0.0005
}


catalog = [

    {
        "catalog_id": "STAR-001",

        "name": "Known Star A",

        "ra": 179.9955,

        "dec": -0.0005
    }
]


# ============================================================
# EXECUTE CATALOG ACTION
# ============================================================

catalog_action = {

    "name":
        "cross_match_catalog",

    "description":
        "Cross-match candidate with astronomical catalogs"
}


print()
print("CATALOG ACTION")
print("-" * 60)


result = cosmos.executor.execute(

    catalog_action,

    candidate=candidate,

    catalog=catalog
)


print(
    "Success:",
    result["success"]
)


print(
    "Matched:",
    result.get(
        "matched",
        False
    )
)


print(
    "Matches:",
    result.get(
        "matches",
        []
    )
)


# ============================================================
# CONVERT EXECUTOR RESULT INTO COSMOS EVIDENCE
# ============================================================

if result["success"]:

    cosmos._process_result(
        result
    )


# ============================================================
# SECOND THINK
# ============================================================

thinking = cosmos.think()


print()
print("SECOND REFLECTION")
print("-" * 60)

for reason in thinking["reflection"]["reasoning"]:

    print("->", reason)


print()
print("REMAINING MISSING EVIDENCE")

for item in thinking["reflection"]["missing_evidence"]:

    print("->", item)


print()
print("STATUS:")

print(
    thinking["reflection"]["status"]
)


# ============================================================
# SHOW CURRENT EVIDENCE
# ============================================================

print()
print("CATALOG EVIDENCE")
print("-" * 60)

for evidence in cosmos.investigation.evidence:

    if evidence.get("type") == "catalog_match":

        print(
            "Matched:",
            evidence.get(
                "matched",
                False
            )
        )

        print(
            "Matches:",
            evidence.get(
                "matches",
                []
            )
        )


# ============================================================
# FINAL STATE
# ============================================================

state = cosmos.state()


print()
print("FINAL HYPOTHESIS")
print("-" * 60)

for name, probability in (
    state["hypotheses"]["hypotheses"].items()
):

    print(
        f"{name}: {probability:.2f}"
    )


print()
print("STRONGEST HYPOTHESIS:")

print(
    state["hypotheses"]["strongest"]
)


print()
print("CONFIDENCE:")

print(
    f"{state['hypotheses']['confidence']:.2f}"
)


print()
print("=" * 60)
print(
    "COSMOS AUTONOMOUS CATALOG REASONING COMPLETE"
)
print("=" * 60)