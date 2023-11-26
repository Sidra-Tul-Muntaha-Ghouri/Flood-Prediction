import streamlit as st
import pandas as pd


districts = [ "Barisal", "Bogra", "Chittagong", "Comilla", "Dhaka", "Khulna", "Mymensingh", "Narayanganj", "Rajshahi", "Sylhet"]

st.title("Forecast")
st.subheader("")


with open('theme.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

box = st.selectbox(label = 'Select District', options = districts)
#days to forecast
dtf = st.slider(label = "Days to Forecast" ,min_value = 1 , max_value = 10 )




