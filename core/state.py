from dataclasses import dataclass, field
from typing import Any


@dataclass
class Observation:
    observation_id: str
    timestamp: str
    ra: float
    dec: float
    brightness: float | None = None
    spectral_data: dict[str, float] = field(
        default_factory=dict
    )
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class Evidence:
    description: str
    value: float
    source: str
    supports: str
    reliability: float = 1.0


@dataclass
class Hypothesis:
    name: str
    prior: float

    supporting_evidence: list[Evidence] = field(
        default_factory=list
    )

    contradicting_evidence: list[Evidence] = field(
        default_factory=list
    )

    @property
    def confidence(self) -> float:

        support = sum(
            e.value * e.reliability
            for e in self.supporting_evidence
        )

        contradiction = sum(
            e.value * e.reliability
            for e in self.contradicting_evidence
        )

        score = (
            self.prior
            + support
            - contradiction
        )

        return max(
            0.0,
            min(1.0, score)
        )


@dataclass
class CognitiveState:

    goal: str

    observations: list[Observation] = field(
        default_factory=list
    )

    evidence: list[Evidence] = field(
        default_factory=list
    )

    hypotheses: list[Hypothesis] = field(
        default_factory=list
    )

    actions: list[str] = field(
        default_factory=list
    )

    findings: list[str] = field(
        default_factory=list
    )

    reflection_count: int = 0

    status: str = "INITIALIZED"