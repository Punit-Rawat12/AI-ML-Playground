import numpy as np 
arr = np.array([10,20,30,40,50])

# find index of elements greater than 25 
indices = np.where(arr>25)

# Extract acutal vaues using index mask 
values = arr[indices]

print(indices)
print(values)