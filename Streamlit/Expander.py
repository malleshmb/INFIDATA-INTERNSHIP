import streamlit as st

st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("See Explanation"):
    st.write("The chart above shows some numbers I picked for you.")
    st.image("img.png")