a=0
b=1
sum=0
for i in range (1000):
    if a>1000:
        break
    print(a,end=" ")
    if (a%2==0):
        sum+=a
    c=a+b
    a=b
    b=c
    
    
print("sum of even valued terms is ",sum)