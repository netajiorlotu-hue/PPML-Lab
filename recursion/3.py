def sumn(n):
    if n==1:
        return 1
    else:
        return n+sumn(n-1)

print(sumn(100))