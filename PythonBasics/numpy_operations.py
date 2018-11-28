import numpy as np

# easiest way to create an array is by using an array function

# Nested lists with equal length, will be converted into a multidimensional array
scores_1 = [[34,56,23,89], [11,45,76,34]]
second_arr = np.array(scores_1)
print (second_arr)
print (second_arr.ndim)  #.ndim gives you the dimensions of an array.
print (second_arr.shape) #(number of rows, number of columns)
print (second_arr.dtype)
