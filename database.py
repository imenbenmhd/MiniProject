#!/usr/bin/env python

import numpy as np
import csv
from sklearn import model_selection




data_base = ['winequality-white.csv',
        'winequality-red.csv',
        'housing.data' ]

wine_variables = [ 'fixed acidity' , 'volatile acidity',
    'citric acid' , 'residual sugar', 'chlorides' , 'free sulfur dioxide',
    'total sulfur dioxide','density' , 'pH' , 'sulphates' , 'alcohol' ]

housing_variables=['CRIM', 'ZN' , 'INDUS', 'CHAS' ,'NOX',
 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']        



def load(data):

  if data==0:
      return np.loadtxt("Data/housing.data")  

  else:  
    with open('Data/'+ data_base[data], 'rt') as f:
        reader = csv.reader(f,delimiter=';')
        data_=[]
        next(reader)
        for row in reader:
            data_.append(np.array([float(x) for x in row]))  
    return np.array(data_)



def split_data(data,seed):
    
    X=data[:,:-1]
    Y=data[:,-1]
    print(Y)
    x_train ,x_test,y_train , y_test = model_selection.train_test_split(X,Y,test_size = 0.5, random_state =seed)
    return x_train,x_test,y_train,y_test 










