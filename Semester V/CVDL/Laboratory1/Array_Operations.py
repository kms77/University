import numpy as np

print('Array operations')

"""

Numpy provides functions and operator overload for various arithmetical 
operations on the arrays, such addition, subtraction, multiplication, dot products etc.

Attention!! np.multiply performs element wise multiplication. 
If you want to perform matrix multiplication, you should use the np.dot function !!

"""

# array operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])

print('a is: ', a)
print('b is: ', b)
# elementwise operations
print('a+b is: ', a+b)
print('a+b is: ', np.add(a, b))

print('a-b is: ', a-b)
print('a-b is: ', np.subtract(a, b))

print('The maximum element in a is: ', np.amax(a))
# by default it returns the max in the flattened array
print('The position of this element in a is: ', np.argmax(a))

print('|a-b| is: ', np.abs(a-b))

print('a*b (element wise) is: ', a*b)
print('a*b (element wise) is: ', np.multiply(a, b))

v = np.array([10, 20])
w = np.array([11 , 11])
print('Dot product v x w is: ', v.dot(w))
print('Dot product v x w is: ', np.dot(v, w))

print('Dot product a x v (matrix x vector) is: ', a.dot(v))
print('Dot product a x b (matrix x matrix) is: ', a.dot(b))

print('Dot product a x v (matrix x vector) is:\n', a.dot(v))
print('Dot product a x b (matrix x matrix) is:\n', a.dot(b))
print('---')