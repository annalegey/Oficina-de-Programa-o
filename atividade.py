import csv
import pandas as pd
arquivo = open('brasil-win.csv', encoding = 'ISO-8859-1')
for registro in csv.reader(arquivo,delimiter =';'):
  print(registro)
  df = pd.DataFrame(registro)
  df
