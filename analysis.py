import numpy as np

def mean_abs_err(prediction, true_labels):
    """
    Calculates the mean absolute error
    Parameters
    ==========
    prediction : numpy.ndarray
        A 1D :py:class:`numpy.ndarray` containing your prediction
    true_labels : numpy.ndarray
          A 1D :py:class:`numpy.ndarray` containing the ground truth labels for
          the input array, organized in the same order.
    Returns
    =======
    MAE : float
        The classification error rate
    """

    mae = (np.abs(prediction - true_labels)).sum() / len(prediction)
    return mae