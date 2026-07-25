import json
import os


def load_data():
    if os.path.exists("expenses.json"):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)

            return (
                data.get("budget", 0),
                data.get("income", []),
                data.get("expenses", [])
            )

        except Exception:
            return 0, [], []

    return 0, [], []


def save_data(budget, income, expenses):
    data = {
        "budget": budget,
        "income": income,
        "expenses": expenses
    }

    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)