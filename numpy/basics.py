"""NumPy 2 basics: explicit dtype, broadcasting, and reproducible random data."""

import numpy as np


def main() -> None:
    # default_rng avoids shared global RNG state; a seed makes this example repeatable.
    random = np.random.default_rng(42)
    samples = random.uniform(-0.2, 0.2, size=(8, 2)).astype(np.float32)
    channel_gain = np.array([0.5, 0.25], dtype=np.float32)
    print(samples * channel_gain)  # Broadcasting applies one gain per channel.
    view = samples[:2]
    copy = samples[:2].copy()
    print("view shares storage:", np.shares_memory(samples, view))
    print("copy shares storage:", np.shares_memory(samples, copy))
    # Promote accumulation deliberately when numerical error matters.
    print("RMS:", np.sqrt(np.mean(samples.astype(np.float64) ** 2, axis=0)))


if __name__ == "__main__":
    main()
