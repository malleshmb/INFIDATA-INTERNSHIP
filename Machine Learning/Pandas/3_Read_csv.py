import  pandas as pd

data = pd.read_csv("diabetes.csv")
print(data) #displaying dataframe

print("Display specfic columns")
print(data['Glucose']) #display single column
print(data[["Glucose","BMI"]]) #multiple column

print(data.shape) #display shape of data set

print(data.size) #dispaly size of data
#index
print(data.head())

print(data.tail())