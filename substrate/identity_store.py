import json
import os
from nacl.signing import SigningKey

KEY_DIR = "keys"
KEY_FILE = os.path.join(KEY_DIR, "keys.json")


def load_or_create_keys():
    os.makedirs(KEY_DIR, exist_ok=True)

    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            return json.load(f)

    keys = {}

    for vid in ["v1", "v2", "v3"]:
        sk = SigningKey.generate()
        vk = sk.verify_key

        keys[vid] = {
            "private_key": sk.encode().hex(),
            "public_key": vk.encode().hex()
        }

    with open(KEY_FILE, "w") as f:
        json.dump(keys, f, indent=2)

    return keys


def get_signing_key(verifier_id):
    keys = load_or_create_keys()
    return SigningKey(bytes.fromhex(keys[verifier_id]["private_key"]))


def get_public_key(verifier_id):
    keys = load_or_create_keys()
    return keys[verifier_id]["public_key"]