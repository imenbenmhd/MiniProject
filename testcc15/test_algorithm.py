#!/usr/bin/env python3


from . import algorithm
import pytest



def test_regression_1():
    for i in range(2):
       for j in range(3):
            ytest,ypred=algorithm.regression(i,j,"LinearRegression")
            assert(len(ytest[0])==len(ypred[0]))
            ytest,ypred=algorithm.regression(i,j,"Regressiontree")
            assert(len(ytest[0])==len(ypred[0]))