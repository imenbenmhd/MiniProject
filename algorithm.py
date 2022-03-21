import numpy as np
import database
import preprocessor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

normalization=['PolynomialFeaturesScaler', 'MinMaxScaler','StandardScaler','normalize']


def regression(data,norm,model):
    y_predicted=[]
    y_tested=[]

    for i in database.seeds:
        training_set=database.extract(data,i,"train")
        testing_set=database.extract(data,i,"test")
        normalization_to_call=getattr(database , normalization[norm])

        
        normalized_train_set=normalization_to_call(training_set)
        y_train=normalized_train_set[:,-1]
        normalized_test_set=normalization_to_call(testing_set)
        y_test=normalized_test_set[:,-1]
        if model=="LinearRegression":
            regressor = LinearRegression()
        if model=="Regressiontree":
            regressor=DecisionTreeRegressor()

        regressor.fit(normalized_train_set,y_train)
        y_predict=regressor.predict(normalized_test_set)
        y_tested.append(y_test)
        y_predicted.append(y_predict)

    return y_tested,y_predicted; # return for the 3 seeds



