# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:34:29 2020

@author: Akshay
"""
import pandas as pd
import html5lib
import lxml
x=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(x.loc['Hawaii'])