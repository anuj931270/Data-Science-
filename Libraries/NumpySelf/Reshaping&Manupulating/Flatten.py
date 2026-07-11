# Convert a multi-dimensional array into a 1D array.
# reshape(rows,columns)
# reshaping doest not creating copy

import numpy as np
arr =np.array([[1,2,3],
              [4,5,6]])
print(arr.flatten())  #returns a copy
print(arr.ravel())    