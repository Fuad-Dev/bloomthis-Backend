transactions = [
    {"id": 1, "amount": 50.00, "status": "completed"},
    {"id": 2, "amount": 120.50, "status": "refunded"},
    {"id": 3, "amount": 75.25, "status": "completed"},
    {"id": 4, "amount": 15.00, "status": "pending"}
]


def calculate_completed_revenue(transactions):
    total_revenue = 0

    for transaction in transactions:
        if transaction["status"] == "completed":
            total_revenue += transaction["amount"]

    return total_revenue


total = calculate_completed_revenue(transactions)
print(f"Total completed revenue: ${total:.2f}")