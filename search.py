def search_transactions(income, expenses):
    keyword = input("\nEnter category, description, or source to search: ").strip().lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for item in income:
        if keyword in item["source"].lower():
            print(f"Income : ₹{item['amount']:.2f} | Source: {item['source']}")
            found = True

    for item in expenses:
        if (keyword in item["category"].lower() or
                keyword in item["description"].lower()):
            print(f"Expense: ₹{item['amount']:.2f}")
            print(f"Category   : {item['category']}")
            print(f"Description: {item['description']}")
            print(f"Mood       : {item['mood']}")
            print("-" * 40)
            found = True

    if not found:
        print("❌ No matching transaction found.")