import streamlit as st

st.title("Arithmetic Operation")
st.markdown("Please Give the Inputs")

st.sidebar.title("select the Operations:")
st.sidebar.markdown("Select the options Accordingly:")

choice = st.sidebar.selectbox('Select',('ADD','MUL'))
selected_status =st.sidebar.selectbox('Select number',options=['2N','3N'])

if choice == 'ADD':
    if selected_status == '2N':
        n1 = st.number_input("Enter n1:")
        n2 = st.number_input("Enter n2:")
        sum = n1+n2
        st.success(sum)
    elif selected_status == '3N':
        n1 = st.number_input("Enter n1:")
        n2 = st.number_input("Enter n2:")
        n3 = st.number_input("Enter n3:")
        sum = n1 + n2 + n3
        st.success(sum)
elif choice == 'MUL':
        if selected_status == '2N':
            n1 = st.number_input("Enter n1:")
            n2 = st.number_input("Enter n2:")
            mul = n1*n2
            st.success(mul)
        elif selected_status == '3N':
            n1 = st.number_input("Enter n1:")
            n2 = st.number_input("Enter n2:")
            n3 = st.number_input("Enter n3:")
            mul = n1*n2*n3
            st.success(mul)
