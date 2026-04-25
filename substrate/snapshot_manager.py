import json
import os

SNAPSHOT_DIR = "state/executions"

def save_execution_snapshot(execution_id, snapshot):
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    path = os.path.join(SNAPSHOT_DIR, f"{execution_id}.json")
    with open(path, "w") as f:
        json.dump(snapshot, f, indent=2)
