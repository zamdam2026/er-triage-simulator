import streamlit as st
from simulator import generate_patients, run_all
from stats import compare, best_by

def main():
    st.set_page_config(page_title="ER Triage Simulator", page_icon="🏥", layout="wide")
    
    st.title("🏥 Emergency Room Triage Simulator")
    st.markdown("Analyze how different hospital policies affect patient waiting times and care equality.")

    with st.expander("ℹ️ How We Prioritize Care (Hospital Policies)"):
        st.markdown("""
        **Our Triage Levels:**
        * **Triage 1 (Critical):** Life-threatening emergencies (e.g., severe trauma).
        * **Triage 2 (Urgent):** Serious but stable conditions (e.g., broken bones).
        * **Triage 3 (Routine):** Non-urgent care.

        **How the Policies Work:**
        * **Triage Protocol (Priority):** Patients with Triage Level 1 are seen completely before Level 2 or 3. Highly effective for emergencies, but routine patients wait a long time.
        * **Doctor Rounds (Round Robin):** Doctors spend a fixed amount of time (e.g., 2 hours) stabilizing a patient before rotating to check on the next person. Highly fair.
        * **Quick Consults (Lottery):** Patients needing very fast treatments (e.g., a 1-hour consult) are prioritized to clear out the waiting room quickly.
        """)

    st.sidebar.header("Current ER Conditions")
    
    num_patients = st.sidebar.number_input("Total Patients in ER", min_value=1, max_value=100, value=10, step=1)
    quantum = st.sidebar.number_input("Doctor Rotation (Hours)", min_value=1, max_value=12, value=2, step=1)
    
    use_seed = st.sidebar.checkbox("Use fixed scenario (for committee review)")
    seed = st.sidebar.number_input("Scenario ID", value=42, step=1) if use_seed else None

    if st.sidebar.button("Process ER Queue", type="primary"):
        
        patients = generate_patients(num_patients, seed=seed)
        triage_map = {1: "1 - Critical 🔴", 2: "2 - Urgent 🟡", 3: "3 - Routine 🟢"}
        
        st.subheader("📋 Current Waiting Room")
        
        md_table = "| Patient ID | Name | Treatment (Hours) | Triage Level |\n|---|---|---|---|\n"
        for p in patients:
            md_table += f"| {p.patient_id} | {p.patient_name} | {p.estimated_hours} | {triage_map[p.triage_level]} |\n"
        
        st.markdown(md_table) 

        with st.spinner("Calculating outcomes..."):
            results = run_all(patients, q=quantum, seed=seed)
            comparison = compare(results)

        st.subheader("📊 Hospital Policy Comparison")
        
        # --- UPDATED: Added Units (Hours) to the table headers ---
        comp_table = "| Policy | Avg Wait (Hours) | Max Wait (Hours) | Avg Turnaround (Hours) | Unfairness Score |\n|---|---|---|---|---|\n"
        for policy_name, metrics in comparison.items():
            comp_table += f"| **{policy_name}** | {metrics['avg_wait']} | {metrics['max_wait']} | {metrics['avg_turnaround']} | {metrics['unfairness']} |\n"
        
        st.markdown(comp_table)
        
        # --- UPDATED: Added an explanation box below the table ---
        st.info("""
        **📋 Guide to the Metrics Above:**
        * **Avg Wait (Hours):** The average time a patient sits in the lobby before a doctor starts treating them.
        * **Max Wait (Hours):** The absolute longest time any single patient was stuck waiting in the lobby.
        * **Avg Turnaround (Hours):** The total time from when a patient walks in the front door to when they are completely treated and discharged.
        * **Unfairness Score:** A statistical measure of equality. A score closer to **0** is better (meaning everyone waited about the same amount of time). A high score means care was very unequal (e.g., some were treated instantly while others were ignored for hours).
        """)

        winner = best_by(comparison)
        st.success(f"⚖️ **Most equitable policy for this group:** {winner}")

if __name__ == "__main__":
    main()