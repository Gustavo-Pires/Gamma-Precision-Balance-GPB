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

#-----ABRINDO O ARQUIVO DE CONTAGEM
ws = xw.Book("amostra.xlsx").sheets['calculo'] 
coluna_ekeV = ws.range("A7:A103").value
coluna_cont = ws.range("D7:D103").value 
coluna_incerteza = ws.range("E7:E103").value 

#------------GRAFICO DE CONTAGEM POR ENERGIA----------------
fig.plot(coluna_ekeV,coluna_cont, label = 'DailyBirths'); fig.grid(True); fig.title("Espectrometria Gama"); fig.xlabel("Energia (keV)"); fig.ylabel("Contagem"); fig.savefig("grafico_contagem.png"); 
fig.show()
