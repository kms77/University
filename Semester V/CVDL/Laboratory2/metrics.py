import numpy as np


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, num_classes=None) -> np.ndarray:
    """"
    Computes the confusion matrix from labels (y_true) and predictions (y_pred).
    The matrix columns represent the prediction labels and the rows represent the ground truth labels.
    The confusion matrix is always a 2-D array of shape `[num_classes, num_classes]`,
    where `num_classes` is the number of valid labels for a given classification task.
    The arguments y_true and y_pred must have the same shapes in order for this function to work
    num_classes represents the number of classes for the classification problem. If this is not provided,
    it will be computed from both y_true and y_pred
    """
    conf_mat = None
    # TODO your code here - compute the confusion matrix
    # even here try to use vectorization, so NO for loops

    # 0. if the number of classes is not provided, compute it based on the y_true and y_pred arrays

    # 1. create a confusion matrix of shape (num_classes, num_classes) and initialize it to 0

    # 2. use argmax to get the maximal prediction for each sample
    # hint: you might find np.add.at useful: https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html
    if num_classes is None:
        num_classes = len(np.unique(np.concatenate([y_true, y_pred])))
    conf_mat = np.zeros((num_classes, num_classes))
    np.add.at(conf_mat, (y_true, y_pred), 1)
    # end TODO your code here
    return conf_mat


def precision_score(y_true: np.ndarray, y_pred: np.ndarray, num_classes=None) -> float:
    """"
    Computes the precision score.
    For binary classification, the precision score is defined as the ratio tp / (tp + fp)
    where tp is the number of true positives and fp the number of false positives.
    For multiclass classification, the precision and recall scores are obtained by summing over the rows / columns
    of the confusion matrix.
    num_classes represents the number of classes for the classification problem. If this is not provided,
    it will be computed from both y_true and y_pred
    """
    precision = 0
    # TODO your code here
    if num_classes is None:
        num_classes = len(np.unique(np.concatenate([y_true, y_pred])))
    conf = confusion_matrix(y_true, y_pred)
    if num_classes == 2:
        precision = conf[0, 0] / (conf[0, 0] + conf[1, 0])
    else:
        precision = np.zeros(num_classes)
        tp = np.diag(conf)
        tpfp = np.sum(conf, axis=0)
        np.divide(tp, tpfp, out=precision, where=tpfp != 0)
    # end TODO your code here
    return precision


def recall_score(y_true: np.ndarray, y_pred: np.ndarray, num_classes=None) -> float:
    """"
    Computes the recall score.
    For binary classification, the recall score is defined as the ratio tp / (tp + fn)
    where tp is the number of true positives and fn the number of false negatives
    For multiclass classification, the precision and recall scores are obtained by summing over the rows / columns
    of the confusion matrix.
    num_classes represents the number of classes for the classification problem. If this is not provided,
    it will be computed from both y_true and y_pred
    """
    recall = None
    # TODO your code here
    if num_classes is None:
        num_classes = len(np.unique(np.concatenate([y_true, y_pred])))
    conf = confusion_matrix(y_true, y_pred)
    if num_classes == 2:
        recall = conf[0, 0] / (conf[0, 0] + conf[0, 1])
    else:
        recall = np.zeros(num_classes)
        tp = np.diag(conf)
        tpfn = np.sum(conf, axis=1)
        np.divide(tp, tpfn, out=recall, where=tpfn != 0)
    # end TODO your code here
    return recall


def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    acc_score = 0
    # TODO your code here
    # remember, use vectorization, so no for loops
    # hint: you might find np.trace useful here https://numpy.org/doc/stable/reference/generated/numpy.trace.html
    acc_score = np.trace(confusion_matrix(y_true, y_pred)) / len(y_true)
    # end TODO your code here
    return acc_score


def f1_score(y_true: np.ndarray, y_pred: np.ndarray, num_classes=None) -> float:
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    if num_classes is None:
        num_classes = len(np.unique(np.concatenate([y_true, y_pred])))

    f1 = np.zeros(num_classes)
    multiply = precision * recall
    s = precision + recall
    np.divide(multiply, s, out=f1, where=s != 0)
    return 2 * f1


if __name__ == '__main__':
    pass
    # TODO your tests here
    # add some test for your code.
    # you could use the sklean.metrics module (with macro averaging to check your results)
    from sklearn import metrics

    y_true = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y_pred = np.array([0, 2, 2, 4, 3, 5, 6, 5, 9, 6])
    assert np.allclose(metrics.confusion_matrix(y_true, y_pred), confusion_matrix(y_true, y_pred))

    assert np.allclose(metrics.precision_score(y_true, y_pred, average=None, zero_division=0),
                       precision_score(y_true, y_pred))
    assert np.allclose(metrics.recall_score(y_true, y_pred, average=None, zero_division=0),
                       recall_score(y_true, y_pred))

    assert metrics.accuracy_score(y_true, y_pred) == accuracy_score(y_true, y_pred)

    assert np.allclose(metrics.f1_score(y_true, y_pred, average=None, zero_division=0),
                       f1_score(y_true, y_pred))