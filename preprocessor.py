"""A simple pre-processing that applies Z-normalization to the input
features"""


from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


#Polynomial scaling

def PolynomialFeaturesScaler(X, degree = X.shape[0]-1, interaction = False):
    """Generate a new feature matrix consisting of all polynomial combinations of the features 
    with degree less than or equal to the specified degree.
    Parameters
    ==========
    X : numpy.ndarray
        A 3D numpy ndarray in which the rows represent examples while the
        columns, features of the data set you want to normalize. Every depth
        corresponds to data for a particular class.
    degree : int or tuple (min_degree, max_degree), default = number of features in X
             If a single int is given, it specifies the maximal degree of the polynomial features. 
             If a tuple (min_degree, max_degree) is passed, then min_degree is the minimum and 
             max_degree is the maximum polynomial degree of the generated features.
    interaction : If True, only interaction features are produced: features that are products of 
                  at most degree distinct input features
        Desired range of transformed data.
    Returns
    =======
    X_std_scaler : numpy.ndarray
        A 3D numpy ndarray with the same dimensions as the input array ``X``,
        but with its values normalized according to class sklearn.preprocessing.StandardScaler.
    """   
    poly = PolynomialFeatures(degree, interaction_only = interaction)
    return poly.fit_transform(X)


#MinMax Scaling

def MinMaxScaler(X, feature_range = (0, 1)):
    """Transforms features by scaling each feature to a given range.
    Parameters
    ==========
    X : numpy.ndarray
        A 3D numpy ndarray in which the rows represent examples while the
        columns, features of the data set you want to normalize. Every depth
        corresponds to data for a particular class.
    feature_range : tuple (min, max), default=(0, 1)
        Desired range of transformed data.
    Returns
    =======
    X_minmax : numpy.ndarray
        A 3D numpy ndarray with the same dimensions as the input array ``X``,
        but with its values normalized according to class sklearn.preprocessing.MinMaxScaler.
    """
    if feature_range == (0, 1):
        min_max_scaler = MinMaxScaler(X)
        X_minmax = min_max_scaler.fit_transform(X)
        
    else:
        X_std = (X - X.min(axis = 0)) / (X.max(axis = 0) - X.min(axis = 0))
        X_minmax = X_std * (max - min) + min
    
    return X_minmax


#Z-normalization

def StandardScaler(X):
    """Standardize features by removing the mean and scaling to unit variance.
    Parameters
    ==========
    X : numpy.ndarray
        A 3D numpy ndarray in which the rows represent examples while the
        columns, features of the data set you want to normalize. Every depth
        corresponds to data for a particular class.
    Returns
    =======
    X_std_scaler : numpy.ndarray
        A 3D numpy ndarray with the same dimensions as the input array ``X``,
        but with its values normalized according to class sklearn.preprocessing.StandardScaler.
    """    
    scaler = StandardScaler().fit(X_train)
    X_std_scaler = scaler.transform(X_train)
    
    return X_std_scaler


def estimate_norm(X):
    """Estimates the mean and standard deviation from a data set
    Parameters
    ==========
    X : numpy.ndarray
        A 2D numpy ndarray in which the rows represent examples while the
        columns, features of the data you want to estimate normalization
        parameters on
    Returns
    =======
    mean : numpy.ndarray
        A 1D numpy ndarray containing the estimated mean over
        dimension 1 (columns) of the input data X
    std : numpy.ndarray
        A 1D numpy ndarray containing the estimated unbiased standard deviation
        over dimension 1 (columns) of the input data X
    """
    return X.mean(axis = 0), X.std(axis = 0, ddof = 1)


def normalize(X, norm):
    """Applies the given norm to the input data set
    Parameters
    ==========
    X : numpy.ndarray
        A 3D numpy ndarray in which the rows represent examples while the
        columns, features of the data set you want to normalize. Every depth
        corresponds to data for a particular class
    norm : tuple
        A tuple containing two 1D numpy ndarrays corresponding to the
        normalization parameters extracted with :py:func:`estimated_norm`
        above.
    Returns
    =======
    X_normed : numpy.ndarray
        A 3D numpy ndarray with the same dimensions as the input array ``X``,
        but with its values normalized according to the norm input.
    """

    return np.array([(k - norm[0]) / norm[1] for k in X])


