#set 2
import random
ran_num={random.randint(15,45) for _ in range(10)}
print("Initial set:", ran_num)

count_30= sum(1 for num in ran_num if num< 30)
print ("count of numbers less than 30:", count_30)

ran_num={num for num in ran_num if num<=35}
print("set after removing numbers greater than 35:", ran_num)
