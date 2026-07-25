import matplotlib.pyplot as plt


def expense_pie_chart(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] = category_totals.get(category, 0) + amount

    plt.figure(figsize=(7, 7))
    plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Expense Distribution by Category")
    plt.show()


def expense_bar_chart(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] = category_totals.get(category, 0) + amount

    plt.figure(figsize=(8, 5))
    plt.bar(category_totals.keys(), category_totals.values())

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=20)

    plt.tight_layout()
    plt.show()