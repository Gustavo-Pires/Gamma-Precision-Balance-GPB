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

#-----ABRINDO O ARQUIVO DE CONTAGEM----------------
ws = xw.Book("amostra.xlsx").sheets['calculo'] 
coluna_ekeV = ws.range("A7:A103").value
coluna_cont = ws.range("D7:D103").value 
coluna_incerteza = ws.range("E7:E103").value 

#------------GRAFICO ESPECTRO DE CONTAGEM POR ENERGIA----------------
fig.plot(coluna_ekeV, coluna_cont); fig.grid(True); fig.axis((min(coluna_ekeV), max(coluna_ekeV), min(coluna_cont) , max(coluna_cont))); 
fig.title("Espectrometria Gama-"); fig.xlabel("Energia (keV)"); fig.ylabel("Contagem"); fig.savefig("grafico_expectro.png"); 


#--------------------------------GRAFICOS GERAIS--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets["Dados brutos"] 

#____________Potassio 40____________
p_40_coluna_concetracao = ws2.range("AD32:AD70").value
p_40_coluna_incerteza = ws2.range("AD32:AD70").value
p_40_total=ws2.range("AF32:AF70").value
med_mundial_p40=((400))


#------------GRAFICO CONCETRACAO MEDIA DE POTASSIO 40----------------
fig.plot( p_40_total, p_40_coluna_concetracao); fig.title("Concentração de Potassio-40"); fig.xlabel("Amostras"); fig.ylabel("Concentração"); fig.savefig("grafico_do_40.png"); 
fig.show()
