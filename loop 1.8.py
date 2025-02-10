n=int(input("Enter nos. in fibonacci series: ")) 
n1=0 
n2=1 
nth=0 
print("0 + 1 + ",end="") 
while n>0: 
  nth=n1+n2 
n1=n2      
n2=nth     
n-=1 
print(nth,"+ ",end="")
