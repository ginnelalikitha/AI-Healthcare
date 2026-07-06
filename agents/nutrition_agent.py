"""
Nutrition Analysis Agent

This agent analyzes the user's profile and generates
personalized nutrition advice using the Groq API.
"""

import os

from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME


class NutritionAgent:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def build_prompt(
        self,
        user_data: dict
    ) -> str:

        prompt = f"""
You are an expert certified nutritionist.

Analyze the following user.

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

Diet Preference:
{user_data['diet']}

Medical Conditions:
{user_data['disease']}

Fitness Goal:
{user_data['goal']}

Generate a detailed report.

Include

1. Overall Health Analysis

2. Recommended Foods

3. Foods to Avoid

4. Daily Protein Recommendation

5. Daily Carbohydrates Recommendation

6. Daily Healthy Fat Recommendation

7. Daily Fiber Recommendation

8. Vitamins Required

9. Minerals Required

10. Hydration Recommendation

11. Important Health Tips

Respond in clean markdown.
"""

        return prompt

    def analyze(
        self,
        user_data: dict
    ) -> str:

        prompt = self.build_prompt(user_data)

        response = self.client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an experienced clinical nutritionist."
                },

                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.4,

            max_tokens=1200

        )

        return response.choices[0].message.content


if __name__ == "__main__":

    sample_user = {

        "name": "John",

        "age": 28,

        "gender": "Male",

        "height": 175,

        "weight": 82,

        "activity": "Moderate",

        "diet": "Vegetarian",

        "disease": "None",

        "goal": "Weight Loss"

    }

    agent = NutritionAgent()

    result = agent.analyze(sample_user)

    print(result)