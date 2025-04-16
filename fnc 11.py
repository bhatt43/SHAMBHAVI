def create_list(list1, list2):
   
    intersection = list(set(list1) & set(list2))
    return intersection

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = create_list(list_a, list_b)
print("Intersection of the two lists:", result)
