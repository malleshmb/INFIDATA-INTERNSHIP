import numpy as np #for array operatiin
import pandas as pd #for creating and handling dataset

data=pd.DataFrame({'x':[-5,-4,-3,-2,-1,0,1,2,3,4,5],
                            'y':[0,0,0,0,0,1,1,1,1,1,1]})

print("data frame",data)#displaying exmaple1 dataframe
print("data shap:",data.shape)

x=data['x'].values.reshape(-1,1) #choosing input values
y=data['y'].values.reshape(-1,1) #choosing output values

from sklearn.linear_model import LinearRegression #importing algo
linear_regressor=LinearRegression() #initalising algorithm
linear_regressor.fit(x,y)  #traing the algo on our data
print('[info] model trainging complete...')


new_user_input=float(input("enter the value of x:"))
new_user_input=[[new_user_input]]
new_output=linear_regressor.predict(new_user_input)


print(f"when x={new_user_input[0][0]},y={new_output[0]}")
