"""
Dashboard Page

Displays:
- User Profile
- BMI
- BMR
- Calories
- Water Intake
- Charts
"""

import streamlit as st

from utils.charts import HealthCharts

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Healthcare Nutrition Coach")

st.markdown("---")

# Check whether report data exists
if "report" not in st.session_state:

    st.warning(
        "No health report available.\n\n"
        "Go back to the Home page and generate a report first."
    )

    st.stop()

report = st.session_state["report"]

user = st.session_state["user"]

calorie = report["calorie"]

###########################################################

st.subheader("👤 User Profile")

col1, col2 = st.columns(2)

with col1:

    st.write(f"**Name:** {user['name']}")

    st.write(f"**Age:** {user['age']}")

    st.write(f"**Gender:** {user['gender']}")

    st.write(f"**Height:** {user['height']} cm")

with col2:

    st.write(f"**Weight:** {user['weight']} kg")

    st.write(f"**Goal:** {user['goal']}")

    st.write(f"**Diet:** {user['diet']}")

    st.write(f"**Disease:** {user['disease']}")

###########################################################

st.markdown("---")

st.subheader("📊 Health Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(

        "BMI",

        calorie["bmi"]

    )

with c2:

    st.metric(

        "BMR",

        f"{calorie['bmr']} kcal"

    )

with c3:

    st.metric(

        "Calories",

        calorie["target_calories"]

    )

with c4:

    st.metric(

        "Water",

        f"{calorie['water']} L"

    )

###########################################################

st.markdown("---")

st.subheader("📈 BMI Gauge")

fig = HealthCharts.bmi_gauge(

    calorie["bmi"]

)

st.plotly_chart(

    fig,

    use_container_width=True

)

###########################################################

st.markdown("---")

st.subheader("🥗 Macronutrient Distribution")

fig = HealthCharts.calorie_chart(

    calorie

)

st.plotly_chart(

    fig,

    use_container_width=True

)

###########################################################

st.markdown("---")

st.subheader("🔥 Daily Calories")

fig = HealthCharts.calorie_breakdown(

    calorie["target_calories"]

)

st.plotly_chart(

    fig,

    use_container_width=True

)

###########################################################

st.success("Dashboard Loaded Successfully ✅")