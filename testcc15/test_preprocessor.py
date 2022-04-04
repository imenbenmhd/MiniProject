"""Test unit for preprocessor code"""

import numpy as np
from . import preprocessor


def test_minmax_0_1():
    X = np.array([[0, 1], [2, 3]])
    X_minmax = preprocessor.MinMaxScaler_(X, feature_range=(0, 1))
    assert np.equal(X_minmax, [[0, 0], [1, 1]]).all()


def test_minmax_04_06():
    X = np.array([[0, 1], [2, 3]])
    X_minmax = preprocessor.MinMaxScaler_(X, feature_range=(0.4, 0.6))
    assert np.equal(X_minmax, [[0.4, 0.4], [0.6, 0.6]]).all()


def test_z_norm():
    X = np.array([[0, 1], [2, 3]])
    X_std_scaler = preprocessor.Standard_Scaler(X)
    assert np.equal(X_std_scaler, [[-1, -1], [1, 1]]).all()


def test_poly_z():
    X = np.array([[0, 1], [2, 3], [4, 5]])
    X_poly = preprocessor.PolynomialFeaturesScaler(X, 'z-norm', 2)
    assert np.isclose(X_poly[:, -1], [-0.98058068, -0.39223227,  1.37281295]).all()

def test_poly_minmax():
    X = np.array([[0, 1], [2, 3], [4, 5]])
    X_poly = preprocessor.PolynomialFeaturesScaler(X, 'minmax', 2)
    assert np.isclose(X_poly[:, -1], [0.  , 0.25, 1.  ]).all()