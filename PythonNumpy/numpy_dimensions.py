import numpy as np

three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#print (three_d_arr[0])
#if you omit later indices, the returned object will be a lowerdimensional
#
# # ndarray consisting of all the data along the higher dimensions

copied_values = (three_d_arr[0].copy()) # copy arr[0] value to copied_values
three_d_arr[0]= 99  # change all values of arr[0] to 99
#print ("New value of three_d_arr: {}".format(three_d_arr) ) # check the new value of three_d_arr
three_d_arr[0] = copied_values # assign copied values back to three_d_arr[0]
print(" three_d_arr again: {}".format(three_d_arr))
