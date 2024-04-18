import streamlit as st
from PIL import Image
img1 = Image.open('img_1.png')
st.title('DISPLAYING IMAGE')
st.image(img1,width=750)
st.title("streamlit demo")
st.header("This is PUNEETH RAJKUMAR")
img2 = Image.open('img.png')
st.image(img2,width=750)
