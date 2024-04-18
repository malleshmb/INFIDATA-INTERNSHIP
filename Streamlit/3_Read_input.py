import streamlit as st
n1 = st.number_input("Enter n1 value: ")
n2 = st.number_input("Enter n2 value: ")
if(n1>n2):
    st.info("n1 is greater than n2")
else:
    st.info("n2 is greater than n1")