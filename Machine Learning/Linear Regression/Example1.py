import numpy as np
import pandas as pd

example1_data = pd.DataFrame({'x':[0,1,2,3,4],
                             'y':[1,2,3,4,5]})
print(example1_data)

x = example1_data['x'].values.reshape(-1,1)
y = example1_data['y'].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(x,y)
print('[info] linear regression model training complete...')

m = linear_regressor.coef_[0][0]
c = linear_regressor.intercept_[0]

print(f"m value is:{m}")
print(f"c value is:{c}")
print(f"equation of line is : y = {m}x+{c}")