#recursive function 2
def binary_equivalent(n):
    if n==0:
        return ""
    return binary_equivalent(n//2)+str(n%2)

num=int(input("Enter a positive integer:"))
if num>0:
    binary=binary_equivalent(num)
    print("Binary equivalent:", binary)
else:
        print("Please enter a positive integer.")
