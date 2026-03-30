#WAP to calculate factorial of a number using recursion
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int(input("eneter a number: "))
if(n<0):
    print("It's a negative number")
else:
    print("facorial of",n,"is: ",factorial(n))
    