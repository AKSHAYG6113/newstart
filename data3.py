# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:43:44 2020

@author: Akshay
"""
import pandas as pd 
import pandas_datareader as data
x=data.data.get_data_yahoo('Apple',start='2018-09-27',end='2018-10-22')
print(x)
x.info()
x[['Open','Close']].plot(figsize=(16,1));
