import json
import os
from substrate.identity_store import get_public_key

PUBLIC_KEY_DIR = "public_keys"


def export_public_keys(verifier_ids):
    os.makedirs(PUBLIC_KEY_DIR, exist_ok=True)

    exported = []

    for vid in verifier_ids:
        public_key = get_public_key(vid)

        artifact = {
            "verifier_id": vid,
            "public_key": public_key
        }

        path = os.path.join(PUBLIC_KEY_DIR, f"{vid}_public.json")

        with open(path, "w") as f:
            json.dump(artifact, f, indent=2)

        exported.append(artifact)

    return exported