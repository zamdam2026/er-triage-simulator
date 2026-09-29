# Python-Essentials---Evaluated-Course-Project
#                                                        ER Triage Simulator

A straightforward, dual-interface tool built in Python to model emergency room queues and evaluate the operational efficiency of different scheduling policies. 
It takes a randomized crowd of incoming ER patients (with varying triage severities and treatment times) and cross-checks them against active queueing algorithms to surface which policy distributes wait times most fairly without neglecting routine cases.

### What It Does

* **Simple Console & GUI Walkthrough:** Walks you through quick terminal prompts or web sliders to configure the patient volume and doctor rotation limits.
* **Crash-Resistant Inputs:** Handles typos, empty inputs, and invalid ranges gracefully by falling back to safe default parameters without breaking the session.
* **Tailored Filtering & Execution:** Evaluates multiple queueing algorithms simultaneously—processing Priority Triage, Doctor Rounds (Round Robin), and Quick Consults (Shortest Job First).
* **Statistical Fairness Scoring:** Computes an "Unfairness Score" using standard deviation to mathematically prove which policy is the most equitable for all patients.
* **Clean, Separated Code:** Organized into clear, focused files so you can tweak the queueing math or update the patient generation rules without touching the user interface code.

### Built With

* **Language:** Python 3.10+
* **Standard & External Libraries:** 
  * `statistics` — Computes the standard deviation for the Unfairness Score;
  * `random` — Generates dynamic, realistic patient batches;
  * `streamlit` — Powers the interactive web dashboard frontend.
* **Version Control:** Git & GitHub.

### Project Structure

```text
print-queue-diplomat/
├── patient.py          # OOP classes modeling patient attributes and severity states
├── schedulers.py       # Queueing algorithms (Priority, Round Robin, Lottery)
├── simulator.py        # Core simulation engine handling patient flow
├── stats.py            # Mathematical variance and unfairness calculators
├── cli.py              # Terminal runner, menus, and user prompt handling
├── app.py              # Streamlit Web GUI dashboard
├── README.md           # Quickstart and overview
└── statement.md        # Background on the problem and original project goals
```
# Installation & Setup

Clone the Repository:

**Bash**

_git clone_

[https://github.com/zamdam2026/er-triage-simulator.git](https://github.com/zamdam2026/er-triage-simulator.git)
cd er-triage-simulator
Initialize and Activate the Virtual Environment:

**Bash**

python -m venv venv

.\venv\Scripts\Activate.ps1

_Install Dependencies:_

*Make sure you have the required UI framework installed:*

**Bash**

pip install streamlit

**Usage Instructions**

The project features a dual-interface architecture. You can run it via the terminal or the web.

**Option 1: Terminal Mode (CLI)**

Run python cli.py in your terminal.

Choose Option 1 from the menu to initiate the simulation.

Enter your details when prompted:

Total Number of Patients

Doctor Rotation Quantum (hours)

Fixed Seed (optional)

View the comparative metrics, wait times, and winning policy printed directly on the console.

Choose Option 2 anytime to view the Terminal Glossary of terms.


**Option 2: Web Dashboard (GUI)**

Run python -m streamlit run app.py in your terminal.

A local server URL will generate, automatically opening the dashboard in your browser.

Use the sidebar sliders to configure your patient volume and execute the simulation visually.

Instructions for Testing
To verify that the application handles inputs and algorithms properly, test these cases manually via the CLI (python cli.py):

1. Standard Execution & Metric Test

Inputs: Patients: 15, Quantum: 2, Seed: [Leave Blank]

Expected Output: Successfully generates 15 random patients, processes them through all three algorithms, and prints a summary table showing Average Wait, Max Wait, Turnaround, and the winning "Most Equitable Policy" based on the lowest Unfairness Score.

2. Fixed Seed Benchmarking Test

Inputs: Patients: 10, Quantum: 2, Seed: 42

Expected Output: Locks the pseudo-random generator. If you run the program three times in a row with seed 42, it will consistently generate the exact same patient roster and yield identical wait-time results for accurate algorithm comparison.

3. Input Validation & Error Handling Test

Invalid Input: Enter abc or hit Enter (blank) at the patient volume prompt.

Expected Output: Intercepted by a try/except block. Program displays "Invalid input detected. Falling back to default values..." and successfully runs a 10-patient simulation without crashing.

Screenshots

<img width="1906" height="967" alt="ss_guidashboard2" src="https://github.com/user-attachments/assets/0aff5ea7-2b3e-4bb2-8db0-4a0af762eabe" />
<img width="1906" height="967" alt="ss_guidashboard2" src="https://github.com/user-attachments/assets/40b4e4af-3208-4232-be38-d10071687906" />
<img width="1226" height="987" alt="ss_terminaldashboard" src="https://github.com/user-attachments/assets/8cbb0f38-6e34-470c-85a1-24ea202e7765" />



