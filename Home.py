import streamlit as st
import pandas as pd
import numpy as np
import json
from streamlit_extras.app_logo import add_logo


st.set_page_config(
    layout="wide", 
    page_title="Flood Prediction", 
    page_icon="⛅",
    initial_sidebar_state="expanded",
 )


with open('theme.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.title('Flood Prediction - Bangladesh 🇧🇩')

#st.image("app/artifactory/Home.png", caption='', use_column_width=True)

st.subheader('**FloodGuard: Integrating Rainfall Time Series and GIS Data for Flood Prediction and Waterbody Forecasting in Bangladesh**')

st.write(""" 
**Problem Statement:**\\
Bangladesh is highly susceptible to flooding due to its unique geography and monsoon climate. Flooding leads to significant socio-economic and environmental consequences, causing the loss of lives, displacing communities, damaging infrastructure, and disrupting livelihoods.\n

**Objective:**\\
The main objective of this project is to enhance forecasting system, minimize damages associated with flooding, and strengthen community resilience in Bangladesh.      
**Scope and Coverage:**\\
_______
**Data Sources:**\\
_______

""")

with st.sidebar:
     add_logo("omdena-bangladesh-chapter.png", height=200)
      
