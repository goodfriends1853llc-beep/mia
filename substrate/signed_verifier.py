from substrate.verifier import verify_package_file
from substrate.identity import get_verifier
from substrate.crypto import sign_data


def signed_verify(package_path, verifier_id):
    base_result = verify_package_file(package_path, verifier_id)
    identity = get_verifier(verifier_id)

    signable = {
        "execution_id": base_result["execution_id"],
        "verifier_id": base_result["verifier_id"],
        "verified": base_result["verified"],
        "seal_valid": base_result["seal_valid"],
        "errors": base_result["errors"]
    }

    required_keys = {"execution_id", "verifier_id", "verified", "seal_valid", "errors"}
    assert set(signable.keys()) == required_keys

    signature = sign_data(signable, identity["signing_key"])

    return {
        **signable,
        "signature": signature,
        "public_key_id": verifier_id
    }