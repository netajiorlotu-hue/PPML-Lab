d1={

}

n=int(input("Enter the no of items in Dictionary"))
for i in (n):
    k=input("Enter the key")
    v=int(input("Enter the value"))
    d1[k]=v 

d2={}
for i in d1.items():
    d2[i[1]]=i[0] 

print(d2)
