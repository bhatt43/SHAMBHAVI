#recursive function 1
def prime_factors(n,divisor=2):
    if n<=1:
        return []

    if n%divisor==0:
        return [divisor]+prime_factors(n//divisor, divisor)
    else:
        return prime_factors(n,divisor+1)

num=int(input("Enter the positive integer:"))
if num>0:
    factors=prime_factors(num)
    print("Prime factors:", factors)
else:
        print("PLease enter a positive integer.")
