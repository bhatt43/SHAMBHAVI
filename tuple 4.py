food=[('burger', 200), ('pizza', 230), ('idli', 120), ('samosa', 180)]
sorted_food=sorted(food, key=lambda item:item[1], reverse=True)
print('Food sorted by price in descending order is:')
for item in sorted_food:
    print(item)
