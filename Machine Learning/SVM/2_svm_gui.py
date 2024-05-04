import joblib
import streamlit as st

st.title("IRIS FLOWER SPECIES DETECTOR")
sepal_length=st.number_input("enter sepal length:")
sepal_width=st.number_input("enter sepal width")
petal_length=st.number_input("enter petal length")
petal_width=st.number_input("enter petal width")

submit_button=st.button('SUBMIT')

if submit_button:
    st.subheader("MODEL DIAGNOSIS")
    model = joblib.load('trained_svm.pkl')
    user_inputs = [[sepal_length,sepal_width,petal_length,petal_width]]
    new_output = model.predict(user_inputs)[0]

    st.info(f"for given inputs ,model prediction is: {new_output}")
else:
    st.error("click submit button!")