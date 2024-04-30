#step1:DATA COLLECTION
import pandas as pd #for creating and handling dataframes
data=pd.read_csv("penguins.csv")
#print(data.head())

#step2:DATA CLEANING
print("looking for NaN values:",data.columns[data.isna().any()])
data=data.dropna()
print("looking for duplicate values:",data.duplicated().any())

#step3:EDA
print(f"shape of data is:",data.shape)
print(f"size of datset is:",data.size)
print(data.info())
print(data.describe())
#3b.ADVANCED EDA
#already done during seaborn fill from that

#step4:DATA PRE-PROCESSING
data=data.drop(["id","year"],axis=1) #dropping the column

print("unique values are:",data['species'].unique())
print("Unique islands:", data['island'].unique())
print("Unique sex:", data['sex'].unique())
data['species']=data['species'].map(
    {
        'Adelie':1,
        'Gentoo':2,
        'Chinstrap':3

    }
)

data['island']=data['island'].map(
    {
       'Torgersen':1,
        'Biscoe':2,
        'Dream':3
    }
)
data['sex']=data['sex'].map(
    {
        'male':1,
        'female':2
    }
)

print(data.columns[data.isna().any()])
print("unique values after encoding are:",data['species'].unique())
print("unique values after encoding are:",data['island'].unique())
print("unique values after encoding are:",data['sex'].unique())

print(data.info())
#FEATURE SELECTION
x=data[["island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"]].values
y=data['species'].values
print('[info] data segregation complete....')
#DATA SPLITTING
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(
    x,y,
    random_state=100,
    test_size=0.2)
print('[info] data split into train-test partitions...')



#step5:MODEL TRAINING
from sklearn.linear_model import LogisticRegression #importing algo
logistic_regressor=LogisticRegression(max_iter=15000)#initalising algorithm
logistic_regressor.fit(x,y)#training algo on train partition
print('[info]  model training complete....')

#step6:MODEL EVALUATION
#using the trained model to predict output for x_test
logistic_regressor_pred=logistic_regressor.predict(x)
#compairing the model answers with actual answers
from sklearn.metrics import classification_report
model_parameters=classification_report(y,logistic_regressor_pred)
print("model evaluation metrics:\n",model_parameters)

#step7: MODEL INFERENCE
#taking inputs from user
island=int(input("enter the island :"))
bill_length_mm=float(input("enter the bill_length_mm:"))
bill_depth_mm=float(input("enter the bill_depth_mm:"))
flipper_length_mm=int(input("enter the flipper_length_mm :"))
body_mass=int(input("enter the body mass:"))
sex=int(input("enter the sex:"))

species_num_to_text = {1:'Adelie',2:'Gentoo',3:'Chinstrap'}

user_inputs=[[island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass,sex]]
print(user_inputs)
#using the trained model to predict output for given inputs
output_number=logistic_regressor.predict(user_inputs)[0]
output_text = species_num_to_text[output_number]
print(f"for given user inputs the predicted species is:{output_text}")