import json
import os
from capabilities.credit import credit_evaluate

SNAPSHOT_DIR = "state/executions"


def load_snapshot(execution_id):
    path = os.path.join(SNAPSHOT_DIR, f"{execution_id}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Snapshot not found: {execution_id}")

    with open(path, "r") as f:
        return json.load(f)


def replay_execution(execution_id):
    snapshot = load_snapshot(execution_id)

    if "task" not in snapshot:
        return {
            "execution_id": execution_id,
            "replayed": False,
            "error": "missing_task"
        }

    task = snapshot["task"]

    if "context" not in task or "inputs" not in task["context"]:
        return {
            "execution_id": execution_id,
            "replayed": False,
            "error": "missing_inputs"
        }

    inputs = task["context"]["inputs"]

    replay_result = credit_evaluate(inputs)

    replay_output = {
        "execution_id": execution_id,
        "result": replay_result
    }

    return {
        "execution_id": execution_id,
        "replayed": True,
        "output": replay_output,
        "original_snapshot": snapshot
    }