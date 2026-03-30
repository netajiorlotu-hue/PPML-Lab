s=input("Enter a sentence")
li=s.split(" ")
for i,j in enumerate(li):
    print(i,j)

li2=[i for i in range(len(li))]

l3=list(zip(li,li2))

print(l3)