import numpy as np
import pandas as pd

example1_data = pd.DataFrame({'x':[0,1,2,3,4],'y':[1.5,2,3.5,5,4.5]})

print(example1_data)

x= example1_data['x'].values.reshape(-1,1)
y= example1_data['x'].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(x,y)
print('[info] linear regression model training completed..')

m= linear_regressor.coef_[0][0]
c= linear_regressor.intercept_[0]

print(f"m values is :{m}")
print(f"m values is :{c}")
print(f"equation of line is :y={m}x+c")

new_user_input = float(input("Enter value of x :"))
new_user_input = [[new_user_input]]
new_output = linear_regressor.predict(new_user_input)[0]
print(f"when x = {new_user_input},y = {new_output}")