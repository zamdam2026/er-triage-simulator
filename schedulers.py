import random
from collections import deque
class PriorityScheduler:
    def run(self, patients):
        #sorting using triage seq.(1 is crucial)followed by shortest treatment time
        queue = sorted(patients, key=lambda x: (x.triage_level, x.estimated_hours))
        current_time = 0
        
        for p in queue:
            p.wait_time = current_time
            current_time += p.estimated_hours
            p.turnaround_time = current_time

class RoundRobinScheduler:
    def __init__(self, quantum_hours=2):
        self.quantum_hours = quantum_hours

    def run(self, patients):
        #setup tracking variables for the loop
        for p in patients:
            p.remaining_time = p.estimated_hours
            p.wait_time = 0
            
        queue = deque(patients)
        current_time = 0
        last_seen = {p.patient_id: 0 for p in patients}

        #ensuring time left reached 0 so tht loop eventually breaks
        while queue:
            p = queue.popleft()
            
            # Add the time they were sitting in the lobby since the doctor last saw them
            p.wait_time += (current_time - last_seen[p.patient_id])
            
            if p.remaining_time > self.quantum_hours:
                # Doctor treats them for the max rotation time, but they still need more
                current_time += self.quantum_hours
                p.remaining_time -= self.quantum_hours
                last_seen[p.patient_id] = current_time
                queue.append(p) # Put them back in line
            else:
                #doc finsihing his duty the earliest
                current_time += p.remaining_time
                p.remaining_time = 0
                p.turnaround_time = current_time
                #end of loop, no append
class LotteryScheduler:
    def __init__(self, seed=None):
        self.seed = seed

    def run(self, patients):
        if self.seed is not None:
            random.seed(self.seed)
            
        queue = patients.copy()
        current_time = 0
        
        while queue:
            #favors shorter arrends but slightly random
            queue.sort(key=lambda x: x.estimated_hours)
            #picking 1 out of 3 least crucial plateints to clear lobby
            pool_size = min(3, len(queue))
            winner_index = random.randint(0, pool_size - 1)
            winner = queue.pop(winner_index)
            
            winner.wait_time = current_time
            current_time += winner.estimated_hours
            winner.turnaround_time = current_time

