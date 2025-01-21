#area and periemter
a=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
c=2*(a+b)
d=a*b
if c>d:
    print("Area is greater than perimeter")
else:
    print("Area is not greater than perimeter")
