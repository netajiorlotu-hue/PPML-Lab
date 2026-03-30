l1=["Mango","Guava","Apple"]
l2=[]
for i in range(len(l1)-1,-1,-1):
    print(l1[i],end=" ")
    print("length: ",len(l1[i]))
    l2.append(l1[i][::-1])
print(l2)