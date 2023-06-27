#CODIGO DE CALCULO DE RADIONUCLIDEOS(CCR) 

#-------------IMPORTANTE--------------------------------
#TODA CONTAGEM TEM QUE SER SALVADA COM O NOME "AMOSTRA"
# DEVE EXISTIR UMA PANILHA COM O PESO E IDENTIFICACAO DAS AMOSTRAS #fazer modelo 
#------------------------------------------------------- 
    
#-------------IMPORTANTE--------------------------------
#Uma pasta do Windows: C:\Windows\Jose\Python
#Um diretório no Linux : /home/user/Maria/Python  
#Ou seja, as barras são invertidas! 
#Se tentar acessar um endereço que não existe (como um C: no Linux ou /home no Windows) vai dar erro sim em seus scripts!
#-------------------------------------------------------

#talvez fazer um arquivo de log onde ele vai la e informa qual amostra foi ja calcula, adicionando a uma lista de execel para 
#posteriormente facilitar a analise dos dados pelo fato de ja saber quais foram analisadas e terem os nomes delas 

#-----Importacoes de bibliotecas que ser serao utilizadas 
import statics as st 
import pandas as pd
import xlrd
import xlwings as xw
import os
import numpy as np
from typing import Union
import matplotlib.pyplot as fig 
import openpyxl
import xlrd 



#-----CONVERTENDO O ARQUIVO DE CONTAGEM
read_file = pd.read_csv (r'amostra.csv') #ele le a amostra no mesmo diretorio, logo é importante colcar o codigo na pasta de cada amostra
read_file.to_excel (r'amostra.xlsx', index = None, header=True) #salva o arquivo convertido em excel

#-----ABRINDO O ARQUIVO DE CONTAGEM
workbook = xlrd.open_workbook('amostra.xls') #creio que pode excluir esse ja que o debaixo faz a mesma coisa, esta funcionando e é mais facil de entender e menor 
worksheet = workbook.sheet_by_name('Calculo') 
worksheet = workbook.sheet_by_index(0)

identificacao_amostra= ()#fazer uma variavel a priori que pega o nome da pasta em que se encontra # que sera usado para o peso da amostra, a celula B1 da planilha de calculo e para o excel de contas gerais 

ws = xw.Book("amostra.xlsx").sheets['calculo'] #---TA FUNCIONADO---# Specifying a sheet
 
 #-----ABRINDO PLANILHA DE PESO DAS AMOSTRAS 
ws1 = xw.Book("peso.xlsx").sheets['peso'] #criar essa planilha com idenficao na coluna b e peso na coluna c aparitr da linha 3
coluna_peso = ws1.range("B3:B203").value #Convertendo a coluna em lista #bom, o limite de amostras é 200 
pré_peso_amostra= coluna_peso.index("identificacao_amostra")# aqui ele pega o index do peso da amostra
Coluna_peso="C"+str(pré_peso_amostra) # a coluna c esta certa, pois é aonde é o peso 
peso_amostra= ws1.range("Coluna_peso").value #bom, aqui é para ele pegar o valor da variavel anterior e declarar como a celula a se retirar a informacao 
#aqui um codigo para ele ir na planilha de calculo e substir o peso pelo peso que ele achou acima 

#CRIANDO UMA LISTA COM OS RADIONUCLIDEOS DA CONTAGEM

#-----PEGANDO OS VALORES DA COLUNA DE CONTAGEM E INCERTEZA E COLOCANDO EM LISTAS SEPARADAS
coluna_ekeV = ws.range("a7:a150").value #COLUNA DE ENERGIA #---TA FUNCIONADO----
coluna_cont = ws.range("D7:D150").value #COLUNA DE CONTAGEM #---TA FUNCIONADO----
coluna_incerteza = ws.range("E7:E150").value #COLUNA DE INCERTEZA #---TA FUNCIONADO---


#o unico problema é que ele no len esta contado até os espacos vazios, nao se se futura mente isso vai ser um problema


#Creio que esses 2 for seram desncecessarios visto que o de cima ja esta fazendo a mesma coisa e até com menos codigo 
for i in range(worksheet.nrows): 
    valor = worksheet.cell_value(i, 0) # Pega os valores do excel
    contagem.append(valor) # Insere os valores na lista
for i in range(worksheet.nrows):
    valor = worksheet.cell_value(i, 1) # Pega os valores do excel
    incerteza.append(valor) # Insere os valores na lista
    
#-----VARIAVEIS DE ENTRADA DE DADOS 
# for type checks

