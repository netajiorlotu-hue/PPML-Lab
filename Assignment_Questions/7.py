#WAP to print the second largest and second smallest element ina list of 10 integers without using sort function

arr=[]
x=int(input("Enter number of elements"))
for i in range(x):
    m=int(input("Enter element"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The sorted array is ")
for i in arr:
    print(i,end =" ")
second_largest=arr[-2]
second_smallest=arr[1]
print("\nSecond largest is",second_largest)
print("second smallest is ",second_smallest)