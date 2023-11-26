import streamlit as st
import pandas as pd

districts = [ "Barisal", "Bogra", "Chittagong", "Comilla", "Dhaka", "Khulna", "Mymensingh", "Narayanganj", "Rajshahi", "Sylhet"]

st.title("Historic Data")
st.subheader("")


with open('theme.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

box = st.selectbox(label = 'Select District', options = districts)

#Select number of days
dn = st.slider(label = "" ,min_value = 5, max_value = 500, step = 5)

if box == "Barisal":
    url = 'https://raw.githubusercontent.com/Sidra-Tul-Muntaha-Ghouri/Flood-Prediction/main/datasets/Barisal.csv'

elif box == "Bogra":
    url = 'https://raw.githubusercontent.com/Sidra-Tul-Muntaha-Ghouri/Flood-Prediction/main/datasets/Bogra.csv'

elif box == "Dhaka":
    url = 'https://raw.githubusercontent.com/Sidra-Tul-Muntaha-Ghouri/Flood-Prediction/main/datasets/Dhaka.csv'

# Read CSV with error_bad_lines parameter
data = pd.read_csv(url, error_bad_lines=False)
df = pd.DataFrame(data)
st.dataframe(df.head(dtf))

