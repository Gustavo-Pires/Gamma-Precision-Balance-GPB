#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import time
start_time1= time.time()
from datetime import datetime
import xlwings as xw
import pandas as pd
import os
import glob
import sys
import csv
import re
import locale
from decimal import Decimal
import locale
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import shutil


#------------------------------------------------------------------------------------------------------
#---------------------------------------------CONTAGEM -------------------------------------
print("=" * 20 + "CALIBRAÇÃO INICIADA" + "=" * 20)

diretorio_atual = os.path.abspath(os.path.dirname(__file__))
arquivos_csv = glob.glob(os.path.join(diretorio_atual, '*.csv'))

if len(arquivos_csv) == 0:
    print("Nenhum arquivo CSV foi encontrado no diretório atual.")
    print("=" * 20 + "CALIBRAÇÃO NÃO REALIZADA" + "=" * 20)
    sys.exit()
elif len(arquivos_csv) > 1:
    print("Mais de um arquivo CSV foi encontrado no diretório atual. \nDeixei apenas o arquivo correto")
    print("=" * 20 + "CALIBRAÇÃO NÃO REALIZADA" + "=" * 20)
    sys.exit()

nome_arquivo_excel = None# Procurar por um arquivo Excel no diretório atual e obter o caminho absoluto do arquivo
for nome_arquivo in os.listdir(diretorio_atual):
    if nome_arquivo.endswith('.xls'): # ou .xls, dependendo da extensão do arquivo
        nome_arquivo_excel = nome_arquivo
        break

if nome_arquivo_excel is not None:
    caminho_arquivo_excel = os.path.join(diretorio_atual, nome_arquivo_excel)

else:
    print("Nenhum arquivo Excel foi encontrado no diretório atual.")

#------------------------------------------------------------------------------------------------------
end_time1= time.time()

elapsed_time1= end_time1 - start_time1
nome = input('Digite seu nome: ')
start_time2= time.time() 
#---------------------------------------------ARQUIVO DE CONTAGEM -------------------------------------
wb = xw.Book("CALI1712.xls")# abre a planilha
ws = wb.sheets['Worksheet']
 
ekev = ws.range("A7:A27").options(numbers=str).value
resolucao = ws.range("B7:B27").options(numbers=str).value
canal = ws.range("F7:F27").options(numbers=str).value
contagem = ws.range("D7:D27").options(numbers=str).value
incerteza = ws.range("E7:E27").options(numbers=str).value
data=ws.range("A2").options(numbers=str).value
nome_amostra= ws.range("A1").options(numbers=str).value
print(nome_amostra)
nome_amostra = nome_amostra.split("\\")[-2]
print(nome_amostra)
wb.close() # fecha a planilha

#----------removendo celulas vazias----------
ekev= [x for x in  ekev if x is not None]
resolucao= [x for x in resolucao if x is not None]
canal= [x for x in canal if x is not None]
contagem= [x for x in contagem if x is not None]
incerteza= [x for x in incerteza if x is not None]

#-------------------------------------------------------------------------------------------------


#---------------------------------------------IMPORTANDO DADOS-------------------------------------
ws2 = xw.Book("Calibracao.xlsx").sheets['Calibracao']

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
media_57 = ws.range("D42").options(numbers=float).value
media_60 = ws.range("I42").options(numbers=float).value
#------------------------------------------------------------------------------------------------------

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

data_hora.append(data)
usuario.append(nome)

#-----------------------------------------ACHANDO OS PICOS-------------------------------------------------------------
valor_procurado = 122.06
encontrado = False

for j in range(len(ekev)):
    valor = ekev[j].replace(" ", "").replace(",", ".")
    if float(valor) >= valor_procurado - 2 and float(valor) <= valor_procurado + 2:
        encontrado = True
        co_57_ekev.append(ekev[j])
        co_57_resolucao.append(resolucao[j])
        co_57_contagem.append(contagem[j])
        co_57_incerteza.append(incerteza[j])
        co_57_canal.append(canal[j])
        break  # interrompe o laço de repetição

if not encontrado:
    print("Pico de energia do co-57 não encontrado dentro da variação.")
    sys.exit()

    
valor_procurado = 1332.5
encontrado = False

for j in range(len(ekev)):
    valor = ekev[j].replace(" ", "").replace(",", ".")
    if float(valor) >= valor_procurado - 2 and float(valor) <= valor_procurado + 2:
        encontrado = True
        co_60_ekev.append(ekev[j])
        co_60_resolucao.append(resolucao[j])
        co_60_contagem.append(contagem[j])
        co_60_incerteza.append(incerteza[j])
        co_60_canal.append(canal[j])
        break  # interrompe o laço de repetição

if not encontrado:
    print("Pico de energia do co-60 não encontrado dentro da variação.")
    sys.exit()


#----------------------------------------------------------------------------------------------------------------

#-----------------------SALVANDO-----------------------------------------------------------------------------------------
# Convertendo os valores para o formato americano com ponto decimal
co_57_ekev = [x.replace('.', ',') for x in co_57_ekev]
co_57_resolucao = [x.replace('.', ',') for x in co_57_resolucao]
co_57_canal = [x.replace('.', ',') for x in co_57_canal]
co_57_contagem = [x.replace('.', ',') for x in co_57_contagem]
co_57_incerteza = [x.replace('.', ',') for x in co_57_incerteza]

co_60_ekev = [x.replace('.', ',') for x in co_60_ekev]
co_60_resolucao = [x.replace('.', ',') for x in co_60_resolucao]
co_60_canal = [x.replace('.', ',') for x in co_60_canal]
co_60_contagem = [x.replace('.', ',') for x in co_60_contagem]
co_60_incerteza = [x.replace('.', ',') for x in co_60_incerteza]

