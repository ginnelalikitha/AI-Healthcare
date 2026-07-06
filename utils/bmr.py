"""
BMR & Calorie Calculator

Uses the Mifflin-St Jeor Equation to calculate:

1. BMR
2. TDEE
3. Target Calories
4. Protein
5. Carbohydrates
6. Fat
7. Water Intake
"""


class BMRCalculator:

    activity_multiplier = {

        "Sedentary": 1.2,

        "Light": 1.375,

        "Moderate": 1.55,

        "Active": 1.725,

        "Very Active": 1.9

    }

    ##################################################

    @staticmethod
    def calculate_bmr(
        gender,
        age,
        height,
        weight
    ):

        """
        Mifflin-St Jeor Equation
        """

        if gender.lower() == "male":

            bmr = (
                10 * weight
                + 6.25 * height
                - 5 * age
                + 5
            )

        else:

            bmr = (
                10 * weight
                + 6.25 * height
                - 5 * age
                - 161
            )

        return round(bmr, 2)

    ##################################################

    @classmethod
    def calculate_tdee(
        cls,
        bmr,
        activity
    ):

        multiplier = cls.activity_multiplier.get(
            activity,
            1.2
        )

        return round(
            bmr * multiplier,
            2
        )

    ##################################################

    @staticmethod
    def target_calories(
        tdee,
        goal
    ):

        goal = goal.lower()

        if "loss" in goal:

            return round(tdee - 500)

        elif "gain" in goal:

            return round(tdee + 500)

        elif "muscle" in goal:

            return round(tdee + 300)

        else:

            return round(tdee)

    ##################################################

    @staticmethod
    def protein(weight, goal):

        goal = goal.lower()

        if "muscle" in goal:

            return round(weight * 2.2)

        elif "loss" in goal:

            return round(weight * 2.0)

        else:

            return round(weight * 1.6)

    ##################################################

    @staticmethod
    def carbohydrates(calories):

        """
        50% calories from carbohydrates
        """

        carbs = (calories * 0.50) / 4

        return round(carbs)

    ##################################################

    @staticmethod
    def fats(calories):

        """
        25% calories from fats
        """

        fats = (calories * 0.25) / 9

        return round(fats)

    ##################################################

    @staticmethod
    def water(weight):

        """
        35 ml per kg
        """

        liters = (weight * 35) / 1000

        return round(liters, 2)

    ##################################################

    @classmethod
    def generate_report(
        cls,
        user
    ):

        bmr = cls.calculate_bmr(

            user["gender"],

            user["age"],

            user["height"],

            user["weight"]

        )

        tdee = cls.calculate_tdee(

            bmr,

            user["activity"]

        )

        calories = cls.target_calories(

            tdee,

            user["goal"]

        )

        protein = cls.protein(

            user["weight"],

            user["goal"]

        )

        carbs = cls.carbohydrates(

            calories

        )

        fats = cls.fats(

            calories

        )

        water = cls.water(

            user["weight"]

        )

        return {

            "bmr": bmr,

            "tdee": tdee,

            "target_calories": calories,

            "protein": protein,

            "carbohydrates": carbs,

            "fats": fats,

            "water": water

        }


##########################################################

if __name__ == "__main__":

    user = {

        "gender": "Female",

        "age": 22,

        "height": 165,

        "weight": 70,

        "activity": "Moderate",

        "goal": "Weight Loss"

    }

    result = BMRCalculator.generate_report(user)

    print(result)