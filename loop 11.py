import math

def sine_taylor_series(x, terms=10):
    sin_x = 0
    for n in range(terms):
        sign = (-1) ** n
        term = (x ** (2 * n + 1)) / math.factorial(2 * n + 1)  
        sin_x += sign * term  
    return sin_x

x = float(input("Enter the value of x in radians: "))
terms = int(input("Enter the number of terms for accuracy: "))
print(f"sin({x}) ≈ {sine_taylor_series(x, terms)}")

print(f"Using math.sin({x}): {math.sin(x)}")
