import numpy as np
import database
import preprocessor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

normalization=['MinMaxScaler_','StandardScaler','PolynomialFeaturesScaler']


def regression(data,norm,model):
    y_predicted=[]
    y_tested=[]

    for i in database.seeds:
        training_set=database.extract(data,i,0)
        testing_set=database.extract(data,i,1)
        degree=training_set.shape[1]-1
        if norm==2:
            print("norma")
            normalization_to_call=getattr(preprocessor , normalization[norm])
            print(training_set.shape[1])
            normalized_train_set=normalization_to_call(training_set,"minmax", degree)
            normalized_test_set=normalization_to_call(testing_set,"minmax",degree)
            print("oknor")
        if norm==3:
            normalization_to_call=getattr(preprocessor , normalization[norm])

            normalized_train_set=normalization_to_call(training_set,"z-norm",degree)
            normalized_test_set=normalization_to_call(testing_set,"z-norm",degree)
        else:
            normalization_to_call=getattr(preprocessor , normalization[norm])

            normalized_train_set=normalization_to_call(training_set)
            normalized_test_set=normalization_to_call(testing_set)

        y_train=normalized_train_set[:,-1]
        y_test=normalized_test_set[:,-1]

        if model=="LinearRegression":
            print("model")
            regressor = LinearRegression()
        if model=="Regressiontree":
            regressor=DecisionTreeRegressor()

        regressor.fit(normalized_train_set,y_train)
        y_predict=regressor.predict(normalized_test_set)
        print(y_predict)
        y_tested.append(y_test)
        y_predicted.append(y_predict)

    return y_tested,y_predicted; # return for the 3 seeds



ytest, ypredict=regression(0,0,"LinearRegression")
