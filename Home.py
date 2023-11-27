import streamlit as st
import pandas as pd
import numpy as np
import json


st.set_page_config(
    layout="wide", 
    page_title="Weather Prediction", 
    page_icon="⛅",
    initial_sidebar_state="expanded",
 )


with open('theme.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.title('Flood Prediction - Bangladesh')

#st.image("app/artifactory/Home.png", caption='', use_column_width=True)

st.subheader('**FloodGuard: Integrating Rainfall Time Series and GIS Data for Flood Prediction and Waterbody Forecasting in Bangladesh**')

st.write(""" 
Bangladesh is highly susceptible to flooding due to its unique geography and monsoon climate. Flooding leads to significant socio-economic and environmental consequences, causing the loss of lives, displacing communities, damaging infrastructure, and disrupting livelihoods.         """)


with st.sidebar:
      st.image("omdena-bangladesh-chapter.png", use_column_width=True)
      st.markdown(
    """
    <style>
    div[data-widget="stSidebar"] {
        background-color: #336599;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True)
      
