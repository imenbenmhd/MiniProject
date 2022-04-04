#!/usr/bin/env python3

import database 
import algorithm
import pytest
def test_load_1():
    i_1=0
    i_2=1
    i_3=2
    r_1=database.load(i_1)
    r_2=database.load(i_2)
    r_3=database.load(i_3)
    assert(r_1.shape[1]==r_2.shape[1]==12)
    assert(r_1.shape[1] != r_3.shape[1])


def test_split_1():
    r_1=database.split_data(0)
    assert(list(r_1)==database.seeds)
    for i in r_1.keys():

        assert(list(r_1[i])==database.subsets)

def test_split_2():
    for j in range(3):
        r_1=database.split_data(j) 

        for i in r_1.keys():
            assert(r_1[i]["train"].shape[0]==pytest.approx(r_1[i]["test"].shape[0],1))





def test_regression_1():
    for i in range(2):
       for j in range(3):
            print(i,j)
            ytest,ypred=algorithm.regression(i,j,"LinearRegression")
            assert(len(ytest[0])==len(ypred[0]))
            ytest,ypred=algorithm.regression(i,j,"Regressiontree")
            assert(len(ytest[0])==len(ypred[0]))


    
#test_regression_1()




