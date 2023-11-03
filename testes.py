#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime
from tkinter import PhotoImage
import xlwings as xw
import time
import pandas as pd
import os
#------------------------------------------------------------------------------------------------------
start_time = time.time()
 
# Obter o caminho absoluto do diretório em que o código está sendo executado
diretorio_atual = os.path.abspath(os.path.dirname(__file__))

# Procurar por um arquivo Excel no diretório atual e obter o caminho absoluto do arquivo
nome_arquivo_excel = None
for nome_arquivo in os.listdir(diretorio_atual):
    if nome_arquivo.endswith('.xls'): # ou .xls, dependendo da extensão do arquivo
        nome_arquivo_excel = nome_arquivo
        break

if nome_arquivo_excel is not None:
    caminho_arquivo_excel = os.path.join(diretorio_atual, nome_arquivo_excel)

else:
    print("Nenhum arquivo Excel foi encontrado no diretório atual.")

#---------------------------------------------CONTAGEM -------------------------------------
wb = xw.Book(caminho_arquivo_excel)
ws = wb.sheets[caminho_arquivo_excel]

ekev = ws.range("A7:A27").options(numbers=str).value
contagem = ws.range("D7:D27").options(numbers=str).value
incerteza = ws.range("E7:E27").options(numbers=str).value
nome_amostra= ws.range("A1").options(numbers=str).value

wb.close()

#----------removendo celulas vazias----------
ekev= [x for x in  ekev if x is not None]
contagem= [x for x in contagem if x is not None]
incerteza= [x for x in incerteza if x is not None]
#----------------------------------------------

nome_amostra = nome_amostra.split("\\")[-2]
#------------------------------------------------------------------------------------------------------

#---------------------------------------------PLANILHA ARMAZENAR DADOS-------------------------------------

wb = xw.Book("concentracao.xlsx")
ws3= wb.sheets['concentracao']

Amostra=ws3.range("C7:C107").options(numbers=str).value

contagem_338=ws3.range("D7:D107").options(numbers=str).value
Incerteza_338=ws3.range("E7:E107").options(numbers=str).value

contagem_911=ws3.range("F7:F107").options(numbers=str).value
Incerteza_911=ws3.range("G7:G107").options(numbers=str).value

contagem_727=ws3.range("H7:H107").options(numbers=str).value
Incerteza_727=ws3.range("I7:I107").options(numbers=str).value

contagem_238=ws3.range("J7:J107").options(numbers=str).value
Incerteza_238=ws3.range("K7:K107").options(numbers=str).value

contagem_351=ws3.range("L7:L107").options(numbers=str).value
Incerteza_351=ws3.range("M7:M107").options(numbers=str).value

contagem_609=ws3.range("N7:N107").options(numbers=str).value
Incerteza_609=ws3.range("O7:O107").options(numbers=str).value

contagem_1120=ws3.range("P7:P107").options(numbers=str).value
Incerteza_1120=ws3.range("Q7:Q107").options(numbers=str).value

contagem_46=ws3.range("S7:R107").options(numbers=str).value
Incerteza_46=ws3.range("S7:S107").options(numbers=str).value

contagem_1460=ws3.range("T7:T107").options(numbers=str).value
Incerteza_1460=ws3.range("U7:U107").options(numbers=str).value

wb.close()


#----------removendo celulas vazias----------
Amostra=[x for x in  Amostra if x is not None]

contagem_338=[x for x in  contagem_338 if x is not None]
Incerteza_338=[x for x in  Incerteza_338 if x is not None]

contagem_911=[x for x in  contagem_911 if x is not None]
Incerteza_911=[x for x in  Incerteza_911 if x is not None]

contagem_727=[x for x in  contagem_727 if x is not None]
Incerteza_727=[x for x in  Incerteza_727 if x is not None]

contagem_238=[x for x in  contagem_238 if x is not None]
Incerteza_238=[x for x in  Incerteza_238 if x is not None]

contagem_351=[x for x in  contagem_351 if x is not None]
Incerteza_351=[x for x in  Incerteza_351 if x is not None]

contagem_609=[x for x in  contagem_609 if x is not None]
Incerteza_609=[x for x in  Incerteza_609 if x is not None]

contagem_1120=[x for x in  contagem_1120 if x is not None]
Incerteza_1120=[x for x in  Incerteza_1120 if x is not None]

contagem_46=[x for x in  contagem_46 if x is not None]
Incerteza_46=[x for x in  Incerteza_46 if x is not None]

contagem_1460=[x for x in  contagem_1460 if x is not None]
Incerteza_1460=[x for x in  Incerteza_1460 if x is not None]
#----------------------------------------------
#------------------------------------------------------------------------------------------------------

#---------------------------------------------MASSA AMOSTRA---------------------------------------------
wb = xw.Book("id_massa.xlsx")
ws4= wb.sheets['massa']

identificacao = ws4.range("B2:B101").options(numbers=str).value
massa = ws4.range("C2:C101").options(numbers=str).value

wb.close()

identificacao=[x for x in  identificacao if x is not None]
massa=[x for x in  massa if x is not None]
#------------------------------------------------------------------------------------------------------

