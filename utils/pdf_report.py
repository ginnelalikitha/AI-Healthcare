"""
PDF Report Generator

Generates a professional healthcare report.

Requires:
pip install reportlab
"""

import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


class PDFReport:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        self.title_style = self.styles["Heading1"]
        self.title_style.alignment = TA_CENTER

        self.heading = self.styles["Heading2"]

        self.normal = self.styles["BodyText"]

    ########################################################

    def add_section(
        self,
        story,
        title,
        content
    ):

        story.append(
            Paragraph(title, self.heading)
        )

        story.append(
            Spacer(1, 10)
        )

        story.append(
            Paragraph(
                str(content).replace("\n", "<br/>"),
                self.normal
            )
        )

        story.append(
            Spacer(1, 20)
        )

    ########################################################

    def generate(
        self,
        filename,
        user,
        calorie,
        nutrition,
        meal,
        exercise,
        progress
    ):

        os.makedirs("reports", exist_ok=True)

        path = os.path.join(
            "reports",
            filename
        )

        document = SimpleDocTemplate(path)

        story = []

        ####################################################

        story.append(
            Paragraph(
                "AI Healthcare Nutrition Coach",
                self.title_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        ####################################################

        user_summary = f"""

        <b>Name:</b> {user['name']}<br/>

        <b>Age:</b> {user['age']}<br/>

        <b>Gender:</b> {user['gender']}<br/>

        <b>Height:</b> {user['height']} cm<br/>

        <b>Weight:</b> {user['weight']} kg<br/>

        <b>Goal:</b> {user['goal']}<br/>

        <b>Diet:</b> {user['diet']}<br/>

        <b>Disease:</b> {user['disease']}<br/>

        """

        self.add_section(

            story,

            "User Profile",

            user_summary

        )

        ####################################################

        calorie_summary = f"""

        BMI : {calorie.get('bmi','N/A')}<br/>

        BMR : {calorie.get('bmr','N/A')} kcal<br/>

        TDEE : {calorie.get('tdee','N/A')} kcal<br/>

        Target Calories : {calorie.get('target_calories','N/A')} kcal<br/>

        Protein : {calorie.get('protein','N/A')} g<br/>

        Carbohydrates : {calorie.get('carbohydrates','N/A')} g<br/>

        Fat : {calorie.get('fats','N/A')} g<br/>

        Water : {calorie.get('water','N/A')} L

        """

        self.add_section(

            story,

            "Calorie Report",

            calorie_summary

        )

        ####################################################

        self.add_section(

            story,

            "Nutrition Analysis",

            nutrition

        )

        ####################################################

        self.add_section(

            story,

            "Meal Plan",

            meal

        )

        ####################################################

        self.add_section(

            story,

            "Exercise Plan",

            exercise

        )

        ####################################################

        if isinstance(progress, dict):

            report = progress.get(

                "analysis",

                str(progress)

            )

        else:

            report = progress

        self.add_section(

            story,

            "Progress Report",

            report

        )

        ####################################################

        document.build(story)

        return path


############################################################

if __name__ == "__main__":

    pdf = PDFReport()

    user = {

        "name":"Likitha",

        "age":22,

        "gender":"Female",

        "height":165,

        "weight":70,

        "goal":"Weight Loss",

        "diet":"Vegetarian",

        "disease":"None"

    }

    calorie = {

        "bmi":25.7,

        "bmr":1450,

        "tdee":2200,

        "target_calories":1800,

        "protein":120,

        "carbohydrates":220,

        "fats":50,

        "water":2.5

    }

    file = pdf.generate(

        "health_report.pdf",

        user,

        calorie,

        "Healthy nutrition recommendations...",

        "Breakfast\nLunch\nDinner",

        "7-day workout plan",

        {"analysis":"Excellent progress!"}

    )

    print("PDF Generated:", file)