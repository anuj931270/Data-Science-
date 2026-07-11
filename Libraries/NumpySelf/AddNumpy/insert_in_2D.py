import numpy as np
arr=np.array([[10,20],[30,40],[50,60]])
print(arr)
new_arr_2d=np.insert(arr,3,[5,6], axis=0)
print(new_arr_2d)
# specific position elements insert