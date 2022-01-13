import cv2
import tensorflow.keras as keras
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

print("Numpy axes")

"""

Another concept that is perhaps confusing for beginners in 
numpy is the concept of axes. As you'll see several mathematical 
functions (np.sum, np.mean, np.min etc.) require you to specify 
the axis along the operation should be applied.

Just as the cartesian coordinate system, numpy arrays have axes. 
For example, for a 2D array, the rows are the first axis (0 axis), 
and the columns are the second axis (axis 1).

"""

"""
image_url = 'http://drive.google.com/uc?export=download&id=1fRvlErNtIV-HX9Vat0I6FINBXEafeDC7'
save_name = 'dance_moves.png' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
image_url = 'https://docs.google.com/uc?export=download&id=1zjltpYscUqnDSP6eUlU-gecadGXvQtTz'
save_name = 'cute_cat.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
image_url = 'http://drive.google.com/uc?export=download&id=1y46KaIsyhgh030Zi9eoAYfO_ezkE4CY3'
save_name = 'axes.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
image_url = 'http://drive.google.com/uc?export=download&id=11Jzu1t1RVXMWxp0OK3KJaUgKv9exqv2O'
save_name = 'sum0.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
image_url = 'http://drive.google.com/uc?export=download&id=1LUYh0HtP6Vd2eq7rPXOhXjBKXlvU--L5'
save_name = 'sum1.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
image_url = 'http://drive.google.com/uc?export=download&id=1q_BsBdLZXxA2fkrY1WXWn8B5RGOFBLUd'
save_name = 'concat0.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
image_url = 'http://drive.google.com/uc?export=download&id=1491c1NZQMOnHlvVp6eiiIl2l1wYO6o56'
save_name = 'concat1.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
"""

img_axes = cv2.imread('axes.jpg')
dpi = plt.rcParams['figure.dpi']
height, width, depth = img_axes.shape
figsize = width/ float(dpi), height/float(dpi)
plt.figure(figsize=figsize)
plt.imshow(img_axes)
plt.show()
print('---')

"""
np.sum(a, axis = 0)
Is is important to understand, for each operation, what the axis element controls.
For the common mathematical operations, which for example aggregate your data, 
the axis parameter controls which axis will be collapsed.
So, for example, if you have an array a, and you perform the operation np.sum(a, axis = 0), 
the rows will be collapsed and this will sum down the columns. (It will not sum the rows).
"""

img_sum0 = cv2.imread('sum0.jpg')
dpi = plt.rcParams['figure.dpi']
height, width, depth = img_sum0.shape
figsize = width / float(dpi), height / float(dpi)
plt.figure(figsize=figsize)
plt.imshow(img_sum0)
plt.show()
print('---')


"""
np.sum(a, axis = 1)
Similarly, if you have an array a, and you perform the operation np.sum(a, axis = 1), 
the columns will be collapsed and this will sum down the rows. (It will not sum the columns).
"""
img_sum1 = cv2.imread('sum1.jpg')
dpi = plt.rcParams['figure.dpi']
height, width, depth = img_sum1.shape
figsize = width/float(dpi), height/float(dpi)
plt.figure(figsize=figsize)
plt.imshow(img_sum1)
plt.show()

"""
np.concatenate([a,b], axis=0)
Another example, for the concatenation operation, the axis 
operator specifies the axis along which to stack the arrays.
If we specify the axis = 0 for concatenation, the arrays 
will be stacked along the rows (they will be concatenated vertically).
"""

img_concat0 = cv2.imread('concat0.jpg')
dpi = plt.rcParams['figure.dpi']
height, width, depth = img_concat0.shape
figsize = width / float(dpi), height / float(dpi)
plt.figure(figsize=figsize)
plt.imshow(img_concat0)
plt.show()

"""
np.concatenate([a,b], axis=1)
If we the axis = 1 for concatenation, the arrays will 
be stacked along the columns (they will be concatenated horizontally).
"""

img_concat1 = cv2.imread('concat1.jpg')
dpi = plt.rcParams['figure.dpi']
height, width, depth = img_concat1.shape
figsize = width / float(dpi), height / float(dpi)
plt.figure(figsize=figsize)
plt.imshow(img_concat1)
plt.show()
print('---')


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('The sum of each column is: \n', np.sum(a, axis = 0))
print('The sum of each row is: \n', np.sum(a, axis = 1))

b = np.array([[1, 1, 1, 1], [2, 2, 2, 2]])
print('Concatenate vertically: \n', np.concatenate([a, b], axis = 0))
print('Concatenate horizontally: \n', np.concatenate([a, b], axis =1))
print('---')

# example with 1D arrays
a = np.array([0, 0, 0])
b = np.array([1, 1, 1])
# attention! 1D arrays have only one axis
print(np.concatenate([a, b], axis = 0))

a = a.reshape((1, 3))
b = b[np.newaxis, :]
print("a = ", a)
print("b = ", b)

print(np.concatenate([a, b], axis = 0))
print('---')