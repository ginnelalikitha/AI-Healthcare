"""
Prompt Templates

Centralized prompts for all AI agents.
"""


class PromptLibrary:

    @staticmethod
    def nutrition_prompt(user):

        return f"""
You are a certified nutritionist.

Analyze the following user.

Name: {user['name']}
Age: {user['age']}
Gender: {user['gender']}
Height: {user['height']} cm
Weight: {user['weight']} kg
Activity Level: {user['activity']}
Diet Preference: {user['diet']}
Medical Conditions: {user['disease']}
Goal: {user['goal']}

Generate:

1. Overall Health Analysis
2. Recommended Foods
3. Foods to Avoid
4. Daily Protein Requirement
5. Daily Carbohydrate Requirement
6. Daily Fat Requirement
7. Vitamin Recommendations
8. Mineral Recommendations
9. Hydration Advice
10. Lifestyle Tips

Return clean markdown.
"""

    ########################################################

    @staticmethod
    def meal_plan_prompt(user, calories):

        return f"""
You are an expert dietitian.

Create a one-day personalized meal plan.

User Details

Name: {user['name']}
Age: {user['age']}
Weight: {user['weight']} kg
Goal: {user['goal']}
Diet: {user['diet']}
Disease: {user['disease']}

Target Calories

{calories} kcal

Include

Breakfast

Morning Snack

Lunch

Evening Snack

Dinner

Bedtime Snack (optional)

Mention calories for each meal.

Provide grocery list.

Return clean markdown.
"""

    ########################################################

    @staticmethod
    def exercise_prompt(user, bmi):

        return f"""
You are a professional fitness trainer.

Create a 7-day workout schedule.

User

Age: {user['age']}
Gender: {user['gender']}
Weight: {user['weight']}
BMI: {bmi}

Goal

{user['goal']}

Medical Conditions

{user['disease']}

Include

Warm-up

Strength Training

Cardio

Stretching

Rest Day

Sleep Recommendation

Step Goal

Calories Burned

Return markdown.
"""

    ########################################################

    @staticmethod
    def progress_prompt(previous, current):

        return f"""
You are an experienced wellness coach.

Compare the user's previous and current health.

Previous Weight

{previous['weight']} kg

Current Weight

{current['weight']} kg

Goal

{current['goal']}

Generate

Progress Summary

Achievements

Areas to Improve

Recommendations

Motivational Message

Return markdown.
"""