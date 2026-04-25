from run_mia import run
from substrate.package import export_execution_package
from substrate.signed_verifier import signed_verify
from substrate.consensus import consensus_verdict
from substrate.public_keys import export_public_keys
from substrate.proof_package import export_proof_package
from external_verify import external_verify


def main():
    case = {
        "task_id": "final_identity_test",
        "context": {
            "inputs": {
                "monthly_revenue": 25000,
                "months_in_business": 36,
                "existing_debt": 5000,
                "avg_bank_balance": 20000,
                "requested_amount": 10000
            }
        }
    }

    r = run(case)
    print("RUN:", r)

    execution_id = r["execution_id"]
    package_path = export_execution_package(execution_id)

    sv1 = signed_verify(package_path, "v1")
    sv2 = signed_verify(package_path, "v2")
    sv3 = signed_verify(package_path, "v3")

    verifier_results = [sv1, sv2, sv3]
    consensus = consensus_verdict(verifier_results)

    print("SV1:", sv1)
    print("CONSENSUS:", consensus)

    public_key_paths = export_public_keys(["v1", "v2", "v3"])

    proof_path = export_proof_package(
        execution_id,
        verifier_results,
        public_key_paths,
        consensus
    )

    print("PROOF:", proof_path)

    result = external_verify(proof_path)
    print("RESULT:", result)


if __name__ == "__main__":
    main()