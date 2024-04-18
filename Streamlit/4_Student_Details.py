import streamlit as st

name = st.text_input("Enter the student name:")
branch = st.text_input("Enter the Branch name:")
usn = st.text_input("Enter the USN:")
email = st.text_input("Enter the email id:")
test1 = st.number_input("Test1 Marks:")
test2 = st.number_input("Test2 Marks:")
test3 = st.number_input("Test3 Marks:")
average = (test1 + test2 + test3) /3
st.write("Student name :",name)
st.write("Branch name:",branch)
st.write("USN:",usn)
st.write("Email:",email)
st.write("Test1 marks:",test1)
st.write("Test2 marks:",test2)
st.write("Test3 marks:",test3)
st.write("Average marks of Tests is:",average)