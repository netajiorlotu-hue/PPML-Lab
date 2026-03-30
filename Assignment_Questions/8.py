# wap to craete 2 lists first list containing 5 integers and second list containing 5 strings. print both the list one element from each list combined at a time.
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
s=[]
for i in range(len(list1)):
    s.append(str(list1[i]))
    s.append(list2[i])
print(s)