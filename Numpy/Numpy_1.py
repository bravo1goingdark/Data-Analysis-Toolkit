# Q --> What is numpy?

"""
NumPy (Numerical Python) is an open source Python library that’s used in almost every field of science and engineering. 
It’s the universal standard for working with numerical data in Python, and it’s at the core of the scientific Python and PyData ecosystems. 
NumPy users include everyone from beginning coders to experienced researchers doing state-of-the-art scientific and industrial research and development.

The NumPy library contains multidimensional array and matrix data structures (you’ll find more information about this in later sections). 
It provides ndarray, a homogeneous n-dimensional array object, with methods to efficiently operate on it. 
NumPy can be used to perform a wide variety of mathematical operations on arrays.
It adds powerful data structures to Python that guarantee efficient calculations with arrays and matrices and it supplies an enormous library of high-level mathematical functions that operate on these arrays and matrices.

"""
# importing numpy

import numpy as np

# Q --> What’s the difference between a Python list and a NumPy array?

"""
NumPy arrays are faster and more compact than Python lists. 
An array consumes less memory and is convenient to use. 
NumPy uses much less memory to store data and it provides a mechanism of specifying the data types. 
This allows the code to be optimized even further.

"""
# Q --> What is an array?

"""
An array can be indexed by a tuple of nonnegative integers, by booleans, by another array, or by integers.
The rank of the array is the number of dimensions.
The shape of the array is a tuple of integers giving the size of the array along each dimension.
One way we can initialize NumPy arrays is from Python lists, using nested lists for two- or higher-dimensional data.

"""

arr = np.array([1,2,3,4,5,6])
print(arr)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr[0])


# type of array in numpy
"""
1-D :  one-dimensional array / axis
2-D :  two-dimensional array / two axis
N-D :  N-dimensional array / n axis

The NumPy ndarray class is used to represent both matrices and vectors.
A vector is an array with a single dimension (there’s no difference between row and column vectors), 
while a matrix refers to an array with two dimensions.
For 3-D or higher dimensional arrays, the term tensor is also commonly used.

"""

# Q --> What are the attributes of an array?

"""

An array is usually a fixed-size container of items of the same type and size.
The number of dimensions and items in an array is defined by its shape. 
The shape of an array is a tuple of non-negative integers that specify the sizes of each dimension.

In NumPy, dimensions are called axes.

"""

# Q --> creating basic array using numpy

"""
1--> np.zeros() : create an array filled with zeroes
2--> np.ones() :  create an array filled with ones
3--> np.empty(n) : create an empty array with n elements
4--> np.arange() : create an array that contains a range of evenly spaced intervals. 
5--> np.linspace(start ,stop , interval) : create an array with values that are spaced linearly in a specified interval

"""

arr = np.zeros(3)
print(arr)

arr = np.ones(3)
print(arr)

arr = np.empty(2)
print(arr)

arr = np.arange(5)
print(arr)

arr = np.arange(0,10,2)
print(arr)

arr = np.linspace(0, 2 , num= 5)
print(arr)

arr = np.ones(3, dtype=np.int64)
print(arr)


# Adding, removing, and sorting elements

"""

1-->np.sort(): sort an array 
2-->np.concatenate(): combine two arrays

"""

arr = np.array([3,4,7,8,5,2,1,6])
sort = np.sort(arr)
print(sort)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
conc = np.concatenate((arr1 , arr2))
print(conc)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6] , [7,8]])
z = np.concatenate((x,y) , axis= 0)
print((z))


# information about the shape and size of an array

"""
1--> ndarray.ndim : will tell you the number of axes, or dimensions, of the array.
2--> ndarray.size : will tell you the total number of elements of the array. This is the product of the elements of the array’s shape.
3--> ndarray.shape : will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).

"""

arr = np.array([[[0, 1, 2, 3],
                 [4, 5, 6, 7]],

                 [[0, 1, 2, 3],
                  [4, 5, 6, 7]],

                 [[0 ,1 ,2, 3],
                  [4, 5, 6, 7]]])

dim = arr.ndim
dimsize = arr.size
dimshape = arr.shape

print(dim)    
print(dimsize)   
print(dimshape)

# reshaping an array

"""
Using arr.reshape() will give a new shape to an array without changing the data. 

the array you want to produce needs to have the same number of elements as the original array.
If you start with an array with 12 elements, 
you’ll need to make sure that your new array also has a total of 12 elements.

1 --> ref_var.reshape() : reshape your array
2 --> newshape :the shape you want new . You can specify an integer or a tuple of integers. 
      If you specify an integer, the result will be an array of that length. 
      The shape should be compatible with the original shape.

"""

arr = np.array([1,2,3,4,5,6])
var = arr.reshape(3,2)
print(var)

new = np.reshape(arr, newshape=(6, 1), order='c')
print(new)