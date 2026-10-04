import torch

from transformer import COSMOSTransformer


HYPOTHESES = (
    "Moving astronomical object",
    "Stationary astronomical source",
    "Measurement or imaging artifact",
    "Transient astronomical event",
)


def main():
    torch.manual_seed(42)

    model = COSMOSTransformer(
        d_model=64,
        num_heads=4,
        d_ff=128,
    )
    model.eval()

    # [observation, motion, spectrum, artifact, catalog]
    x = torch.tensor([
        [0.80, 0.95, 0.70, 0.10, 0.20],
    ], dtype=torch.float32)

    with torch.no_grad():
        output = model(x, return_attention=True)

    probabilities = output["probabilities"][0]
    attention = output["attention"]

    assert output["tokens"].shape == (1, 5, 64)
    assert output["fused"].shape == (1, 64)
    assert probabilities.shape == (4,)
    assert attention.shape == (1, 4, 5, 5)
    assert torch.isclose(probabilities.sum(), torch.tensor(1.0), atol=1e-6)

    print("=" * 60)
    print("COSMOS TRANSFORMER EVIDENCE FUSION")
    print("=" * 60)
    print()
    print("INPUT EVIDENCE")
    print("-" * 60)
    print("Observation :", float(x[0, 0]))
    print("Motion      :", float(x[0, 1]))
    print("Spectrum    :", float(x[0, 2]))
    print("Artifact    :", float(x[0, 3]))
    print("Catalog     :", float(x[0, 4]))
    print()
    print("TENSOR SHAPES")
    print("-" * 60)
    print("Evidence tokens:", tuple(output["tokens"].shape))
    print("Fused F_t     :", tuple(output["fused"].shape))
    print("Attention     :", tuple(attention.shape))
    print()
    print("HYPOTHESIS DISTRIBUTION")
    print("-" * 60)
    for name, probability in zip(HYPOTHESES, probabilities.tolist()):
        print(f"{name}: {probability:.4f}")

    strongest_index = int(torch.argmax(probabilities))
    print()
    print("Strongest hypothesis:", HYPOTHESES[strongest_index])
    print()
    print("NOTE: These probabilities are from an untrained model.")
    print("Training is the next step before scientific interpretation.")
    print()
    print("COSMOS TRANSFORMER TEST PASSED")


if __name__ == "__main__":
    main()
