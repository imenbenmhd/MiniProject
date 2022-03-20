#!/usr/bin/env python

import numpy as np
import csv
from sklearn import model_selection

seeds=[2,3,4]

PROTOCOLS = {
        'proto1': {'train': seeds[0], 'test': seeds[0]},
        'proto2': {'train': seeds[1], 'test': seeds[1]},
        'proto3' : {'train': seeds[2], 'test': seeds[2]}
        }

data_base = ['winequality-white.csv',
        'winequality-red.csv',
        'housing.data' ]

wine_variables = [ 'fixed acidity' , 'volatile acidity',
    'citric acid' , 'residual sugar', 'chlorides' , 'free sulfur dioxide',
    'total sulfur dioxide','density' , 'pH' , 'sulphates' , 'alcohol' ]

housing_variables=['CRIM', 'ZN' , 'INDUS', 'CHAS' ,'NOX',
 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']        

subsets=["train", "test"]



def load(data):

  if data==2:
      return np.loadtxt("Data/housing.data")  

  else:  
    with open('Data/'+ data_base[data], 'rt') as f:
        reader = csv.reader(f,delimiter=';')
        data_=[]
        next(reader)
        for row in reader:
            data_.append(np.array([float(x) for x in row]))  
    return np.array(data_)



def split_data(data):
    loaded_data=load(data)
    X=loaded_data[:,:-1]
    Y=loaded_data[:,-1]
    data_= dict([(k,[]) for k in seeds])
    for k in seeds:
        x_train,x_test,y_train,y_test= model_selection.train_test_split(X,Y,test_size = 0.5, random_state =k)
        train=np.append(x_train, np.reshape(y_train,(x_train.shape[0],1)), axis=1)
        test=np.append(x_test,np.reshape(y_test,(x_test.shape[0],1)),axis=1)
        (data_[k].append(train)).append(test)
    return data_



def extract(data, protocol, subset):
    values= split_data(data)
    interest=values[seeds[protocol]]
    return interest[subsets.index(subset)]








