import sys

import numpy as np
from lab2.activations import softmax


class SoftmaxClassifier:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.W = None
        self.initialize()

    def initialize(self):
        # TODO your code here
        # initialize the weight matrix (remember the bias trick) with small random variables
        # you might find np.random.randn userful here *0.001
        self.W = np.random.randn(self.input_shape - 1, self.num_classes) * 0.001
        self.W = np.concatenate([self.W, np.ones((1, self.num_classes))], axis=0)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        scores = None
        # TODO your code here
        # 0. compute the dot product between the weight matrix and the input X
        # remember about the bias trick!
        # 1. apply the softmax function on the scores
        # 2, returned the normalized scores
        assert len(X.shape) == 2
        scores = softmax(X.dot(self.W))
        return scores

    def predict(self, X: np.ndarray) -> int:
        label = None
        # TODO your code here
        # 0. compute the dot product between the weight matrix and the input X as the scores
        # 1. compute the prediction by taking the argmax of the class scores
        assert len(X.shape) == 2
        label = np.argmax(X.dot(self.W), axis=1)
        return label

    def fit(self, X_train: np.ndarray, y_train: np.ndarray,
            **kwargs) -> dict:
        history = []

        bs = kwargs['bs'] if 'bs' in kwargs else 128
        reg_strength = kwargs['reg_strength'] if 'reg_strength' in kwargs else 1e3
        steps = kwargs['steps'] if 'steps' in kwargs else 100
        lr = kwargs['lr'] if 'lr' in kwargs else 1e-3

        print(bs, reg_strength, steps, lr)
        # run mini-batch gradient descent
        for iteration in range(0, steps):
            if iteration % 5 == 1:
               print(iteration, history[-1])
            # TODO your code here
            # sample a batch of images from the training set
            # you might find np.random.choice useful
            running_loss = 0.0
            batches = np.arange(0, len(X_train), bs)

            for start in batches:
                end = start + bs
                if start + bs > len(X_train):
                    end = len(X_train)
                indices = list(range(start, end))
                current_bs = end-start

                #indices = np.random.choice(range(len(X_train)), bs)
                X_batch, y_batch = X_train[indices], y_train[indices]
                #linear score function f(Xi) = Xi dot W
                output = X_batch.dot(self.W)
                #subtract a constant c from Xi, If this shifting constant, c is the maximum of the vector, then we can stabilize our softmax computation
                stabilized_output = output - np.max(output, axis=1, keepdims=True)
                #Li = -fyi + log(sum(e^fj))
                loss = -stabilized_output[range(0, current_bs), y_batch].reshape(current_bs, 1) \
                        + np.log(np.sum(np.exp(stabilized_output), axis=1, keepdims=True))

                #Lt = 1/N * sum(Li) + reg_strength*sum(W^2)
                loss = np.mean(loss) + (reg_strength/(2*current_bs))*np.sum(np.power(self.W, 2))
                running_loss += loss

                CT = softmax(output)
                #CTi = s(Xi*W) - (one hot encoded value of the ground truth yi)
                CT[range(current_bs), y_batch] -= 1
                dW = X_batch.T.dot(CT) + reg_strength/current_bs * self.W

                # end TODO your code here
                # compute the loss and dW
                # perform a parameter update

                self.W -= lr * dW
                # append the training loss, accuracy on the training set and accuracy on the test set to the history dict
                history.append(loss)
            if iteration % 20 == 0 and iteration != 0:
                lr /= 10
            history.append(running_loss / len(batches))

        return history

    def get_weights(self, img_shape):
        W = None
        # TODO your code here
        # 0. ignore the bias term
        # 1. reshape the weights to (*image_shape, num_classes)
        W = np.reshape(self.W[:-1], (*img_shape, self.num_classes))
        return W

    def load(self, path: str) -> bool:
        # TODO your code here
        # load the input shape, the number of classes and the weight matrix from a file
        self.W = np.load(path)
        return True

    def save(self, path: str) -> bool:
        # TODO your code here
        # save the input shape, the number of classes and the weight matrix to a file
        # you might find np.save useful for this
        # TODO your code here
        np.save(path, self.W)
        return True
