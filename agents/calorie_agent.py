"""
Calorie & Health Assessment Agent

Responsibilities:
- BMI Calculation
- BMI Category
- BMR Calculation
- TDEE Calculation
- Daily Calorie Goal
- Protein Recommendation
- Water Intake Recommendation
"""

from dataclasses import dataclass


@dataclass
class HealthMetrics:
    bmi: float
    bmi_category: str
    bmr: float
    tdee: float
    target_calories: float
    protein_grams: float
    water_liters: float


class CalorieAgent:

    def __init__(self):
        pass

    # -----------------------------------
    # BMI
    # -----------------------------------

    def calculate_bmi(
        self,
        weight: float,
        height_cm: float
    ) -> float:

        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)

        return round(bmi, 2)

    def bmi_category(
        self,
        bmi: float
    ) -> str:

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal Weight"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obese"

    # -----------------------------------
    # BMR
    # Mifflin-St Jeor Equation
    # -----------------------------------

    def calculate_bmr(
        self,
        gender: str,
        weight: float,
        height_cm: float,
        age: int
    ) -> float:

        gender = gender.lower()

        if gender == "male":

            bmr = (
                10 * weight
                + 6.25 * height_cm
                - 5 * age
                + 5
            )

        else:

            bmr = (
                10 * weight
                + 6.25 * height_cm
                - 5 * age
                - 161
            )

        return round(bmr, 2)

    # -----------------------------------
    # Activity Multiplier
    # -----------------------------------

    def get_activity_factor(
        self,
        activity: str
    ) -> float:

        factors = {

            "Sedentary": 1.2,

            "Light": 1.375,

            "Moderate": 1.55,

            "Active": 1.725,

            "Very Active": 1.9
        }

        return factors.get(activity, 1.2)

    # -----------------------------------
    # TDEE
    # -----------------------------------

    def calculate_tdee(
        self,
        bmr: float,
        activity: str
    ) -> float:

        factor = self.get_activity_factor(activity)

        return round(bmr * factor, 2)

    # -----------------------------------
    # Goal Calories
    # -----------------------------------

    def calorie_goal(
        self,
        tdee: float,
        goal: str
    ) -> float:

        goal = goal.lower()

        if goal == "weight loss":

            return round(tdee - 500, 2)

        elif goal == "weight gain":

            return round(tdee + 500, 2)

        elif goal == "muscle gain":

            return round(tdee + 300, 2)

        return round(tdee, 2)

    # -----------------------------------
    # Protein
    # -----------------------------------

    def protein_target(
        self,
        weight: float,
        goal: str
    ) -> float:

        goal = goal.lower()

        if goal == "muscle gain":

            return round(weight * 2.2, 1)

        elif goal == "weight loss":

            return round(weight * 1.8, 1)

        return round(weight * 1.5, 1)

    # -----------------------------------
    # Water Intake
    # -----------------------------------

    def water_intake(
        self,
        weight: float
    ) -> float:

        liters = weight * 0.035

        return round(liters, 2)

    # -----------------------------------
    # Complete Analysis
    # -----------------------------------

    def analyze(
        self,
        user_data: dict
    ) -> HealthMetrics:

        bmi = self.calculate_bmi(
            user_data["weight"],
            user_data["height"]
        )

        category = self.bmi_category(bmi)

        bmr = self.calculate_bmr(
            user_data["gender"],
            user_data["weight"],
            user_data["height"],
            user_data["age"]
        )

        tdee = self.calculate_tdee(
            bmr,
            user_data["activity"]
        )

        calories = self.calorie_goal(
            tdee,
            user_data["goal"]
        )

        protein = self.protein_target(
            user_data["weight"],
            user_data["goal"]
        )

        water = self.water_intake(
            user_data["weight"]
        )

        return HealthMetrics(

            bmi=bmi,

            bmi_category=category,

            bmr=bmr,

            tdee=tdee,

            target_calories=calories,

            protein_grams=protein,

            water_liters=water
        )


# ---------------------------------------
# Test
# ---------------------------------------

if __name__ == "__main__":

    user = {

        "age": 25,

        "gender": "Male",

        "height": 175,

        "weight": 80,

        "activity": "Moderate",

        "goal": "Weight Loss"
    }

    agent = CalorieAgent()

    result = agent.analyze(user)

    print(result)