"""
Database Module

SQLite database for AI Healthcare Nutrition Coach.
"""

import sqlite3
import os


class HealthDatabase:

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.connection = sqlite3.connect(
            "database/health.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    ##################################################

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            age INTEGER,

            gender TEXT,

            height REAL,

            weight REAL,

            activity TEXT,

            diet TEXT,

            disease TEXT,

            goal TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS progress(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_name TEXT,

            weight REAL,

            bmi REAL,

            calories REAL,

            date TEXT

        )

        """)

        self.connection.commit()

    ##################################################

    def add_user(self, user):

        self.cursor.execute("""

        INSERT INTO users(

            name,

            age,

            gender,

            height,

            weight,

            activity,

            diet,

            disease,

            goal

        )

        VALUES(?,?,?,?,?,?,?,?,?)

        """,

        (

            user["name"],

            user["age"],

            user["gender"],

            user["height"],

            user["weight"],

            user["activity"],

            user["diet"],

            user["disease"],

            user["goal"]

        ))

        self.connection.commit()

    ##################################################

    def save_progress(

        self,

        user_name,

        weight,

        bmi,

        calories,

        date

    ):

        self.cursor.execute("""

        INSERT INTO progress(

            user_name,

            weight,

            bmi,

            calories,

            date

        )

        VALUES(?,?,?,?,?)

        """,

        (

            user_name,

            weight,

            bmi,

            calories,

            date

        ))

        self.connection.commit()

    ##################################################

    def get_user(self, name):

        self.cursor.execute(

            "SELECT * FROM users WHERE name=?",

            (name,)

        )

        return self.cursor.fetchone()

    ##################################################

    def get_all_users(self):

        self.cursor.execute(

            "SELECT * FROM users"

        )

        return self.cursor.fetchall()

    ##################################################

    def get_progress(self, name):

        self.cursor.execute("""

        SELECT *

        FROM progress

        WHERE user_name=?

        ORDER BY id DESC

        """,

        (name,)

        )

        return self.cursor.fetchall()

    ##################################################

    def delete_user(self, name):

        self.cursor.execute(

            "DELETE FROM users WHERE name=?",

            (name,)

        )

        self.connection.commit()

    ##################################################

    def close(self):

        self.connection.close()


########################################################

if __name__ == "__main__":

    db = HealthDatabase()

    sample = {

        "name":"Likitha",

        "age":22,

        "gender":"Female",

        "height":165,

        "weight":70,

        "activity":"Moderate",

        "diet":"Vegetarian",

        "disease":"None",

        "goal":"Weight Loss"

    }

    db.add_user(sample)

    db.save_progress(

        "Likitha",

        70,

        25.7,

        1800,

        "2026-07-06"

    )

    print(db.get_all_users())

    print(db.get_progress("Likitha"))

    db.close()