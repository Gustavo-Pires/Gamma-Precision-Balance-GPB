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

#_________________________________Potassio 40_________________________________
p_40_coluna_concentracao = ws2.range("AD32:AD70").value
p_40_coluna_incerteza = ws2.range("AE32:AE70").value
med_mundial_p40=((400))


for index, value in enumerate(p_40_coluna_concentracao):
    if value <0:
        print(index)
        remover=(index)
        p_40_coluna_concentracao.remove(value)
        p_40_coluna_incerteza.remove(remover)


def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

media_concentracao_def=((somalista(p_40_coluna_concentracao))/len(p_40_coluna_incerteza )
media_concentracao_def=((somalista(p_40_coluna_concentracao))/len(p_40_coluna_incerteza )
        
#-----------MEDIAS----------
p_40_med_concentracao = statistics.mean(p_40_coluna_concentracao)
p_40_med_incerteza=statistics.mean(p_40_coluna_incerteza)
