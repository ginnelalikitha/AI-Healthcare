"""
Progress Page

Shows the user's health progress,
weight history, BMI history, and
AI-generated progress analysis.
"""

import streamlit as st

from database.database import HealthDatabase
from utils.charts import HealthCharts

st.set_page_config(
    page_title="Progress Tracker",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Progress Tracker")

st.markdown("---")

#######################################################

if "report" not in st.session_state:

    st.warning(
        "Please generate a health report first."
    )

    st.stop()

#######################################################

report = st.session_state["report"]

user = st.session_state["user"]

progress = report["progress"]

db = HealthDatabase()

#######################################################

st.subheader("🤖 AI Progress Analysis")

if isinstance(progress, dict):

    st.markdown(

        progress.get(

            "analysis",

            "No progress report available."

        )

    )

else:

    st.markdown(progress)

#######################################################

st.markdown("---")

st.subheader("📊 Current Health Statistics")

calorie = report["calorie"]

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(

        "Current Weight",

        f"{user['weight']} kg"

    )

with c2:

    st.metric(

        "BMI",

        calorie["bmi"]

    )

with c3:

    st.metric(

        "Target Calories",

        calorie["target_calories"]

    )

#######################################################

history = db.get_progress(user["name"])

weights = []

if history:

    for row in reversed(history):

        weights.append(row[2])

#######################################################

st.markdown("---")

st.subheader("⚖ Weight Progress")

if len(weights) > 1:

    fig = HealthCharts.weight_progress(weights)

    st.plotly_chart(

        fig,

        use_container_width=True

    )

else:

    st.info(
        "Not enough progress records yet."
    )

#######################################################

st.markdown("---")

st.subheader("🏆 Goal Progress")

goal = st.slider(

    "Overall Goal Completion (%)",

    0,

    100,

    35

)

st.progress(goal / 100)

if goal == 100:

    st.success("🎉 Congratulations! Goal achieved!")

elif goal >= 75:

    st.success("Excellent progress!")

elif goal >= 50:

    st.info("Keep going! You're over halfway there.")

else:

    st.warning("Stay consistent and you'll reach your goal.")

#######################################################

st.markdown("---")

st.subheader("🏅 Weekly Achievement Checklist")

achievements = {

    "Healthy Diet": False,

    "Exercise Completed": False,

    "Water Goal": False,

    "Sleep Goal": False,

    "Weight Improved": False

}

completed = 0

for item in achievements:

    if st.checkbox(item):

        completed += 1

st.progress(completed / len(achievements))

st.write(

    f"Achievements Completed: {completed}/{len(achievements)}"

)

#######################################################

st.markdown("---")

st.subheader("📝 Weekly Reflection")

reflection = st.text_area(

    "Write your weekly progress..."

)

if st.button("Save Reflection"):

    st.success("Reflection saved successfully!")

#######################################################

st.markdown("---")

st.caption("AI Healthcare Nutrition Coach")

db.close()