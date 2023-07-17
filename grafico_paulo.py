import xlwings as xw
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates
import os 

diretorio_atual = os.path.abspath(os.path.dirname(__file__))  # Obtain the absolute path of the current directory

nome_arquivo_excel = None  # Search for an Excel file in the current directory and obtain the absolute path of the file
for nome_arquivo in os.listdir(diretorio_atual):
    if nome_arquivo.endswith('.xls'):  # or .xls, depending on the file extension
        nome_arquivo_excel = nome_arquivo
        break

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
    ax4.set_ylim(1.5, 3)  # Definindo os limites do eixo Y para o Co-60
    ax4.axhline(y=media_60)
    ax4.axhline(y=media_60 + incerteza_60, color='red', linestyle='--', label='Maior Incerteza')
    ax4.axhline(y=media_60 - incerteza_60, color='green', linestyle='--', label='Menor Incerteza')

    fig.suptitle(titulo)

    ax1.xaxis.set_major_locator(mdates.DayLocator())
    ax2.xaxis.set_major_locator(mdates.DayLocator())
    ax3.xaxis.set_major_locator(mdates.DayLocator())
    ax4.xaxis.set_major_locator(mdates.DayLocator())

    plt.tight_layout()
    plt.show()
    plt.savefig(f'{nome_arquivo}.png', dpi=300)



wb = xw.Book(nome_arquivo)
ws = wb.sheets['Plan1']

ekev_57 = ws.range("C9:C40").options(numbers=str).value
ekev_60 = ws.range("H9:H40").options(numbers=str).value
reso_57 = ws.range("D9:D40").options(numbers=str).value
reso_60 = ws.range("I9:I40").options(numbers=str).value
dia = ws.range("B9:B40").options(numbers=datetime).value
titulo = ws.range('C5').value
media_57 = ws.range("D42").options(numbers=float).value
media_60 = ws.range("I42").options(numbers=float).value
mes = ws.range("K5").options(numbers=str).value

dia = [str(x.day)[:2] for x in dia if x is not None]
titulo_completo = f"{titulo} {mes[4:]}"

ekev_57 = [float(x) for x in ekev_57 if x is not None and x.strip() != '']
ekev_60 = [float(x) for x in ekev_60 if x is not None and x.strip() != '']
reso_57 = [float(x) for x in reso_57 if x is not None and x.strip() != '']
reso_60 = [float(x) for x in reso_60 if x is not None and x.strip() != '']

incerteza_57 = 0.2 * media_57  # 20% da média de incerteza para o Cobalto-57
incerteza_60 = 0.3 * media_60  # 30% da média de incerteza para o Cobalto-60


plotar_grafico(ekev_57, ekev_60, dia, titulo_completo, media_57, media_60, incerteza_57, incerteza_60)
