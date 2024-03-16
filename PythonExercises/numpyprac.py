import numpy as np

#In contrast to lists in python you numpy arrays
#are designed to contain element of the same type
a = np.array([1, 2, 3, 4], np.float32)
#np.arange similar to the python range function.
np.arange(2.0, 2.4, 0.1)
#create array of 4 elements that are zeros:
print(np.zeros(4))

arr = np.arange(1, 4) #returns nd-array
print(arr)
#Automatically applies the cosinus func to all elements!!
print(np.cos(arr))
#create array with random values between 0 and 1 of size 3
print(np.random.rand(3))

#create array of size 5 with random values between 1 and 3 excluding 3
print(np.random.randint(1, 3, 5))

average_of_10000_throws = np.average(np.random.randint(1, 7, size=(10000, 2)).sum(axis=1))
print("average: {}".format(average_of_10000_throws))

print(np.random.randint(1, 7, size=(10000, 2)).shape)

#Initialize zero array with specific shape/dimensions:
#Below is example with 2 rows and 3 columns
print(np.zeros(shape=(2, 3)))
#can also do this with random values:
print(np.random.random((2,3)))
#indexing into multidimensional arrays:
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#this prints 7
print(arr1[1,2])
#this prints [1 2 3]
#it states that we should enter the first row and then take
#from the first til the 3 index not including the element on the last index (kinda like range)
print(arr1[0,0:3])
#if you want all values in a given dimension just use :
print(arr1[:,1]) # should print [2 6]
#Defining a:
a = np.array([[1, 2 ,3],[4, 5, 6], [7, 8, 9]])
#Defining b as the first 2 rows and cols of a
b = a[0:2, 0:2]
#changing element on index [0,0] in b
b[0,0] = 8
#noticing it also changes a???
print(a)
#slices are references. Use np.copy to make copys!!
b = np.copy(a[0:2, 0:2])
print(b)
#almost everything in python happens by reference.



