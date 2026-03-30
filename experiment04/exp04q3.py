print("Enter 3 numbers")
a=int(input())
b=int(input())
c=int(input())

i=a if a<b and a<c else b if b<c else c
while(i>=1):
    if(a%i==0 and b%i==0 and c%i==0):
        print("The GCD is ",i)
        break
    i=i-1