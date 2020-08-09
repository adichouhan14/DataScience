# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:20:01 2020

@author: adichouhanofficial
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

titanic=pd.read_csv(r'C:\Users\adichouhanofficial\Documents\datascience\datasets\titanic.csv')
print(titanic.isnull().sum())
titanic.dropna(['Embarked'],inplace=True)
print(titanic2.isnull().sum())