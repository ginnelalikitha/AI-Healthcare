"""
BMI Utility

Provides functions to:
1. Calculate BMI
2. Determine BMI category
3. Calculate ideal weight range
"""


class BMI:

    @staticmethod
    def calculate(weight, height):
        """
        Calculate BMI.

        Parameters:
            weight (float): Weight in kilograms
            height (float): Height in centimeters

        Returns:
            float: BMI value
        """

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        return round(bmi, 2)

    ####################################################

    @staticmethod
    def category(bmi):
        """
        Return BMI category.
        """

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal Weight"

        elif bmi < 30:
            return "Overweight"

        elif bmi < 35:
            return "Obesity Class I"

        elif bmi < 40:
            return "Obesity Class II"

        else:
            return "Obesity Class III"

    ####################################################

    @staticmethod
    def ideal_weight(height):
        """
        Calculate ideal weight range using BMI.

        Parameters:
            height (float): Height in centimeters

        Returns:
            tuple: (minimum_weight, maximum_weight)
        """

        height_m = height / 100

        minimum = 18.5 * (height_m ** 2)

        maximum = 24.9 * (height_m ** 2)

        return (
            round(minimum, 1),
            round(maximum, 1)
        )

    ####################################################

    @classmethod
    def report(cls, weight, height):
        """
        Generate a BMI report.
        """

        bmi = cls.calculate(weight, height)

        category = cls.category(bmi)

        ideal_min, ideal_max = cls.ideal_weight(height)

        return {
            "bmi": bmi,
            "category": category,
            "ideal_weight_min": ideal_min,
            "ideal_weight_max": ideal_max
        }


########################################################

if __name__ == "__main__":

    weight = 72

    height = 165

    report = BMI.report(weight, height)

    print("\nBMI REPORT\n")

    print(f"BMI              : {report['bmi']}")

    print(f"Category         : {report['category']}")

    print(
        f"Ideal Weight     : "
        f"{report['ideal_weight_min']} kg - "
        f"{report['ideal_weight_max']} kg"
    )