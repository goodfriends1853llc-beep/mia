from run_mia import run
from substrate.diff_engine import diff_executions


def main():
    case_a = {
        "task_id": "diff_test_a",
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

    case_b = {
        "task_id": "diff_test_b",
        "context": {
            "inputs": {
                "monthly_revenue": 12000,
                "months_in_business": 12,
                "existing_debt": 15000,
                "avg_bank_balance": 3000,
                "requested_amount": 10000
            }
        }
    }

    run_a = run(case_a)
    run_b = run(case_b)

    execution_id_a = run_a["execution_id"]
    execution_id_b = run_b["execution_id"]

    diff_result = diff_executions(execution_id_a, execution_id_b)

    print("RUN A:", run_a)
    print("RUN B:", run_b)
    print("DIFF:", diff_result)


if __name__ == "__main__":
    main()