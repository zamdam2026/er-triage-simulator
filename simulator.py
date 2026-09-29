import copy
import random

from patient import Patient
from schedulers import RoundRobinScheduler, PriorityScheduler, LotteryScheduler

PATIENT_NAMES = ["Aarav", "Priya", "Rahul", "Ananya", "Vikram", "Sneha", "Karan", "Meera"]

def generate_patients(n=10, seed=None):
    # Setup random for reproducibility
    rand = random.Random(seed) if seed else random
    
    cases = []
    
    for i in range(1, n + 1):
        treatment = rand.randint(1, 8)
        level = rand.randint(1, 3)
        name = rand.choice(PATIENT_NAMES)
        
        # All arrive at time 0 for batch
        p = Patient(i, name, treatment, level, arr_time=0.0)
        cases.append(p)
    
    return cases


def run_all(cases, q=2, seed=None):
    # Dict of scheduler configurations
    policies = {
        "Doctor Rounds": RoundRobinScheduler(quantum_hours=q),
        "Triage Protocol": PriorityScheduler(),
        "Quick Consults": LotteryScheduler(seed=seed),
    }
    
    outcomes = {}
    
    for policy_name, scheduler in policies.items():
        # Need fresh state, deepcopy avoids cross-contamination
        working = copy.deepcopy(cases)
        scheduler.run(working)
        outcomes[policy_name] = working
    
    return outcomes
