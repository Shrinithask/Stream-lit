import streamlit as st
import pandas as pd
import datetime

# Header image (replace URL or upload your own)
st.image("https://cdn.pixabay.com/photo/2016/11/18/18/51/dog-1839808_960_720.jpg", use_column_width=True)

# Custom CSS for colors and fonts
st.markdown("""
    <style>
    .main {
        background-color: #f0f7f7;
    }
    h1, h2, h3 {
        color: #2a9d8f;
    }
    .stButton>button {
        background-color: #2a9d8f;
        color: white;
        font-weight: bold;
    }
    .st-bd {
        background-color: #e0f7fa;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐾 Pet Health Tracker")
st.subheader("Track your pet's vaccinations, medications, and meals — with love 💖")

# Session state initialization
if 'vaccine_data' not in st.session_state:
    st.session_state.vaccine_data = pd.DataFrame(columns=['Pet Name', 'Vaccine', 'Date'])

if 'medication_data' not in st.session_state:
    st.session_state.medication_data = pd.DataFrame(columns=['Pet Name', 'Medication', 'Dosage', 'Start Date', 'End Date'])

if 'diet_data' not in st.session_state:
    st.session_state.diet_data = pd.DataFrame(columns=['Pet Name', 'Meal Time', 'Food', 'Quantity'])

menu = st.sidebar.radio("🧭 Navigation", ["Vaccination", "Medications", "Diet", "Gallery"])

# ====== Vaccination ======
if menu == "Vaccination":
    st.header("💉 Vaccination Records")
    with st.form("vaccine_form"):
        col1, col2 = st.columns(2)
        pet = col1.text_input("Pet Name")
        vaccine = col2.text_input("Vaccine")
        date = st.date_input("Vaccination Date", datetime.date.today())
        submit = st.form_submit_button("Add Record")
        if submit:
            new = pd.DataFrame([[pet, vaccine, date]], columns=st.session_state.vaccine_data.columns)
            st.session_state.vaccine_data = pd.concat([st.session_state.vaccine_data, new], ignore_index=True)
            st.success("✅ Vaccine added!")
    st.dataframe(st.session_state.vaccine_data)

# ====== Medications ======
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

# ====== Diet ======
elif menu == "Diet":
    st.header("🍽️ Diet Menu")
    with st.form("diet_form"):
        col1, col2 = st.columns(2)
        pet = col1.text_input("Pet Name", key="diet_pet")
        meal = col2.selectbox("Meal Time", ["Morning", "Afternoon", "Evening"])
        food = col1.text_input("Food")
        qty = col2.text_input("Quantity (g)")
        submit = st.form_submit_button("Add Diet Record")
        if submit:
            new = pd.DataFrame([[pet, meal, food, qty]], columns=st.session_state.diet_data.columns)
            st.session_state.diet_data = pd.concat([st.session_state.diet_data, new], ignore_index=True)
            st.success("✅ Diet record added!")
    st.dataframe(st.session_state.diet_data)

# ====== Gallery ======
elif menu == "Gallery":
    st.header("📸 Pet Gallery")
    uploaded = st.file_uploader("Upload a cute photo of your pet 🐶🐱", type=["png", "jpg", "jpeg"])
    if uploaded:
        st.image(uploaded, caption="Your Pet!", use_column_width=True)
        st.success("Photo uploaded successfully!")

    st.markdown("You can also use this section to keep records of appearance, accessories, or IDs.")



