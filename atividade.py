import csv
arquivo = open('brasil-win.csv', encoding = 'ISO-8859-1')
for registro in csv.reader(arquivo,delimiter =','):
    
