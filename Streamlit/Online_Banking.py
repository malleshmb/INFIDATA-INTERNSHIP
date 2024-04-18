import streamlit as st

st.sidebar.title('Welcome to SBI')
account_type=st.sidebar.selectbox('Create Account',options=[None,'Create account'])
option=st.sidebar.selectbox('Select Operation',options=[None,'Deposit','Withdraw','Display'])

st.title('Online Banking')
if (account_type=='Create account'):
    name=st.text_input('Name:')
    c_number=st.text_input('Cid:')
    branch=st.text_input(' Branch:')
    initial_amount=st.number_input('Initial amount')

if (option=='Deposit'):
    deposit=st.number_input('Enter the amount to be deposit')
    balance1=initial_amount + deposit
    st.write('Updated balance after deposit:',balance1)

elif(option=='Withdraw'):
    withdraw=st.number_input('Enter the amount to withdraw')
    balance2=initial_amount-withdraw
    if initial_amount <= withdraw:
        st.write("Balance after deposit:",balance2)
    else:
        st.warning("Insufficient Balance")
    st.write('Updated balance after deposit:',balance2)

elif(option=='Display'):
    st.write('The Name is:',name)
    st.write('The C_number is:', c_number)
    st.write('The Branch is:', branch)
    st.write('The Initail amount is:',initial_amount)