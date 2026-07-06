"""
Progress Monitoring Agent

Tracks the user's health progress, compares previous
records, and generates a progress report with
recommendations.

Author: AI Healthcare Nutrition Coach
"""

from datetime import datetime
from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME


class ProgressAgent:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def calculate_progress(self, previous_data: dict, current_data: dict):

        previous_weight = previous_data["weight"]
        current_weight = current_data["weight"]

        weight_change = round(
            current_weight - previous_weight,
            2
        )

        if previous_weight != 0:
            percentage = round(
                abs(weight_change) / previous_weight * 100,
                2
            )
        else:
            percentage = 0

        return {
            "previous_weight": previous_weight,
            "current_weight": current_weight,
            "weight_change": weight_change,
            "progress_percentage": percentage
        }

    def build_prompt(
        self,
        previous_data,
        current_data,
        progress
    ):

        return f"""
You are an expert health coach.

Analyze the user's health progress.

PREVIOUS DATA

Weight:
{previous_data['weight']} kg

CURRENT DATA

Weight:
{current_data['weight']} kg

Goal

{current_data['goal']}

Weight Difference

{progress['weight_change']} kg

Progress

{progress['progress_percentage']} %

Generate

1. Progress Summary

2. Performance Analysis

3. Motivation

4. What improved

5. What should improve

6. Recommendations for next week

7. Healthy habits

Return clean markdown.
"""

    def generate_report(
        self,
        previous_data,
        current_data
    ):

        progress = self.calculate_progress(
            previous_data,
            current_data
        )

        prompt = self.build_prompt(
            previous_data,
            current_data,
            progress
        )

        response = self.client.chat.completions.create(

            model=MODEL_NAME,

            temperature=0.4,

            max_tokens=1000,

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an experienced wellness coach."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return {
            "statistics": progress,
            "analysis":
            response.choices[0].message.content,
            "generated_on":
            datetime.now().strftime("%d-%m-%Y %H:%M")
        }


if __name__ == "__main__":

    previous = {

        "weight": 78,

        "goal": "Weight Loss"

    }

    current = {

        "weight": 74,

        "goal": "Weight Loss"

    }

    agent = ProgressAgent()

    report = agent.generate_report(
        previous,
        current
    )

    print(report["statistics"])
    print()
    print(report["analysis"])