# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:54:49 2020

@author: Abdullah
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np


###############################################################################
#
# arr is a numpy array with rershape(-1,1)
#
###############################################################################


def IsoForest(df, colName, arr):
    temp = np.array(df[colName])
    clf = IsolationForest(random_state=0).fit(temp.reshape(-1,1))
    return clf.predict(arr)
