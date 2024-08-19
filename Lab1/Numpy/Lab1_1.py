#NumPy as np
import numpy as np 
#Create a NumPy ndarray Object
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#0-D Arrays
arr1 = np.array(42,ndmin=5)
#2-D Arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#3-D Arrays
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#Creating Arrays With a Defined Data Type
arr4 = np.array([1, 2, 3, 4], dtype='S')
#Converting Data Type on Existing Arrays
newarr = arr.astype(bool)
#Array test Copy and view
arr5 = np.array([1, 2, 3, 4, 5])
#Iterating Arrays
arr6 = np.array([1, 2, 3])
arr6_1 = np.array([5, 6, 7])

#Check Number of Dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(arr)
print(arr1)
print(arr2)
print(arr3)

print('number of dimensions :', arr1.ndim)
#Access Array Elements
print(arr[0])
#Access 2-D Arrays
print('2nd element on 1st row: ', arr2[0, 1])
#Access 3-D Arrays
print(arr3[0, 1, 2])
#Negative Indexing
print('Last element from 2nd dim: ', arr2[1, -1])
#Slicing arrays
print(arr[2:5])
print(arr[4:])
print(arr[:4])
#Negative Slicing
print(arr[-3:-1])
#STEP
print(arr[1:5:2])
#Slicing 2-D Arrays
print(arr2[1, 1:4])
#Checking the Data Type of an Array
print(arr.dtype)
print(arr4)
print(arr4.dtype)
#Converting Data Type on Existing Arrays
print(newarr)
print(newarr.dtype)
#Copy
x = arr5.copy()
arr5[0] = 42

print(arr5)
print(x)
#View
x = arr5.view()

print(arr5)
print(x)
#Get the Shape of an Array
print(arr2.shape)
#Reshape From 1-D to 2-D
newarr = arr.reshape(4, 3)
print(newarr)
#Reshape From 1-D to 3-D
newarr1 = arr.reshape(2, 3, 2)
print(newarr1)
#Iterating Arrays
for x in arr6:
  print(x)

#Iterating 2-D Arrays  
for x in arr2:
  print(x)
#Iterating 3-D Arrays
for x in arr3:
  print(x)
#Iterating Arrays Using nditer()
for x in np.nditer(arr3):
  print(x) 
#Iterating Array With Different Data Types
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
#Iterating With Different Step Size
for x in np.nditer(arr2[:, ::2]):
  print(x)
#Enumerated Iteration Using ndenumerate()
for idx, x in np.ndenumerate(arr):
  print(idx, x)
#Joining NumPy Arrays
arr7 = np.concatenate((arr5, arr6))
print(arr7)
#Stacking Along Rows
arr8 = np.hstack((arr5, arr6))

print(arr8)
#Stacking Along Columns
arr9 = np.vstack((arr6_1, arr6))

print(arr9)
#Stacking Along Height (depth)
arr10 = np.dstack((arr6_1, arr6))

print(arr10)
#Splitting NumPy Arrays
newarr = np.array_split(arr5, 3)

print(newarr)
#Split Into Arrays
newarr = np.array_split(arr5, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
#Splitting 2-D Arrays
arr11 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr11, 3)

print(newarr)
#Searching Arrays
arr12 = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr12 == 4)

print(x)
#Search Sorted
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
#Sorting Arrays
print(np.sort(arr))
#Sorting a 2-D Array
print(np.sort(arr2))
#Filtering Arrays
arr12 = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr12[x]

print(newarr)
#Creating the Filter Array
    #Create an empty list
filter_arr = []

# go through each element in arr
for element in arr12:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr12[filter_arr]

print(filter_arr)
print(newarr)
#Checking NumPy Version
print(np.__version__)

