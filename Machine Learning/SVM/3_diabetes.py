#step 1: DATA COLLECTION
import pandas as pd  #for creating and handling dataframe
data=pd.read_csv("diabetes.csv")
#print(data.head())

#STEP2:DATA CLEANING
print("looking for NAN values:",data.columns[data.isna().any()])
print("looking for duplicate values:",data.duplicated().any())

#STEP3:EDA
print(f"shape of data is:",data.shape)
print(f"size of the data is:",data.size)
print(f"info of data is:",data.info())
print(data.describe())

#STEP4:DATA PRE-PROCESSING
#data=data.drop(['Id'],axis=1)  #droping id column
#FEATURE SDELECTION
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
print('[info]data segregation complete...')
#DATA SPLITTING
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    random_state=100,
    test_size=0.2
)
print('[info]data splite into train and test partitions...')
print("unique values are:",data['Outcome'].unique())
#label encoding
data['Outcome']=data['Outcome'].map(
    {
        'Outcome':1,
        'Outcome':0
    }
)
print(data.columns[data.isna().any()])
print("unique values after encoding are:",data['Outcome'].unique())

#STEP5: MODEL TRAINGING

from sklearn.svm import SVC#importing algo
svm=SVC()#initilizing algo
svm.fit(x_train,y_train)#training algo on train partition
print('[info]model training complete...')

#STEP6:MODEL EVALUATION
#using the training model to predict output for x_test
svm_pred=svm.predict(x_test)
#comparing the model answer with actual answer
from sklearn.metrics import classification_report
model_parameters=classification_report(y_test,svm_pred)
print('MODEL EVALUATION METRIC:\n',model_parameters)
from sklearn.metrics import confusion_matrix
svm_cf=confusion_matrix(y_test,svm_pred)
print("confusion matrix :\n",svm_cf)
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(svm_cf,fmt='d',cmap='Blues',annot=True)
plt.xlabel('PRIDICTED')
plt.ylabel('ACTUAL')
plt.show()

#STEP7:MODEL INFERENCE
#taking inputs from user
Pregnancies=float(input("enter Pregnancies :"))
Glucose=float(input('enter Glucose:'))
BloodPressure=float(input("enter BloodPressure:"))
SkinThickness=float(input("enter SkinThickness:"))
Insulin=float(input("enter Insulin:"))
BMI=float(input("enter BMI:"))
DiabetesPedigreeFunction=float(input("enter DiabetesPedigreeFunction:"))
Age=float(input("enter Age:"))

user_inputs=[[Pregnancies,Glucose,BloodPressure,SkinThickness,
              Insulin,BMI,DiabetesPedigreeFunction,Age]]

#useing the trained model to predict output for gib=ving inputs
output=svm.predict(user_inputs)[0]
print(f"for given user inputs the predicted species is:{output}")

import joblib
joblib.dump(svm,'trained_svm.pkl')
print('[info] tarined model saving to hard disk...')