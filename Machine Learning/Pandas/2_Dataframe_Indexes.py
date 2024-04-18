import pandas as pd

data = pd.DataFrame({
    "calories":[420,399,288],
    "duration":[10,20,30]
})

print("First column of data is:\n",data['calories'])
print("First column of data is:\n",data.calories)