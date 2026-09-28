from dataclasses import dataclass, field


@dataclass
class Investigation:

    candidate_id: str

    goal: str = (
        "Determine whether this candidate "
        "represents a genuine moving "
        "astronomical object."
    )

    evidence: list = field(
        default_factory=list
    )

    hypotheses: dict = field(
        default_factory=dict
    )

    actions: list = field(
        default_factory=list
    )

    observations: list = field(
        default_factory=list
    )

    reflections: list = field(
        default_factory=list
    )

    status: str = "INITIALIZED"

    def add_evidence(
        self,
        evidence
    ):

        self.evidence.append(
            evidence
        )

    def add_observation(
        self,
        observation
    ):

        self.observations.append(
            observation
        )

    def add_action(
        self,
        action
    ):

        self.actions.append(
            action
        )

    def reflect(
        self,
        reflection
    ):

        self.reflections.append(
            reflection
        )

    def summary(self):

        return {

            "candidate_id":
                self.candidate_id,

            "goal":
                self.goal,

            "evidence_count":
                len(self.evidence),

            "observation_count":
                len(self.observations),

            "actions_taken":
                len(self.actions),

            "reflections":
                len(self.reflections),

            "status":
                self.status
        }