import json
import hashlib


def stable(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def verify_package_file(package_path, verifier_id="verifier_1"):
    with open(package_path, "r") as f:
        package = json.load(f)

    errors = []

    if "execution_id" not in package:
        errors.append("missing_execution_id")

    if "snapshot" not in package:
        errors.append("missing_snapshot")
        return {
            "verifier_id": verifier_id,
            "verified": False,
            "errors": errors
        }

    snapshot = package["snapshot"]

    if "seal" not in snapshot:
        errors.append("missing_seal")
    else:
        stored_hash = snapshot["seal"].get("hash")
        core_snapshot = dict(snapshot)
        core_snapshot.pop("seal", None)
        recomputed_hash = hashlib.sha256(stable(core_snapshot).encode()).hexdigest()

        if stored_hash != recomputed_hash:
            errors.append("seal_hash_mismatch")

    if "output" not in snapshot:
        errors.append("missing_output")

    if "execution_id" not in snapshot:
        errors.append("snapshot_missing_execution_id")
    elif snapshot["execution_id"] != package["execution_id"]:
        errors.append("execution_id_mismatch")

    verified = len(errors) == 0

    return {
        "execution_id": package.get("execution_id"),
        "verifier_id": verifier_id,
        "verified": verified,
        "seal_valid": "seal_hash_mismatch" not in errors and "missing_seal" not in errors,
        "errors": errors
    }