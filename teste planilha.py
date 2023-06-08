#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import time
start_time = time.time()
from datetime import datetime
import xlwings as xw
import pandas as pd
import os
import glob
#------------------------------------------------------------------------------------------------------
#---------------------------------------------CONTAGEM -------------------------------------

diretorio_atual = os.path.abspath(os.path.dirname(__file__))  # Obter o caminho absoluto do diretório atual
arquivos_csv = glob.glob(os.path.join(diretorio_atual, '*.csv'))  # Obter a lista de arquivos CSV no diretório

    # Ler o arquivo CSV utilizando o pandas
df = pd.read_csv(arquivo_csv)


ekev = df['A7:A27'].astype(str).values.tolist()
contagem = df['D7:D27'].astype(str).values.tolist()
incerteza = df['E7:E27'].astype(str).values.tolist()
nome_amostra = df.columns[0] 
   
#----------removendo celulas vazias---------- 
ekev = [x for x in ekev if pd.notnull(x)]
contagem = [x for x in contagem if pd.notnull(x)]
incerteza = [x for x in incerteza if pd.notnull(x)]
#----------------------------------------------

nome_amostra = os.path.basename(arquivo_csv)
nome_amostra = nome_amostra.split("\\")[-2]
#-------------------------------------------------------------------------------------------------

wb = xw.Book("massa_id.xlsx")
ws3= wb.sheets['dados']

massa=ws3.range("C7:C107").options(numbers=str).value
identificacao=ws3.range("D7:D107").options(numbers=str).value

massa=[x for x in  massa if x is not None]
identificacao=[x for x in  identificacao if x is not None]


for j in range(len(identificacao)):
    if abs(float(identificacao=nome_amostra):
           encontrado = True
           valor_massa = massa[j]
           nome = identificacao[j]
           break



#---------------------------------------------PLANILHA ARMAZENAMENTO-------------------------------------

wb = xw.Book("concentracao.xlsx")
ws3= wb.sheets['concentracao']

# IMPORTAR OS VALORES ACHADOS PARA AQUI
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

#wb.close()

#----------removendo celulas vazias----------
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

#---------------------------------------------PLANILHA CONTAS-------------------------------------
wb = xw.Book("conta.xlsx")
ws2= wb.sheets['conta']
ws3.range('B2').options(transpose=True).value = [nome]

#------------------------------------------------------------------------------------------------
cont = []
incert = []

def adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza):
    encontrado = False
    cont_valor = None
    incert_valor = None
    for j in range(len(ekev)):
        if abs(float(ekev[j].replace(',', '.').strip()) - valor_procurado) <= 1:
            encontrado = True
            cont_valor = contagem[j]
            incert_valor = incerteza[j]
            break
    return encontrado, cont_valor, incert_valor

valor_procurados = [338, 911, 727, 238, 351, 609, 1120, 46, 1460]

for valor_procurado in valor_procurados:
    encontrado, cont_valor, incert_valor = adicionar_valores_na_lista(valor_procurado, ekev, contagem, incerteza)
    cont.append(cont_valor)
    incert.append(incert_valor)

# Atualizar as células correspondentes no Excel
for i in range(len(valor_procurados)):
    ws2.range(f'S{i+5}').value = cont[i]
    ws2.range(f'T{i+5}').value = incert[i]

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||FUNCIONANDO DAQUI PARA BAIXO||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#----------------------------------------------------------------------------------------------------------------
#TIRANDO O RESULTADO FINAL DA PLANILHA E SALVANDO NA VARIAVEL
contagem_338.append(ws2.range("W5").options(numbers=str).value)
Incerteza_338.append(ws2.range("X5").options(numbers=str).value)
contagem_911.append(ws2.range("W6").options(numbers=str).value)
Incerteza_911.append(ws2.range("X6").options(numbers=str).value)
contagem_727.append(ws2.range("W7").options(numbers=str).value)
Incerteza_727.append(ws2.range("X7").options(numbers=str).value)
contagem_238.append(ws2.range("W8").options(numbers=str).value)
Incerteza_238.append(ws2.range("X8").options(numbers=str).value)
contagem_351.append(ws2.range("W12").options(numbers=str).value)
Incerteza_351.append(ws2.range("X12").options(numbers=str).value)
contagem_609.append(ws2.range("W13").options(numbers=str).value)
Incerteza_609.append(ws2.range("X13").options(numbers=str).value)
contagem_1120.append(ws2.range("W14").options(numbers=str).value)
Incerteza_1120.append(ws2.range("X14").options(numbers=str).value)
contagem_46.append(ws2.range("W15").options(numbers=str).value)
Incerteza_46.append(ws2.range("X15").options(numbers=str).value)
contagem_1460.append(ws2.range("W18").options(numbers=str).value)
Incerteza_1460.append(ws2.range("X18").options(numbers=str).value)
ws2.range('B2').options(transpose=True).value = [str(nome_amostra)]
#----------------------------------------------------------------------------------------------------------------
wb.save()
Amostra.append(nome_amostra)
#----------------------------------------------------------------------------------------------------------------
wb = xw.Book("concentracao.xlsx")
ws3= wb.sheets['amostra']
#----------------------------------------------------------------------------------------------------------------
#SALVANDOS OS VALORES DA VARIAVEL NOS DADOS BRUTOS
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
ws3.range('T7:T107').options(transpose=True).value = [contagem_1460 ]
ws3.range('U7:U107').options(transpose=True).value = [Incerteza_1460 ]
#----------------------------------------------------------------------------------------------------------------

wb.save()# fecha a planilha

end_time = time.time()
elapsed_time = end_time - start_time

print("Tempo de execução:", elapsed_time, "segundos")
print("Calculo de concentração de radionuclídeos concluido")