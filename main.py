expenses = []
income = []


def show_menu():
    print("\n" + "=" * 50)
    print("              ExpenseTracker+ 💰")
    print("                 Version 1.1")
    print("=" * 50)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Financial Health Score")
    print("5. Exit")
    print("=" * 50)


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter income amount (₹): "))
            source = input("Enter income source: ")

            income.append({
                "amount": amount,
                "source": source
            })

            print("\n✅ Income added successfully!")

        except ValueError:
            print("\n❌ Please enter a valid amount.")

    elif choice == "2":
        try:
            amount = float(input("Enter expense amount (₹): "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            print("\nSelect your mood while spending")
            print("1. Happy 😊")
            print("2. Sad 😔")
            print("3. Stressed 😣")
            print("4. Excited 🤩")
            print("5. Normal 🙂")

            mood_choice = input("Enter mood (1-5): ")

            moods = {
                "1": "Happy",
                "2": "Sad",
                "3": "Stressed",
                "4": "Excited",
                "5": "Normal"
            }

            mood = moods.get(mood_choice, "Unknown")

            expenses.append({
                "amount": amount,
                "category": category,
                "description": description,
                "mood": mood
            })

            print("\n✅ Expense added successfully!")

        except ValueError:
            print("\n❌ Please enter a valid amount.")

    elif choice == "3":

        print("\n" + "=" * 50)
        print("            TRANSACTION HISTORY")
        print("=" * 50)

        if len(income) == 0:
            print("\nNo income records.")
        else:
            print("\n------ Income ------")
            for i, item in enumerate(income, start=1):
                print(f"{i}. ₹{item['amount']} | Source: {item['source']}")

        if len(expenses) == 0:
            print("\nNo expense records.")
        else:
            print("\n------ Expenses ------")
            for i, item in enumerate(expenses, start=1):
                print(f"{i}. ₹{item['amount']}")
                print(f"   Category    : {item['category']}")
                print(f"   Description : {item['description']}")
                print(f"   Mood        : {item['mood']}")
                print("-" * 40)

        total_income = sum(item["amount"] for item in income)
        total_expense = sum(item["amount"] for item in expenses)
        balance = total_income - total_expense

        print("\n" + "=" * 50)
        print(f"Total Income   : ₹{total_income:.2f}")
        print(f"Total Expense  : ₹{total_expense:.2f}")
        print(f"Current Balance: ₹{balance:.2f}")
        print("=" * 50)

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
        print("\n👋 Thank you for using ExpenseTracker+!")
        break

    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 5.")