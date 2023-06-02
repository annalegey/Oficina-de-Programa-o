import pandas as pd
import st as streamlit

df = pd.read_csv('brasil-win.csv', encoding='ISO-8859-1')

st.write(df)
