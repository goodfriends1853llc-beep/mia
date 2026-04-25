from run_mia import run
from substrate.replay_engine import replay_execution
from substrate.replay_compare import compare_replay_to_snapshot


def main():
    case = {
        "task_id": "replay_test",
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
    execution_id = r["execution_id"]

    replay_data = replay_execution(execution_id)
    comparison = compare_replay_to_snapshot(replay_data)

    print("RUN:", r)
    print("REPLAY:", replay_data)
    print("COMPARISON:", comparison)


if __name__ == "__main__":
    main()