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



def load(i):
    """Load the desired data from the Data folder
    ==========
    i : int
        The index of data_base list to know which data to load.

    Returns
    =======
    data_ : numpy.ndarray
        A 3D numpy ndarray where the columns are the features of the data and the last column is the 
        value that we would like to predict.
    """

    if i==2:
        return np.loadtxt("Data/housing.data")  
    # the files don't have the same extension so we seperate in two cases
    else:  
        with open('Data/'+ data_base[i], 'rt') as f:
            reader= csv.reader(f,delimiter=';')
            data_=[]
            next(reader)
            for row in reader:
                data_.append(np.array([float(x) for x in row]))  
    return np.array(data_)



def split_data(i):
    """Split the data into 3 different test and train sets with the use of train_test_split
    function from sklearn
    ==========
    i : int
        The index of data_base list to know which data to load.

    Returns
    =======
    data_ : dict(k,dict(subset : np.array))
        A dictionnary where the keys k represent the protocol used to split the data
        and subset is either "train" or "test".
    """

    loaded_data=load(i)
    X=loaded_data[:,:-1]
    Y=loaded_data[:,-1]
    data_= dict([(k,{"train" : [], "test" : [] }) for k in seeds])
    for k in seeds:
        x_train,x_test,y_train,y_test= model_selection.train_test_split(X,Y,test_size = 0.5, random_state =k)
        train=np.append(x_train, np.reshape(y_train,(x_train.shape[0],1)), axis=1)
        test=np.append(x_test,np.reshape(y_test,(x_test.shape[0],1)),axis=1)
        data_[k]["train"]=train
        data_[k]["test"]=test
    return data_



def extract(i, protocol, subset):
    """Split the data into 3 different test and train sets with the use of train_test_split
    function from sklearn
    ==========
    i : int
        The index of data_base list to know which data to load.
    protocol : int
        The index of seeds list to know which protocol to use to split the data.
    subset : int
        The index of subsets list to know if we extract train set or test set.

    Returns
    =======
    X : np.ndarray
        A 3D array of the desired dataset, split protocol and subset.
    """
    values= split_data(i)
    interest=values[seeds[protocol]]
    X=interest[subsets[subset]]
    return X







