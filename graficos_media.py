
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
#------------------------------------------------------------------------------------------


#--------------------------------GRAFICOS CONCENTRACAO MEDIA A2--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228_kev338_A2= ws2.range("AL61").value		
Ac_228_keV911_A2=ws2.range("AL64").value
Ac_228_media_A2=((float(Ac_228_kev338_A2)+float(Ac_228_keV911_A2))/2) 			
Bi_212_A2=ws2.range("AL67").value	
Pb_212_A2=ws2.range("AL70").value	
Pb_214_A2=ws2.range("AL76").value	
Bi_214_kev609_A2=ws2.range("AL79").value
Bi_214_keV1120_A2=ws2.range("AL82").value	
Bi_214_media_A2=((float(Bi_214_kev609_A2)+float(Bi_214_keV1120_A2))/2)		
K_40_A2=ws2.range("AL88").value 		
#____________EIXOS____________
Elementos=[Ac_228_media_A2,Bi_212_A2,Pb_212_A2,Pb_214_A2,Bi_214_media_A2,K_40_A2] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(False); fig.title("Concentração média-A2"); fig.xlabel("Elemento"); fig.ylabel("Concentração(Bq/kg)"); fig.savefig("concentracao_A2.png"); 
fig.close('all');
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA A3--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228_kev338_A3= ws2.range("AM61").value		
Ac_228_keV911_A3=ws2.range("AM64").value 
Ac_228_keV911_A3=float(Ac_228_keV911_A3)
Ac_228_media_A3=((float(Ac_228_kev338_A3)+float(Ac_228_keV911_A3))/2) 	
Bi_212_A3=ws2.range("AM67").value	
Pb_212_A3=ws2.range("AM70").value	
Pb_214_A3=ws2.range("AM76").value	
Bi_214_keV609_A3=ws2.range("AM79").value
Bi_214_keV1120_A3=ws2.range("AM82").value	
Bi_214_media_A3=((float(Bi_214_keV609_A3)+float(Bi_214_keV1120_A3))/2)		
K_40_A3=ws2.range("AM88").value 		
#____________EIXOS____________
Elementos=[Ac_228_media_A3,Bi_212_A3,Pb_212_A3,Pb_214_A3,Bi_214_media_A3,K_40_A3] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(False); fig.title("Concentração média-A3"); fig.xlabel("Elemento"); fig.ylabel("Concentração(Bq/kg)"); fig.savefig("concentracao_A3.png"); 
fig.close('all');
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA AS--------------------------------
#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets['Planilha1'] 
#____________elementos____________
Ac_228_kev338_AS= ws2.range("AN61").value
Ac_228_keV911_AS=ws2.range("AN64").value 	
Ac_228_media_AS=((float(Ac_228_kev338_AS)+float(Ac_228_keV911_AS))/2)		
Bi_212_AS=ws2.range("AN67").value	
Pb_212_AS=ws2.range("AN70").value	
Pb_214_AS=ws2.range("AN76").value	
Bi_214_keV1120_AS=ws2.range("AN79").value
Bi_214_keV1120_AS=ws2.range("AN82").value	
Bi_214_media_AS=((float(Bi_214_keV1120_AS)+float(Bi_214_keV1120_AS)/2))		
K_40_AS=ws2.range("AN88").value 		
#____________EIXOS____________
Elementos=[Ac_228_media_AS,Bi_212_AS,Pb_212_AS,Pb_214_AS,Bi_214_media_AS,K_40_AS] #EIXO Y
#------------PLOT----------------
fig.bar(concetracao, Elementos ); fig.grid(False); fig.title("Concentração média-AS"); fig.xlabel("Elemento"); fig.ylabel("Concentração(Bq/kg)"); fig.savefig("concentracao_AS.png"); 
fig.close('all');
#------------------------------------------------------------------------------------------

#--------------------------------GRAFICOS CONCENTRACAO MEDIA K-40--------------------------------
#____________EIXOS____________
k40=(K_40_A1, K_40_A2, K_40_A3, K_40_AS, 400) 
Elementos=("A1", "A2", "A3", "AS", "Media mundial") 
#------------PLOT----------------
fig.bar( Elementos, k40); fig.grid(False); fig.title("Concentração média Potassio-40"); fig.xlabel("Elemento"); fig.ylabel("Concentração(Bq/kg)"); fig.savefig("comparacao_concentracao_k40png"); 
fig.close('all'); 
