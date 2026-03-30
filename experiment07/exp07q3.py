s=input("enter a paragraph")

li=s.split(" ")
print("Total number of words: ",len(li))

count=0
for i in li:
    if i==i[::-1]:
        count+=1
print("total number of palindrome :",count)

for i in li:
    print(i[::-1])