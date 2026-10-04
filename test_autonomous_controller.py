from agi.autonomous_controller import (
    AutonomousController
)


print()
print("=" * 60)
print("COSMOS FULL AUTONOMOUS CONTROLLER")
print("=" * 60)


# ============================================================
# CANDIDATE
# ============================================================

candidate = {

    "ra": 179.9955,

    "dec": -0.0005
}


# ============================================================
# CATALOG
# ============================================================

catalog = [

    {
        "catalog_id": "STAR-001",

        "name": "Known Star A",

        "ra": 179.9955,

        "dec": -0.0005
    }
]


# ============================================================
# CREATE CONTROLLER
# ============================================================

controller = AutonomousController(

    candidate_id="candidate_1042",

    candidate=candidate,

    catalog=catalog,

    max_cycles=5
)


# ============================================================
# OBSERVATIONS
# ============================================================

controller.add_observation({

    "epoch": "A",

    "x": 300.0,

    "y": 250.0
})


controller.add_observation({

    "epoch": "B",

    "x": 304.0,

    "y": 253.0
})


# ============================================================
# INITIAL SCIENCE EVIDENCE
# ============================================================

controller.add_evidence({

    "type": "motion",

    "delta_x": 4.0,

    "delta_y": 3.0,

    "pixel_displacement": 5.0,

    "pixel_velocity": 0.5,

    "source": "motion_tracking"
})


controller.add_evidence({

    "type": "spectrum",

    "available": True,

    "source": "spectral_analysis"
})


# ============================================================
# RUN AUTONOMOUS LOOP
# ============================================================

final_state = controller.run()


# ============================================================
# FINAL REPORT
# ============================================================

print()
print("=" * 60)
print("FINAL COSMOS STATE")
print("=" * 60)

print()

print(
    "Candidate:",
    final_state["candidate"]
)

print()

print(
    "Strongest hypothesis:",
    final_state[
        "hypotheses"
    ]["strongest"]
)

print()

print(
    "Confidence:",
    f"{final_state['hypotheses']['confidence']:.2f}"
)

print()

print(
    "Investigation status:",
    final_state[
        "investigation"
    ]["status"]
)

print()
print("=" * 60)
print(
    "COSMOS AUTONOMOUS CONTROLLER COMPLETE"
)
print("=" * 60)