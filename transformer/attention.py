import math
import torch
from torch import nn


class MultiHeadSelfAttention(nn.Module):
    """Standard scaled dot-product multi-head self-attention."""

    def __init__(self, d_model=64, num_heads=4, dropout=0.0):
        super().__init__()
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads.")

        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)

    def _split_heads(self, x):
        batch, tokens, _ = x.shape
        x = x.view(batch, tokens, self.num_heads, self.head_dim)
        return x.transpose(1, 2)

    def forward(self, x, return_attention=False):
        q = self._split_heads(self.q_proj(x))
        k = self._split_heads(self.k_proj(x))
        v = self._split_heads(self.v_proj(x))

        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        weights = torch.softmax(scores, dim=-1)
        weights = self.dropout(weights)

        attended = torch.matmul(weights, v)
        attended = attended.transpose(1, 2).contiguous()
        attended = attended.view(x.shape[0], x.shape[1], self.d_model)
        output = self.out_proj(attended)

        if return_attention:
            return output, weights
        return output
