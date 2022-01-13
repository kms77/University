import numpy as np

print('Rank, Shape, Type')

""""

We'll frequently use the numpy library for this lecture; numpy is perhaps the most popular library 
used for scientific computing in Python. numpy works with multidimensional arrays, and provides several 
operations to efficiently manipulate these arrays.

An array contains elements of the same type, arranged in a grid of values. 
An array can be accessed by a tuple of non-negative integers, by booleans, by another array, or by integers, 
as we'll see later in this laboratory.

An array is described by its:

rank - the number of dimensions of the array
shape - a tuple that specifies the size of the array along each dimension
type - the library provides several numeric datatypes (uint8, float32, int32 etc.)
There are several ways you can create an array in numpy:

"""
# create an array with rank 1
a =  np.array([1,2,3])
print('a is a numpy array ', type(a))
print('the shape of a is ', a.shape, 'and its rank is ', len(a.shape))
print('the type of the elements stored in a is ', a.dtype)
print('---')

b = np.array([[1.0, 2, 3], [4, 5, 6]])
print('the shape of b is ', b.shape, ' and its rank is ', len(b.shape))
print('the type of the elements stored in b is ', b.dtype)
print('---')
# numpy automatically determines the type of the elements that will be stored in the array
# but you can also specify the type in the constructor

c = np.array([[[0]]], dtype=np.uint8)
print('the shape of c is ', c.shape, ' and its rank is ', len(c.shape))
print('the type of the elements stored in c is ', c.dtype)
print('---')

# there are also other array constructors that you might find useful
# creates an array filled with 0s of shape (1, 2) - 1 row, two columns
a = np.zeros(shape=(1,2))
print('zeros array {} of shape {}'.format(a, a.shape))
print('---')

# creates an array filled with ones of shape (224, 224, 3) and type uint8
b = np.ones((224, 224, 3), dtype=np.uint8)
print('ones array {} of shape {}'.format(b, b.shape))
print('---')

# creates an array filled with 255 of shape (4, 4, 3)
c = np.full((4, 4, 3), 255)
print('array of 255 elements {} of shape {}'.format(c, c.shape))
print('---')

# creates an identity matrix of size (3x3)
d = np.eye(3)
print('identity matrix of size 3x3 ', d)
print('---')

# creates an array of 10 elements, filled with random values
r = np.random.random(10)
print('array of 10 random elements {} of shape {}'.format(r, r.shape))
print('---')

# create a new array with the same shape as r, but filled with 0 values
zl = np.zeros_like(r)
print('array of 10 random elements with the same shape as r, filled with 0s', zl)
print('---')
