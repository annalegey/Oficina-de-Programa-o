import pandas as pd

df = pd.read_csv('brasil-win.csv')

st.write(df)
st.area_chart(df)
