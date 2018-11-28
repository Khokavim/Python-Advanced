import numpy as np

#you may want to select a subset of your data, for which Numpy array indexing is really useful


new_arr = np.arange(12)
print (new_arr)
print (new_arr[5])
print (new_arr[4:9])
new_arr[4:9] = 99

#assign sequence of values from 4 to 9 as 99
print (new_arr)