# Salvando os dados convertidos no formato americano
ws2.range('B9:B40').options(transpose=True).value = [data_hora]
ws2.range('C9:C40').options(transpose=True).value = [co_57_ekev]
ws2.range('D9:D40').options(transpose=True).value = [co_57_resolucao]
ws2.range('E9:E40').options(transpose=True).value = [co_57_canal]
ws2.range('F9:F40').options(transpose=True).value = [co_57_contagem]
ws2.range('G9:G40').options(transpose=True).value = [co_57_incerteza]
ws2.range('H9:H40').options(transpose=True).value = [co_60_ekev]
ws2.range('I9:I40').options(transpose=True).value = [co_60_resolucao]
ws2.range('J9:J40').options(transpose=True).value = [co_60_canal]
ws2.range('K9:K40').options(transpose=True).value = [co_60_contagem]
ws2.range('L9:L40').options(transpose=True).value = [co_60_incerteza]
ws2.range('M9:M40').options(transpose=True).value = [usuario]

#----------------------------------------------------------------------------------------------------------------

# CODIGO DE PLOT 
# FUNCIONAL 

diretorio_atual = os.path.abspath(os.path.dirname(__file__))  # Obter o caminho absoluto do diretório atual

arquivos_excel = glob.glob(os.path.join(diretorio_atual, '*.xls'))  # Obter a lista de arquivos Excel no diretório

def plotar_grafico(ekev_57, ekev_60, dia, titulo, media_57, media_60, incerteza_57, incerteza_60):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    ax1, ax2, ax3, ax4 = axs.flatten()

    ax1.scatter(dia, co_57_ekev, color='blue', alpha=0.5, label='Cobalto-57 (122,06 keV)')
    ax1.set_title('Cobalto-57 (122,06 keV)')
    ax1.set_xlabel('Dia')
    ax1.set_ylabel('Energia(keV)')
    ax1.axhline(y=124.06, color='red', linestyle='--', label='124.06')
    ax1.axhline(y=120.06, color='green', linestyle='--', label='120.06')
    ax1.set_ylim(117.06, 127.06)

    ax2.scatter(dia, co_57_resolucao, color='blue', alpha=0.5, label='Cobalto-57 (122,06 keV)')
    ax2.set_title('Cobalto-57 (122,06 keV)')
    ax2.set_xlabel('Dia')
    ax2.set_ylabel('Resolucao')
    ax2.set_ylim(0.5, 2)  # Definindo os limites do eixo Y para o Co-57
    ax2.axhline(y=media_57)
    ax2.axhline(y=media_57 + incerteza_57, color='red', linestyle='--', label='Maior Incerteza')
    ax2.axhline(y=media_57 - incerteza_57, color='green', linestyle='--', label='Menor Incerteza')


    ax3.scatter(dia, co_60_ekev, color='blue', alpha=0.5, label='Cobalto-60 (1332,5 keV)')
    ax3.set_title('Cobalto-60 (1332,5 keV)')
    ax3.set_xlabel('Dia')
    ax3.set_ylabel('Energia(keV)')
    ax3.axhline(y=1330.5, color='red', linestyle='--', label='1330.5')
    ax3.axhline(y=1334.5, color='green', linestyle='--', label='1334.5')
    ax3.set_ylim(1327.5, 1337.5)
    
    ax4.scatter(dia, co_60_resolucao, color='blue', alpha=0.5, label='Cobalto-60 (1332,5 keV)')
    ax4.set_title('Cobalto-60 (1332,5 keV)')
    ax4.set_xlabel('Dia')
    ax4.set_ylabel('Resolucao')
    ax4.set_ylim(1, 3)  # Definindo os limites do eixo Y para o Co-60
    ax4.axhline(y=media_60)
    ax4.axhline(y=media_60 + incerteza_60, color='red', linestyle='--', label='Maior Incerteza')
    ax4.axhline(y=media_60 - incerteza_60, color='green', linestyle='--', label='Menor Incerteza')

    fig.suptitle(nome_arquivo)

    ax1.xaxis.set_major_locator(mdates.DayLocator())
    ax2.xaxis.set_major_locator(mdates.DayLocator())
    ax3.xaxis.set_major_locator(mdates.DayLocator())
    ax4.xaxis.set_major_locator(mdates.DayLocator())

    plt.tight_layout()
    plt.savefig(f'{nome_arquivo}.png', dpi=300)
    wb.close() 

total_dias = [] 

dia = ws.range("B9:B40").options(numbers=str).value
dia = [x.strftime('%d') if isinstance(x, datetime) else x for x in dia if x is not None]
total_dias.extend(dia)  # Adiciona os dias � lista total_dias
  
titulo_completo = f"{nome_arquivo}"

incerteza_57 = 0.2 * media_57  # 20% da m�dia de incerteza para o Cobalto-57
incerteza_60 = 0.3 * media_60  # 30% da m�dia de incerteza para o Cobalto-60

plotar_grafico(co_57_ekev, co_60_ekev, dia, titulo_completo, media_57, media_60, incerteza_57, incerteza_60)

num_arquivos_excel = len(arquivos_excel)
num_dias_calibracao = len(total_dias)


end_time2= time.time()
elapsed_time2= end_time2 - start_time2
elapsed_time = elapsed_time1 + elapsed_time2


print("Tempo de execução:", elapsed_time, "segundos")
print("="*20 + "CALIBRAÇÃO CONCLUIDA" + "="*20  )


try:
    wb.close()
except Exception as e:
    print("Erro ao fechar o arquivo:", str(e))


    
    
