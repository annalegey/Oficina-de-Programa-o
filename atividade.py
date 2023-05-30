import csv
import streamlit as st
import pandas as pd
import numpy as np

arquivo = open('brasil-win.csv', encoding = 'ISO-8859-1')
for registro in csv.reader(arquivo,delimiter =',')
    print(registro)
