list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10]

list3 = [num for num in list1 if num not in list2]


print("First List:", list1)
print("Second List:", list2)
print("Third List (Elements from first list not in second list):", list3)
