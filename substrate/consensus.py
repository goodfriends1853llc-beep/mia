def consensus_verdict(results):
    accept_count = sum(1 for r in results if r["verified"])
    reject_count = sum(1 for r in results if not r["verified"])

    if accept_count >= 2:
        consensus = "ACCEPTED"
    elif reject_count >= 2:
        consensus = "REJECTED"
    else:
        consensus = "DISPUTED"

    execution_id = results[0]["execution_id"] if results else None

    consensus_result = {
        "execution_id": execution_id,
        "consensus": consensus,
        "rule": "2_of_3",
        "accept_count": accept_count,
        "reject_count": reject_count,
        "results": results
    }

    required_keys = {
        "execution_id",
        "consensus",
        "rule",
        "accept_count",
        "reject_count",
        "results"
    }
    assert set(consensus_result.keys()) == required_keys

    return consensus_result