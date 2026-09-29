# Project Statement: ER Triage Simulator

## Problem Statement
Emergency rooms (ERs) are experiencing a serious problem with overcrowding. In conventional waiting areas rigid rules for sorting patients are used—those who are most critical are given priority. Although this is necessary for saving lives, it usually causes stable patients who are in pain (for example, those with broken bones or deep cuts) to have to wait in the lobby for 12 or more hours. At present, hospital managers do not have easy, risk-free means by which to try out new strategies for the waiting room. They need a method of working out how to assign doctors more efficiently without having to carry out experiments on real patients during a shift.

### Why It Matters
When an emergency room bottlenecks, the consequences are severe: patients walk out without receiving care, nurses suffer from extreme burnout, and hospital resources are wasted. Finding the perfect balance between treating critical emergencies and clearing routine cases isn't just an administrative task—it is a matter of public health. This simulator matters because it gives hospitals a mathematical, risk-free sandbox to optimize their waiting rooms. By proving which scheduling policies work best on a computer, hospitals can drastically reduce wait times and improve patient care in the real world.

## Scope of the Project
The ER Triage Simulator functions as a digital environment in which to test hospital operations. Rather than employing actual medical data, the software creates a virtual waiting room containing randomly generated patients. It enables users to go through these imaginary patients using different doctor-assignment rules (for example, 'Critical First' as opposed to 'Quickest Fix First') in order to prove by mathematical means which approach clears the lobby most quickly while ensuring that the wait times are fair for all. 

## Target Users
* Hospital administrators and operations managers: Individuals who wish to improve their staff scheduling and decrease the number of patients leaving due to long waiting times.
* Students in the field of healthcare policy: Those who study the effect of various triage systems on hospital efficiency.
* **Assessors and Teachers:** The people who evaluate the project with regard to its modular software design, user-friendly interfaces, and logical data processing.

## High-Level Features
1. **Virtual Patient Generator:** Is able to automatically generate a realistic number of incoming patients, each with randomly assigned levels of severity and an estimated time for treatment.
2. **Smart Sorting Algorithms:** The algorithms test various waiting room rules at the same time (for example, Priority Triage and Doctor Round-Robin) to examine the effect that each one has on the queue.
3. **The "Fairness" Score:** A mathematical calculator built into the system which identifies whether a particular sorting rule is causing ordinary cases to remain in the waiting room for an unfairly long time.
4. **Interactive Visual Dashboard:** This is a web interface which allows users to click and drag in order to modify the number of patients and see easy-to-read performance charts, without it being necessary for them to understand the underlying code.
