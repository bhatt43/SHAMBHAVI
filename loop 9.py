def print_reverse_natural_numbers(N):
    for i in range(N, 0, -1):  
        print(i, end=" ")

N = int(input("Enter a number: "))
print_reverse_natural_numbers(N)
