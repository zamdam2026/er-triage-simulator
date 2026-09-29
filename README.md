# Python-Essentials---Evaluated-Course-Project
# ER Triage Simulator

A straightforward, dual-interface tool built in Python to model emergency room queues and evaluate the operational efficiency of different scheduling policies.

It takes a randomized crowd of incoming ER patients, with varying triage severities and treatment times, and cross-checks them against different queueing algorithms to study how each policy affects patient waiting time, turnaround time, and fairness.

## What It Does

* **Simple Console & GUI Walkthrough:** Walks you through quick terminal prompts or a web dashboard to configure the patient volume and doctor rotation limits.
* **Crash-Resistant Inputs:** Handles invalid inputs gracefully by falling back to safe default parameters instead of breaking the session.
* **Multiple Scheduling Policies:** Evaluates three queueing approaches simultaneously — Priority Triage, Doctor Rounds (Round Robin), and Quick Consults.
* **Statistical Fairness Scoring:** Computes an "Unfairness Score" using standard deviation to measure how evenly waiting time is distributed among patients.
* **Clean, Separated Code:** Organized into clear, focused files so the queueing logic, patient generation and user interfaces can be worked on separately.

## Built With

* **Language:** Python 3.10+
* **Standard & External Libraries:**
  * `statistics` — Used for calculating the standard deviation for the Unfairness Score.
  * `random` — Used to generate different patient scenarios and randomized scheduling choices.
  * `streamlit` — Used to build the interactive web dashboard.
* **Version Control:** Git & GitHub.

## Project Structure

```text
er-triage-simulator/
├── patient.py          # OOP class used to model patient information
├── schedulers.py       # Scheduling algorithms (Priority, Round Robin, Lottery)
├── simulator.py        # Core simulation engine
├── stats.py            # Statistical calculations and policy comparison
├── cli.py              # Terminal runner and user prompts
├── app.py              # Streamlit web dashboard
├── README.md           # Project overview and setup instructions
└── statement.md        # Problem statement and project goals
```

# Installation & Setup

Before starting, make sure that **Python 3.10+** and **Git** are installed on your computer.

>
> Open the project in **VS Code**, then open **Terminal → New Terminal** and enter the commands shown below.

## 1. Clone the Repository

Open the VS Code terminal and run:

```bash
git clone https://github.com/zamdam2026/er-triage-simulator.git
```

## 2. Navigate to the Project Folder

Move into the project directory:

```bash
cd er-triage-simulator
```

You can also open the folder directly in VS Code using:

**File → Open Folder → er-triage-simulator**

## 3. Create a Virtual Environment

Create a separate Python environment for the project:

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows PowerShell

Run:

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal should show something similar to:

```text
(venv) PS C:\...\er-triage-simulator>
```

This means the virtual environment is active.

### If PowerShell blocks the activation script

On some Windows systems, PowerShell may prevent the activation script from running.

In that case, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Press `Y` when prompted.

Then activate the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install the Required Dependency

With the virtual environment activated, install Streamlit:

```bash
pip install streamlit
```

The other libraries used by the project, such as `random`, `statistics`, `copy` and `collections`, are part of Python's standard library.

# Usage Instructions

The project has a dual-interface architecture. The same core simulation is available through:

1. **Terminal Mode (CLI)**
2. **Web Dashboard (Streamlit)**

Both interfaces use the same underlying simulation, scheduling and statistical-analysis modules.

## Option 1: Terminal Mode (CLI)

Make sure the virtual environment is active and run:

```bash
python cli.py
```

A menu will appear:

```text
🏥 ER TRIAGE SIMULATOR: TERMINAL MODE

1. Run ER Simulation
2. View Terminal Glossary & Definitions
3. Exit
```

Choose **Option 1** to start the simulation.

You will then be asked for:

* Total Number of Patients
* Doctor Rotation Quantum (hours)
* Fixed Seed (optional)

The program will generate the patient batch, run all three scheduling policies and display:

* Average Wait Time
* Maximum Wait Time
* Average Turnaround Time
* Unfairness Score
* Most Equitable Policy

Choose **Option 2** anytime to view the Terminal Glossary and definitions of the terms used in the simulation.

## Option 2: Web Dashboard (GUI)

To start the Streamlit version, run:

```bash
python -m streamlit run app.py
```

A local Streamlit server will start and a browser window should normally open automatically.

The web dashboard allows you to:

* Set the total number of patients.
* Set the doctor rotation time.
* Enable a fixed scenario using a Scenario ID.
* View the generated waiting-room data.
* Run all three scheduling policies.
* Compare the resulting performance metrics.

The application runs efficiently in both the **terminal interface** and the **Streamlit web interface**. Both interfaces use the same core simulation and statistical-analysis modules, so the main scheduling logic remains consistent between them.

# Quick Start

For Windows users, after opening the VS Code terminal, the setup can be completed using:

```bash
git clone https://github.com/zamdam2026/er-triage-simulator.git
cd er-triage-simulator
python -m venv venv
```

Then activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell gives an execution-policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

and then activate the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

Install Streamlit:

```bash
pip install streamlit
```

After installation, choose either of the following:

### Run the Terminal Version

```bash
python cli.py
```

### Run the Streamlit Version

```bash
python -m streamlit run app.py
```

# Instructions for Testing

The following test cases can be used to verify that the application handles the main inputs and scheduling logic correctly.

## 1. Standard Execution & Metric Test

**Input:**

* Patients: `15`
* Quantum: `2`
* Seed: Leave blank

**Expected Output:**

The program should successfully generate 15 patients, process them through all three scheduling policies and display the calculated:

* Average Wait
* Maximum Wait
* Average Turnaround
* Unfairness Score
* Most Equitable Policy

## 2. Fixed Seed Benchmarking Test

**Input:**

* Patients: `10`
* Quantum: `2`
* Seed: `42`

**Expected Output:**

Using the same seed should reproduce the same generated patient scenario. Running the program again with the same inputs should therefore produce the same random patient data and reproducible scheduling results.

This is useful when comparing the three policies under exactly the same starting conditions.

## 3. Input Validation & Error Handling Test

**Invalid Input:**

Enter:

```text
abc
```

at the patient volume prompt.

**Expected Output:**

The program should catch the invalid input using the `try/except` block and display a fallback message similar to:

```text
Invalid input detected. Falling back to default values (10 patients, 2h quantum).
```

The simulation should then continue using the default values.

### Default Input Test

Leave the patient volume prompt blank and press **Enter**.

**Expected Output:**

The program should accept the blank input and use the default value of:

```text
10 patients
```

The same default-input behavior applies to the doctor rotation quantum when the input is left blank.

# Screenshots

## Streamlit Web Dashboard

<img width="1906" height="967" alt="ss_guidashboard1" src="https://github.com/user-attachments/assets/0aff5ea7-2b3e-4bb4-a0af-7626f5e-abee" />

<img width="1906" height="967" alt="ss_guidashboard2" src="https://github.com/user-attachments/assets/40b4e4af-3208-4232-be38-d10071687906" />

## Terminal / CLI Output

<img width="1226" height="987" alt="ss_terminaldashboard" src="https://github.com/user-attachments/assets/8cbb0f38-6e34-470c-85a1-24ea202e7765" />

# Notes

* The patient scenarios are generated dynamically using Python's randomization functions.
* A fixed seed can be used when a repeatable scenario is required.
* The project does not require a database or any external data files.
* The Streamlit dashboard is intended to provide a more visual way of running and comparing the simulations, while the CLI provides a lightweight terminal-based alternative.
