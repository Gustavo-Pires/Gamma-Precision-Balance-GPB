#----------------------------------------BIBLIOTECAS----------------------------------------
import xlwings as xw
import statistics
from statistics import median
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

#-----ABRINDO O ARQUIVO DE CONTAGEM----------------
ws = xw.Book("contas.xlsx").sheets['Dados brutos'] 

p_50_coluna_concetracao = ws.range("AD32:AD88").value
p_50_coluna_incerteza = ws.range("AE32:AE88").value

#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
p_50_coluna_concetracao= [x for x in p_50_coluna_concetracao if x is not None]
p_50_coluna_incerteza= [x for x in p_50_coluna_incerteza if x is not None]

for index, value in enumerate(p_50_coluna_concetracao):
    if value <0:
        p_50_coluna_concetracao.remove(value)
      
for index, value in enumerate(p_50_coluna_incerteza):
    if value <0:
        p_50_coluna_incerteza.remove(value)
            
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
media_con_sum=(sum(p_50_coluna_concetracao)/len(p_50_coluna_concetracao))
media_inc_sum=(sum(p_50_coluna_incerteza)/len(p_50_coluna_incerteza))

media_con_statistics=(statistics.mean(p_50_coluna_concetracao))
media_inc_statistics=(statistics.mean(p_50_coluna_incerteza))
#-------------------------------------------------------------------------------------------
print("-"*50)
print("A media concentracao pela statistics é:", media_con_statistics)         #------------------statistics
print("A media incerteza pela statistics é:", media_inc_statistics)
print("-"*50)
print("A media concentracao pela sum é:", media_con_sum)                       #------------------SUM
print("A media incerteza pela sum é:", media_inc_sum)
print("-"*50)
print("A media concentracao pelo excel é:", ws2.range("AK88").value)            #------------------excel 
print("A media incerteza pelo excel é:", ws2.range("AK89").value)
print("   ")
print("-"*50)
print("-"*50)
print("   ")
#-------------------------------------------------------------------------------------------
print("-"*20,"Funções pela statistics","-"*20 )
print("A média geométrica dos dados de concetracao pela statistics é:", statistics.geometric_mean(p_50_coluna_concetracao))
print("A média harmonica dos dados de concetracao pela statistics é:", statistics.harmonic_mean(p_50_coluna_concetracao))
print("A Mediana(valor do meio) dos dados de concetracao pela statistics é:", statistics.median(p_50_coluna_concetracao))
print("A Mediana inferior dos dados de concetracao pela statistics é:", statistics.median_low(p_50_coluna_concetracao))
print("A Mediana superior dos dados de concetracao pela statistics é:", statistics.median_high(p_50_coluna_concetracao))
print("A  Mediana, ou o 50º percentil dos dados agrupados de concetracao pela statistics é:", statistics.median_grouped(p_50_coluna_concetracao))
print("A Moda (valor mais comum) de dados discretos ou nominais de concetracao pela statistics é:", statistics.mode(p_50_coluna_concetracao))
print("A MList of modes (most common values) of discrete or nominal data de concetracao pela statistics é:", statistics.multimode(p_50_coluna_concetracao))
print("A divisão dos dados em intervalos com probabilidade igua de concetracao pela statistics é:", statistics.quantiles(p_50_coluna_concetracao))




