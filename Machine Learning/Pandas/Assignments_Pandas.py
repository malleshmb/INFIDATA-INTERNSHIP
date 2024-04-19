import pandas as pd  # question 1

data=pd.DataFrame({
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New york','Los Angeles','Chicago']
})

print(data)


data.to_csv('person_info.csv',index=False)  # question 2


data=pd.read_csv('person_info.csv')  # question 3
print(data)

print(data.shape) # question 4

print('statistical info:\n',data.describe())  #question 5

print('basic info:\n',data.info())  # question 6

print(data.size) # question 7

data=pd.read_json('sales.json')  #question 8
print(data)