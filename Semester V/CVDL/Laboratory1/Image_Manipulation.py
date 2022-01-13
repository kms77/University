import cv2
import matplotlib.pyplot as plt
import numpy as np

print("Image Manipulation")

"""

Computer vision is about images (or image sequences), so you'll definitely need some 
image manipulation skills. For now, we'll just need some functions to read and write images.
We'll use the opencv library to work images; opencv is an open-source, cross-platform computer 
vision library and it support a variety of programming languages (C++, Python, Java).
The python version of opencv is very simple and it allows you to express your brilliant ideas 
in fewer line of codes, while maintaining a high readability of the code.

"""

print('---')
print("Reading, writing and displaying an image")

"""
To read an image you'll use the <i>imread</i> function from the opencv library. 
To display an image you can use the <i>imshow</i> function from the matplolib library . 
Pretty simple, isn't it? 
"""

# BGR , RGB
# BGR -> RGB
img = cv2.imread('cute_cat.jpg')
# opencv uses BGR channel ordering, while matplotlib uses RGB channel ordering
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

"""
An image is essentially just a numpy array. The type of the elements stored in this array is np.uint8, 
so each element ranges from 0 (corresponding to the black color in grayscale images) and 255 (corresponding 
to the white color in grayscale images).
To get the size of the image, we can use the size attribute.
"""

img_height, img_width, img_channels = img.shape[0], img.shape[1], img.shape[2]
print('The image resolution is ', img_width, 'x', img_height)
print('The number of channels is ', img_channels)

# You can use the function imresize to change the resolution of an image.
# resize image to(120, 400) - breaks the aspect ratio
img_resize_fixed = cv2.resize(img, (120, 400))
print('The shape of the resize image is:', img_resize_fixed.shape)
plt.imshow(img_resize_fixed)
plt.show()

# resize the image to w/4 x h/4 (keeps the aspect ratio)
img_resize_prop = cv2.resize(img, (0,0), fx = 0.25, fy = 0.25)
print('The shape of the resize image is:', img_resize_prop.shape)
plt.imshow(img_resize_prop)
plt.show()

"""
A color image consists of 3 image channels (the red, green and blue channels).
A grayscale image has a single channel. One way of converting a color image to grayscale is using the equation:
Gray = 0.2126 R + 0.7152 G + 0.0722 B
,where R, G and B are the red, green and blue channels of the input image.
"""

img_gray = 0.2126 * img_resize_prop[:, :, 0] + 0.7152 * img_resize_prop[: , :, 1] + 0.0722 * img_resize_prop[:, :, 2]
img_gray = img_gray.astype(np.uint8)
# use cmap='gray' (colormap) to display a grayscale image
plt.imshow(img_gray, cmap= 'gray', vmin=0, vmax=255)
plt.show()

"""
A histogram is graphical representation of the grayscale values (or color tones in the input image). 
From a histogram we can determine statistical properties of the image, such as the average brightness 
and the contrast of the image.
"""

# [0-255], 256
hist, bins = np.histogram(img_gray, bins=255)
print('The histogram is:\n', hist)
plt.bar(np.arange(255), hist, color='cornflowerblue')
plt.title('Histogram of the grayscale image')
plt.show()

"""
Plot the histograms of the red, blue and green channel of an image on the same plot. 
The histogram of the red channel should be displayed in red bars, the histogram of the 
blue channel should be displayed in blue bars and the histogram of the green channel should 
be displayed with green bars.
"""
img_cat = cv2.imread('cute_cat.jpg')
img_cat = cv2.cvtColor(img_cat, cv2.COLOR_BGR2RGB)
img_cat = cv2.resize(img_cat, (0,0), fx = 0.25, fy = 0.25)
hist, bins = np.histogram(img_cat[:,:,0], bins=255)
plt.xlim([0, 256])
#plt.subplot(3, 1, 1)
plt.bar(np.arange(255), hist, color='red')
#plt.title('Histogram of the red channel')

hist, bins = np.histogram(img_cat[:,:,1], bins=255)
#plt.subplot(3, 1, 2)
plt.bar(np.arange(255), hist, color='green')
#plt.title('Histogram of the green channel')

hist, bins = np.histogram(img_cat[:,:,2], bins=255)
#plt.subplot(3, 1, 3)
plt.bar(np.arange(255), hist, color='blue')
#plt.title('Histogram of the blue channel')

#plt.subplots_adjust(hspace=0.7)
plt.title('Histogram of the red, green and blue channels')
plt.show()

