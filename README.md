# Python-Essentials---Evaluated-Course-Project
# ER Triage Simulator

A straightforward, dual-interface tool built in Python to model emergency room queues and evaluate the operational efficiency of different scheduling policies.

It takes a randomized crowd of incoming ER patients (with varying triage severities and treatment times) and cross-checks them against active queueing algorithms to study how each policy distributes wait times and handles routine cases.

### What It Does

* **Simple Console & GUI Walkthrough:** Walks you through quick terminal prompts or web sliders to configure the patient volume and doctor rotation limits.
* **Crash-Resistant Inputs:** Handles typos, empty inputs, and invalid ranges gracefully by falling back to safe default parameters without breaking the session.
* **Tailored Filtering & Execution:** Evaluates multiple queueing algorithms simultaneously—processing Priority Triage, Doctor Rounds (Round Robin), and Quick Consults (Lottery-style).
* **Statistical Fairness Scoring:** Computes an "Unfairness Score" using standard deviation to measure how evenly wait times are distributed across patients.
* **Clean, Separated Code:** Organized into clear, focused files so you can tweak the queueing math or update the patient generation rules without touching the user interface code.

### Built With

* **Language:** Python 3.10+
* **Standard & External Libraries:** 
  * `statistics` — Computes the standard deviation for the Unfairness Score.
  * `random` — Generates dynamic patient batches and handles the randomized scheduling choice.
  * `streamlit` — Powers the interactive web dashboard frontend.
* **Version Control:** Git & GitHub.

### Project Structure

```text
er-triage-simulator/
├── patient.py          # OOP class modeling patient attributes
├── schedulers.py       # Queueing algorithms (Priority, Round Robin, Lottery)
├── simulator.py        # Core simulation engine handling patient flow
├── stats.py            # Statistical comparison and unfairness calculations
├── cli.py              # Terminal runner, menus, and user prompt handling
├── app.py              # Streamlit Web GUI dashboard
├── README.md           # Quickstart and project overview
└── statement.md        # Background on the problem and original project goals
```

# Installation & Setup

Before starting, make sure **Python 3.10+** and **Git** are installed on your computer.

> **Important:** `README.md` is only a guide. The commands shown below should be entered in the **VS Code Terminal** (`Terminal → New Terminal`), not inside the README file.

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

Make sure your terminal prompt now shows the `er-triage-simulator` folder before continuing. For example:

```text
PS C:\Users\YourName\er-triage-simulator>
```

You can also open this folder directly in VS Code using:

**File → Open Folder → er-triage-simulator**


## 3. Install the Required Dependency

With the virtual environment activated, install Streamlit:

```bash
pip install streamlit
```

The project otherwise uses Python's standard libraries such as `statistics`, `random`, `copy`, and `collections`.

# Usage Instructions

The project features a dual-interface architecture. You can run it via the terminal or the web dashboard.

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

Choose **Option 1** from the menu to initiate the simulation.

Enter your details when prompted:

* Total Number of Patients
* Doctor Rotation Quantum (hours)
* Fixed Seed (optional)

The program will then generate the patient batch, process it through all three scheduling policies and print:

* Average Wait Time
* Maximum Wait Time
* Average Turnaround Time
* Unfairness Score
* Most Equitable Policy

Choose **Option 2** anytime to view the Terminal Glossary and definitions.

## Option 2: Web Dashboard (GUI)

To start the Streamlit interface, run:

```bash
python -m streamlit run app.py
```

A local Streamlit server will start and should normally open the dashboard automatically in your browser.

Use the sidebar controls to configure the patient volume, doctor rotation time, and optional fixed scenario, then click **Process ER Queue** to run the simulation.

The Streamlit interface shows the current waiting room, the policy comparison table, and explanations of the metrics.

The program runs efficiently on both the **terminal interface** and the **Streamlit GUI**. Both interfaces use the same underlying simulation and statistics modules.

# Instructions for Testing

The following test cases can be used to verify that the application handles the main inputs and scheduling logic correctly.

## 1. Standard Execution & Metric Test

**Inputs:**

* Patients: `15`
* Quantum: `2`
* Seed: Leave blank

**Expected Output:**

Successfully generates 15 random patients, processes them through all three algorithms, and prints a summary showing Average Wait, Max Wait, Turnaround, Unfairness Score, and the Most Equitable Policy.

## 2. Fixed Seed Benchmarking Test

**Inputs:**

* Patients: `10`
* Quantum: `2`
* Seed: `42`

**Expected Output:**

Using the same seed should reproduce the same patient scenario. Running the program again with the same inputs should therefore generate the same patient data and reproducible scheduling results.

## 3. Input Validation & Error Handling Test

**Invalid Input:**

Enter:

```text
abc
```

at the patient volume prompt.

**Expected Output:**

The program should catch the invalid input using the `try/except` block, display the fallback message, and continue with the default values of 10 patients and a 2-hour quantum.

### Default Input Test

Leave the patient volume prompt blank and press **Enter**.

**Expected Output:**

The program should accept the blank input and use the default value of 10 patients.

# Screenshots

## Streamlit Web Dashboard

<img width="1906" height="967" alt="ss_guidashboard2" src="https://github.com/user-attachments/assets/0aff5ea7-2b3e-4bb4-a0af-7626f5e-abee" />

<img width="1906" height="967" alt="ss_guidashboard2" src="https://github.com/user-attachments/assets/40b4e4af-3208-4232-be38-d10071687906" />

## Terminal / CLI Output

<img width="1226" height="987" alt="ss_terminaldashboard" src="https://github.com/user-attachments/assets/8cbb0f38-6e34-470c-85a1-24ea202e7765" />

# Notes

* The patient scenarios are generated dynamically using Python's randomization functions.
* A fixed seed can be used when a repeatable scenario is required.
* The project does not require a database or any external data files.
* The Streamlit dashboard is intended to provide a more visual way of running and comparing the simulations, while the CLI provides a lightweight terminal-based alternative.
