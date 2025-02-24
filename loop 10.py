def fibonacci_series(N):
    a, b = 0, 1  
    for _ in range(N):
        print(a, end=" ")  
        a, b = b, a + b  


N = int(input("Enter the number of Fibonacci terms: "))
fibonacci_series(N)
