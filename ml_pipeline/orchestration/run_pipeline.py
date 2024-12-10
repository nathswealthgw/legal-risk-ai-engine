import argparse
import subprocess


def run_train(date: str) -> None:
    print(f"[pipeline] running training for snapshot={date}")
    subprocess.run(["python", "ml_pipeline/jobs/train_model.py", "--output", "artifacts/model"], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["train"], required=True)
    parser.add_argument("--date", required=True)
    args = parser.parse_args()

    if args.mode == "train":
        run_train(args.date)


if __name__ == "__main__":
    main()
