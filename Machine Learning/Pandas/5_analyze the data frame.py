import pandas as pd

df = pd.read_csv("diabetes.csv")

#head
print("accessing from the dataset from first 10 rows\n",df.head(10))
print("Accessing from the dataset from first 5 rows\n",df.head())

#tail
print("Accessing from the dataset from last 5 rows\n",df.tail())
print("Accessing from the dataset from last 10 rows\n",df.tail(10))

print(df.shape)
print(df.columns[df.isna().any()]) #to check null values

#informaton data
print("Basic info:\n",df.info())

#basic stastical information
print("Statistical info:\n",df.describe())