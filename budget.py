def set_budget():
    """Set monthly budget"""
    while True:
        try:
            budget = float(input("\nEnter your monthly budget (₹): "))
            if budget <= 0:
                print("❌ Budget must be greater than 0.")
                continue
            print(f"\n✅ Monthly Budget Set: ₹{budget:.2f}")
            return budget
        except ValueError:
            print("❌ Please enter a valid number.")


def show_budget(budget, expenses):
    """Display budget details"""

    if budget == 0:
        print("\n⚠ No budget has been set yet.")
        return

    total_expense = sum(item["amount"] for item in expenses)
    remaining = budget - total_expense
    used_percent = (total_expense / budget) * 100

    print("\n========== MONTHLY BUDGET ==========")
    print(f"Budget          : ₹{budget:.2f}")
    print(f"Spent           : ₹{total_expense:.2f}")
    print(f"Remaining       : ₹{remaining:.2f}")
    print(f"Budget Used     : {used_percent:.2f}%")

    if used_percent < 50:
        print("🟢 Excellent Budget Control")
    elif used_percent < 80:
        print("🟡 Good Budget Control")
    elif used_percent <= 100:
        print("🟠 Warning: Budget almost exhausted!")
    else:
        print("🔴 Budget Exceeded!")

    print("=" * 36)