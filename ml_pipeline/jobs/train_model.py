import argparse
from pathlib import Path

import numpy as np

from ml_pipeline.training.model import build_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/model")
    parser.add_argument("--model-version", type=int, default=1)
    args = parser.parse_args()

    if args.model_version < 1:
        parser.error("--model-version must be a positive integer")

    return args


def main() -> None:
    args = parse_args()

    x = np.random.rand(1000, 8)
    y = (x[:, 0] + x[:, 1] * 0.8 + np.random.rand(1000) * 0.1 > 0.9).astype(int)

    model = build_model(input_dim=8)
    model.fit(x, y, validation_split=0.2, epochs=4, batch_size=64, verbose=0)

    out = Path(args.output)
    versioned_out = out / str(args.model_version)
    versioned_out.mkdir(parents=True, exist_ok=True)
    model.export(str(versioned_out))


if __name__ == "__main__":
    main()
