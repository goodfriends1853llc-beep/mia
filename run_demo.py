from run_phase3_test import main as proof_demo
from run_replay_test import main as replay_demo
from run_diff_test import main as diff_demo


def main():
    print("\n=== MIA PROOF PIPELINE ===")
    proof_demo()

    print("\n=== MIA REPLAY TEST ===")
    replay_demo()

    print("\n=== MIA DIFF TEST ===")
    diff_demo()


if __name__ == "__main__":
    main()