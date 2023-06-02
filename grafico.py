import pandas as pd
import csv
import streamlit as st

df = pd.read_csv('brasil-win.csv', encoding='ISO-8859-1')

st.title('Habitantes por área: Municípios Brasileiros')
st.write(df)
st.bar_chart(df, x = 'estado' , y= ['area', 'habitantes'])
