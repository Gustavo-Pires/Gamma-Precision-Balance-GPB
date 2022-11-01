

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



#--------------------------------GRAFICOS CONCENTRACAO MEDIA A1--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228_keV338_A1= ws2.range("AK61").value		
Ac_228_keV911_A1=ws2.range("AK64").value 
Ac_228_media_A1=((float(Ac_228_keV338_A1)+float(Ac_228_keV911_A1))/2)
Bi_212_A1=ws2.range("AK67").value	
Pb_212_A1=ws2.range("AK70").value
Pb_214_A1=ws2.range("AK76").value	
Bi_214_keV609_A1=ws2.range("AK79").value
Bi_214_keV1120_A1=ws2.range("AK82").value
Bi_212_media_A1=(float(Bi_214_keV609_A1)+float(Bi_214_keV1120_A1)/2)			
K_40_A1=ws2.range("AK88").value 		

#____________EIXOS____________
concetracao=("Ac-228", "Bi-212", "Pb-212", "Pb-214", "Bi-214", "K-40") #EIXO X
Elementos=[Ac_228_media_A1, Bi_212_media_A1, Pb_212_A1, Pb_214_A1, Bi_214_keV609_A1, K_40_A1] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(False); fig.title("Concentração média-A1"); fig.xlabel("Elemento"); fig.ylabel("Concentração(Bq/kg)"); fig.savefig("concentracao_A1.png"); 

fig.close('all');

K_40_A1=(800)
K_40_A2=(500)
K_40_A3=(623)
K_40_AS=(550)
concetracao=("Ac-228", "Bi-212", "Pb-212", "Pb-214", "Bi-214", "K-40") #EIXO X
med_mundial_p40=(400)

#--------------------------------GRAFICOS CONCENTRACAO MEDIA K-40--------------------------------
#____________EIXOS____________
k40=(K_40_A1 ,K_40_A2,K_40_A3,K_40_AS, med_mundial_p40) 
Elementos=("A1", "A2", "A3", "AS" "Media mundial") 
#------------PLOT----------------
fig.bar(k40, Elementos); fig.grid(False); fig.title("Concentração média Potassio-40"); fig.xlabel("Elemento"); fig.ylabel("Concentração(Bq/kg)"); fig.savefig("comparacao_concentracao_k40png"); 
fig.close('all'); 
