# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:23:40 2020

@author: Akshay
"""
import pandas as pd
import html5lib
import lxml
y=pd.read_html("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
print(y)
print(type(y))
z=tuple(y)
print(z)