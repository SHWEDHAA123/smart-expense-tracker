expenses = []

amount = float(input("Enter expense amount: "))
category = input("Enter expense category: ")

expenses.append({
    "amount": amount,
    "category": category
})

print("\nExpense added successfully!")
print("Amount:", amount)
print("Category:", category)