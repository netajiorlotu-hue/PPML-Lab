n = int(input("enter a non-negative number"))
if n<0:
    print("negative number")
else:
    fact=1
    i=1
    while(i<=n):
        fact*=i
        i+=1
    print("factorial ",fact)