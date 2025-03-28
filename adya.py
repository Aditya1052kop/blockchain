import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize an empty hospital ledger
hospital_ledger_advanced = {}

# Function to add or update patient visits
def add_patient_visit_advanced(patient_name, treatment, cost, date_of_visit):
    # Create a dictionary for the visit
    visit = {
        "treatment": treatment,
        "cost": cost,
        "date_of_visit": date_of_visit
    }
    
    # Add the visit to the patient's list of visits
    if patient_name not in hospital_ledger_advanced:
        hospital_ledger_advanced[patient_name] = []

    hospital_ledger_advanced[patient_name].append(visit)

# Streamlit UI
st.title("Hospital Ledger Management")

# Collect user input for the visit details
patient_name = st.text_input("Enter the patient's name:")
treatment = st.text_input("Enter the treatment received:")
cost = st.number_input("Enter the cost of the treatment ($)", min_value=0.0, step=0.01)
date_of_visit = st.date_input("Enter the date of visit:", min_value=datetime.today())

# Button to add the visit
if st.button("Add Visit"):
    if patient_name and treatment and cost > 0:
        add_patient_visit_advanced(patient_name, treatment, cost, date_of_visit)
        st.success(f"Visit added for {patient_name} on {date_of_visit} for treatment {treatment} costing ${cost}.")
    else:
        st.error("Please fill in all fields correctly.")

# Display the advanced hospital ledger
if len(hospital_ledger_advanced) > 0:
    st.subheader("Advanced Hospital Ledger")
    for patient, visits in hospital_ledger_advanced.items():
        st.write(f"### Patient: {patient}")
        for visit in visits:
            st.write(f"- Treatment: {visit['treatment']}, Cost: ${visit['cost']}, Date: {visit['date_of_visit']}")
else:
    st.info("No visits have been added yet.")
