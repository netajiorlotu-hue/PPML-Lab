#WAP to find the factorial of a number

x=int(input("Enter a number"))
factorial = 1
if x<0:
    print("It's a negative numebr")
elif x==0:
    print(f"factorial of {x} is {factorial}")
else:
    for i in range(1,x+1):
        factorial*=i
    print(f"The factorial of {x} is {factorial}")