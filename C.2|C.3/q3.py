import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder 
import scipy
import numpy as np
from sklearn.compose import ColumnTransformer 
from sklearn.datasets import dump_svmlight_file
from libsvm.svmutil import *


data = pd.read_csv('abalone.data', names=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"])

data.loc[data['Rings'] < 10, 'Rings'] = -1
data.loc[data['Rings'] > 9, 'Rings'] = 1




y = data.Rings

dummies = pd.get_dummies(data.Sex)
X = pd.concat([dummies, data.drop(['Sex','Rings'],axis='columns')],axis = 'columns') 


X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=1044)


dump_svmlight_file(X_train,y_train,'input_train_data',zero_based=False)

dump_svmlight_file(X_test,y_test,'input_test_data',zero_based=False)
