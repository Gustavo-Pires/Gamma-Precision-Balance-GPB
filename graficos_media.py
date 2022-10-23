
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
Ac_228A1= ws2.range("AK61").value		
keV911A1=ws2.range("AK64").value 			
Bi_212A1=ws2.range("AK67").value	
Pb_212A1=ws2.range("AK70").value	
Pb_214A1=ws2.range("AK76").value	
Bi_214A1=ws2.range("AK79").value
keV1120A1=ws2.range("AK82").value			
K_40A1=ws2.range("AK88").value 		
#____________EIXOS____________
concetracao=("Ac-228", "ekeV-911", "Bi-212", "Pb-212", "Pb-214", "Bi-214", "ekeV-1120", "K-40") #EIXO X
Elementos=[Ac_228A1,keV911A1,Bi_212A1,Pb_212A1,Pb_214A1,Bi_214A1,keV1120A1,K_40A1] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(True); fig.title("Concetração média-A1"); fig.xlabel("Elemento"); fig.ylabel("Concetração(Bq/kg)"); fig.savefig("concentracao_amostras.png"); 
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA A2--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228A2= ws2.range("AL61").value		
keV911A2=ws2.range("AL64").value 			
Bi_212A2=ws2.range("AL67").value	
Pb_212A2=ws2.range("AL70").value	
Pb_214A2=ws2.range("AL76").value	
Bi_214A2=ws2.range("AL79").value
keV1120A2=ws2.range("AL82").value			
K_40A2=ws2.range("AL88").value 		
#____________EIXOS____________
concetracao=("Ac-228", "ekeV-911", "Bi-212", "Pb-212", "Pb-214", "Bi-214", "ekeV-1120", "K-40") #EIXO X
Elementos=[Ac_228A2,keV911A2,Bi_212A2,Pb_212A2,Pb_214A2,Bi_214A2,keV1120A2,K_40A2] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(True); fig.title("Concetração média-A2"); fig.xlabel("Elemento"); fig.ylabel("Concetração(Bq/kg)"); fig.savefig("concentracao_A1.png"); 
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA A3--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228A3= ws2.range("AM61").value		
keV911A3=ws2.range("AM64").value 			
Bi_212A3=ws2.range("AM67").value	
Pb_212A3=ws2.range("AM70").value	
Pb_214A3=ws2.range("AM76").value	
Bi_214A3=ws2.range("AM79").value
keV1120A3=ws2.range("AM82").value			
K_40A3=ws2.range("AM88").value 		
#____________EIXOS____________
concetracao=("Ac-228", "ekeV-911", "Bi-212", "Pb-212", "Pb-214", "Bi-214", "ekeV-1120", "K-40") #EIXO X
Elementos=[Ac_228A3,keV911A3,Bi_212A3,Pb_212A3,Pb_214A3,Bi_214A3,keV1120A3,K_40A3] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(True); fig.title("Concetração média-A3"); fig.xlabel("Elemento"); fig.ylabel("Concetração(Bq/kg)"); fig.savefig("concentracao_A2.png"); 
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA AS--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228AS= ws2.range("AN61").value		
keV911AS=ws2.range("AN64").value 			
Bi_212AS=ws2.range("AN67").value	
Pb_212AS=ws2.range("AN70").value	
Pb_214AS=ws2.range("AN76").value	
Bi_214AS=ws2.range("AN79").value
keV1120AS=ws2.range("AN82").value			
K_40AS=ws2.range("AN88").value 		
#____________EIXOS____________
concetracao=("Ac-228", "ekeV-911", "Bi-212", "Pb-212", "Pb-214", "Bi-214", "ekeV-1120", "K-40") #EIXO X
Elementos=[Ac_228AS,keV911AS,Bi_212AS,Pb_212AS,Pb_214AS,Bi_214AS,keV1120AS,K_40AS] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(True); fig.title("Concetração média-AS"); fig.xlabel("Elemento"); fig.ylabel("Concetração(Bq/kg)"); fig.savefig("concentracao_A3.png"); 
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA K-40--------------------------------
k40=(K_40A1, K_40A2, K_40A3, K_40AS, 400)
Elementos=("A1", "A2", "A3", "AS" "Media mundial") #EIXO X
fig.bar(Elementos, k40,); fig.grid(True); fig.title("Concetração média-AS"); fig.xlabel("Elemento"); fig.ylabel("Concetração(Bq/kg)"); fig.savefig("comparacao_concentracao_k40png"); 
