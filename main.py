import json
import os

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
        json.dump({"income": income, "expenses": expenses}, f, indent=4)

load_data()

def show_menu():
    print("\n" + "="*45)
    print("        ExpenseTracker+ ð°")
    print("="*45)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Financial Health Score")
    print("5. Exit")
    print("="*45)

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Income Amount: â¹"))
            source = input("Income Source: ")
            income.append({"amount": amount, "source": source})
            save_data()
            print("â Income added.")
        except ValueError:
            print("â Invalid amount.")

    elif choice == "2":
        try:
            amount = float(input("Expense Amount: â¹"))
            category = input("Category: ")
            description = input("Description: ")
            print("Mood: 1.Happy 2.Sad 3.Stressed 4.Excited 5.Normal")
            mood = {"1":"Happy","2":"Sad","3":"Stressed","4":"Excited","5":"Normal"}.get(input("Choose: "), "Unknown")
            expenses.append({
                "amount": amount,
                "category": category,
                "description": description,
                "mood": mood
            })
            save_data()
            print("â Expense added.")
        except ValueError:
            print("â Invalid amount.")

    elif choice == "3":
        print("\n--- Income ---")
        if income:
            for i,x in enumerate(income,1):
                print(f"{i}. â¹{x['amount']} | {x['source']}")
        else:
            print("No income.")
        print("\n--- Expenses ---")
        if expenses:
            for i,x in enumerate(expenses,1):
                print(f"{i}. â¹{x['amount']} | {x['category']} | {x['description']} | {x['mood']}")
        else:
            print("No expenses.")
        ti = sum(x["amount"] for x in income)
        te = sum(x["amount"] for x in expenses)
        print(f"\nTotal Income: â¹{ti:.2f}")
        print(f"Total Expense: â¹{te:.2f}")
        print(f"Balance: â¹{ti-te:.2f}")

    elif choice == "4":
        ti = sum(x["amount"] for x in income)
        te = sum(x["amount"] for x in expenses)
        if ti == 0:
            print("Please add income first.")
        else:
            score = ((ti-te)/ti)*100
            print(f"Health Score: {score:.2f}%")
            if score >= 80:
                print("ð¢ Excellent")
            elif score >= 60:
                print("ð¡ Good")
            elif score >= 40:
                print("ð  Average")
            else:
                print("ð´ Poor")

    elif choice == "5":
        print("Thank you for using ExpenseTracker+!")
        break
    else:
        print("Invalid choice.")
            