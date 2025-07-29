import streamlit as st
import pandas as pd
import datetime
import matplotlib as plt

st.set_page_config(page_title="Pet Health Tracker", layout="wide")

st.title("🐾 Pet Health Tracker App")
st.markdown("Manage your pet's **vaccinations**, **medications**, and **diet** easily.")

# Session state to store data
if 'vaccine_data' not in st.session_state:
    st.session_state.vaccine_data = pd.DataFrame(columns=['Pet Name', 'Vaccine', 'Date'])

if 'medication_data' not in st.session_state:
    st.session_state.medication_data = pd.DataFrame(columns=['Pet Name', 'Medication', 'Dosage', 'Start Date', 'End Date'])

if 'diet_data' not in st.session_state:
    st.session_state.diet_data = pd.DataFrame(columns=['Pet Name', 'Meal Time', 'Food', 'Quantity'])

# Sidebar for navigation
menu = st.sidebar.radio("Go to", ["Vaccination Records", "Medications", "Diet Menu", "Visualization"])

# =========================
# Vaccination Records
# =========================
if menu == "Vaccination Records":
    st.header("💉 Vaccination Records")

    with st.form("vaccine_form"):
        pet_name = st.text_input("Pet Name")
        vaccine = st.text_input("Vaccine Name")
        date = st.date_input("Date", datetime.date.today())
        submitted = st.form_submit_button("Add Record")
        if submitted:
            new_row = pd.DataFrame([[pet_name, vaccine, date]], columns=st.session_state.vaccine_data.columns)
            st.session_state.vaccine_data = pd.concat([st.session_state.vaccine_data, new_row], ignore_index=True)
            st.success("Vaccination record added.")

    st.subheader("📋 Vaccination History")
    st.dataframe(st.session_state.vaccine_data)

# =========================
# Medications
# =========================
elif menu == "Medications":
    st.header("💊 Medication Tracker")

    with st.form("medication_form"):
        pet_name = st.text_input("Pet Name", key="med_pet")
        medication = st.text_input("Medication")
        dosage = st.text_input("Dosage")
        start_date = st.date_input("Start Date", datetime.date.today(), key="start_med")
        end_date = st.date_input("End Date", datetime.date.today(), key="end_med")
        submitted = st.form_submit_button("Add Medication")
        if submitted:
            new_row = pd.DataFrame([[pet_name, medication, dosage, start_date, end_date]], columns=st.session_state.medication_data.columns)
            st.session_state.medication_data = pd.concat([st.session_state.medication_data, new_row], ignore_index=True)
            st.success("Medication added.")

    st.subheader("📋 Medication List")
    st.dataframe(st.session_state.medication_data)

# =========================
# Diet Menu
# =========================
elif menu == "Diet Menu":
    st.header("🍽️ Diet Menu Tracker")

    with st.form("diet_form"):
        pet_name = st.text_input("Pet Name", key="diet_pet")
        meal_time = st.selectbox("Meal Time", ["Morning", "Afternoon", "Evening"])
        food = st.text_input("Food")
        quantity = st.text_input("Quantity (grams)")
        submitted = st.form_submit_button("Add Diet Entry")
        if submitted:
            new_row = pd.DataFrame([[pet_name, meal_time, food, quantity]], columns=st.session_state.diet_data.columns)
            st.session_state.diet_data = pd.concat([st.session_state.diet_data, new_row], ignore_index=True)
            st.success("Diet entry added.")

    st.subheader("📋 Diet Plan")
    st.dataframe(st.session_state.diet_data)

# =========================
# Visualization
# =========================
elif menu == "Visualization":
    st.header("📊 Health Overview Dashboard")

    if st.session_state.vaccine_data.empty:
        st.warning("No vaccination records available to visualize.")
    else:
        vaccine_counts = st.session_state.vaccine_data['Vaccine'].value_counts()
        fig, ax = plt.subplots()
        vaccine_counts.plot(kind='bar', ax=ax)
        ax.set_title("Vaccine Distribution")
        ax.set_xlabel("Vaccine Name")
        ax.set_ylabel("Number of Doses")
        st.pyplot(fig)

    st.markdown("---")
    st.write("🔁 You can navigate to the sidebar to add more data.")

