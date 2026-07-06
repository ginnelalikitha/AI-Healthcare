"""
Coordinator Agent

This is the main orchestrator of the AI Healthcare Nutrition Coach.

Workflow

User
   │
   ▼
Coordinator
   │
   ├── Calorie Agent
   ├── Nutrition Agent
   ├── Meal Planner Agent
   ├── Exercise Agent
   └── Progress Agent
"""

from agents.calorie_agent import CalorieAgent
from agents.nutrition_agent import NutritionAgent
from agents.meal_planner_agent import MealPlannerAgent
from agents.exercise_agent import ExerciseAgent
from agents.progress_agent import ProgressAgent


class Coordinator:

    def __init__(self):

        self.calorie_agent = CalorieAgent()

        self.nutrition_agent = NutritionAgent()

        self.meal_agent = MealPlannerAgent()

        self.exercise_agent = ExerciseAgent()

        self.progress_agent = ProgressAgent()

    def run(self, user_data, previous_data=None):

        print("Running Calorie Agent...")

        calorie_result = self.calorie_agent.calculate(user_data)

        print("Running Nutrition Agent...")

        nutrition_result = self.nutrition_agent.analyze(
            user_data
        )

        print("Running Meal Planner Agent...")

        meal_result = self.meal_agent.generate_meal_plan(
            user_data,
            calorie_result
        )

        print("Running Exercise Agent...")

        exercise_result = self.exercise_agent.generate_workout(
            user_data,
            calorie_result
        )

        if previous_data:

            print("Running Progress Agent...")

            progress_result = self.progress_agent.generate_report(
                previous_data,
                user_data
            )

        else:

            progress_result = {
                "message":
                "No previous records found."
            }

        return {

            "calorie": calorie_result,

            "nutrition": nutrition_result,

            "meal_plan": meal_result,

            "exercise": exercise_result,

            "progress": progress_result

        }


if __name__ == "__main__":

    current_user = {

        "name": "Likitha",

        "age": 22,

        "gender": "Female",

        "height": 165,

        "weight": 72,

        "activity": "Moderate",

        "diet": "Vegetarian",

        "disease": "PCOS",

        "goal": "Weight Loss"

    }

    previous_user = {

        "weight": 75,

        "goal": "Weight Loss"

    }

    coordinator = Coordinator()

    report = coordinator.run(

        current_user,

        previous_user

    )

    print("\n========== FINAL REPORT ==========\n")

    print(report["calorie"])

    print(report["nutrition"])

    print(report["meal_plan"])

    print(report["exercise"])

    print(report["progress"])