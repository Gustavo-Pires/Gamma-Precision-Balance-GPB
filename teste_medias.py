#----------------------------------------BIBLIOTECAS----------------------------------------
import xlwings as xw
import statistics
from statistics import median
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

#-----ABRINDO O ARQUIVO DE CONTAGEM----------------
ws = xw.Book("contas.xlsx").sheets['Dados brutos'] 
coluna_ekeV = ws.range("A7:A103").value
coluna_cont = ws.range("D7:D103").value 
coluna_incerteza = ws.range("E7:E103").value 
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
p_40_coluna_concetracao = ws.range("AD32:AD70").value
p_40_coluna_incerteza = ws.range("AE32:AE70").value
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
for index, value in enumerate(p_40_coluna_concetracao):
    if value <0:
      p_40_coluna_concetracao.remove(value)
      numero= index
      #p_40_coluna_incerteza.remove(numero)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
media_con_sum=(sum(p_40_coluna_concetracao)/len(p_40_coluna_concetracao))
media_inc_sum=(sum(p_40_coluna_incerteza)/len(p_40_coluna_incerteza))

media_con_statistics=(statistics.mean(p_40_coluna_concetracao))
media_inc_statistics=(statistics.mean(p_40_coluna_incerteza))
#-------------------------------------------------------------------------------------------
print("-"*40)
print("A media concentracao pela statistics é:", media_con_statistics)         #------------------statistics
print("A media incerteza pela statistics é:", media_inc_statistics)
print("-"*40)
print("A media concentracao pela sum é:", media_con_sum)                       #------------------SUM
print("A media incerteza pela sum é:", media_inc_sum)
print("-"*40)
print("A media concentracao pelo excel é:", ws.range("AK88").value)            #------------------excel 
print("A media incerteza pelo excel é:", ws.range("AK89").value)
print("-"*40)