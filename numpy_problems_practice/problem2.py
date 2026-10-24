import numpy as np 
arr = np.arange(1 , 13)
print("original array : ",arr)
matrix = arr.reshape(3,4)
print("sum of columns")
print(matrix.sum(axis = 0))
print("sum of rows")
print(matrix.sum(axis = 1))

