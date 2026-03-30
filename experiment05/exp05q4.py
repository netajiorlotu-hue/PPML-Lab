l=[]

n=int(input("enter number of elements in the list")) 

for i in range (n):
    l.append(int(input()))

l = list(set(l)) 

l.sort()
print(l)

