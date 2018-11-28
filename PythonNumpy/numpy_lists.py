import numpy as np

#A major diffence between lists and array is that, array slices are views on the original array. This means that
# the data is not copied, and any modifications to the view will be reflected in the source
# array.

new_arr = np.arange(12)
modi_arr = new_arr[4:9]
modi_arr[0] = 12345
print (new_arr)                  # you can see the changes are refelected in main array.
modi_arr[:]                  # the sliced variable
