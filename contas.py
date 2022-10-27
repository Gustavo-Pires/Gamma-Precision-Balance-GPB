import matplotlib.pyplot as fig 
import numpy as ny 
import openpyxl
import xlrd 
import pandas as pd
import xlrd
import xlwings as xw
import os
import numpy as np
from typing import Union
import statistics
from statistics import median
from math import isnan
from itertools import filterfalse

#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets["Dados brutos"] 

#____________Potassio 40____________
p_40_coluna_concetracao = ws2.range("AD32:AD70").value
p_40_coluna_incerteza = ws2.range("AE32:AE70").value
p_40_total=ws2.range("AF32:AF70").value
med_mundial_p40=((400))

for index, value in enumerate(p_40_coluna_concetracao):
    if value <0:
      p_40_coluna_concetracao.remove(value)
        #p_40_coluna_concetracao[index] = 
        
#-----------MEDIAS----------
p_40_med_concetracao = statistics.mean(p_40_coluna_concetracao)
p_40_med_incerteza=statistics.mean(p_40_coluna_incerteza)