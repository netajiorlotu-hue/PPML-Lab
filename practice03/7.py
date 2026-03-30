import numpy as np
arr = np.array([1,2,3,45,12,5,689,43])

print("Mean: ",arr.mean())
print("Mean: ",np.mean(arr))
print("Median: ",np.median(arr))
#print("Median: ",arr.meadian()) # Gives error
print("Standard Deviation: ",arr.std())
print("Standard Deviation: ",np.std(arr))

arr2 = arr.reshape(4,2)
print(arr2)

print("Mean: ",np.mean(arr2))
print("Median: ",np.median(arr2))
print("Standard Deviation: ",np.std(arr2))