for i in range(20):
        
    import time
    start_time = time.time()  # Captura o tempo de inÃ­cio
    import xlwings as xw
    import matplotlib.pyplot as plt
    from datetime import datetime
    import matplotlib.dates as mdates
    import os
    import glob
    
    diretorio_atual = os.path.abspath(os.path.dirname(__file__))  # Obter o caminho absoluto do diretÃ³rio atual
    
    arquivos_excel = glob.glob(os.path.join(diretorio_atual, '*.xls'))  # Obter a lista de arquivos Excel no diretÃ³rio
    
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
        total_dias.extend(dia)  # Adiciona os dias à lista total_dias
      
        nome_arquivo = os.path.splitext(os.path.basename(arquivo_excel))[0]  # Obter o nome do arquivo sem a extensão
        titulo_completo = f"{nome_arquivo}"
    
        ekev_57 = [float(x) for x in ekev_57 if x is not None and x.strip() != '']
        ekev_60 = [float(x) for x in ekev_60 if x is not None and x.strip() != '']
        reso_57 = [float(x) for x in reso_57 if x is not None and x.strip() != '']
        reso_60 = [float(x) for x in reso_60 if x is not None and x.strip() != '']
    
        incerteza_57 = 0.2 * media_57  # 20% da média de incerteza para o Cobalto-57
        incerteza_60 = 0.3 * media_60  # 30% da média de incerteza para o Cobalto-60
    
        plotar_grafico(ekev_57, ekev_60, dia, titulo_completo, media_57, media_60, incerteza_57, incerteza_60)
        #matplotlib.pyplot.close()
    end_time = time.time()  
    elapsed_time = end_time - start_time  
    
    num_arquivos_excel = len(arquivos_excel)
    num_dias_calibracao = len(total_dias)
    
    # Exibe os resultados
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
    print(f"Número de arquivos Excel analisados: {num_arquivos_excel}")
    print(f"Número de dias de calibração plotados: {num_dias_calibracao}")
    
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Tempo de execução:", elapsed_time, "segundos")
    print("Calibração concluida")
    
    # Formata elapsed_time como string com separador decimal ponto
    tempo_str = "{:.2f}".format(elapsed_time)
    print("Tempo formatado:", tempo_str)
    
    wb = xw.Book("tempo.xlsx")
    ws3 = wb.sheets['tempo'] 
    tempo = ws3.range("E3:E22").options(numbers=str).value
    tempo = [x for x in tempo if x is not None]
    
    tempo.append(tempo_str)
    ws3.range('E3:E22').options(transpose=True).value = tempo
    print("Resultado de Teste armazenado")
    print("Teste numero:", len(tempo))
    
    wb.save()
    
    
