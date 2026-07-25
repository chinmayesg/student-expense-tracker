def show_analytics(income, expenses):
    print("\n========== ANALYTICS ==========")

    total_income = sum(item["amount"] for item in income)
    total_expense = sum(item["amount"] for item in expenses)
    savings = total_income - total_expense

    print(f"Total Income    : ₹{total_income:.2f}")
    print(f"Total Expenses  : ₹{total_expense:.2f}")
    print(f"Savings         : ₹{savings:.2f}")

    if expenses:
        category_totals = {}

        for item in expenses:
            category = item["category"]
            category_totals[category] = category_totals.get(category, 0) + item["amount"]

        highest = max(category_totals, key=category_totals.get)
        print(f"Highest Category: {highest}")

        mood_count = {}

        for item in expenses:
            mood = item["mood"]
            mood_count[mood] = mood_count.get(mood, 0) + 1

        common_mood = max(mood_count, key=mood_count.get)
        print(f"Most Common Mood: {common_mood}")

    print("=" * 30)