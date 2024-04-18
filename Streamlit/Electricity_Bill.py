import streamlit as st

cname = st.text_input('Enter the Customer Name:')
cid = st.text_input('Enter the Customer Id:')
unit = st.number_input('Enter the units:')

if (unit <= 100):
    price = unit * 0
    st.write('Electricity Charges is:', price)

elif (unit >= 100 and unit<=200):
    price = (unit - 100) * 5
    st.write('Electricity Charges is:', price)

elif (unit > 200):
    price = (unit - 100) * 10
    st.write('Electricity Charges is:',price)