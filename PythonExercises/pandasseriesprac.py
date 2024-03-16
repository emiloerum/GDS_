import pandas as pd
import numpy as np

#series is like a 1D numpy array - but with labels
#Dataframe is like a 2D data structure with labeled columns

np_array = np.array([1.0, 2.0, 3.0])

#convert numpy array to pandas series
pd_series = pd.Series(np_array, index=['a', 'b', 'c'])

print(pd_series)

#we can use numpy functions on series:
print(np.cos(pd_series))

#Just like dictionaries, we can ask for a specific value by key:
print(pd_series['b']) #prints 2.0

#labels are used for alignment.
#can add 2 series together even though they dont have
#the same amount of elements.
#Below it finds that 2 elements has the same key and can therefore add them
print(pd_series + pd_series[1:]) 

#We can ask to drop the values for which there was a missing values:
print((pd_series + pd_series[1:]).dropna())

#Can convert elements in series to other types:
print(pd_series.astype('string'))

#we can operate on strings and other types using accessors:
pd_series1 = pd.Series({'a' : 'I', 'b' : 'love', 'c' : 'python'})
#this turns the elements I, love, python to uppercase
print(pd_series1.str.upper())

#Exercise:
#1. Use range to create a list of values from 0 to 99 and use it to initialize a Series.
lst1 = list(range(100))

pd_series2 = pd.Series(data=lst1)
print(pd_series2)

#2. Convert the series to type string, and calculate the lenght of entries.
pd_series2 = pd_series2.astype('string')
print(pd_series2)
print(len(pd_series2))

#calculate the lengths of each entry
lengths = pd_series2.str.len()
print("Lengths:\n", lengths)





