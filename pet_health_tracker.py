import streamlit as st
import pandas as pd
import datetime

# Try to import matplotlib only if needed
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

st.set_page_config(page_title="Pet Health Tracker", layout="wide")

st.title("🐾 Pet Health Tracker App")
st.markdown("Manage your pet's **vaccinations**, **medications**, and **diet** easily.")

# Initialize session state
if 'vaccine_data' not in st.session_state:
    st.session_state.vaccine_data = pd.DataFrame(columns=['Pet Name', 'Vaccine', 'Date'])

if 'medication_data' not in st.session_state:
    st.session_state.medication_data = pd.DataFrame(columns=['Pet Name', 'Medication', 'Dosage', 'Start Date', 'End Date'])

if 'diet_data' not in st.session_state:
    st.session_state.diet_data = pd.DataFrame(columns=['Pet Name', 'Meal Time', 'Food', 'Quantity'])

# Sidebar navigation
menu = st.sidebar.radio("Go to", ["Vaccination Records", "Medications", "Diet Menu", "Visualization"])

# ================= Vaccination Tab =================
if menu == "Vaccination Records":
    st.header("💉 Vaccination Records")
    with st.form("vaccine_form"):
        pet = st.text_input("Pet Name")
        vaccine = st.text_input("Vaccine Name")
        date = st.date_input("Vaccination Date", datetime.date.today())
        submit = st.form_submit_button("Add Record")
        if submit:
            new_entry = pd.DataFrame([[pet, vaccine, date]], columns=st.session_state.vaccine_data.columns)
            st.session_state.vaccine_data = pd.concat([st.session_state.vaccine_data, new_entry], ignore_index=True)
            st.success("Vaccination record added.")

    st.dataframe(st.session_state.vaccine_data)

# ================= Medications Tab =================
elif menu == "Medications":
    st.header("💊 Medication Tracker")
    with st.form("med_form"):
        pet = st.text_input("Pet Name", key="med_pet")
        med = st.text_input("Medication")
        dose = st.text_input("Dosage")
        start = st.date_input("Start Date", datetime.date.today(), key="med_start")
        end = st.date_input("End Date", datetime.date.today(), key="med_end")
        submit = st.form_submit_button("Add Medication")
        if submit:
            new_entry = pd.DataFrame([[pet, med, dose, start, end]], columns=st.session_state.medication_data.columns)
            st.session_state.medication_data = pd.concat([st.session_state.medication_data, new_entry], ignore_index=True)
            st.success("Medication added.")

    st.dataframe(st.session_state.medication_data)

# ================= Diet Tab =================
elif menu == "Diet Menu":
    st.header("🍽️ Diet Menu")
    with st.form("diet_form"):
        pet = st.text_input("Pet Name", key="diet_pet")
        meal = st.selectbox("Meal Time", ["Morning", "Afternoon", "Evening"])
        food = st.text_input("Food")
        qty = st.text_input("Quantity (g)")
        submit = st.form_submit_button("Add Diet Record")
        if submit:
            new_entry = pd.DataFrame([[pet, meal, food, qty]], columns=st.session_state.diet_data.columns)
            st.session_state.diet_data = pd.concat([st.session_state.diet_data, new_entry], ignore_index=True)
            st.success("Diet record added.")

    st.dataframe(st.session_state.diet_data)

# ================= Visualization =================
elif menu == "Visualization":
    st.header("📊 Vaccine Distribution")

    if not MATPLOTLIB_AVAILABLE:
        st.error("matplotlib is not installed. Please add it to requirements.txt.")
    elif st.session_state.vaccine_data.empty:
        st.info("No vaccination data available to plot.")
    else:
        counts = st.session_state.vaccine_data['Vaccine'].value_counts()
        fig, ax = plt.subplots()
        counts.plot(kind='bar', ax=ax)
        ax.set_title("Vaccines Administered")
        ax.set_xlabel("Vaccine")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    st.markdown("🔁 Add more data from the sidebar to see updated graphs.")

