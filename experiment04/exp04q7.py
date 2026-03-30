n=int(input("Enter  the num,ber of terms \n"))
a=0
b=1
count=0
while(count<n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b
    count+=1
