from agents.calorie_agent import CalorieAgent
from agents.nutrition_agent import NutritionAgent
from agents.meal_planner_agent import MealPlannerAgent
from agents.exercise_agent import ExerciseAgent
from agents.progress_agent import ProgressAgent

calorie = CalorieAgent()
nutrition = NutritionAgent()
meal = MealPlannerAgent()
exercise = ExerciseAgent()
progress = ProgressAgent()


def calorie_node(state):
    state["calorie"] = calorie.run(
        state["user_data"]
    )
    return state


def nutrition_node(state):
    state["nutrition"] = nutrition.run(
        state["user_data"]
    )
    return state


def meal_node(state):

    state["meal_plan"] = meal.generate_meal_plan(
        state["user_data"],
        state["calorie"]
    )

    return state


def exercise_node(state):

    state["exercise"] = exercise.generate_workout(
        state["user_data"],
        state["calorie"]
    )

    return state

def progress_node(state):
    state["progress"] = progress.run(
        state["user_data"]
    )
    return state