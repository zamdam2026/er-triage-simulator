
import statistics

def summarize(jobs):
    # Collect wait times and turnarounds
    waits = [job.wait_time for job in jobs]
    turnarounds = [job.turnaround_time for job in jobs]
    
    return {
        "avg_wait": round(statistics.mean(waits), 2),
        "max_wait": round(max(waits), 2),
        "avg_turnaround": round(statistics.mean(turnarounds), 2),
        "unfairness": round(statistics.pstdev(waits), 2),
    }


def compare(jobs_by_policy):
    # Map each policy to its summary
    out = {}
    
    for policy, jobs in jobs_by_policy.items():
        out[policy] = summarize(jobs)
    
    return out


def best_by(policy_results, metric="unfairness"):
    # Find best policy based on the given metric
    best = None
    best_val = None
    
    for policy in policy_results:
        val = policy_results[policy][metric]
        if best is None or val < policy_results[best][metric]:
            best = policy
            best_val = val
    
    return best
