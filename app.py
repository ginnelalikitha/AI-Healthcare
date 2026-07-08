import streamlit as st
from agents.coordinator import Coordinator
from database.database import HealthDatabase

coordinator = Coordinator()
db = HealthDatabase()

st.set_page_config(
    page_title="AI Healthcare Nutrition Coach",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 AI Healthcare Nutrition Coach")

st.write(
    "A Multi-Agent AI system for personalized nutrition and fitness."
)

st.sidebar.header("Personal Information")

name = st.sidebar.text_input("Name")

age = st.sidebar.number_input(
    "Age",
    1,
    100,
    25
)

gender = st.sidebar.selectbox(
    "Gender",
    [
        "Male",
        "Female"
    ]
)

height = st.sidebar.number_input(
    "Height (cm)",
    100,
    250,
    170
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    20,
    250,
    70
)

activity = st.sidebar.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Light",
        "Moderate",
        "Active",
        "Very Active"
    ]
)

goal = st.sidebar.selectbox(
    "Goal",
    [
        "Weight Loss",
        "Weight Gain",
        "Muscle Gain",
        "Maintain Weight"
    ]
)

disease = st.sidebar.multiselect(
    "Medical Conditions",
    [
        "None",
        "Diabetes",
        "Hypertension",
        "PCOS",
        "Thyroid",
        "Heart Disease",
        "Obesity"
    ]
)

diet = st.sidebar.selectbox(
    "Diet Preference",
    [
        "Vegetarian",
        "Non Vegetarian",
        "Vegan"
    ]
)

st.subheader("👤 User Summary")

col1, col2 = st.columns(2)

with col1:

    st.metric("Age", age)

    st.metric("Height", f"{height} cm")

    st.metric("Weight", f"{weight} kg")

with col2:

    st.metric("Goal", goal)

    st.metric("Diet", diet)

    st.metric("Activity", activity)

st.divider()

if st.button("Generate AI Health Plan"):

    user_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity": activity,
        "goal": goal,
        "diet": diet,
        "disease": ", ".join(disease)
    }

    with st.spinner("Generating your AI Health Plan..."):

        report = coordinator.run(user_data)

    st.session_state["user"] = user_data
    st.session_state["report"] = report

    st.success("✅ Health Plan Generated!")

    st.subheader("🔥 Calorie Analysis")
    st.json(report["calorie"])

    st.subheader("🥗 Nutrition")
    st.markdown(report["nutrition"])

    st.subheader("🍽 Meal Plan")
    st.markdown(report["meal_plan"])

    st.subheader("🏋 Exercise")
    st.markdown(report["exercise"])

    st.subheader("📈 Progress")
    st.write(report["progress"])