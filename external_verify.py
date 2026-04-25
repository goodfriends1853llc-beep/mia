import json
import hashlib
from nacl.signing import VerifyKey
from substrate.crypto import canonical_bytes, verify_signature


def verify_seal(snapshot):
    if "seal" not in snapshot:
        return False, "missing_seal"

    stored_hash = snapshot["seal"].get("hash")

    core_snapshot = dict(snapshot)
    core_snapshot.pop("seal", None)

    recomputed_hash = hashlib.sha256(canonical_bytes(core_snapshot)).hexdigest()

    if stored_hash != recomputed_hash:
        return False, "seal_hash_mismatch"

    return True, None


def verify_public_key_map(public_keys):
    return {item["verifier_id"]: item["public_key"] for item in public_keys}


def verify_verifier_signature(verifier_result, public_key_hex):
    verify_key = VerifyKey(bytes.fromhex(public_key_hex))

    signature = verifier_result.get("signature")
    if signature is None:
        return False, "missing_signature"

    signable = {
        "execution_id": verifier_result["execution_id"],
        "verifier_id": verifier_result["verifier_id"],
        "verified": verifier_result["verified"],
        "seal_valid": verifier_result["seal_valid"],
        "errors": verifier_result["errors"]
    }

    required_keys = {"execution_id", "verifier_id", "verified", "seal_valid", "errors"}
    assert set(signable.keys()) == required_keys

    try:
        verify_signature(signable, signature, verify_key)
        return True, None
    except Exception:
        return False, "signature_invalid"


def verify_consensus(consensus, verifier_results):
    accept_count = sum(1 for r in verifier_results if r["verified"])
    reject_count = sum(1 for r in verifier_results if not r["verified"])

    if accept_count >= 2:
        expected = "ACCEPTED"
    elif reject_count >= 2:
        expected = "REJECTED"
    else:
        expected = "DISPUTED"

    if consensus.get("consensus") != expected:
        return False, "consensus_mismatch"

    return True, None


def external_verify(proof_path):
    with open(proof_path, "r") as f:
        proof = json.load(f)

    errors = []

    execution_id = proof.get("execution_id")
    snapshot = proof.get("snapshot")
    verifier_results = proof.get("verifier_results", [])
    public_keys = proof.get("public_keys", [])
    consensus = proof.get("consensus", {})

    if not execution_id:
        errors.append("missing_execution_id")

    if snapshot is None:
        errors.append("missing_snapshot")
    else:
        seal_ok, seal_error = verify_seal(snapshot)
        if not seal_ok:
            errors.append(seal_error)

    public_key_map = verify_public_key_map(public_keys)

    for result in verifier_results:
        verifier_id = result.get("verifier_id")
        if verifier_id not in public_key_map:
            errors.append(f"missing_public_key:{verifier_id}")
            continue

        sig_ok, sig_error = verify_verifier_signature(result, public_key_map[verifier_id])
        if not sig_ok:
            errors.append(f"{verifier_id}:{sig_error}")

    consensus_ok, consensus_error = verify_consensus(consensus, verifier_results)
    if not consensus_ok:
        errors.append(consensus_error)

    return {
        "execution_id": execution_id,
        "verified": len(errors) == 0,
        "errors": errors
    }