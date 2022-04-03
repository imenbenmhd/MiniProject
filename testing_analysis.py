"""Test unit for analysis code"""

import analysis
import numpy as np


def analysis_mae(predictions, true_labels, expected):
    """Runs a single test case for MAE
    Parameters
    ==========
    predictions : list
        A list of integer predictions to input
    true_labels : list
        Ground truth values to compare to
    expected : float
        The expected mean absolute error rate
    Raises
    ======
    AssertionError
        In case something goes wrong
    """

    predictions = np.array(predictions)
    true_labels = np.array(true_labels)

    mae = analysis.mean_abs_err(predictions, true_labels)

    assert np.isclose(mae, expected), "Expected %r, but got %r" % (
        expected,
        mae,
    )


def test_MAE_0():
    analysis_mae([0, 1, 0, 1], [0, 1, 0, 1], 0)


def test_MAE_50_50():
    analysis_mae([1, 1, 1, 1], [0, 1, 0, 1], 0.5)


def test_MAE_20_80():
    analysis_mae([1, 1, 0, 1, 1], [1, 1, 1, 1, 1], 0.2)


def test_MAE_1():
    analysis_mae([1, 1, 1, 1], [0, 0, 0, 0], 1)