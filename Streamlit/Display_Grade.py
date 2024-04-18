import streamlit as st
name = st.text_input("Enter the student Name:")
per = st.number_input("Enter the Percentage")
if(per>90):
    st.write("Grade A")
elif(per>80 and per<=90):
    st.write("Grade B")
elif(per>=60 and per<=80):
    st.write("Grade C")
elif(per<60):
    st.write("Grade D")