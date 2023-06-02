import pandas as pd
import csv
import streamlit as st

df = pd.read_csv('brasil-win.csv', encoding='ISO-8859-1')

st.write(df)
st.bar_chat(df)
