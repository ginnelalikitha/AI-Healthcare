"""
Meal Planner Agent

This agent generates a personalized daily meal plan
using the user's calorie target, health conditions,
diet preference, and fitness goal.

Requires:
- Groq API
- config.py
"""

from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME


class MealPlannerAgent:

    def __init__(self):
        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def build_prompt(self, user_data: dict, calorie_data: dict):

        return f"""
You are an expert dietitian.

Create a ONE DAY healthy meal plan.

User Information

Name: {user_data['name']}

Age: {user_data['age']}

Gender: {user_data['gender']}

Height: {user_data['height']} cm

Weight: {user_data['weight']} kg

Diet Preference:
{user_data['diet']}

Medical Conditions:
{user_data['disease']}

Fitness Goal:
{user_data['goal']}

Daily Calories:
{calorie_data['target_calories']} kcal

Protein Target:
{calorie_data['protein']} grams

Instructions

Create:

Breakfast

Morning Snack

Lunch

Evening Snack

Dinner

Before Bed (if required)

For every meal include

• Food Items

• Approximate Calories

• Protein

• Benefits

At the end provide

1. Total Calories

2. Total Protein

3. Hydration Recommendation

4. Grocery List

Return the response in clean markdown.
"""

    def generate_meal_plan(
        self,
        user_data: dict,
        calorie_data: dict
    ):

        prompt = self.build_prompt(
            user_data,
            calorie_data
        )

        response = self.client.chat.completions.create(

            model=MODEL_NAME,

            temperature=0.4,

            max_tokens=1500,

            messages=[

                {
                    "role": "system",
                    "content":
                    "You are a professional clinical dietitian."
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        )

        return response.choices[0].message.content

    def run(self, user_data):

     pass

if __name__ == "__main__":

    sample_user = {

        "name": "Likitha",

        "age": 22,

        "gender": "Female",

        "height": 165,

        "weight": 72,

        "diet": "Vegetarian",

        "disease": "PCOS",

        "goal": "Weight Loss"

    }

    calorie_data = {

        "target_calories": 1800,

        "protein": 120

    }

    planner = MealPlannerAgent()

    result = planner.generate_meal_plan(
        sample_user,
        calorie_data
    )

    print(result)