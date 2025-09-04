# numpy_introduction.py

import numpy as np

arr = np.array([1, 2, 3])

print (arr)

arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])

print (arr)

print (arr[1][1])

# slicing a 2 d array

print(arr[2:, 2:])


# reshape
print (arr.shape)
reshaped = arr.reshape((2,8))
print (reshaped)
reshaped = arr.reshape((16, 1))
print (reshaped)

# initialising my array
arr = np.zeros((3, 5))

print (arr)

arr = np.arange(1, 17).reshape((4,4))

print (arr)


arr = np.random.randint(1, 100, (10, 10))

print (arr)


# math operations on an array

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [2, 3, 4]])

print (np.dot(arr, arr2))
       


