#----------------------------------------------
wb = xw.Book("conta.xlsx")
ws2= wb.sheets['conta']

#-----------------------------------------eKEV 338-------------------------------------------------------------
valor_procurado = 338
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S5').value = contagem[j]
            ws2.range('T5').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_338.append(ws2.range("W5").options(numbers=str).value)
Incerteza_338.append(ws2.range("X5").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------

#-----------------------------------------eKEV 911-------------------------------------------------------------
valor_procurado = 911
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S6').value = contagem[j]
            ws2.range('T6').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_911.append(ws2.range("W6").options(numbers=str).value)
Incerteza_911.append(ws2.range("X6").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------

#-----------------------------------------eKEV 727-------------------------------------------------------------
valor_procurado = 727
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S7').value = contagem[j]
            ws2.range('T7').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_727.append(ws2.range("W7").options(numbers=str).value)
Incerteza_727.append(ws2.range("X7").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------eKEV 238-------------------------------------------------------------
valor_procurado = 238
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S8').value = contagem[j]
            ws2.range('T8').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_238.append(ws2.range("W8").options(numbers=str).value)
Incerteza_238.append(ws2.range("X8").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------eKEV 351-------------------------------------------------------------
valor_procurado = 351
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S12').value = contagem[j]
            ws2.range('T12').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_351.append(ws2.range("W12").options(numbers=str).value)
Incerteza_351.append(ws2.range("X12").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------eKEV 609-------------------------------------------------------------
valor_procurado = 609
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S13').value = contagem[j]
            ws2.range('T13').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_609.append(ws2.range("W13").options(numbers=str).value)
Incerteza_609.append(ws2.range("X13").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------eKEV 1120-------------------------------------------------------------
valor_procurado = 1120
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S14').value = contagem[j]
            ws2.range('T14').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_1120.append(ws2.range("W14").options(numbers=str).value)
Incerteza_1120.append(ws2.range("X14").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------eKEV 46-------------------------------------------------------------
valor_procurado = 46
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S15').value = contagem[j]
            ws2.range('T15').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_46.append(ws2.range("W15").options(numbers=str).value)
Incerteza_46.append(ws2.range("X15").options(numbers=str).value)
#----------------------------------------------------------------------------------------------------------------
#-----------------------------------------eKEV 1460-------------------------------------------------------------
valor_procurado = 1460
def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            ws2.range('S18').value = contagem[j]
            ws2.range('T18').value = incerteza[j]
            wb.save()
            break
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)

contagem_1460.append(ws2.range("W18").options(numbers=str).value)
Incerteza_1460.append(ws2.range("X18").options(numbers=str).value)


ws2.range('B2').options(transpose=True).value = [str(nome_amostra)]

#-------------------------------MASSA-------------------------------
def encontrar_massa(identificacao, massa, nome_amostra):
    try:
        indice_amostra = identificacao.index(nome_amostra)
        return massa[indice_amostra]
    except ValueError:
        return None
    
massa_amostra = encontrar_massa(identificacao, massa, nome_amostra)

if massa_amostra is not None:
    # Escrever a massa na célula X2
    ws2.range('X2').value = massa_amostra
else:
    print(f"Amostra {nome_amostra} não encontrada na lista de identificação.")

#------------------------------------------------------------------
wb.save()
Amostra.append(nome_amostra)
#----------------------------------------------------------------------------------------------------------------
 
wb = xw.Book("concentracao.xlsx")
ws3= wb.sheets['concentracao']

ws3.range('C7:C107').options(transpose=True).value = [Amostra]

ws3.range('D7:D107').options(transpose=True).value = [contagem_338 ]
ws3.range('E7:E107').options(transpose=True).value = [Incerteza_338 ]

ws3.range('F7:F107').options(transpose=True).value = [contagem_911 ]
ws3.range('G7:G107').options(transpose=True).value = [Incerteza_911 ]

ws3.range('H7:H107').options(transpose=True).value = [contagem_727 ]
ws3.range('I7:I107').options(transpose=True).value = [Incerteza_727 ]

ws3.range('J7:J107').options(transpose=True).value = [contagem_238 ]
ws3.range('K7:K107').options(transpose=True).value = [Incerteza_238 ]

ws3.range('L7:L107').options(transpose=True).value = [contagem_351 ]
ws3.range('M7:M107').options(transpose=True).value = [Incerteza_351 ]

ws3.range('N7:N107').options(transpose=True).value = [contagem_609 ]
ws3.range('O7:O107').options(transpose=True).value = [Incerteza_609 ]

ws3.range('P7:P107').options(transpose=True).value = [contagem_1120 ]
ws3.range('Q7:Q107').options(transpose=True).value = [Incerteza_1120 ]

ws3.range('R7:R107').options(transpose=True).value = [contagem_46 ]
ws3.range('S7:S107').options(transpose=True).value = [Incerteza_46 ]

ws3.range('T7:T107').options(transpose=True).value = [contagem_1120 ]
ws3.range('U7:U107').options(transpose=True).value = [Incerteza_1120 ]

wb.save()
wb.close()


end_time = time.time()
elapsed_time = end_time - start_time

print("Tempo de execução:", elapsed_time, "segundos")
print("Calculo de concentração de radionuclídeos concluido")
