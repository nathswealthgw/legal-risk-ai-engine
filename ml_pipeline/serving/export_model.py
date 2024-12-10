from pathlib import Path
import shutil


def export_for_tf_serving(source_dir: str, serving_dir: str, version: int = 1) -> str:
    destination = Path(serving_dir) / str(version)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source_dir, destination)
    return str(destination)
