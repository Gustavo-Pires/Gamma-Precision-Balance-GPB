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

def clearzero():
    for index, value in enumerate(listadef):
        if value <0:
            negativo=(index(value)
            p_40_coluna_concentracao.remove(negativo)
            p_40_coluna_incerteza.remove(negativo)
            
def calculo_media():
    def somalista():
        soma = 0
        for i in media:
            soma = soma + i
        return soma
    def fazendomedia():
        media=((soma)/len(media))

media=()


#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets["Dados brutos"] 

#_________________________________Potassio 40__________________________________
p_40_coluna_concentracao = ws2.range("AD32:AD70").value
p_40_coluna_incerteza = ws2.range("AE32:AE70").value
med_mundial_p40=((400))

clearzero() #para retirar os negativos

media=p_40_coluna_concentracao
med_def_con_p40= calculo_media()

media=p_40_coluna_incerteza
med_def_inc_p40=calculo_media() 
#______________________________________________________________________________


#media_concentracao_def=((somalista(p_40_coluna_concentracao))/len(p_40_coluna_incerteza )            
#media_concentracao_def=((somalista(p_40_coluna_concentracao))/len(p_40_coluna_incerteza )
        
#-----------MEDIAS----------
p_40_med_= statistics.mean(p_40_coluna_concentracao)
p_40_incerteza=statistics.mean(p_40_coluna_incerteza)

print("A media concetracao pela funcao que soma a lista é:", ed_def_con_p40)   #------------------FUNCAO DEF
print("A media incerteza pela funcao que soma a lista é:", med_def_inc_p40)

print("A media concentracao pela statistics é:", p_40_med)                     #------------------statistics
print("A media incerteza pela fstatistics é:", p_40_incerteza)
