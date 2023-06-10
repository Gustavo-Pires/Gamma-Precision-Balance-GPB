#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime
from tkinter import PhotoImage
import xlwings as xw
import time

start_time = time.time()
#------------------------------------------------------------------------------------------------------
nome = "gustavo" #fazer iput para o nome do usuario
#---------------------------------------------ARQUIVO DE CONTAGEM -------------------------------------
import pandas as pd
pd.options.display.float_format = "{:.2f}".format  # <-- nova linha adicionada


# abre a planilha
wb = xw.Book("cali.xlsx")
ws = wb.sheets['cali']
 
ekev = ws.range("A7:A27").options(numbers=str).value
resolucao = ws.range("C7:C27").options(numbers=str).value
canal = ws.range("F7:F27").options(numbers=str).value
contagem = ws.range("D7:D27").options(numbers=str).value
incerteza = ws.range("E7:E27").options(numbers=str).value
data=ws.range("A2").options(numbers=str).value
# fecha a planilha
wb.close()

ekev = [float(x.replace(' ', '').replace(',', '.')) for x in ekev]


#----------removendo celulas vazias----------
ekev= [x for x in  ekev if x is not None]
resolucao= [x for x in resolucao if x is not None]
canal= [x for x in canal if x is not None]
contagem= [x for x in contagem if x is not None]
incerteza= [x for x in incerteza if x is not None]
#----------------------------------------------
print(ekev)
#------------------------------------------------------------------------------------------------------
#impotar as colunas da planilha de armazenamnto nessas variavies: 
ws2 = xw.Book("calibracao.xls").sheets['Calibracao']

data_hora= ws2.range("B9:B40").options(numbers=str).value

co_57_ekev= ws2.range("C9:C40").options(numbers=str).value
co_57_resolucao= ws2.range("D9:D40").options(numbers=str).value
co_57_canal =ws2.range("E9:E40").options(numbers=str).value
co_57_contagem =ws2.range("F9:F40").options(numbers=str).value
co_57_incerteza =ws2.range("G9:G40").options(numbers=str).value

co_60_ekev= ws2.range("H9:H40").options(numbers=str).value
co_60_resolucao= ws2.range("I9:I40").options(numbers=str).value
co_60_canal =ws2.range("J9:J40").options(numbers=str).value
co_60_contagem =ws2.range("K9:K40").options(numbers=str).value
co_60_incerteza =ws2.range("L9:L40").options(numbers=str).value

usuario= ws2.range("M9:M40").options(numbers=str).value

#----------removendo celulas vazias----------
data_hora=[x for x in data_hora if x is not None]

co_57_ekev= [x for x in co_57_ekev if x is not None]
co_57_resolucao= [x for x in co_57_resolucao if x is not None]
co_57_canal =[x for x in co_57_canal if x is not None]
co_57_contagem =[x for x in co_57_contagem if x is not None]
co_57_incerteza =[x for x in co_57_incerteza if x is not None]

co_60_ekev= [x for x in co_60_ekev if x is not None]
co_60_resolucao= [x for x in co_60_resolucao if x is not None]
co_60_canal =[x for x in co_60_canal if x is not None]
co_60_contagem =[x for x in co_60_contagem if x is not None]
co_60_incerteza=[x for x in co_60_incerteza if x is not None]

usuario= [x for x in usuario if x is not None]

#----------------------------------------------
#-----------------------------------------COBALTO 57-------------------------------------------------------------
valor_procurado= 122.06 
def adicionar_valores_na_lista(valor_procurado, ekev, resolucao, contagem, incerteza, canal):
    global co_57_ekev, co_57_resolucao, co_57_contagem, co_57_incerteza, co_57_canal, data_hora, usuario
    encontrado = False
    for i in range(len(canal)):
        for j in range(len(ekev)):
            if abs(float(ekev[j]) - valor_procurado) <= 1:
                encontrado = True
                co_57_ekev.append(ekev[j])
                co_57_resolucao.append(resolucao[j])
                co_57_contagem.append(contagem[j])
                co_57_incerteza.append(incerteza[j])
                co_57_canal.append(canal[j])
                data_hora.append(data)
                usuario.append(nome)
                break  # interrompe o laço de repetição mais próximo
        if encontrado:
            break  # interrompe o laço de repetição mais próximo
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, resolucao, contagem, incerteza, canal)


ws2.range('B9').options(transpose=True).value = [data_hora]
ws2.range('C9').options(transpose=True).value = [co_57_ekev]
ws2.range('D9').options(transpose=True).value = [co_57_resolucao]
ws2.range('E9').options(transpose=True).value = [co_57_canal]
ws2.range('F9').options(transpose=True).value = [co_57_contagem]
ws2.range('G9').options(transpose=True).value = [co_57_incerteza]


#----------------------------------------------------------------------------------------------------------------

#-----------------------------------------COBALTO 60-------------------------------------------------------------
valor_procurado= 1332.5
def adicionar_valores_na_lista(valor_procurado, ekev, resolucao, contagem, incerteza, canal):
    global co_57_ekev, co_57_resolucao, co_57_contagem, co_57_incerteza, co_57_canal, data_hora, usuario
    encontrado = False
    for i in range(len(canal)):
        for j in range(len(ekev)):
            if abs(float(ekev[j]) - valor_procurado) <= 1:
                encontrado = True
                co_60_ekev.append(ekev[j])
                co_60_resolucao.append(resolucao[j])
                co_60_contagem.append(contagem[j])
                co_60_incerteza.append(incerteza[j])
                co_60_canal.append(canal[j])
                break  # interrompe o laço de repetição mais próximo
        if encontrado:
            break  # interrompe o laço de repetição mais próximo
    return encontrado

adicionar_valores_na_lista(valor_procurado, ekev, resolucao, contagem, incerteza, canal)


ws2.range('H9').options(transpose=True).value = [co_60_ekev]
ws2.range('I9').options(transpose=True).value = [co_60_resolucao]
ws2.range('J9').options(transpose=True).value = [co_60_canal]
ws2.range('K9').options(transpose=True).value = [co_60_contagem]
ws2.range('L9').options(transpose=True).value = [co_60_incerteza] 
ws2.range('M9').options(transpose=True).value = [usuario]

# fecha a planilha

#----------------------------------------------------------------------------------------------------------------
end_time = time.time()
elapsed_time = end_time - start_time
print("Tempo de execução:", elapsed_time, "segundos")
print("Calibração concluida")