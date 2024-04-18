import pandas as pd

#how to conver dictionary to dataframe
data = pd.DataFrame({
    "name":["Ali","Khan","Mahesh","Vinit"],
    "age" :[20,25,30,25],
    "Branch":["cse","me","ise","ece"],
    "place":["Bangalore","Delhi","Mysore","Porbandar"]
})
print(data)
#saving the dataframe created as csv file
data.to_csv('id.csv',index=False)