import cv2
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import decode_predictions
from keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
import matplotlib.pyplot as plt
import urllib.request


model = ResNet50(weights='imagenet')

image_url = 'https://docs.google.com/uc?export=download&id=1X9au_JCNv4fg2Wgsr4DFT-N0OZht6Zmp'
save_name = 'elephant.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)

"""

In the last part of this introductory laboratory, you'll "meet" a convolutional network for object classification.
For now, consider it just as a black box that takes an image as input and outputs the 3-top predictions; however
this network requires that the input data has the following properties:
- the size of the input image must be 224x224
- the channels of the image should be stored in BGR format
- the type of the data (of the numpy array) is float32
- the values [103.939, 116.779, 123.68] (BGR mean) should be subtracted from each pixel of the array
- prior to feeding the image to model.predict() should be added such that the shape of the image is (1, 224, 224, 3)
Your task is to pre-process the input images such that they are in the format requested by the network.

"""

img_path = './elephant.jpg'
img = cv2.imread(img_path)

# image is stored in BGR format
img = img.astype(np.float32)
img_resized = cv2.resize(img, (224, 224))
img_resized = img_resized - np.array([103.939, 116.779, 123.68])
img_resized = img_resized[np.newaxis, :, :, :]

# image = preprocess_input(img_resized)
preds = model.predict(img_resized)

# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
predictions = decode_predictions(preds, top=3)[0]
print('The top 3 predictions are: ')
for pred in predictions:
    print('\t %s with probability %0.2f%%'% (pred[1], float(pred[2])*100))


"""

Apply different effects (crop it, lower the contrast, change the brightness) on the training image and see 
if you can "fool" the network. Also, upload other images from your computer and see what the network predicts.

"""


img_path = './elephant.jpg'
img = cv2.imread(img_path)

img = img[0:200, 400:800, :]
img = np.clip(img, 0, 255)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
img = img.astype(np.float32)
img_resized = cv2.resize(img, (224, 224))
img_resized = img_resized - np.array([103.939, 116.779, 123.68])
img_resized = img_resized[np.newaxis, :, :, :]

preds = model.predict(img_resized)

# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
predictions = decode_predictions(preds, top=3)[0]
print('The top 3 predictions are: ')
for pred in predictions:
    print('\t %s with probability %0.2f%%'% (pred[1], float(pred[2])*100))


# test with some images from my computer

img1 = cv2.imread('elephant_myimage.jpg')
img2 = cv2.imread('dog_myimage.jpg')


img_resized1 = cv2.resize(img1, (224, 224))
img_resized2 = cv2.resize(img2, (224, 224))


plt.subplot(1, 2, 1)
plt.title('Image 1')
plt.imshow(cv2.cvtColor(img_resized1, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title('Image 2')
plt.imshow(cv2.cvtColor(img_resized2, cv2.COLOR_BGR2RGB))
plt.subplots_adjust(wspace=0.5)
plt.show()

img_resized2 = img_resized2.astype(np.float32)
img_resized1 = img_resized1.astype(np.float32)

img_resized2 = img_resized2 - np.array([103.939, 116.779, 123.68])
img_resized2 = img_resized2[np.newaxis, :, :, :]
img_resized1 = img_resized1 - np.array([103.939, 116.779, 123.68])
img_resized1 = img_resized1[np.newaxis, :, :, :]

preds1 = model.predict(img_resized1)
preds2 = model.predict(img_resized2)

# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
predictions = decode_predictions(preds1, top=3)[0]
print('The top 3 predictions for image 1 are: ')
for pred1 in predictions:
    print('\t %s with probability %0.2f%%'% (pred1[1], float(pred1[2])*100))
print('The top 3 predictions for image 2 are: ')
predictions = decode_predictions(preds2, top=3)[0]
for pred2 in predictions:
    print('\t %s with probability %0.2f%%' % (pred2[1], float(pred2[2]) * 100))

"""
Congratulations for reaching this point! This is the end of first laboratory. Next time we'll build 
(from scratch) a simple linear classifier to recognize different objects from images.
"""