import streamlit as st

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

    st.success("Profile Received")

    progress = st.progress(0)

    st.write("🥗 Nutrition Agent Running...")
    progress.progress(20)

    st.write("🔥 Calorie Agent Running...")
    progress.progress(40)

    st.write("🍽️ Meal Planner Agent Running...")
    progress.progress(60)

    st.write("🏋️ Exercise Agent Running...")
    progress.progress(80)

    st.write("📈 Progress Agent Running...")
    progress.progress(100)

    st.success("All Agents Completed!")

    st.subheader("Results")

    st.info(
        "The next version will display personalized recommendations from each AI agent."
    )

st.divider()

st.markdown("""
## AI Agents

🥗 Nutrition Analysis Agent

🔥 Calorie Assessment Agent

🍽️ Meal Planning Agent

🏋️ Exercise Recommendation Agent

📈 Progress Monitoring Agent

---

Developed using *Streamlit + Groq API + SQLite*
""")
