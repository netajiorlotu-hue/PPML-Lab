import numpy as np
arr = np.array([73,1,2,34,27])
print(np.sort(arr)) #arr.sort() returns None

print(np.sort(arr)[::-1]) #argsort() returns indexes of the sorted array