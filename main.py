import json
import os
from analytics import show_analytics

expenses = []
income = []


def load_data():
    global income, expenses

    if os.path.exists("expenses.json"):
        try:
            with open("expenses.json", "r") as f:
                data = json.load(f)
                income = data.get("income", [])
                expenses = data.get("expenses", [])
        except Exception:
            income = []
            expenses = []


def save_data():
    with open("expenses.json", "w") as f:
        json.dump(
            {
                "income": income,
                "expenses": expenses
            },
            f,
            indent=4
        )


load_data()


def show_menu():
    print("\n" + "=" * 45)
    print("        ExpenseTracker+ 💰")
    print("=" * 45)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Financial Health Score")
    print("5. Analytics Dashboard")
    print("6. Exit")
    print("=" * 45)


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        try:

            amount = float(input("Income Amount (₹): "))
            source = input("Income Source: ")

            income.append({
                "amount": amount,
                "source": source
            })

            save_data()

            print("\n✅ Income Added Successfully!")

        except ValueError:

            print("\n❌ Invalid amount.")

    elif choice == "2":

        try:

            amount = float(input("Expense Amount (₹): "))
            category = input("Category: ")
            description = input("Description: ")

            print("Mood:")
            print("1. Happy")
            print("2. Sad")
            print("3. Stressed")
            print("4. Excited")
            print("5. Normal")

            mood_choice = input("Choose Mood: ")

            mood = {
                "1": "Happy",
                "2": "Sad",
                "3": "Stressed",
                "4": "Excited",
                "5": "Normal"
            }.get(mood_choice, "Unknown")

            expenses.append({
                "amount": amount,
                "category": category,
                "description": description,
                "mood": mood
            })

            save_data()

            print("\n✅ Expense Added Successfully!")

        except ValueError:

            print("\n❌ Invalid amount.")

    elif choice == "3":

        print("\n========== TRANSACTIONS ==========")

        if income:

            print("\n----- Income -----")

            for i, item in enumerate(income, start=1):

                print(f"{i}. ₹{item['amount']} | Source: {item['source']}")

        else:

            print("\nNo income records.")

        if expenses:

            print("\n----- Expenses -----")

            for i, item in enumerate(expenses, start=1):

                print(f"{i}. ₹{item['amount']}")
                print(f"   Category    : {item['category']}")
                print(f"   Description : {item['description']}")
                print(f"   Mood        : {item['mood']}")
                print("-" * 40)

        else:

            print("\nNo expense records.")

        total_income = sum(item["amount"] for item in income)
        total_expense = sum(item["amount"] for item in expenses)

        print("\n=================================")
        print(f"Total Income   : ₹{total_income:.2f}")
        print(f"Total Expense  : ₹{total_expense:.2f}")
        print(f"Balance        : ₹{total_income - total_expense:.2f}")
        print("=================================")

    elif choice == "4":

        total_income = sum(item["amount"] for item in income)
        total_expense = sum(item["amount"] for item in expenses)

        if total_income == 0:

            print("\n⚠ Please add income first.")

        else:

            score = ((total_income - total_expense) / total_income) * 100

            print("\n========== FINANCIAL HEALTH ==========")

            if score >= 80:
                print("🟢 Excellent Financial Health")
            elif score >= 60:
                print("🟡 Good Financial Health")
            elif score >= 40:
                print("🟠 Average Financial Health")
            else:
                print("🔴 Poor Financial Health")

            print(f"Health Score : {score:.2f}%")
            print(f"Balance      : ₹{total_income - total_expense:.2f}")
    elif choice == "5":

        show_analytics(income, expenses)

    elif choice == "6":

        print("\n👋 Thank you for using ExpenseTracker+!")
        break

    else:

        print("\n❌ Invalid choice! Please enter a number between 1 and 6.")

            