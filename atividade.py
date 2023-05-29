import csv
arquivo = open('brasil-win.csv', encoding = 'ISO-8859-1')
contador = 0
for registro in csv.reader(arquivo,delimiter =';'):
  print(registro)
  if contador == 10:
