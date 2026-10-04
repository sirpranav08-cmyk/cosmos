from torch import nn


class HypothesisHead(nn.Module):
    """Map the fused evidence representation to COSMOS hypotheses."""

    HYPOTHESES = (
        "Moving astronomical object",
        "Stationary astronomical source",
        "Measurement or imaging artifact",
        "Transient astronomical event",
    )

    def __init__(self, d_model=64):
        super().__init__()
        self.classifier = nn.Linear(d_model, len(self.HYPOTHESES))

    def forward(self, fused):
        return self.classifier(fused)
