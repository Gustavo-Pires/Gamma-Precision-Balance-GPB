from tkinter import Tk
from tkinter.filedialog import askopenfilename

janela_padrao = Tk().withdraw()
caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos Excel", "*.xlsx"), ("Arquivos Excel", "*.xls")))

import time
start_time = time.time()  # Captura o tempo de início
import xlwings as xw
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import os
import glob
import tkinter as tk

def plotar_grafico(ekev_57, ekev_60, dia, titulo, media_57, media_60, incerteza_57, incerteza_60):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    ax1, ax2, ax3, ax4 = axs.flatten()

    ax1.scatter(dia, ekev_57, color='blue', alpha=0.5, label='Cobalto-57 (122,06 keV)')
    ax1.set_title('Cobalto-57 (122,06 keV)')
    ax1.set_xlabel('Dia')
    ax1.set_ylabel('Energia(keV)')
    ax1.axhline(y=124.06, color='red', linestyle='--', label='124.06')
    ax1.axhline(y=120.06, color='green', linestyle='--', label='120.06')
    ax1.set_ylim(117.06, 127.06)

    ax2.scatter(dia, reso_57, color='blue', alpha=0.5, label='Cobalto-57 (122,06 keV)')
    ax2.set_title('Cobalto-57 (122,06 keV)')
    ax2.set_xlabel('Dia')
    ax2.set_ylabel('Resolucao')
    ax2.set_ylim(0.5, 2)  # Definindo os limites do eixo Y para o Co-57
    ax2.axhline(y=media_57)
    ax2.axhline(y=media_57 + incerteza_57, color='red', linestyle='--', label='Maior Incerteza')
    ax2.axhline(y=media_57 - incerteza_57, color='green', linestyle='--', label='Menor Incerteza')


    ax3.scatter(dia, ekev_60, color='blue', alpha=0.5, label='Cobalto-60 (1332,5 keV)')
    ax3.set_title('Cobalto-60 (1332,5 keV)')
    ax3.set_xlabel('Dia')
    ax3.set_ylabel('Energia(keV)')
    ax3.axhline(y=1330.5, color='red', linestyle='--', label='1330.5')
    ax3.axhline(y=1334.5, color='green', linestyle='--', label='1334.5')
    ax3.set_ylim(1327.5, 1337.5)
    
    ax4.scatter(dia, reso_60, color='blue', alpha=0.5, label='Cobalto-60 (1332,5 keV)')
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


wb = xw.Book(caminho_do_arquivo)
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

     # Verificar as condições para reso_57
if reso_57[-1] < (media_57 - incerteza_57) or reso_57[-1] > (media_57 + incerteza_57):
    if reso_57[-1] < (media_57 - incerteza_57):
        print("Resolução Cobalto 57 está baixa\nCalibração não realizada\nChame um responsável")
    else:
        print("Resolução Cobalto 57 está alta\nCalibração não realizada\nChame um responsável")

    # Verificar as condições para reso_60
elif reso_60[-1] < (media_60 - incerteza_60) or reso_60[-1] > (media_60 + incerteza_60):
    if reso_60[-1] < (media_60 - incerteza_60):
        print("Resolução Cobalto 60 está baixa\nCalibração não realizada\nChame um responsável")
    else:
        print("Resolução Cobalto 60 está alta\nCalibração não realizada\nChame um responsável")
else:
    print("Calibração realizada com sucesso")
        

plotar_grafico(ekev_57, ekev_60, dia, titulo_completo, media_57, media_60, incerteza_57, incerteza_60)

end_time = time.time()  
elapsed_time = end_time - start_time  

num_arquivos_excel = len(arquivos_excel)
num_dias_calibracao = len(total_dias)

# Exibe os resultados
print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
print(f"N�mero de arquivos Excel analisados: {num_arquivos_excel}")
print(f"N�mero de dias de calibra��o plotados: {num_dias_calibracao}")
