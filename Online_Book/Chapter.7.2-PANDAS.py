#Pandas -> One-dimensional ndarray with axis labels (including time series).
#Data structure in Pandas
#pandas.Series()
#pandas.DataFrame() -> DataFrame is a 2-dimensional labeled data structure with columns of potentially different types

import pandas as pd

#index           element
#------------------------
#  A                10
#  B                20
#  C                30
#  D                40
#  E                50

series1 = pd.Series([10, 20, 30, 40, 50], index = ['A', 'B', 'C', 'D', 'E'])
print (series1)
print('----------------------------')
print ('series1.index = ', series1.index)
print('----------------------------')
print ('series1.values = ', series1.values)
print('----------------------------')
print ('series1 > = 20 => ', series1[series1 >= 20])
print('----------------------------')
print ('series1  < 50 => ', series1[series1 < 50])
print('----------------------------')
print ('series1.A = ', series1.A)
print('----------------------------')
print ('series1[D] = ', series1['D'])
print('----------------------------')
series1.index = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']
print ('series1.index = ', series1.index)
print('----------------------------')
print ('series1 = ',series1)
print('----------------------------')       
               
                                                   #columns
#                     A                B                 C                 D                  E                     
#index
#----------------------------------------------------------------------------------------------
#  1                10                15                14                897                11
#  2                20                25                18                7896               12 
#  3                30                35                135               1                  8
#  4                40                45                789               1235               5
#  5                50                55                422               48                 14


import numpy as np
array1 = np.array([[10, 15, 14, 897, 11],[20, 25, 18, 7896, 12 ],[30, 35, 135, 1, 8],[40, 45, 789, 1235, 5],[50, 55, 422, 48, 14]])
data_frame1 = pd.DataFrame(array1, index=[1, 2, 3, 4, 5],columns=['A', 'B', 'C', 'D','E'])
print ('data_frame1 = ')
print (data_frame1)
print('----------------------------') 
print ('data_frame1.index = ')
print (data_frame1.index)
print('----------------------------')
print ('data_frame1.columns = ')
print (data_frame1.columns)
print('----------------------------')
print ('data_frame1.values = ')
print (data_frame1.values)

print('--------------------------------')
print('------------Dictionary----------') 

Dictionary1 = {'A':[10, 15, 14, 897, 11], 'B':[20, 25, 18, 7896, 12 ], 'C':[30, 35, 135, 1, 8], 'D':[40, 45, 789, 1235, 5], 'E':[50, 55, 422, 48, 14]}
data_frame1 = pd.DataFrame(array1, index=[1, 2, 3, 4, 5],columns=['A', 'B', 'C', 'D','E'])
print ('data_frame1 = ')
print (data_frame1)
print('----------------------------') 
print ('data_frame1.loc [4][:] = ')
print (data_frame1.loc [4][:])
print('----------------------------')
print ('data_frame1.loc [:][B] = ')
print (data_frame1.loc [:]['B'])
print('----------------------------')
print ('data_frame1.loc [3][C] = ')
print (data_frame1.loc [3]['C'])
print('----------------------------')

#DataFrame.iloc =>  is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
print ('data_frame1.iloc [2][3] = ')
print (data_frame1.iloc [2][3])
print('----------------------------')
print ('data_frame1.iloc [0][0] = ')
print (data_frame1.iloc [0][0])
print('----------------------------')
print ('data_frame1.iloc [1][:] = ')
print (data_frame1.iloc [1][:])
print('----------------------------')
data_frame1.loc[[2,3],'A'] = 1
print ('data_frame1 = ')
print (data_frame1)
print('----------------------------')
data_frame1.loc[[2,3]] = 0
print ('data_frame1 = ')
print (data_frame1)
print('----------------------------')
data_frame1['D'] = [1 ,2 ,3 ,4,5]
print ('data_frame1 = ')
print (data_frame1)
print('----------------------------')
print('data_frame1.rename(columns = {A:s}) = ')
print(data_frame1.rename(columns = {'A':'s'}))
print('----------------------------')
print('data_frame1.replace({1:222},regex=True) = ')
print(data_frame1.replace({1:222},regex=True))
print('----------------------------')
print('data_frame1.drop(1,axis=1) = ')
print(data_frame1.drop('B',axis=1))
print('----------------------------')
print('data_frame1.reset_index(drop=True) = ')
print(data_frame1.reset_index(drop=True))
print('----------------------------')

print('data_frame1.head() = ')
print(data_frame1.head())
print('----------------------------')
print('data_frame1.head(3) = ')
print(data_frame1.head(3))
print('----------------------------')
print('data_frame1.head(1) = ')
print(data_frame1.head(1))
print('----------------------------')

print('data_frame1.tail() = ')
print(data_frame1.tail())
print('----------------------------')
print('data_frame1.tail(4) = ')
print(data_frame1.tail(4))
print('----------------------------')
print('data_frame1.tail(1) = ')
print(data_frame1.tail(1))
print('----------------------------')


print('data_frame1.sort_values(by=D,ascending=False) = ')
print(data_frame1.sort_values(by='D',ascending=False))
print('----------------------------')
print('data_frame1.sort_values(by=D,ascending=True) = ')
print(data_frame1.sort_values(by='D',ascending=True))
print('----------------------------')

print('data_frame1.sort_index(axis=1,ascending=False) = ')
print(data_frame1.sort_index(axis=1,ascending=False))
print('----------------------------')
print('data_frame1.sort_index(axis=0,ascending=False) = ')
print(data_frame1.sort_index(axis=0,ascending=False))
print('----------------------------')

#'''''''''''
data_frame1.B = ['{:.4f}'.format(x) for x in data_frame1.iloc[:,1] ]
print('[{:.4f}.format(x) for x in data_frame1.iloc[:,0] ')
print(data_frame1)
print('----------------------------')
data_frame1['A'] = data_frame1['A'].apply(lambda x:'{0:.5f}'.format(x))
print('data_frame1[D].apply(lambda x:{0:.5f}.format(x))')
print(data_frame1)

