m=int(input("enter lower bound: "))
n=int(input("Enter upper bound: "))

li=[]

for i in range(m,n):
    li.append(i)

print("sum",sum(li))
print("avrage",sum(li)/len(li))
print("largest",max(li))
print("smallest",min(li))