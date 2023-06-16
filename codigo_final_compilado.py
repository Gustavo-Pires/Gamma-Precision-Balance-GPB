#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import time
start_time1= time.time()
from datetime import datetime
import xlwings as xw
import pandas as pd
import os
import sys
import glob
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as mdates
import shutil

#------------------------------------------------------------------------------------------------------
#---------------------------------------------CONTAGEM -------------------------------------
print("="*20 + "CALIBRAÇÃO INICIADA" + "="*20  )

diretorio_atual = os.path.abspath(os.path.dirname(__file__))  # Obter o caminho absoluto do diretório atual
arquivos_csv = glob.glob(os.path.join(diretorio_atual, '*.csv'))  # Obter a lista de arquivos CSV no diretório

if not os.path.exists('log.txt'):
    open('log.txt', 'w').close()  # Cria o arquivo vazio

# Redirecionar a saída para o arquivo de log
log_file = open('log.txt', 'w')
sys.stdout = log_file

# Verificar a quantidade de arquivos CSV no diretório
if len(arquivos_csv) == 0:
    print("Nenhum arquivo CSV foi encontrado no diretório atual.")
    print("="*20 + "CALIBRAÇÃO NÃO REALIZADA" + "="*20  )
    sys.exit()  # Encerrar a execução do código
elif len(arquivos_csv) > 1:
    print("Mais de um arquivo CSV foi encontrado no diretório atual. \nDeixei apenas o aquivo correto")
    print("="*20 + "CALIBRAÇÃO NÃO REALIZADA" + "="*20  )
    sys.exit()  # Encerrar a execução do código

# Se chegarmos aqui, há exatamente um arquivo CSV no diretório
nome_arquivo_csv = os.path.basename(arquivos_csv[0])
nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo_csv)[0]
print("Arquivo de calibração: " + nome_arquivo_csv)

# Importar valores do arquivo CSV
with open(nome_arquivo_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    ekev = []
    contagem = []
    incerteza = []
    data = []
    canal = []
    resolucao = []

    linha_atual = 0
    for linha in leitor_csv:
        linha_atual += 1
        if linha_atual >= 7 and linha_atual <= 27:
            ekev.append(linha[0])
            contagem.append(linha[3])
            incerteza.append(linha[4])
            data.append(linha[0])
            if len(linha) >= 6:  # Verificar se a linha possui pelo menos 6 elementos
                canal.append(linha[5])
            if len(linha) >= 2:  # Verificar se a linha possui pelo menos 2 elementos
                resolucao.append(linha[1])

arquivo_csv.close()

#----------removendo celulas vazias---------- 
ekev = [x for x in ekev if pd.notnull(x)]
contagem = [x for x in contagem if pd.notnull(x)]
incerteza = [x for x in incerteza if pd.notnull(x)]
canal = [x for x in canal if pd.notnull(x)]
resolucao = [x for x in resolucao if pd.notnull(x)]
#----------------------------------------------


#-------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
end_time1= time.time()
elapsed_time1= end_time1 - start_time1

nome = input('Digite seu nome: ')

start_time2= time.time() 

#---------------------------------------------IMPORTANDO DADOS-------------------------------------
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

media_57 = ws2.range("D42").options(numbers=float).value
media_60 = ws2.range("I42").options(numbers=float).value

incerteza_57 = 0.2 * media_57  # 20% da média de incerteza para o Cobalto-57
incerteza_60 = 0.3 * media_60  # 30% da média de incerteza para o Cobalto-60
    
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
    if abs(float(ekev[j]) - valor_procurado) <= 2:
        encontrado = True
        co_57_ekev.append(ekev[j])
        co_57_resolucao.append(resolucao[j])
        co_57_contagem.append(contagem[j])
        co_57_incerteza.append(incerteza[j])
        co_57_canal.append(canal[j])
        break  # interrompe o laço de repetição

if not encontrado:
    print("Pico de energia não encontrado dentro da variação.")
    sys.exit()

valor_procurado = 1332.5
encontrado = False

for j in range(len(ekev)):
    if abs(float(ekev[j]) - valor_procurado) <= 2:
        encontrado = True
        co_60_ekev.append(ekev[j])
        co_60_resolucao.append(resolucao[j])
        co_60_contagem.append(contagem[j])
        co_60_incerteza.append(incerteza[j])
        co_60_canal.append(canal[j])
        break  # interrompe o laço de repetição

if not encontrado:
    print("Pico de energia não encontrado dentro da variação.")
    sys.exit()

#----------------------------------------------------------------------------------------------------------------

#-----------------------SALVANDO-----------------------------------------------------------------------------------------
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

#wb.save()
#ws2.close()

print("="*20 + "ANALISE DE CALIBRAÇÃO CONCLUIDA" + "="*20  )


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

for arquivo_excel in arquivos_excel:
    print(arquivo_excel)
    wb = xw.Book(arquivo_excel)
    ws = wb.sheets['Plan1']

    ekev_57 = ws.range("C9:C40").options(numbers=str).value
    ekev_60 = ws.range("H9:H40").options(numbers=str).value
    reso_57 = ws.range("D9:D40").options(numbers=str).value
    reso_60 = ws.range("I9:I40").options(numbers=str).value
    media_57 = ws.range("D42").options(numbers=float).value
    media_60 = ws.range("I42").options(numbers=float).value

    dia = ws.range("B9:B40").options(numbers=str).value
    dia = [x.strftime('%d') if isinstance(x, datetime) else x for x in dia if x is not None]
    total_dias.extend(dia)  # Adiciona os dias � lista total_dias
  
    nome_arquivo = os.path.splitext(os.path.basename(arquivo_excel))[0]  # Obter o nome do arquivo sem a extens�o
    titulo_completo = f"{nome_arquivo}"

    ekev_57 = [float(x) for x in ekev_57 if x is not None and x.strip() != '']
    ekev_60 = [float(x) for x in ekev_60 if x is not None and x.strip() != '']
    reso_57 = [float(x) for x in reso_57 if x is not None and x.strip() != '']
    reso_60 = [float(x) for x in reso_60 if x is not None and x.strip() != '']

    incerteza_57 = 0.2 * media_57  # 20% da m�dia de incerteza para o Cobalto-57
    incerteza_60 = 0.3 * media_60  # 30% da m�dia de incerteza para o Cobalto-60

    plotar_grafico(ekev_57, ekev_60, dia, titulo_completo, media_57, media_60, incerteza_57, incerteza_60)

num_arquivos_excel = len(arquivos_excel)
num_dias_calibracao = len(total_dias)


end_time2= time.time()
elapsed_time2= end_time2 - start_time2
elapsed_time = elapsed_time1 + elapsed_time2

# Movendo o arquivo para a pasta
nome_pasta = 'ARQUIVO'
shutil.move(nome_arquivo_csv, nome_pasta)

# Exibe os resultados
print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
print("="*20 + "PLOT DE CALIBRAÇÃO CONCLUIDA" + "="*20  )

log_file.close()

