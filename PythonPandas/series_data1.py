#Pandas library helps with importing datasets , working with series and dataframes
import pandas as pd
import numpy as np

from pandas import Series, DataFrame
# Series and Data Frame are two data structures available in python

series_a = Series([7,6,5,4,3,2,1])# a simple series
"""
#print(series_a)
# A series is represented by index on the left and values on the right
print(series_a.values) # similar to dictionary. ".values" command returns values in a series
print(series_a.index) # returns the index values of the series

series_b = Series([5,4,3,2,1,8,-29], index =['a','b','c','d','e','f','h']) # The index is specified
print (series_b) # try series_b.index and series_b.values


print (series_b['a']) # selecting a particular value from a Series, by using index


series_b['d'] = 9 # change the value of a particular element in series
print (series_b)
print(series_b([['a','b','c']]))
# select a group of values

print (series_b[series_b>0]) # returns only the positive values
print (series_b *2) # multiplies 2 to each element of a series
"""
series_b = Series([5,4,3,2,1,8,-29], index =['a','b','c','d','e','f','h']) # The index is specified

print(np.mean(series_b)) # you can apply numpy functions to a Series

print('b' in series_b) # checks whether the index is present in Series or not
print('z' in series_b)

