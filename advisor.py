def smart_spending_advisor(income, expenses):
    print("\n========== 🤖 SMART SPENDING ADVISOR ==========")

    if not income:
        print("⚠ No income recorded.")
        return

    total_income = sum(i["amount"] for i in income)
    total_expense = sum(e["amount"] for e in expenses)
    savings = total_income - total_expense

    print(f"\n💰 Total Income   : ₹{total_income:.2f}")
    print(f"💸 Total Expense  : ₹{total_expense:.2f}")
    print(f"💵 Savings        : ₹{savings:.2f}")

    if total_income > 0:
        saving_percent = (savings / total_income) * 100

        print(f"\n📊 Savings Rate : {saving_percent:.1f}%")

        if saving_percent >= 50:
            print("✅ Excellent! You are saving more than 50% of your income.")
        elif saving_percent >= 30:
            print("👍 Good financial habits. Keep it up!")
        else:
            print("⚠ Try reducing unnecessary expenses.")

    if not expenses:
        print("\nNo expenses available for analysis.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] = category_totals.get(category, 0) + amount

    highest = max(category_totals, key=category_totals.get)

    print("\n📂 Category Analysis")

    for category, amount in category_totals.items():
        percent = (amount / total_expense) * 100
        print(f"{category}: ₹{amount:.2f} ({percent:.1f}%)")

    print("\n🤖 Suggestions")

    if highest.lower() == "food":
        print("🍔 Food expenses are high. Consider meal planning.")
    elif highest.lower() == "shopping":
        print("🛍 Shopping is your biggest expense. Set a monthly shopping limit.")
    elif highest.lower() == "travel":
        print("🚌 Travel costs are high. Consider public transport.")
    elif highest.lower() == "entertainment":
        print("🎬 Entertainment spending is high. Look for free activities.")
    else:
        print(f"📌 Highest spending category: {highest}")

    print("\n🎉 Keep tracking your expenses regularly!")
    print("=" * 50)