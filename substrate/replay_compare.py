def compare_outputs(original_output, replay_output):
    if original_output == replay_output:
        return {
            "match": True,
            "differences": {}
        }

    differences = {}

    original_result = original_output.get("result", {})
    replay_result = replay_output.get("result", {})

    all_keys = set(original_result.keys()) | set(replay_result.keys())

    for key in all_keys:
        if original_result.get(key) != replay_result.get(key):
            differences[key] = {
                "original": original_result.get(key),
                "replay": replay_result.get(key)
            }

    return {
        "match": False,
        "differences": differences
    }


def compare_replay_to_snapshot(replay_data):
    if not replay_data.get("replayed"):
        return {
            "execution_id": replay_data.get("execution_id"),
            "verified": False,
            "error": replay_data.get("error", "replay_failed")
        }

    snapshot = replay_data["original_snapshot"]

    if "output" not in snapshot:
        return {
            "execution_id": replay_data["execution_id"],
            "verified": False,
            "error": "missing_original_output"
        }

    original_output = snapshot["output"]
    replay_output = replay_data["output"]

    comparison = compare_outputs(original_output, replay_output)

    return {
        "execution_id": replay_data["execution_id"],
        "verified": comparison["match"],
        "differences": comparison["differences"]
    }