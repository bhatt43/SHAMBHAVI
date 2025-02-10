n=int(input("Enter no: ")) 
#for prime no. 
for i in range(2,n,1): 
    if(n%i==0): 
        print("Not a prime no.") 
        break 
    else: 
        print("Prime no.") 
        break 
#for perfect no. 
p=0 
for i in range(1,n,1): 
    if (n%i==0): 
        p+=i 
if (p==n): 
    print("It is a perfect no.") 
else: 
    print("It is not a perfect no.") 
#for armstrong no. 
a=0 
b=n 
while n>0: 
    m=n%10 
    a+=m*m*m 
    n//=10 
 
 
