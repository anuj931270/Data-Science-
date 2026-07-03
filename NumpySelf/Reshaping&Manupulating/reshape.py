# Changing the dimensions of an array without changing data is called reshape.

import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6])
new_arr=arr.reshape(2,-3)
print(new_arr)

# Reshape into 3D Array

arr1=np.array([1,2,3,4,5,6,7,8])
new_arr1=arr1.reshape(2,2,2)
print(new_arr1)