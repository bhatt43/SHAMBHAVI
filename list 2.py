import random

numbers = [random.randint(1, 10) for _ in range(20)]

print("Generated List:", numbers)

user_number = int(input("Enter a number to find its positions: "))

positions = [i for i, num in enumerate(numbers) if num == user_number]

if positions:
    print(f"The number {user_number} is found at positions: {positions}")
else:
    print(f"The number {user_number} is not in the list.")
