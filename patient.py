class Patient:
    def __init__(self, pid, name, est_hours, level, arr_time=0.0):
        
        #mapping of patient attributes
        self.patient_id = pid
        self.patient_name = name
        self.estimated_hours = est_hours
        self.triage_level = level
        self.arrival_time = arr_time
        
        #simulation counter
        self.wait_time = 0.0
        self.turnaround_time = 0.0
        self.remaining_time = est_hours