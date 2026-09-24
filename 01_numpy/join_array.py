import numpy as np 
arr1 = np.array([[1,2],[2,3]])
arr2 = np.array([[4,5],[6,7]])
newarr = np.concatenate((arr1 , arr2) , axis =1 )
print(newarr)