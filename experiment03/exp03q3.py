print("Enter 3 unequal numbers ")
a=int(input())
b=int(input())
c=int(input())

max = a if a>c and a>b else b if b>c else c

print ("The maximum value is ",max)