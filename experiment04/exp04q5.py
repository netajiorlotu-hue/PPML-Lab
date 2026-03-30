a = int(input("enter a positive integer\n"))
b=a
rev=0
while(a!=0):
    digit=a%10
    rev=rev*10+digit
    a//=10
if rev==b:
    print("palindrome")
else:
    print("not palindrome")