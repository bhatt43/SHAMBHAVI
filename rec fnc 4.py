#recursive function 4
def reverse_list(list):
    if len(list)==0:
        return[]
    return [list[-1]]+reverse_list(list[:-1])

numbers=list(map(int, input("Enter numbers seperated by space:".split())))

reversed_numbers=reverse_list(numbers)
print("Reversed list:", reversed_numbers)
