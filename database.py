#!/usr/bin/env python

import numpy as np
import csv
data_base = ['winequality-white.csv',
        'winequality-red.csv',
        'housing.data'

        ]


def load(data):

  if data==0:
      return np.loadtxt("Data/housing.data")  

  else:  
    with open('Data/'+ data +'.csv', 'rt') as f:
        reader = csv.reader(f,delimiter=';')
        data_=[]
        next(reader)
        for row in reader:
            data_.append(np.array([float(x) for x in row]))  
    return np.array(data_)



def split_data(data,seed):





