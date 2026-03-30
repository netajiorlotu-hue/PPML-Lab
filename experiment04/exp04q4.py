a = int(input("enter a positive integer\n"))

sum=0
while(a!=0):
    digit=a%10
    sum+=digit
    a=int(a/10)
print("sum of the digit is ",sum)