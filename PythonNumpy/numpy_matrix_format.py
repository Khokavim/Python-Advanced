import numpy as np

matrix_arr =np.array([[3,4,5],[6,7,8],[9,5,1]])
print("The original matrix {}:".format(matrix_arr))
print("slices the first two rows:{}".format(matrix_arr[:2])) # similar to list slicing. returns first two rows of the array
print("Slices the first two rows and two columns:{}".format(matrix_arr[:2, 1:]))
print("returns 6 and 7: {}".format(matrix_arr[1,:2]))
print("Returns first column: {}".format(matrix_arr[:,:1])) #Note that a colon by itself means to take the entire axis
