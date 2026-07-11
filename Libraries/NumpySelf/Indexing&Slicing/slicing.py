#extracting subset of data is called slicing
# array[start:stop:step]

import numpy as np
arr=np.array([2,5,8,7,8])
print(arr[1:5])
print(arr[:3])
print(arr[::2])
print(arr[::-1])