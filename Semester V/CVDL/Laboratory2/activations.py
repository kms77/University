import numpy as np


def softmax(x, t=1):
    """"
    Applies the softmax temperature on the input x, using the temperature t
    """
    # TODO your code here
    axis = 1 if len(x.shape) == 2 else None
    x_stabilized = x - np.max(x, axis=axis, keepdims=True)

    return np.exp(x_stabilized / t) / np.sum(np.exp(x_stabilized / t), axis=axis, keepdims=True)
    # end TODO your code here
