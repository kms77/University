import numpy as np

print('Indexing')

a = np.array([1, 2 ,3])
print('a is ', a)
a[2] = 4
print('Set the 2nd element to 4')
print('Modified a is:')
print(a)

print('---')
b = np.eye(3)
print('Set the 2nd element from the second row to 2')
b[1, 1] = 2
print('Modified b is:')
print(b)

# you can use normal integer indexing
print('The first row of b is: ', b[0])
print('The second element from the second row of b is: ', b[1, 1])
print('---')


# Slicing
"""
Similar to python lists, numpy allows you to slice the array; this is just a flexible way to access subarrays.
"""
# returns an array with evenly spaced values in the interval [1, 10), with a step of 1
a = np.arange(1, 10, 1)
print('a is: ', a)
# get a slice from index 3 to 6 (exclusive)
print('a[3:6] is: ', a[3:6])
# get a slice from index 3 to the end
print('a[3:] is: ', a[3:])
# get a slice from the start to index 3 (exclusive)
print('a[:3] is: ', a[:3])
# get a slice from index 4 start to the last element of the array (exclusive)
print('a[4:-1] is: ', a[4:-1])
print('---')

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print('a: ', a)

## ATTENTION! a slice is just a view on an array, so it points to the same data
# modifying it, it will modify the original array

r = a[:1, :]
print('row1: ', r)
print('a[0][0]: ', a[0][0])
print('r[0][0]: ', r[0][0])
print('r[0][0] = 100')
r[0][0] = 100
print('row1: ', r)
print('a[0][0]: ', a[0][0])
print('r[0][0]: ', r[0][0])
print('---')


#integer array indexing
"""
Numpy also support integer array indexing.
Attention, there is a slight (and important) difference when using integer array indexing: when using 
slicing, the result will also be a subarray of the existing array (a view on the existing array), 
while integer array indexing allows you to create new arrays based on the the data in the original array.
"""
a = np.array(np.arange(0,6,1))
indices = [0, 2, 4]
# this will get the elements from the indices 0, 2, 4 from the array a
b = a[indices]
print('original array: \n', a)
print('The elements in a from the indices', indices, 'are: \n', b)
print('---')

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# this will get the elements from the indices (0, 2), (1, 1) and (2, 0) from the array a
indices = [[0, 1, 2], [2, 1, 0]]
# b will be [3, 6, 9]
b = a[tuple(indices)]
print('original array: \n', a)
print('The elements in the array at indices', indices, 'are: \n', b)
print('---')

# modifying this array, won't modify the original array
print(b)
b[0] = 100
print('b[0] = 100')
print('a = ', a)
print('b = ', b)
print('---')

print('More array indexing examples: ')
# with array indexing you can reuse the same index from the original array
b = a[[0 ,0], [1, 1]]
print('b = ', b)
# equivalent to
b = [a[0, 1], a[0, 1]]
print('b = ', b)
print('---')

print('Using array indexing to modify an element from each row in a matrix: ')
# modifing an element from each row in a matrix
ind = np.array([1, 0, 1])
a[np.arange(3), ind] = -100
print('a = ', a)


# mix array indexing with array slicing
"""
Array indexing can be mixed with slicing. When using slicing the resulting array will 
have the same rank as the original array, while when using array indexing you will get 
an array with a lower rank than the original array.
"""
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
last_row_indexing = a[-1, :]
last_row_slicing = a[2:3, :]
print('Last row obtained with array indexing: \n', last_row_indexing, 'has shape: ', last_row_indexing.shape)
print('Last row obtained with array slicing: \n', last_row_slicing, 'has shape: ', last_row_slicing.shape)
print('---')


# boolean array indexing
"""
numpy also allows you to use boolean array indexing, in which an array of 
booleans is used as a mask to select arbitrary elements in the array.
"""
a = np.array([11, 12, 13, 14])
indices = (a > 12)
# a > 12 returns an array of boolean of the same size as a:
# an element in this array is True is the element stored in the same position in a is larger than 12
print('a>12:\n', indices)
print('The numbers larger than 12 in a are:\n', a[indices])
print('---')