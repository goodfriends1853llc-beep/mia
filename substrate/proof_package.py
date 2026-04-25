import json
import os
from substrate.package import load_snapshot

PROOF_DIR = "proofs"


def build_proof_package(execution_id, verifier_results, public_keys, consensus):
    snapshot = load_snapshot(execution_id)

    proof = {
        "execution_id": execution_id,
        "snapshot": snapshot,
        "verifier_results": verifier_results,
        "public_keys": public_keys,
        "consensus": consensus
    }

    required_keys = {
        "execution_id",
        "snapshot",
        "verifier_results",
        "public_keys",
        "consensus"
    }
    assert set(proof.keys()) == required_keys

    return proof


def export_proof_package(execution_id, verifier_results, public_keys, consensus):
    os.makedirs(PROOF_DIR, exist_ok=True)

    proof = build_proof_package(execution_id, verifier_results, public_keys, consensus)
    path = os.path.join(PROOF_DIR, f"{execution_id}_proof.json")

    with open(path, "w") as f:
        json.dump(proof, f, indent=2)

    return path