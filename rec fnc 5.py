def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
a=int(input("Enter the base (a):"))
b=int(input("Enter the exponent (b):"))

result=power(a,b)
print(f"the result of {a}^{b} is: {result}")
