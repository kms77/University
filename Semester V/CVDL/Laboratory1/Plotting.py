import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Plotting")

"""

During this course we'll frequently create plots to show the distribution of some data, 
to show the performance of the developed models etc. We'll use the matplotlib library for this.

Using this library is straightforward, and the function that we'll use the most is plot(). 
You can check more about this library in the documentation: https://matplotlib.org/3.3.1/contents.html .

For example, to display a sine wave we could do the following:

"""
"""
# compute the x range
x = np.arange(0 ,5 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)

# set the title ant the name of the x and y axes
plt.title('Sine function')
plt.ylabel('sine value')

# show the figure
plt.show()
print('---')


# We can plot different data in the same plot using subplot. Below is an example:
# compute the x range
x = np.arange(0, 2 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# parameters: 1 - one row, 2 - two columns, 1 - first column from the two
# subplot with 1 row and 2 columns
# the first subplot is the active one
plt.subplot(1, 2, 1)

# make the first plot
plt.plot(x, y_sin)
plt.grid(True)
plt.title('Sine')

# active the second plot
plt.subplot(1, 2, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# adjust the spacing between the plots
plt.subplots_adjust(wspace=0.5)
plt.show()
"""

"""
You might be familiar from the Artificial Intelligence class with some of the activation 
functions used in neural networks: ReLU, tahh, sigmoid and their friends. In the image below 
you have the common activation functions depicted as dance moves.
Pick your favourite three "dance moves" and plot them with matplotlib using subplots. 
"""

dance_moves_img = cv2.imread('dance_moves.png')
dpi = plt.rcParams['figure.dpi']

height, width, depth = dance_moves_img.shape
figsize = width / float(dpi), height / float(dpi)
plt.figure(figsize=figsize)
plt.imshow(dance_moves_img)

"""
Sigmoid
The main reason why we use sigmoid function is because it exists between (0 to 1). 
Therefore, it is especially used for models where we have to predict the probability as 
an output.Since probability of anything exists only between the range of 0 and 1, 
sigmoid is the right choice.
"""

x = np.linspace(-10, 10)
y = 1 / (1 + np.exp(-x))
plt.figure(figsize=(10, 5))
plt.grid(True)
plt.plot(x, y)
plt.legend(['Sigmoid function'])
plt.title('Sigmoid Function')
plt.show()

"""
ReLU - Rectified Linear Unit
The ReLU is the most used activation function in the world right now.Since, it is used in almost 
all the convolutional neural networks or deep learning.
f(z) is zero when z is less than zero and f(z) is equal to z when z is above or equal to zero.
Range: [ 0 to infinity)
The function and its derivative both are monotonic.
But the issue is that all the negative values become zero immediately which decreases the ability 
of the model to fit or train from the data properly. That means any negative input given to the ReLU 
activation function turns the value into zero immediately in the graph, which in turns affects the 
resulting graph by not mapping the negative values appropriately.
"""

x = np.linspace(-10, 10)
y = np.maximum(0, x)
plt.figure(figsize = (10, 5))
plt.grid(True)
plt.plot(x, y)
plt.legend(['ReLU function'])
plt.title('Rectified Linear Unit Function')
plt.show()


"""
Tanh
Tanh is also like logistic sigmoid but better. The range of the tanh function is from (-1 to 1). 
Tanh is also sigmoidal (s - shaped).
The advantage is that the negative inputs will be mapped strongly negative and the zero inputs 
will be mapped near zero in the tanh graph.
"""

x = np.linspace(-10, 10)
y = ( 2 / (1 + np.exp(-2*x) ) ) -1
plt.figure(figsize = (10, 5))
plt.grid(True)
plt.plot(x, y)
plt.legend(['Tanh function'])
plt.title('Tanh Function')
plt.show()