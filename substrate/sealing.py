import hashlib
from substrate.crypto import canonical_bytes


def seal_snapshot(snapshot):
    core_snapshot = dict(snapshot)

    if "seal" in core_snapshot:
        del core_snapshot["seal"]

    h = hashlib.sha256(canonical_bytes(core_snapshot)).hexdigest()

    sealed = dict(core_snapshot)
    sealed["seal"] = {
        "hash": h
    }

    return sealed


def verify_seal(snapshot):
    if "seal" not in snapshot:
        return False

    provided_hash = snapshot["seal"].get("hash")

    core_snapshot = dict(snapshot)
    del core_snapshot["seal"]

    computed_hash = hashlib.sha256(canonical_bytes(core_snapshot)).hexdigest()

    return provided_hash == computed_hash