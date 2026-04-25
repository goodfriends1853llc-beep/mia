import json
import os

SNAPSHOT_DIR = "state/executions"

def verify_execution_snapshot(execution_id):
    path = os.path.join(SNAPSHOT_DIR, f"{execution_id}.json")
    if not os.path.exists(path):
        return {"verified": False, "error": "missing"}
    with open(path) as f:
        snapshot = json.load(f)
    if "seal" not in snapshot:
        return {"verified": False, "error": "no_seal"}
    return {"verified": True}
