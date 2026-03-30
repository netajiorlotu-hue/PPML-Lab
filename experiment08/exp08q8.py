def Largest(a,b,c):
    l=a if a>b and a>c else b if b>c else c
    return l
print("The largest among 10,20,30 is",Largest(10,20,30))