import json
from nacl.signing import SigningKey, VerifyKey


def canonical_bytes(data):
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    ).encode()


def generate_keys():
    sk = SigningKey.generate()
    vk = sk.verify_key
    return sk, vk


def sign_data(data, signing_key):
    message = canonical_bytes(data)
    signed = signing_key.sign(message)
    return signed.signature.hex()


def verify_signature(data, signature_hex, verify_key):
    message = canonical_bytes(data)
    signature = bytes.fromhex(signature_hex)
    verify_key.verify(message, signature)
    return True