array = list, np.ndarray
Array = Union[list, np.ndarray]
Number = Union[int, float]

#---------Margem de variacao de pico EkeV 
>=337 and <=339
>=910 and <=912
>=726 and <=728
>=237 and <=239
>=350 and <=352
>=608 and <=610
>=1119 and <=1121
>=45 and <=47
>=1459 and <=1461

#aqui vai ser onde ele ira encontrar os  radiomuclideos  na tabela convertida  baseado nas variacoes 
#acima descrias, logo o programa ira procurar, dar um find, e essa variavel ira armazenar qual o index desse pico


radionuclideo_338 = #aqui vai ter um index para achar algo entre   >=337 and <=339        #ws.range("D18").value  foi sugestao do git hub auto copilot
radionuclideo_911= 
radionuclideo_727 =
radionuclideo_238 =
radionuclideo_351 =
radionuclideo_609 =
radionuclideo_1120 =
radionuclideo_46 =
radionuclideo_1460 =


#aqui ele ira usar o index delcarado nas variaveis acima para saber aonde se encontra os dados
#D é contagem e E é incerteza 
cont_338="D"+str(radionuclideo_338)  #aqui ele vai pegar o index a coluna D formando a celula a qual esta a contagem desse elemento 
incer_338="E"+str(radionuclideo_338)
cont_911="D"+str(radionuclideo_911)
incer_911="E"+str(radionuclideo_911)
cont_727= "D"+str(radionuclideo_727)
incer_727= "E"+str(radionuclideo_727)
cont_238= "D"+str(radionuclideo_238)
incer_238= "E"+str(radionuclideo_238)
cont_351= "D"+str(radionuclideo_351)
incer_351= "E"+str(radionuclideo_351)
cont_609= "D"+str(radionuclideo_609)
incer_609= "E"+str(radionuclideo_609)
cont_1122= "D"+str(radionuclideo_1122)
incer_1120= "E"+str(radionuclideo_1120)
cont_46= "D"+str(radionuclideo_46)
incer_46= "E"+str(radionuclideo_46)
cont_1460= "D"+str(radionuclideo_1460)
incer_1460= "E"+str(radionuclideo_1460)

#-----SAIDA DOS RESULTADOS DO CALCULO 
calculo_conc_338= #coluna w4 #aqui ele vai escever na coluna w7 o valor que foi declarado acima 
calcilo_incer_338=#coluna x4
calculo_conc_911= #coluna w5
calcilo_incer_911= #coluna x5
calculo_conc_727= #coluna w6
calcilo_incer_727= #coluna x6
calculo_conc_238= #coluna x7
calcilo_incer_238= #coluna x7
calculo_conc_351= #coluna x11
calcilo_incer_351= #coluna x11
calculo_conc_609= #coluna x12
calcilo_incer_609= #coluna x12
calculo_conc_1120= #coluna x13
calcilo_incer_1120= #coluna x13
calculo_conc_46= #coluna x14
calcilo_incer_46= #coluna x14
calculo_conc_1460= #coluna x17
calcilo_incer_1460= #coluna x17


#-----COLOCANDO OS A CONCENTRACAO E INCERTEZA NA PLANILHA DE CALCULO GERAL
#abrir outra planilha para o caulo gera 
#acho que posso pegar os dados dessa planilha, coneverter em lista, dar um apend e inserir o que acabou de ser caculado e depois escrever no excel, idem ao gerador em massa de cpf 


#-----CRIANDO UMA PLANILHA COM OS RESULTADOS DO CALCULO GERAL 
Amostras= a1p1-1, a1p1-2, a1p1-3, a1p2-1, a1p2-2, a1p2-3 #varivael aleatoria das amostras ja analisadas 
#usar para salvar com o nome da amostra
with open('cpf.txt', 'w') as temp_file:
    for item in cpf:
        temp_file.write("%s\n" % item)
file = open('cpf.txt', 'r')
print(file.read())
            

df = pd.read_csv('cpf.txt') # can replace with df = pd.read_table('input.txt') for '\t'
df.to_excel('{colcoar o numero do elemento da lista apra salvar com o nome }.xlsx', 'Sheet1', index=False) #tentar salvar em um arquivo de excel com o nome da amostra

#Futuro calculos
#media da concentracao 
statistics.mean()
    #desvio padrao da concentracao 
    #desvio padrao da media da concentracao 

#media da incerteza 
    #desvio padrao da incerteza 
    #desvio padrao da media da incerteza 
    


