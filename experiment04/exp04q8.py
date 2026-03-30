n=int(input("Enter an integer"))
rev=0
while n>0:
    rev = (rev*10)+(n%10)
    n//=10
print("reversed number is ",rev)