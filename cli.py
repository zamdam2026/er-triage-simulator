"""
cli.py
Command Line Interface (Terminal Mode) for the ER Triage Simulator.
Includes built-in terminal descriptions and glossary for evaluation.
"""

from simulator import generate_patients, run_all
from stats import compare, best_by

def show_glossary():
    print("\n========================================")
    print("📖 ER TRIAGE TERMINAL GLOSSARY")
    print("========================================")
    print("• Doctor Rotation Quantum (q):")
    print("  The time limit a doctor spends on a patient during")
    print("  the Doctor Rounds policy before rotating.")
    print("")
    print("• Unfairness Score (Standard Deviation):")
    print("  Measures wait-time disparity. A low score means everyone")
    print("  waited fairly; a high score means some waited hours longer.")
    print("")
    print("• Priority Protocol:")
    print("  Medical-first triage where critical trauma patients go first.")
    print("")
    print("• Doctor Rounds:")
    print("  Time-shared rotation (Round Robin) cycling through patients.")
    print("")
    print("• Quick Consults:")
    print("  Shortest-job-first or lottery-style consultation strategy.")
    print("========================================")

def run_simulation():
    try:
        n_input = input("Enter total number of patients [default 10]: ").strip()
        num_patients = int(n_input) if n_input else 10
        
        q_input = input("Enter doctor rotation quantum hours [default 2]: ").strip()
        quantum = int(q_input) if q_input else 2
        
        seed_input = input("Enter fixed seed (optional, press Enter for random): ").strip()
        seed = int(seed_input) if seed_input else None
        
    except ValueError:
        print("Invalid input detected. Falling back to default values (10 patients, 2h quantum).")
        num_patients, quantum, seed = 10, 2, None

    print(f"\n[+] Generating batch of {num_patients} ER patients...")
    patients = generate_patients(num_patients, seed=seed)
    
    print("[+] Executing simulation across scheduling policies...")
    results = run_all(patients, q=quantum, seed=seed)
    
    print("[+] Computing statistical metrics and unfairness scores...")
    metrics = compare(results)
    best_policy = best_by(metrics, metric="unfairness")

    print("\n----------------------------------------")
    print("📊 SIMULATION RESULTS SUMMARY")
    print("----------------------------------------")
    for policy_name, stats_dict in metrics.items():
        print(f"Policy: {policy_name}")
        print(f"  - Average Wait Time: {stats_dict['avg_wait']} hrs")
        print(f"  - Maximum Wait Time: {stats_dict['max_wait']} hrs")
        print(f"  - Average Turnaround: {stats_dict['avg_turnaround']} hrs")
        print(f"  - Unfairness Score (StdDev): {stats_dict['unfairness']}")
        print("-" * 40)

    print(f"\n🏆 Most Equitable Policy: {best_policy}")
    print("========================================")

def main():
    while True:
        print("\n========================================")
        print("🏥 ER TRIAGE SIMULATOR: TERMINAL MODE")
        print("========================================")
        print("1. Run ER Simulation")
        print("2. View Terminal Glossary & Definitions")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            run_simulation()
        elif choice == "2":
            show_glossary()
        elif choice == "3":
            print("\nExiting Terminal Mode. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()