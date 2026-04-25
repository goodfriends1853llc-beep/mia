from substrate.identity_store import get_signing_key, get_public_key

verifiers = {}


def create_verifier(verifier_id):
    verifier = {
        "verifier_id": verifier_id,
        "signing_key": get_signing_key(verifier_id),
        "public_key": get_public_key(verifier_id)
    }
    verifiers[verifier_id] = verifier
    return verifier


def get_verifier(verifier_id):
    if verifier_id not in verifiers:
        return create_verifier(verifier_id)
    return verifiers[verifier_id]