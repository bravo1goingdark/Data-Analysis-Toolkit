import numpy as np

"""
np.unique() : return an array of removed duplicated item from original array

You can pass the return_counts argument in np.unique() 
along with your array to get the frequency count of unique values in a NumPy array.

valid for 2D array also
"""

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique = np.unique(a)
unique_index , indices , frequency = np.unique(a , return_index= True , return_counts=True)
print(unique)
print(indices)
print(frequency)


# Transposing and reshaping a matrix

"""
1--> arr.reshape(): used to reshape an array along row and column
2--> arr.transpose(): used to transpose the matrix

"""

arr = np.array([[1,2,3] , [4,5,6]])
reshape = arr.reshape((3,2))
transpose = arr.transpose()
trans = arr.T
print(reshape)
print(transpose)
print(transpose)


#  reverse an array

""""
np.flip() : function allows you to flip, or reverse, the contents of an array along an axis.
"""

arr = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([[1,2,3] , [4,5,6] ,[7,8,9]])
flip1 , flip2 = np.flip(arr) , np.flip(arr2)
print(flip1)
print(flip2)


# Reshaping and flattening multidimensional arrays

"""
.flatten():
ravel() :

The primary difference between the two is that the new array created using ravel() is actually 
a reference to the parent array (i.e., a “view”).
This means that any changes to the new array will affect the parent array as well. 
Since ravel does not create a copy, it’s memory efficient.

"""

arr = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

val , value , value2 = arr.flatten() , arr2.flatten() , arr2.ravel()
print(val)
print(value)
print(value2)


# Working with mathematical formulas

m = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,2,3,4,5,6,7,8,9,10])
error = 1/10 * np.sum(np.square(m - y))
print(error)