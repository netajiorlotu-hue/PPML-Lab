import numpy as np
arr1 = np.array([[2,3],[5,6]])
arr2 = np.array([[8,7],[4,3]])

print(np.multiply(arr1,arr2))
arr3 =arr1@arr2
print(arr3)
print(np.dot(arr1,arr2))
