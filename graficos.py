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
from statistics import median
from math import isnan
from itertools import filterfalse

#-----ABRINDO O ARQUIVO DE CONTAGEM----------------
ws = xw.Book("amostra.xlsx").sheets['calculo'] 
coluna_ekeV = ws.range("A7:A103").value
coluna_cont = ws.range("D7:D103").value 
coluna_incerteza = ws.range("E7:E103").value 

#------------GRAFICO ESPECTRO DE CONTAGEM POR ENERGIA----------------
#fig.plot(coluna_ekeV, coluna_cont); fig.grid(True); fig.axis((min(coluna_ekeV), max(coluna_ekeV), min(coluna_cont) , max(coluna_cont))); fig.title("Espectrometria Gama"); fig.xlabel("Energia (keV)", fontsize=9); fig.ylabel("Contagem"); fig.savefig("grafico_expectro.png"); 
#fig.close('all');

#--------------------------------GRAFICOS GERAIS--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets["Dados brutos"] 

#____________Potassio 40____________
p_40_coluna_concetracao = ws2.range("AD32:AD88").value
p_40_coluna_incerteza = ws2.range("AE32:AE88").value
p_40_total=ws2.range("AF32:AF88").value
med_mundial_p40=((400))

for index, value in enumerate(p_40_coluna_concetracao):
    if value <0:
      p_40_coluna_concetracao.remove(value)
        #p_40_coluna_concetracao[index] = 0
        #fazer um if-else-elif onde o if é se ele for none para remover da lista, else se ele for menor que 0 para remover da lista e elif para ele continuar 
        
quantidade=()
lenp40=len(p_40_coluna_concetracao)
lista=list(range( lenp40))
            
#------------GRAFICO CONCETRACAO MEDIA DE POTASSIO 40----------------
fig.plot( lista, p_40_coluna_concetracao); fig.title("Amostras A1-Concentração de Potassio-40 ");fig.grid(True); fig.xlabel("Amostras"); fig.ylabel("Concentração"); fig.savefig("grafico_do_40_amostras_a1.png"); 
fig.close('all');


