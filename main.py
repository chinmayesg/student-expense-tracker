import json
import os
from datetime import datetime
from analytics import show_analytics
from budget import set_budget, show_budget
from charts import expense_pie_chart, expense_bar_chart
from advisor import smart_spending_advisor
from auth import register_user, login_user, change_password
from search import search_transactions

expenses = []
income = []


def load_data(username):
    global income, expenses

    filename = f"{username}_expenses.json"

    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                income = data.get("income", [])
                expenses = data.get("expenses", [])
        except Exception:
            income = []
            expenses = []


def save_data(username):
    filename = f"{username}_expenses.json"

    with open(filename, "w") as f:
        json.dump(
            {
                "income": income,
                "expenses": expenses
            },
            f,
            indent=4
        )



budget = 0
current_user = None

while current_user is None:
    print("\n========== WELCOME ==========")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        current_user = login_user()
        if current_user:
            load_data(current_user)
    elif option == "2":
        register_user()
        print("\nPlease login with your new account.\n")
        current_user = login_user()
    elif option == "3":
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice!")
def show_menu():
    print("\n" + "=" * 45)
    print("        ExpenseTracker+ 💰")
    print("=" * 45)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Financial Health Score")
    print("5. Analytics Dashboard")
    print("6. Set Monthly Budget")
    print("7. View Budget")
    print("8. Expense Pie Chart")
    print("9. Expense Bar Chart")
    print("10. Smart Spending Advisor")
    print("11. Search Transaction")
    print("12. Change Password")
    print("13. Exit")
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
            "source": source,
            "date": datetime.now().strftime("%d-%m-%Y"),
            "time": datetime.now().strftime("%I:%M %p")
        })

            save_data(current_user)

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
                "mood": mood,
                "date": datetime.now().strftime("%d-%m-%Y"),
                "time": datetime.now().strftime("%I:%M %p")
        })

            save_data(current_user)

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
       budget = set_budget()

    elif choice == "7":
       show_budget(budget, expenses)

    elif choice == "8":
       expense_pie_chart(expenses)

    elif choice == "9":
       expense_bar_chart(expenses)

    elif choice == "10":
       smart_spending_advisor(income, expenses)

    elif choice == "11":
       search_transactions(income, expenses)

    elif choice == "12":
        change_password()

    elif choice == "13":
        print("\n👋 Thank you for using ExpenseTracker+!")
        break

else:
    print("\n❌ Invalid choice! Please enter a number between 1 and 13.")