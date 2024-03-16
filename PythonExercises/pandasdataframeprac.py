import numpy as np
import pandas as pd

#Dataframe is the "main" data type in pandas
#Equivalent to SQL table

np_array = np.arange(6).reshape((2,3))
df = pd.DataFrame(np_array, index=['a', 'b'], columns=['col1', 'col2', 'col3'])
print(df)
#We have to specify both index and colnames for df's.
#where index specifies the row and columns specify the column

print(df.index)
print(df.columns)
print(df.values)

#indexing into a dataframe. USE THESE TWO (LOC AND ILOC)
#get by label:
print(df.loc['a', 'col2'])
#get by index:
print(df.iloc[0, 1])
#These two methods supports slicing (ENDPOINTS INCLUDED)
#or by using these two functions:

print(df.at['a', 'col2'])
print(df.iat[0, 1])
#This one is faster for lookup of single values

#Get column by label:
print(df['col2']) #outputs the col specifiec by label col2 as a series

#Slice rows by index range:
print(df[0:1]) #outputs the first row in the df

np_array = np.arange(6).reshape((3,2))
df1 = pd.DataFrame(np_array, index=['a', 'b', 'c'], columns=['col1', 'col2'])

print(df1)

print(df1.loc[:, 'col1']>2) #prints df all rows, col1 and a bool if each element are greater than 2

#index into entire df and change elements to 0 if the boolean expression is true
# That is if elements are greater than 0
#This i sometimes called a "mask"
df1.loc[df1.loc[:, 'col1']>2] = 0
print(df1)

#Adding columns:
df1 = df1.assign(col3 = df1.loc[:, 'col1'])
print(df1)

#We can concatenate dataframes both entending the cols or the rows:
df2 = pd.concat([df1, df], axis=1)
print(df2)
#It simple fills empty elements with NaN's
#to make the sizes of the 2 dataframes match
df3 = pd.concat([df1, df], axis=0)
print(df3)

#One can also use all SQL functionality but im not gonna do that here



