import csv
python manage.py import_data --no-input brasil-win.csv.xz
arquivo = open('brasil-win.csv', encoding = 'ISO-8859-1')
contador = 0
for registro in csv.reader(arquivo,delimiter =';'):
  print(registro)
  if contador == 10:
 
