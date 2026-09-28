from core.state import CognitiveState

from planning.planner import Planner
from perception.perception import Perception
from reasoning.reasoning import ReasoningEngine
from verification.verifier import Verifier
from language.reporter import Reporter
from tools.tools import ScientificTools
from memory.memory import Memory
from world.world_model import WorldModel

from reasoning.evidence import EvidenceEngine
from reasoning.reflection import ReflectionEngine


class CosmosBrain:

    def __init__(self):

        self.perception = Perception()

        self.planner = Planner()

        self.reasoning = ReasoningEngine()

        self.verifier = Verifier()

        self.reporter = Reporter()

        self.tools = ScientificTools()

        self.memory = Memory()

        self.world = WorldModel()

        self.evidence_engine = EvidenceEngine()

        self.reflection = ReflectionEngine()

    def investigate(
        self,
        goal,
        raw_observations
    ):

        state = CognitiveState(
            goal=goal
        )

        print("\n" + "=" * 60)

        print("COSMOS COGNITIVE ENGINE")

        print("=" * 60)

        print(
            "\nGOAL:",
            goal
        )

        # ----------------------------
        # 1. PLAN
        # ----------------------------

        plan = self.planner.create_plan(
            goal
        )

        state.actions = plan

        print("\nPLAN:")

        for step in plan:

            print(" ->", step)

        # ----------------------------
        # 2. PERCEPTION
        # ----------------------------

        state.observations = (
            self.perception.observe(
                raw_observations
            )
        )

        print(
            "\nOBSERVATIONS:",
            len(state.observations)
        )

        # ----------------------------
        # 3. WORLD MODEL
        # ----------------------------

        for observation in state.observations:

            self.world.add_object(
                observation.observation_id,
                {
                    "ra": observation.ra,
                    "dec": observation.dec,
                    "timestamp": observation.timestamp
                }
            )

        # ----------------------------
        # 4. CREATE HYPOTHESES
        # ----------------------------

        state.hypotheses = (
            self.reasoning.create_hypotheses()
        )

        print("\nHYPOTHESES:")

        for hypothesis in state.hypotheses:

            print(
                f" - {hypothesis.name}: "
                f"{hypothesis.prior:.2f}"
            )

        # ----------------------------
        # 5. MOTION ANALYSIS
        # ----------------------------

        if len(state.observations) >= 2:

            motion = (
                self.tools.calculate_motion(
                    state.observations[0],
                    state.observations[1]
                )
            )

            print(
                "\nMOTION:",
                motion
            )

            evidence = (
                self.reasoning.analyze_motion(
                    motion
                )
            )

            self.evidence_engine.add(
                state,
                evidence
            )

        # ----------------------------
        # 6. SPECTRAL ANALYSIS
        # ----------------------------

        spectrum = (
            self.tools.analyze_spectrum(
                state.observations[0]
            )
        )

        print(
            "\nSPECTRUM:",
            spectrum
        )

        evidence = (
            self.reasoning.analyze_spectrum(
                spectrum
            )
        )

        self.evidence_engine.add(
            state,
            evidence
        )

        # ----------------------------
        # 7. REFLECTION
        # ----------------------------

        print("\nREFLECTION:")

        reflections = (
            self.reflection.reflect(
                state
            )
        )

        for reflection in reflections:

            print(
                " ->",
                reflection
            )

        # ----------------------------
        # 8. RESULTS
        # ----------------------------

        print("\nUPDATED HYPOTHESES:")

        for hypothesis in state.hypotheses:

            print(
                f" - {hypothesis.name}: "
                f"{hypothesis.confidence:.2f}"
            )

        strongest = max(
            state.hypotheses,
            key=lambda h: h.confidence
        )

        print(
            "\nSTRONGEST HYPOTHESIS:",
            strongest.name
        )

        print(
            "CONFIDENCE:",
            f"{strongest.confidence:.2f}"
        )

        print(
            "STATUS:",
            state.status
        )

        # ----------------------------
        # 9. MEMORY
        # ----------------------------

        self.memory.remember_investigation({

            "goal": goal,

            "observations":
                len(state.observations),

            "evidence": [

                {
                    "description":
                        e.description,

                    "value":
                        e.value,

                    "source":
                        e.source

                }

                for e in state.evidence
            ],

            "hypotheses": [

                {
                    "name":
                        h.name,

                    "confidence":
                        h.confidence

                }

                for h in state.hypotheses
            ],

            "status":
                state.status
        })

        return state