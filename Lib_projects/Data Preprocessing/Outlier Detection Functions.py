# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:39:33 2020

@author: Abdullah
"""

import numpy as np
from sklearn.neighbors import LocalOutlierFactor
import pandas as pd

###############################################################################
# Developers Notes:
# While using this with arrays, convert to numpy arrays and use .reshape(-1,1)
# to get the right results
###############################################################################

def outlierrDetection(df):
    clf = LocalOutlierFactor(n_neighbors=10)
    clf.fit_predict(df)
    return clf.negative_outlier_factor_