import numpy as np
from . import database
from . import preprocessor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

normalization = ["MinMaxScaler_", "Standard_Scaler", "PolynomialFeaturesScaler"]


def normalize(X, norm):
    """
    chose a preproccessing method to apply to the data

    Parameters:

        X : np.ndarray
            The data to normalize

        norm : int
            The index of normalization list to know which preprocessing method to use.

    Returns:
        numpy.ndarray,
            a 2D array same shape as the input but normalized.

    """

    degree = 2
    if norm == 2:
        normalization_to_call = getattr(preprocessor, normalization[2])
        normalized_set = normalization_to_call(X, scale="minmax", degree=degree)
    elif norm == 3:
        normalization_to_call = getattr(preprocessor, normalization[2])
        normalized_set = normalization_to_call(X, scale="z-norm", degree=degree)
    else:
        normalization_to_call = getattr(preprocessor, normalization[norm])
        normalized_set = normalization_to_call(X)
    return normalized_set


def regression(data, norm, model):
    """
    apply the regression model to the data with a specific normalization method as preprocessing

    Parameters:

        data : int
            The index of data_base list to know which data to load.

        norm : int
            The index of normalization list to know which preprocessing method to use.

        model : string
            Which regression model to apply.

    Returns: 
        list of np.array,
            A list of the values of the predicted attribute for every protocol.
        
        list of np.array,
            A list of the true values of the test set to compare with the prediction.

    """

    y_predicted = []
    y_tested = []

    for i in range(len(database.seeds)):
        training_set = database.extract(data, i, 0)
        testing_set = database.extract(data, i, 1)
        normalized_train = normalize(training_set, norm)
        normalized_test = normalize(testing_set, norm)

        y_train = normalized_train[:, -1]
        y_test = normalized_test[:, -1]

        if model == "LinearRegression":
            regressor = LinearRegression()
        if model == "Regressiontree":
            regressor = DecisionTreeRegressor()

        regressor.fit(normalized_train, y_train)
        y_predict = regressor.predict(normalized_test)
        y_tested.append(y_test)
        y_predicted.append(y_predict)

    return y_tested, y_predicted
    # return for the 3 seeds