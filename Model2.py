# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 13:02:13 2021

@author: Raagulbharatwaj
"""

import pandas 
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.tree import DecisionTreeRegressor
df=pandas.read_csv("C:\\Users\\Raagulbharatwaj\\Desktop\\train.csv")
df['AREA']=np.log(df['SQUARE_FT'])
x=df.drop(['TARGET','SQUARE_FT'],axis=1)
y=df['TARGET']
from sklearn.model_selection import train_test_split ,cross_val_score,RandomizedSearchCV
X_train ,X_test,y_train ,y_test =train_test_split(x,y,test_size =.2 , random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.fit_transform(X_test)
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(r2_score(y_pred,y_test))
df1=pandas.read_csv("C:\\Users\\Raagulbharatwaj\\Desktop\\test.csv")
df1['AREA']=np.log(df1['SQUARE_FT'])
df1=df1.drop(['SQUARE_FT'],axis=1)
df1=scaler.fit_transform(df1)
price=model.predict(df1)
result=pandas.DataFrame(price,columns=["TARGET"])
result.to_csv("C:\\Users\\Raagulbharatwaj\\Desktop\\result.csv",index=None)