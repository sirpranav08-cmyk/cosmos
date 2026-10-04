import torch
from torch import nn


class EvidenceEncoder(nn.Module):
    """Encode five COSMOS evidence scores into Transformer tokens.

    Input shape:  [batch, 5]
    Token order: observation, motion, spectrum, artifact, catalog.
    Output shape: [batch, 5, d_model]
    """

    EVIDENCE_TYPES = (
        "observation",
        "motion",
        "spectrum",
        "artifact",
        "catalog",
    )

    def __init__(self, d_model=64):
        super().__init__()
        self.value_projection = nn.Linear(1, d_model)
        self.type_embedding = nn.Parameter(torch.randn(5, d_model) * 0.02)
        self.norm = nn.LayerNorm(d_model)

    def forward(self, x):
        if x.ndim != 2 or x.shape[1] != 5:
            raise ValueError("Evidence input must have shape [batch, 5].")

        tokens = self.value_projection(x.unsqueeze(-1))
        tokens = tokens + self.type_embedding.unsqueeze(0)
        return self.norm(tokens)
