#----------------------------------------BIBLIOTECAS----------------------------------------
import xlwings as xw
import numpy as np
from typing import Union
import statistics
from statistics import median
from math import isnan
from itertools import filterfalse
#def media_filterfalse(media_filterfalse): #calcula a media usando a funcao filterfalse
    #media_con_filterfalse.append(sum(filterfalse(lambda x: x == 0, funcoesmed))/len(filterfalse(lambda x: x == 0, funcoesmed)))
    #media_inc_filterfalse.append(sum(filterfalse(lambda x: x == 0, funcoesinc))/len(filterfalse(lambda x: x == 0, funcoesinc)))
#----------------------------------------VARIAVEIS INICIAIS----------------------------------------
analise_amostra=["--------------------------------ANALISE--------------------------------"]
media_con_sum=[]
media_inc_sum=[]
media_con_statistics=[]
media_inc_statistics=[]
#----------------------------------------FUNCOES DE CALCULOS----------------------------------------
def clearzero(clearzero): #Limpar os zeros da lista
    for index, value in enumerate(funcoesmed): #enumerate(listadef)
        if value <=0:
            funcoesmed.remove((index(value)))#'int' object is not callable
            funcoesinc.remove((index(value)))#'int' object is not callable
            continue
        else:
            continue

#ambas as medias de def estao funcionais e sem erro
def media_sum(media_sum):#calcula a media fazendo a somatoria e divide pelo numero de elementos da lista
    media_con_sum.append(sum(funcoesmed)/len(funcoesmed))
    media_inc_sum.append(sum(funcoesinc)/len(funcoesinc))

def media_statistics(media_statistics): #calcula a media usando a funcao statistics
    media_con_statistics.append(statistics.mean(funcoesmed))
    media_con_statistics.append(statistics.mean(funcoesinc))
    
def analise(analise):
    #int(med_mundial).clear()#'int' object has no attribute 'clear' ---Simplesmente acho que eu posso atribuir a média mundial a cada elemento sem precisar excluir
    #int(elemento).clear() #mesma anotacao
    analise_amostra=[]
    a=[((("-"*30), elemento, ("-"*30)))]
    analise_amostra.append(a)
    b=[((("-"*30), elemento, ("-"*30)))]
    analise_amostra.append(b)
    c=[(("A média da concentração de", elemento, "foi de", media_con_sum, "Bq/kg"))]
    analise_amostra.append(c)
    d=[(("A média da incerteza de", elemento, "foi de", media_inc_sum, "Bq/kg"))]
    analise_amostra.append(d)
    e=[("A maior concentração registrada foi de ", min(funcoesinc), "Bq/kg")]
    analise_amostra.append(e)
    f=[("A menor concentração registrada foi de ", max(funcoesinc), "Bq/kg")]
    analise_amostra.append(f)
    

    def condicoes(condicoes):
        if valor_analise < variacao_1_med_mundial: #350
            analise_amostra = analise_amostra + ("O ", elemento, " está abaixo da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (med_mundial-valor_analise), "Bq/kg a menos, o equivalente a ", (valor_analise/med_mundial),"vezes abaixo da média mundial, o que repretenta um valor", str((valor_analise*100)/med_mundial), "% abaixo da média mundial.")
        elif valor_analise > variacao_2_med_mundial: #450
            analise_amostra = analise_amostra +("O", elemento, " está avalor_analiseima da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (valor_analise-med_mundial), "Bq/kg a mais, o equivalente a ", (valor_analise/med_mundial),"vezes avalor_analiseima da média mundial, o que repretenta um valor", str((((valor_analise*100)/med_mundial)-100)), "% avalor_analiseima da média mundial.")
        else: 
            if valor_analise <med_mundial :#menor que 400
               analise_amostra = analise_amostra +("0", elemento, " está dentro dos limites da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (med_mundial-valor_analise), "Bq/kg, o equivalente a ", (valor_analise/med_mundial),"vezes abaixo da média mundial.", str(((valor_analise*100)/med_mundial)))
            elif valor_analise >med_mundial :#maior que 400
                analise_amostra = analise_amostra +("O ", elemento, " está dentro dos limites da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (valor_analise-med_mundial), "Bq/kg, o equivalente a ", (valor_analise/med_mundial),"vezez abaixo da média mundial.", str(((valor_analise*100)/med_mundial)-100))
            else: #igual a 400
                analise_amostra = analise_amostra +("O ", elemento, " está exatamente dentro dos limites da média mundial. A média mundial é de", (med_mundial), ".") 
    analise_amostra.append((("-"*70)))

#-----ABRINDO O ARQUIVO DE CONTAS----------------
ws2 = xw.Book("contas.xlsx").sheets["Dados brutos"] 

#--------------------------------------------------------Potassio 40--------------------------------------------------------
p_40_coluna_concentracao = ws2.range("AD32:AD77").value
p_40_coluna_incerteza = ws2.range("AE32:AE77").value
med_mundial_p40=((400))

#variaveis para as funcoes
funcoesmed=p_40_coluna_concentracao
funcoesinc=p_40_coluna_incerteza

#------------variaveis-----------
elemento=("Potassio 40")
med_mundial=(400)          
variacao_1_med_mundial=(med_mundial)- 50
variacao_2_med_mundial=(med_mundial)+50 
media_con_p40=()
media_inc_p40=()
media_con_sum=()
valor_analise=media_con_sum #ele ta pegando o valor da media da funcao SUM e nao da funcao statistics para fazer a analise

#--------------DEFs--------------
clearzero #para retirar os negativos
media_sum#media
media_statistics#media
analise#analise

#---------------------------------------------------------------------------------------------------------------------------

#esse é um print só para ver qual deles é melhor e mais preciso/veridicio
media_con_statistic=[]
print("A media concentracao pela statistics é:", media_con_statistic)               #------------------statistics
print("A media incerteza pela statistics é:", media_inc_statistics)

print("A media concentracao pela sum é:", media_con_sum)                      #------------------SUM
print("A media incerteza pela sum é:", media_inc_sum)

print("A media concentracao pelo excel é:", ws2.range("AK88").value)               #------------------excel 
print("A media incerteza pelo excel é:", ws2.range("AK89").value)

#final=condicoes(condicoes)
#----------------------------SALVANDO ANALISE----------------------------
print(analise)
with open('ANALISE.txt', 'w') as temp_file:
    for item in analise_amostra:
        temp_file.write("%s\n" % item)
    file = open('ANALISE.txt', 'r')
    print(file.read())
#------------------------------------------------------------------------
