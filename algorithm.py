from locale import normalize
import database
import preprocessor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier



seed=[2,3,4]


def linear_regression(data,seed):
    data_f=database.load(data)

    y_predicted=[]
    x_train ,x_test,y_train , y_test=database.split_data(data_f,i)
    regressor = LinearRegression()
    
        regressor.fit(x_train, y_train)
        y_predict=regressor.predict(x_test)
        y_predicted.append(y_predict)

    return y_predicted; # return for the 4 normalization

def regressionTree(data,seed):
    data_f=database.load(data)
    y_predicted=[]
    y_tested=[]


    return y_predicted;
