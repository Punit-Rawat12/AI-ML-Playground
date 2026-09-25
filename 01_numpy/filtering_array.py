import numpy as np
vals = np.array([5,12,18,3,25])
new_arr = vals[vals % 2 == 0]
print(new_arr)