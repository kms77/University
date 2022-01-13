import numpy as np

print("Broadcasting")
print("\n")

"""

Broadcasting is a numpy features that allows us to perform operations on arrays with different shapes; 
frequently we may need to work with arrays with different size and apply some operations on these arrays. 
With broadcasting, if the arrays don't have the same size, the smaller size array is "broadcast" to 
match the shape of the larger array. This also helps with vectoring array operations.

To be able to broadcast, the size of the arrays in the trailing axes must be the same, or one of these 
dimensions must be 1. If the arrays don't have the same rank, we add 1 dimensions to the left 
(prepend the shape property with ones), until the arrays have the same rank.

Always, the result of broadcasting is the maximum size along each dimension from the input arrays.

You can check this tutorial for further information: 
http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc

"""

# shape: (3, 3)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("a= \n", a)
print("\n")

# shape: (3)
b = np.array([0, 1, 2])
print("b= \n", b)
print("\n")

# shape: (1, 3)
x1 = np.array([[1, 2, 3]])
print("x1= \n", x1)
print("\n")

# shape: (3, 1)
x2 = np.array([1, 2, 3]).reshape((3,1))
print("x2= \n", x2)
print("\n")

print("x1 + x2= \n", x1 + x2)
print("\n")

s = a + b
print("s= \n", s)
print("\n")

# the code snippet above is equivalent to the code below (but without making unnecessary copies)
print(b.shape)
# this stacks 3 copies of b -> (3, 3)
b_expanded = np.tile(b, (3,1))
print("b_expanded.shape: ", b_expanded.shape)
print("b_expanded: \n", b_expanded)
print("\n")
s = a + b_expanded
print("a + b_expanded= \n", s)
print("\n")

# add a vector to each column of a matrix
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([0, 2])
# transpose the matrix a (a.T) such that is has shape (3, 2), the array b has shape (2,)
# they can be broadcast together and then we can transpose the result
print("a.T= \n", a.T)
print("\n")
print("(a.T + b= \n", a.T + b)
print("\n")
print("(a.T + b).T = \n", (a.T + b).T)
print("\n")

a = np.array([0, 1, 2, 3])
b = np.array([4 ,5 ,6])
print("Shape of a: ", a.shape)
print("a= \n", a)
print("\n")
print("Shape of b: ", b.shape)
print("b= \n", b)
print("\n")
try:
    print("a+b= \n", a+b)
    print("\n")
except ValueError:
    print('Unable to broadcast arrays with shapes ', a.shape, b.shape)

a = a.reshape((4, 1))
# or you might see this syntax: a = a[:, np.newaxis]
print("Shape of a: ", a.shape)
print("Shape of b: ", b.shape)
print("a+b= \n", a+b)
print("\n")
print("Shape of a+b: ", (a+b).shape)