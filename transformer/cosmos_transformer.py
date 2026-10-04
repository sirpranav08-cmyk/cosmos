import torch
from torch import nn

from .attention import MultiHeadSelfAttention
from .evidence_encoder import EvidenceEncoder
from .hypothesis_head import HypothesisHead


class COSMOSTransformer(nn.Module):
    """Proposed Transformer-based COSMOS evidence-fusion model.

    Pipeline:
        X_t -> embedding -> MHA -> fusion -> P(H_t | E_t)
    """

    def __init__(self, d_model=64, num_heads=4, d_ff=128, dropout=0.0):
        super().__init__()
        self.encoder = EvidenceEncoder(d_model=d_model)
        self.attention = MultiHeadSelfAttention(
            d_model=d_model,
            num_heads=num_heads,
            dropout=dropout,
        )
        self.norm1 = nn.LayerNorm(d_model)
        self.feed_forward = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model),
        )
        self.norm2 = nn.LayerNorm(d_model)
        self.hypothesis_head = HypothesisHead(d_model=d_model)

    def forward(self, x, return_attention=False):
        tokens = self.encoder(x)

        attended, attention_weights = self.attention(
            tokens,
            return_attention=True,
        )
        tokens = self.norm1(tokens + attended)
        tokens = self.norm2(tokens + self.feed_forward(tokens))

        # Mean pooling creates the fused evidence representation F_t.
        fused = tokens.mean(dim=1)
        logits = self.hypothesis_head(fused)
        probabilities = torch.softmax(logits, dim=-1)

        result = {
            "tokens": tokens,
            "fused": fused,
            "logits": logits,
            "probabilities": probabilities,
        }

        if return_attention:
            result["attention"] = attention_weights

        return result
