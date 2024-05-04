#step 1: DATA COLLECTION
import pandas as pd  #for creating and handling dataframe
data=pd.read_csv("iris.csv")
#print(data.head())

#STEP2:DATA CLEANING
print("looking for NAN values:",data.columns[data.isna().any()])
print("looking for duplicate values:",data.duplicated().any())

#STEP3:EDA
print(f"shape of data is:",data.shape)
print(f"size of the data is:",data.size)
print(f"info of data is:",data.info())
print(data.describe())

#3d.ADVANCE EDA
#already done during seaborn

#STEP4:DATA PRE-PROCESSING
data=data.drop(['Id'],axis=1)  #droping id column
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
print('[info]data split into train and test partitions...')
print("unique values are:",data['Species'].unique())
#label encoding
data['Species']=data['Species'].map(
    {
        'Iris-setosa':1,
        'Iris-versicolor':2,
        'Iris-virginica':3
    }
)
print(data.columns[data.isna().any()])
print("unique values after encoding are:",data['Species'].unique())

#STEP5: MODEL TRAINGING

from sklearn.neighbors import KNeighborsClassifier#importing algo
knn=KNeighborsClassifier()#initilizing algo
knn.fit(x_train,y_train)#training algo on train partition
print('[info]model training complete...')

#STEP6:MPDEL EVALUATION
#using the training model to predict output for x_test
knn_pred=knn.predict(x_test)
#comparing the model answer with actual answer
from sklearn.metrics import classification_report
model_parameters=classification_report(y_test,knn_pred)
print('MODEL EVALUATION METRIC:\n',model_parameters)

#STEP7:MODEL INFERENCE
#taking inputs from user
sepal_length=float(input("enter sepal length:"))
sepal_width=float(input('enter sepal width:'))
petal_length=float(input("enter petal length:"))
petal_width=float(input("enter petal width:"))

user_inputs=[[sepal_length,sepal_width,
              petal_length,petal_width]]

#useing the trained model to predict output for giving inputs
output=knn.predict(user_inputs)[0]
print(f"for given user inputs the predicted species is:{output}")