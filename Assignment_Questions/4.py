#WAP to check wheather a string is symmetriacal or pallindrome

x=input("Enter a string")

z=str(str(x)[::-1])

if x==z:
    print("It's palindrome")
else:
    print("ts not palindrome")