"""
Add to each element in the grayscale image with a positive number and store the result in img_l1.
What do you think is the effect of this operation? Display the image img_l1. Make sure that the 
result is in the range [0, 255].
"""
number = 100
img = cv2.imread('cute_cat.jpg')
# BGR to RGB
img_cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray_cat = 0.2126 * img_cat[:, :, 0] + 0.7152 * img_cat[: , :, 1] + 0.0722 * img_cat[:, :, 2]
img_l1 = np.clip(img_gray_cat + number, 0, 255)
img_l1 =  img_l1.astype(np.uint8)
plt.subplot(1,2,1)
plt.imshow(img_gray_cat, cmap= 'gray', vmin=0, vmax=255)
plt.title('Image before addition')
plt.subplot(1,2,2)
plt.imshow(img_l1, cmap= 'gray', vmin=0, vmax=255)
plt.title('Image after addition')
plt.subplots_adjust(wspace=0.5)
plt.show()
# The image gets brighter after the addition

"""
Compute and display the histogram of img_l1.  What do you notice? How is this histogram different 
than the previous one?
"""

hist, bins = np.histogram(img_gray_cat, bins=255)
print("Histogram before addition: \n", hist)
plt.subplot(2, 1, 1)
plt.title('Histogram before addition')
plt.bar(np.arange(255), hist, color='red')

hist, bins = np.histogram(img_l1, bins=255)
print("Histogram after addition: \n", hist)
plt.subplot(2, 1, 2)
plt.title('Histogram after addition')
plt.bar(np.arange(255), hist, color='red')
plt.subplots_adjust(hspace=0.7)
plt.show()

# The histogram is shifted to the right


"""
Now add to the grayscale image a negative number and store the result in img_l2. 
If the resulting value is less than 0, clamp it to this 0. What do you think is 
the effect of this operation?
"""

number = 80
img = cv2.imread('cute_cat.jpg')
# BGR to RGB
img_cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray_cat = 0.2126 * img_cat[:, :, 0] + 0.7152 * img_cat[: , :, 1] + 0.0722 * img_cat[:, :, 2]
img_l2 = np.clip(img_gray_cat - number, 0, 255)
img_l2 = img_l2.astype(np.uint8)
plt.subplot(1,2,1)
plt.imshow(img_gray_cat, cmap= 'gray', vmin=0, vmax=255)
plt.title('Image before subtraction')
plt.subplot(1,2,2)
plt.imshow(img_l2, cmap= 'gray', vmin=0, vmax=255)
plt.title('Image after subtraction')
plt.subplots_adjust(wspace=0.5)
plt.show()
# The image gets darker after the subtraction

"""
Compute and display the histogram of img_l2. What do you notice? How is this histogram 
different than the previous ones?
"""

hist, bins = np.histogram(img_gray_cat, bins=255)
print("Histogram before subtraction: \n", hist)
plt.subplot(2, 1, 1)
plt.title('Histogram before subtraction')
plt.bar(np.arange(255), hist, color='red')

hist, bins = np.histogram(img_l2, bins=255)
print("Histogram after subtraction: \n", hist)
plt.subplot(2, 1, 2)
plt.title('Histogram after subtraction')
plt.bar(np.arange(255), hist, color='red')
plt.subplots_adjust(hspace=0.7)
plt.show()

# The histogram is shifted to the left according to the subtracted number

"""
Add a positive number (for example 40) to the red channel of the color image and store the 
result in imgg. If the result of the addition exceeds 255, clamp it to 255. What do you think 
is the effect of this operation? Display the resulting image imgr.
"""

img = cv2.imread('cute_cat.jpg')
# BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.title('Image before')
plt.imshow(img)
img = cv2.imread('cute_cat.jpg')
# BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_red = img + np.array([40, 0, 0])
img_red = np.clip(img_red, 0, 255)
cv2.imwrite('imgg.png', img_red)
plt.subplot(1, 2, 2)
plt.title('Image after')
plt.imshow(img_red)
plt.show()

# makes the image reddish


"""
Display a region of interest from the input image defined by the rectangle (x=350, y=400, sz=(500x400)).
Hint: an image is just a numpy array, so you can easily achieve this with array slicing.
"""
img = cv2.imread('cute_cat.jpg')
# BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
x = 350
y = 400
sz = (500, 400)
img = img[x:x+sz[0], y:y+sz[1], :]
plt.imshow(img)
plt.show()
