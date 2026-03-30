print("Enter marks of 5 subjects")
li=[]
for i in range(0,5):
    li.append(float(input()))

sum=0
for i in li:
    sum+=i

per=(sum/250)*100

if(per>=90 and per <100):
    print("O")
elif(per>=80):
    print("E")
elif(per>=70):
    print("A")
elif(per>=60):
    print("B")
elif(per>=50):
    print("C")
elif(per>=0):
    print("F")
else:
    print("Invalid")