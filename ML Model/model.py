
import pandas as pd
import numpy as np
import pylab as pl
import sklearn
from sklearn import linear_model

regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
#training the model
regr.fit (train_x, train_y)
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_hat = regr.predict(test_x)
# Testing with discrete values
new = regr.predict([[8.4]])
print(new)