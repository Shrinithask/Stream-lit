import streamlit as st
import pandas as pd
import datetime

# ========= Header Section (no image) ========= #
st.title("🐾 Pet Health Tracker")
st.subheader("Track your pet's vaccinations, medications, and meals — with love 💖")

# ========= Session Initialization ========= #
if 'vaccine_data' not in st.session_state:
    st.session_state.vaccine_data = pd.DataFrame(columns=['Pet Name', 'Vaccine', 'Date'])

if 'medication_data' not in st.session_state:
    st.session_state.medication_data = pd.DataFrame(columns=['Pet Name', 'Medication', 'Dosage', 'Start Date', 'End Date'])

if 'diet_data' not in st.session_state:
    st.session_state.diet_data = pd.DataFrame(columns=['Pet Name', 'Meal Time', 'Food', 'Quantity', 'Unit'])

# ========= Navigation ========= #
menu = st.sidebar.radio("🧭 Navigation", ["Vaccination", "Medications", "Diet", "Gallery"])

# ========= VACCINATION SECTION ========= #
if menu == "Vaccination":
    st.header("💉 Vaccination Records")
    with st.form("vaccine_form"):
        col1, col2 = st.columns(2)
        pet = col1.text_input("Pet Name")
        vaccine = col2.text_input("Vaccine Name")
        date = st.date_input("Vaccination Date", datetime.date.today())
        submit = st.form_submit_button("Add Record")
        if submit:
            new = pd.DataFrame([[pet, vaccine, date]], columns=st.session_state.vaccine_data.columns)
            st.session_state.vaccine_data = pd.concat([st.session_state.vaccine_data, new], ignore_index=True)
            st.success("✅ Vaccine added!")
    st.dataframe(st.session_state.vaccine_data)

# ========= MEDICATIONS SECTION ========= #
elif menu == "Medications":
    st.header("💊 Medication Tracker")
    with st.form("med_form"):
        col1, col2 = st.columns(2)
        pet = col1.text_input("Pet Name", key="med_pet")
        medication = col2.text_input("Medication")
        dosage = st.text_input("Dosage")
        start = col1.date_input("Start Date", datetime.date.today())
        end = col2.date_input("End Date", datetime.date.today())
        submit = st.form_submit_button("Add Medication")
        if submit:
            new = pd.DataFrame([[pet, medication, dosage, start, end]], columns=st.session_state.medication_data.columns)
            st.session_state.medication_data = pd.concat([st.session_state.medication_data, new], ignore_index=True)
            st.success("✅ Medication added!")
    st.dataframe(st.session_state.medication_data)

# ========= DIET SECTION ========= #
elif menu == "Diet":
    st.header("🍽️ Diet Menu")
    with st.form("diet_form"):
        col1, col2 = st.columns(2)
        pet = col1.text_input("Pet Name", key="diet_pet")
        meal = col2.selectbox("Meal Time", ["Morning", "Afternoon", "Evening"])
        food = col1.text_input("Food")
        qty = col2.text_input("Quantity")
        unit = col1.selectbox("Unit", ["grams", "ml", "cups", "pieces"])
        submit = st.form_submit_button("Add Diet Record")
        if submit:
            new = pd.DataFrame([[pet, meal, food, qty, unit]], columns=st.session_state.diet_data.columns)
            st.session_state.diet_data = pd.concat([st.session_state.diet_data, new], ignore_index=True)
            st.success("✅ Diet record added!")
    st.dataframe(st.session_state.diet_data)

# ========= GALLERY SECTION ========= #
elif menu == "Gallery":
    st.header("📸 Pet Gallery")
    uploaded = st.file_uploader("Upload a photo of your pet 🐶🐱", type=["png", "jpg", "jpeg"])
    if uploaded:
        st.image(uploaded, caption="Your Pet!", use_container_width=True)
        st.success("Photo uploaded successfully!")
    else:
        st.info("Upload an image to view it here.")



