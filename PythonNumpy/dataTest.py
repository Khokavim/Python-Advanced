import numpy as np

scores_1 = [[34,56,23,89], [11,45,76,34]]
second_arr = np.array(scores_1)
print (second_arr)
print (second_arr.ndim)  #.ndim gives you the dimensions of an array.
print (second_arr.shape) #(number of rows, number of columns)
print (second_arr.dtype)

x = np.zeros(10) # returns a array of zeros, the same applies for np.ones(10)
np.zeros((4,3)) # you can also mention the shape of the array
np.arange(15)
