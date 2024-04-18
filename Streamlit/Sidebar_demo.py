import streamlit as st
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email","Home Phone","Mobile Phone")
)
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)","Express (2-15 days)")
    )
    name=st.text_input("Enter Customer Name")