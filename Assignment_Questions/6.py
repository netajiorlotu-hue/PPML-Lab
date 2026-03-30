#WAP to remove al duplicates from a given string.
x=input("Enter a string")
result=""
for c in x:
    if c not in result:
        result=result+c
print(result)