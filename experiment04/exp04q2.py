a = int(input("Enter a number\n"))

i=1
count=0
while(i<=a):
    if(a%i==0):
        count=count+1
    i+=1

if(count==2):
    print("It's a prime number")
else:
    print("It's not a prime number")