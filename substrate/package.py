import json
import os

SNAPSHOT_DIR = "state/executions"
PACKAGE_DIR = "packages"


def load_snapshot(execution_id):
    path = os.path.join(SNAPSHOT_DIR, f"{execution_id}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Snapshot not found: {execution_id}")

    with open(path, "r") as f:
        return json.load(f)


def build_execution_package(execution_id):
    snapshot = load_snapshot(execution_id)

    package = {
        "execution_id": execution_id,
        "snapshot": snapshot
    }

    required_keys = {"execution_id", "snapshot"}
    assert set(package.keys()) == required_keys

    return package


def export_execution_package(execution_id):
    os.makedirs(PACKAGE_DIR, exist_ok=True)

    package = build_execution_package(execution_id)
    path = os.path.join(PACKAGE_DIR, f"{execution_id}.json")

    with open(path, "w") as f:
        json.dump(package, f, indent=2)

    return path