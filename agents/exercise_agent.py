"""
Exercise & Lifestyle Agent

This agent generates a personalized 7-day workout plan
based on the user's profile, BMI, activity level,
medical conditions, and fitness goal.

Author: AI Healthcare Nutrition Coach
"""

from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME


class ExerciseAgent:

    def __init__(self):
        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def build_prompt(
        self,
        user_data: dict,
        calorie_data: dict
    ) -> str:

        return f"""
You are a certified fitness trainer and physiotherapist.

Generate a personalized 7-day workout plan.

USER DETAILS

Name:
{user_data['name']}

Age:
{user_data['age']}

Gender:
{user_data['gender']}

Height:
{user_data['height']} cm

Weight:
{user_data['weight']} kg

Activity Level:
{user_data['activity']}

Medical Conditions:
{user_data['disease']}

Fitness Goal:
{user_data['goal']}

BMI:
{calorie_data['bmi']}

Target Calories:
{calorie_data['target_calories']}

Generate:

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

For each day include:

• Warm-up

• Main Workout

• Cardio

• Stretching

• Estimated Calories Burned

• Workout Duration

Also provide:

- Daily Step Goal
- Sleep Recommendation
- Water Intake Recommendation
- Recovery Tips
- Safety Precautions
- Weekly Motivation Message

Return everything in clean Markdown.
"""

    def generate_workout(
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

            max_tokens=1800,

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an experienced fitness coach and rehabilitation specialist."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content

   

if __name__ == "__main__":

    sample_user = {

        "name": "Likitha",

        "age": 22,

        "gender": "Female",

        "height": 165,

        "weight": 72,

        "activity": "Moderate",

        "disease": "PCOS",

        "goal": "Weight Loss"

    }

    calorie_data = {

        "bmi": 26.4,

        "target_calories": 1800

    }

    agent = ExerciseAgent()

    result = agent.generate_workout(
        sample_user,
        calorie_data
    )

    print(result)