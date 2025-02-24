import random

random_numbers = [random.randint(1, 30) for _ in range(50)]

unique_numbers = list(dict.fromkeys(random_numbers))

print("Original List (with duplicates):", random_numbers)
print("List after removing duplicates:", unique_numbers)
