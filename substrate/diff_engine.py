import json
import os

SNAPSHOT_DIR = "state/executions"


def load_snapshot(execution_id):
    path = os.path.join(SNAPSHOT_DIR, f"{execution_id}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Snapshot not found: {execution_id}")

    with open(path, "r") as f:
        return json.load(f)


def diff_dict(a, b):
    differences = {}
    all_keys = set(a.keys()) | set(b.keys())

    for key in all_keys:
        av = a.get(key)
        bv = b.get(key)

        if av != bv:
            differences[key] = {
                "a": av,
                "b": bv
            }

    return differences


def classify_difference(snapshot_a, snapshot_b):
    task_a = snapshot_a.get("task", {})
    task_b = snapshot_b.get("task", {})

    output_a = snapshot_a.get("output", {})
    output_b = snapshot_b.get("output", {})

    input_a = task_a.get("context", {}).get("inputs", {})
    input_b = task_b.get("context", {}).get("inputs", {})

    input_diff = diff_dict(input_a, input_b)
    output_diff = diff_dict(output_a.get("result", {}), output_b.get("result", {}))

    if input_diff and output_diff:
        category = "input_changed"
    elif not input_diff and output_diff:
        category = "output_changed"
    elif input_diff and not output_diff:
        category = "input_changed_but_output_same"
    else:
        category = "no_difference"

    return {
        "category": category,
        "input_diff": input_diff,
        "output_diff": output_diff
    }


def diff_executions(execution_id_a, execution_id_b):
    snapshot_a = load_snapshot(execution_id_a)
    snapshot_b = load_snapshot(execution_id_b)

    classification = classify_difference(snapshot_a, snapshot_b)

    return {
        "execution_a": execution_id_a,
        "execution_b": execution_id_b,
        "match": classification["category"] == "no_difference",
        "category": classification["category"],
        "input_diff": classification["input_diff"],
        "output_diff": classification["output_diff"]
    }