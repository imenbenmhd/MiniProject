"""Test unit for result code"""

from . import result
import numpy as np

def mae_size(data, norm, expected):
    """Runs a single test case for size of MAE table
    Parameters
    ==========
    data : int
        Dataset to analyze
    norm : int
        Normalization method
    expected : tuple
        The expected dimension of table
    Raises
    ======
    AssertionError
        In case something goes wrong
    """

    mae = result.test_mae(data, norm)[0].shape

    assert np.isclose(mae, expected), "Expected %r, but got %r" % (
        expected,
        mae,
    )

def test_norms_01():
    mae_size(0, 1, (3, 2))

def test_norms_12():
    mae_size(1, 2, (3, 2))