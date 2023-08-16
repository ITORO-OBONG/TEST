import streamlit as st
from PIL import Image
img = Image.open("STRONGYLOIDES SPP.JPG")
st.sidebar.image(img.resize((500, 400)))
st.header("My Crazy App")
st.subheader("This is my first application")
st.number_input("input any number", step =1)
st.text_input("what is your name")
st.date_input("select your year of birth")
st.checkbox("Do you agree")
st.selectbox("Gender", ['Male', 'Female', 'Others'])
st.select_slider("input", [5, 10, 15])
st.sidebar.radio("Gender", ['Male', 'Female', 'Others'])


pip install streamlit