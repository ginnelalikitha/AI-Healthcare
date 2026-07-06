"""
User Model

Represents a user profile for the
AI Healthcare Nutrition Coach.
"""

from dataclasses import dataclass, asdict


@dataclass
class User:

    name: str

    age: int

    gender: str

    height: float

    weight: float

    activity: str

    diet: str

    disease: str

    goal: str

    def to_dict(self):
        """
        Convert User object into dictionary.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        """
        Create User object from dictionary.
        """
        return cls(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            height=data["height"],
            weight=data["weight"],
            activity=data["activity"],
            diet=data["diet"],
            disease=data["disease"],
            goal=data["goal"]
        )

    @property
    def bmi(self):
        """
        Calculate BMI.
        """
        height_m = self.height / 100
        return round(
            self.weight / (height_m ** 2),
            2
        )

    @property
    def ideal_weight(self):
        """
        Returns ideal weight range.
        """
        h = self.height / 100

        minimum = round(18.5 * h * h, 1)
        maximum = round(24.9 * h * h, 1)

        return (minimum, maximum)

    def summary(self):
        """
        Returns a formatted user summary.
        """
        return f"""
Name       : {self.name}
Age        : {self.age}
Gender     : {self.gender}
Height     : {self.height} cm
Weight     : {self.weight} kg
Activity   : {self.activity}
Diet       : {self.diet}
Disease    : {self.disease}
Goal       : {self.goal}
BMI        : {self.bmi}
Ideal Wt   : {self.ideal_weight[0]} - {self.ideal_weight[1]} kg
"""
        

if __name__ == "__main__":

    user = User(

        name="Likitha",

        age=22,

        gender="Female",

        height=165,

        weight=70,

        activity="Moderate",

        diet="Vegetarian",

        disease="PCOS",

        goal="Weight Loss"

    )

    print(user.summary())

    print(user.to_dict())