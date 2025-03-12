import numpy as np

#creating rank 1 array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n", arr)

#creating rank 2 array
arr = np.array([[1, 2, 3],
               [4, 5, 6]])
print("Array with Rank 2: \n", arr)

#creating array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)


# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)
 
# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)
 
# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], #X
                [3, 2, 1, 0]] #Y
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)