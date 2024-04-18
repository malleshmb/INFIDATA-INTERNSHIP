#Assuming a dataframe is already present
#This is how we read and load it
import pandas as pd

#jason = JavaScript Object Notation.
df = pd.read_json("data.json")
print(df)