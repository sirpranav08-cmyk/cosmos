from science_engine.investigation_engine import InvestigationEngine
from agi.science_adapter import ScienceEvidenceAdapter
from agi.hypothesis_manager import HypothesisManager
from agi.reflection import ReflectionEngine
from agi.action_planner import ActionPlanner
from agi.action_executor import ActionExecutor


print()
print("=" * 60)
print("COSMOS REASONING LOOP")
print("=" * 60)


# ============================================================
# STEP 1 — TWO OBSERVATION EPOCHS
# ============================================================

epoch_a = [
    {
        "source_id": 1,
        "x": 300.0,
        "y": 250.0
    },
    {
        "source_id": 2,
        "x": 200.0,
        "y": 350.0
    }
]

epoch_b = [
    {
        "source_id": 1,
        "x": 304.0,
        "y": 253.0
    },
    {
        "source_id": 2,
        "x": 200.0,
        "y": 350.0
    }
]


# ============================================================
# STEP 2 — SCIENCE INVESTIGATION
# ============================================================

investigation_engine = InvestigationEngine(
    max_match_distance=10.0
)

investigations = investigation_engine.investigate(
    epoch_a,
    epoch_b,
    time_delta=10.0
)


# ============================================================
# STEP 3 — SCIENCE → AGI EVIDENCE
# ============================================================

adapter = ScienceEvidenceAdapter()

motion_evidence = adapter.motion_evidence(
    investigations
)


print()
print("SCIENCE EVIDENCE")
print("-" * 60)

for item in motion_evidence:

    print(
        f"Candidate {item['candidate_id']}: "
        f"displacement = "
        f"{item['pixel_displacement']}"
    )


# ============================================================
# STEP 4 — HYPOTHESIS UPDATE
# ============================================================

hypothesis_manager = HypothesisManager()

for evidence in motion_evidence:

    hypothesis_manager.update(
        evidence
    )


hypothesis = hypothesis_manager.report()


print()
print("HYPOTHESIS")
print("-" * 60)

print(
    "Strongest:",
    hypothesis["strongest"]
)

print(
    "Confidence:",
    f"{hypothesis['confidence']:.2f}"
)


# ============================================================
# STEP 5 — CREATE INVESTIGATION OBJECT
# ============================================================

class InvestigationState:

    def __init__(self):

        self.observations = []

        self.evidence = []

        self.reflection_result = None

    def add_observation(
        self,
        observation
    ):

        self.observations.append(
            observation
        )

    def add_evidence(
        self,
        evidence
    ):

        self.evidence.append(
            evidence
        )

    def reflect(
        self,
        reflection
    ):

        self.reflection_result = reflection


state = InvestigationState()


state.add_observation(epoch_a)
state.add_observation(epoch_b)


for evidence in motion_evidence:

    state.add_evidence(
        evidence
    )


# ============================================================
# STEP 6 — REFLECTION
# ============================================================

reflection_engine = ReflectionEngine()

reflection = reflection_engine.reflect(
    state
)


print()
print("COSMOS REFLECTION")
print("-" * 60)

for reason in reflection["reasoning"]:

    print(
        "->",
        reason
    )


print()
print("MISSING EVIDENCE")

for missing in reflection["missing_evidence"]:

    print(
        "->",
        missing
    )


print()
print("STATUS:")

print(
    reflection["status"]
)


# ============================================================
# STEP 7 — ACTION PLANNING
# ============================================================

planner = ActionPlanner()

actions = planner.plan(
    reflection
)


print()
print("PLANNED ACTIONS")
print("-" * 60)

for action in actions:

    print(
        "->",
        action["name"]
    )

    print(
        "   ",
        action["description"]
    )


# ============================================================
# STEP 8 — CATALOG DATA
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
# STEP 9 — EXECUTE CATALOG ACTION
# ============================================================

executor = ActionExecutor()

print()
print("ACTION EXECUTION")
print("-" * 60)

for action in actions:

    if action["name"] != "cross_match_catalog":
        continue

    result = executor.execute(
        action,
        candidate=candidate,
        catalog=catalog
    )

    print(
        "Action:",
        action["name"]
    )

    print(
        "Success:",
        result["success"]
    )

    if result["success"]:

        output = result["result"]

        print(
            "Matched:",
            output["matched"]
        )

        print(
            "Matches:",
            output["matches"]
        )

        # ----------------------------------------
        # Convert catalog result to AGI evidence
        # ----------------------------------------

        catalog_evidence = {
            "type": "catalog_match",

            "matched":
                output["matched"],

            "matches":
                output["matches"],

            "source":
                "catalog_search"
        }

        state.add_evidence(
            catalog_evidence
        )

        hypothesis_manager.update(
            catalog_evidence
        )


# ============================================================
# STEP 10 — UPDATED HYPOTHESIS
# ============================================================

updated_hypothesis = (
    hypothesis_manager.report()
)


print()
print("UPDATED HYPOTHESIS")
print("-" * 60)

for name, probability in (
    updated_hypothesis["hypotheses"].items()
):

    print(
        f"{name}: "
        f"{probability:.2f}"
    )


print()
print(
    "Strongest hypothesis:",
    updated_hypothesis["strongest"]
)

print(
    "Confidence:",
    f"{updated_hypothesis['confidence']:.2f}"
)


print()
print("=" * 60)
print("COSMOS REASONING LOOP COMPLETE")
print("=" * 60)