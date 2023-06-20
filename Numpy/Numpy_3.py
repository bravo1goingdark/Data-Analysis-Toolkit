# How to create an array from existing data

"""
1--> np.vstack((tuple of array)): vertically stack up the two array
2--> np.hstack((tuple of array)): horizontally stack up the two array
3--> np.hsplit(arr,parts): split an array into several smaller array

"""
import numpy as np
from math import pi

arr1 = np.array([[1, 1],[2, 2]])
arr2 = np.array([[3,3] , [4,4]])
vstack = np.vstack((arr1,arr2))
hstack = np.hstack((arr1,arr2))
print(vstack)
print()
print(hstack)

x = np.arange(1, 25).reshape(2, 12)
y = np.hsplit(x, 4)
print(x)
print()
print(y)


# Basic mathematical operation in numpy
"""
1--> sum(axis) : sum all the element inside an array if argument is not provided
                 else it sum along axis if it is provided
2--> max() : find maximum in array
3--> min() : find minimumof array                
"""
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)
print(data - ones)
print(data / ones)
print(data * ones)

a = np.array([1,2,3,4,5,6,7,8,9])
d = np.array([[1,2,3,4] , [5,6,7,8]])
b = a.sum()
c = d.sum(axis = 1)
max = a.max()
min = a.min()
print(b)
print(c)
print(max)
print(min)


# Broadcasting

"""
There are times when you might want to carry out an operation between an array and a single number
(also called an operation between a vector and a scalar) or between arrays of two different sizes.

NumPy understands that the multiplication should happen with each cell. That concept is called broadcasting. 
Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes. 
The dimensions of your array must be compatible, 
for example, when the dimensions of both arrays are equal or when one of them is 1

"""

a = np.array([1,2,3,4,5,6,7])
b = a * pi # pi is multiplied to each element in a i.e called broadcasting

print(b)



# Generating random numbers
# the simplest way to generate random matrices
rng = np.random.default_rng()
matrice = rng.random((3,3))
print(matrice)

val = rng.integers(5 , size=(3,3))
print(val)
