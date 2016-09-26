from __future__ import print_function
import os
import pandas as pd

def loadDataSet(name):
    data_path = os.path.join(os.getcwd(), 'datasets', name + '.csv')
    return pd.read_csv(data_path, delimiter = ',')

print "telos"
