"""
Nutrition Page

Displays the nutrition analysis generated
by the Nutrition Agent.
"""

import streamlit as st

st.set_page_config(
    page_title="Nutrition Analysis",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 Nutrition Analysis")

st.markdown("---")

######################################################

if "report" not in st.session_state:

    st.warning(
        "Please generate a health report first."
    )

    st.stop()

######################################################

report = st.session_state["report"]

nutrition = report["nutrition"]

######################################################

st.success("Personalized Nutrition Report")

st.markdown(nutrition)

######################################################

st.markdown("---")

st.info(
"""
### Healthy Eating Tips

✅ Eat more vegetables

✅ Include fruits every day

✅ Drink enough water

✅ Limit processed foods

✅ Reduce sugar intake

✅ Include lean protein

✅ Choose whole grains

✅ Eat at regular intervals
"""
)

######################################################

st.markdown("---")

st.subheader("Daily Nutrition Checklist")

water = st.checkbox("💧 Drank enough water")

vegetables = st.checkbox("🥦 Ate vegetables")

fruits = st.checkbox("🍎 Ate fruits")

exercise = st.checkbox("🏃 Exercised today")

sleep = st.checkbox("😴 Slept 7-8 hours")

######################################################

score = sum([
    water,
    vegetables,
    fruits,
    exercise,
    sleep
])

st.progress(score / 5)

st.write(f"Health Score: **{score}/5**")

######################################################

if score == 5:

    st.success("Excellent! Keep maintaining these healthy habits.")

elif score >= 3:

    st.info("Good job! A few more healthy habits and you'll reach your goal.")

else:

    st.warning("Try to improve your daily routine for better health.")

######################################################

st.markdown("---")

st.caption("AI Healthcare Nutrition Coach")