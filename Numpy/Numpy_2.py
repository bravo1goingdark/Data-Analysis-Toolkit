# Q --> How to convert a 1D array into a 2D array

"""
1 --> np.newaxis : will increase the dimensions of your array by one dimension when used once.
2 --> np.expand_dims : expand an array by inserting a new axis at a specified position 

"""
import numpy as np

arr = np.array([1,2,3,4,5,6])
var = arr.shape
print(var)

newarr = arr[np.newaxis , :]
col_vector = arr[:, np.newaxis]
var = newarr.shape
col = col_vector.shape
print(var)
print(col)

arr = np.array([1,2,3,4,5,6])
newarr = np.expand_dims(arr, axis = 1)
newarr1 = np.expand_dims(arr, axis = 0)
var = newarr.shape
var1 = newarr1.shape
print(var)
print(var1)



# indexing and slicing

data = np.array([1,2,3,4,5])
a1 = data[0]
a2 = data[0:3]
a3 = data[1:]
a4 = data[-3:]
print(a1)
print(a2)
print(a3)
print(a4)


# selecting values from your array that fulfill certain conditions
"""
1--> np.nonzero() :  to select elements or indices from an array.

"""


arr = np.array([[1,2,3,4,5] ,[6,7,8,9,10] , [11,12,13,14,15]])
arrsliced = arr[arr < 5]
arrsliced1 = arr[arr % 2 == 0]
arrsliced2 = arr[(arr > 2) & (arr < 10)]
arrsliced3 = arr[(arr > 5) | (arr == 5)]
print(arrsliced)
print(arrsliced1)
print(arrsliced2)
print(arrsliced3)


"""
a tuple of arrays was returned: one for each dimension.
The first array represents the row indices where these values are found, 
and the second array represents the column indices where the values are found.

b = np.nonzero(arr < 5)
print(b)
Output:---> (array([0, 0, 0, 0], dtype=int64), array([0, 1, 2, 3], dtype=int64)) 

"""
b = np.nonzero(arr > 5) ### above code
print(b)

# better way to write above code  
list_of_coordinates= list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    print(coord)
