import streamlit as st

st.title("Reg Form")
with st.form(key ='Form1'):
    with st.sidebar:

        user_word = st.text_input("Enter a Keyword:")
        select_language = st.radio('Tweet language',('All','English','Hindi'))
        include_retweets = st.checkbox('Include retweets in data')
        num_of_tweets = st.number_input("Minimum number of tweets",100)
        submitted1 = st.form_submit_button(label='Search twitter')

st.write("Keyword is:",user_word)
st.write("language is:",select_language)