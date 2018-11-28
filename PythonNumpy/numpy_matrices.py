import numpy as np
# arrays can be treated like matrices

matrix_arr =np.array([[3,4,5],[6,7,8],[9,5,1]])
#print(matrix_arr)
#print(matrix_arr[1])
#print(matrix_arr[2][2]) #first row and third column
#print(matrix_arr[0,2]) # This is same as the above operation


matrix_arr =np.array([[3,4,5],[6,7,8],[9,5,1]])
print(format(matrix_arr))
#print("slices the first two rows:{}".format(matrix_arr[:2])) # similar to list slicing. returns first two rows of the array
#print("Slices the first two rows and two columns:{}".format(matrix_arr[:2, 1:]))
print("returns 6 and 7: {}".format(matrix_arr[1,:2]))
#print("Returns first column: {}".format(matrix_arr[:,:1])) #Note that a colon by itself means to take the entire axis

