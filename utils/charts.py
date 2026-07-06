"""
Charts Utility

Generates Plotly charts for the
AI Healthcare Nutrition Coach.
"""

import plotly.graph_objects as go
import plotly.express as px


class HealthCharts:

    ##################################################

    @staticmethod
    def bmi_gauge(bmi):

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=bmi,

            title={"text": "BMI"},

            gauge={

                "axis": {"range": [10, 40]},

                "bar": {"color": "darkblue"},

                "steps": [

                    {"range": [10, 18.5], "color": "#87CEEB"},

                    {"range": [18.5, 25], "color": "#90EE90"},

                    {"range": [25, 30], "color": "#FFD700"},

                    {"range": [30, 40], "color": "#FF7F7F"}

                ]

            }

        ))

        fig.update_layout(height=400)

        return fig

    ##################################################

    @staticmethod
    def calorie_chart(calories):

        labels = [

            "Protein",

            "Carbohydrates",

            "Fat"

        ]

        values = [

            calories["protein"] * 4,

            calories["carbohydrates"] * 4,

            calories["fats"] * 9

        ]

        fig = px.pie(

            names=labels,

            values=values,

            title="Daily Macronutrient Distribution"

        )

        return fig

    ##################################################

    @staticmethod
    def weight_progress(weights):

        days = list(

            range(

                1,

                len(weights) + 1

            )

        )

        fig = px.line(

            x=days,

            y=weights,

            markers=True,

            labels={

                "x": "Record",

                "y": "Weight (kg)"

            },

            title="Weight Progress"

        )

        return fig

    ##################################################

    @staticmethod
    def calorie_breakdown(target):

        consumed = target * 0.85

        remaining = target - consumed

        fig = go.Figure(

            data=[

                go.Bar(

                    x=["Calories"],

                    y=[consumed],

                    name="Consumed"

                ),

                go.Bar(

                    x=["Calories"],

                    y=[remaining],

                    name="Remaining"

                )

            ]

        )

        fig.update_layout(

            barmode="stack",

            title="Daily Calorie Goal"

        )

        return fig

    ##################################################

    @staticmethod
    def water_chart(liters):

        fig = go.Figure(go.Indicator(

            mode="number",

            value=liters,

            number={"suffix": " L"},

            title={"text": "Daily Water Intake"}

        ))

        return fig


##########################################################

if __name__ == "__main__":

    calorie_data = {

        "protein": 120,

        "carbohydrates": 220,

        "fats": 55

    }

    bmi = 24.8

    weights = [

        78,

        77,

        76,

        75,

        74,

        73

    ]

    HealthCharts.bmi_gauge(bmi).show()

    HealthCharts.calorie_chart(

        calorie_data

    ).show()

    HealthCharts.weight_progress(

        weights

    ).show()

    HealthCharts.calorie_breakdown(

        2000

    ).show()

    HealthCharts.water_chart(

        2.8

    ).show()