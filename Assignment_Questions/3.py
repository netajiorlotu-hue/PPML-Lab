#WAP to check leap year
x=int(input("Enter a year"))
if x%4==0 and (x%100!=0 or x%400==0):
    print(x,"is leap year")
else:
    print("It's not a leap year")