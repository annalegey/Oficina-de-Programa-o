import pandas as pd

df = pd.read_csv('brasil-win.csv', encoding='utf-8')

st.write(df)
st.area_chart(df)
