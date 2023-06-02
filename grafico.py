import csv
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('brasil-win.csv')
st.write(df)
st.area_chart(df)
