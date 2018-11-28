import numpy as np

# # 3d arrays -> this is a 2x2x3 array
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print (three_d_arr)
print ("returns the second list inside first list {}".format(three_d_arr[0,1]))
