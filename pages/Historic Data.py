import streamlit as st
import pandas as pd
import csv
from io import StringIO

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

response = pd.read_csv(url, header=None)


csv_data = StringIO(response.to_csv(index=False, header=None))
csv_reader = csv.reader(csv_data, delimiter=',')
data = []
for row in csv_reader:
    if len(row) == response.shape[1]:
        data.append(row)

df = pd.DataFrame(data, columns =response.columns)
st.dataframe(df.head(dn))

