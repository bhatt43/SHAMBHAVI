prices = {
    'rice': 50,
    'wheat': 40,
    'sugar': 30,
    'milk': 20,
    'oil': 100
}

quantities = {
    'rice': 2,
    'wheat': 3,
    'sugar': 1,
    'milk': 5,
    'oil': 1
}

total_bill = 0

for item in prices:
    if item in quantities:
        total_cost = prices[item] * quantities[item]
        total_bill += total_cost
        print(f"{item.capitalize()}: {quantities[item]} x {prices[item]} = {total_cost}")

print(f"\nTotal Bill: ₹{total_bill}")
