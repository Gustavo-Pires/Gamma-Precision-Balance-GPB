#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import time
start_time1= time.time()
from datetime import datetime
import xlwings as xw
import os
import glob
import sys
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
    print("Mais de um arquivo CSV foi encontrado no diretório atual. \nDeixe apenas o arquivo correto")
    print("=" * 20 + "CALIBRAÇÃO NÃO REALIZADA" + "=" * 20)
    sys.exit()

arquivo_csv = arquivos_csv[0]

try:
    with open(arquivo_csv, newline='') as file:
        lines = file.readlines()

        # Extrair as colunas específicas
        ekev = [str(line.split(';')[0]).replace(',', '.') for line in lines[6:27]]
        resolucao = [str(line.split(';')[1]).replace(',', '.') for line in lines[6:27]]
        canal = [str(line.split(';')[5]).replace(',', '.') for line in lines[6:27]]
        contagem = [str(line.split(';')[3]).replace(',', '.') for line in lines[6:27]]
        incerteza = [str(line.split(';')[4]).replace(',', '.') for line in lines[6:27]]
        data = str(lines[1].split(';')[0])
        data_hora = str(lines[1].split(';')[0].strip())  # Remover espaços em branco extras
        nome_amostra = os.path.basename(arquivo_csv).rsplit(".", 1)[0]
        print("O nome do arquivo de calibração é: ", nome_amostra)
        
        # Remover células vazias
        ekev = [x if x != 'None' else '' for x in ekev]
        resolucao = [x if x != 'None' else '' for x in resolucao]
        canal = [x if x != 'None' else '' for x in canal]
        contagem = [x if x != 'None' else '' for x in contagem]
        incerteza = [x if x != 'None' else '' for x in incerteza]

        # Extrair dia e mês da data
        data_obj = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")
        dia_mes = data_obj.strftime("%d-%m")
        
        # Mover o arquivo CSV para a pasta "ARQUIVO"
        pasta_destino = os.path.join(diretorio_atual, 'ARQUIVO')
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        # Novo nome do arquivo
        novo_nome_arquivo = f"{dia_mes}.csv"
        caminho_destino = os.path.join(pasta_destino, novo_nome_arquivo)
        
        shutil.move(arquivo_csv, caminho_destino)

except FileNotFoundError:
   print("Arquivo CSV não encontrado.")
#------------------------------------------------------------------------------------------------------
end_time1= time.time()

elapsed_time1= end_time1 - start_time1
nome = input('Digite seu nome: ')
start_time2= time.time() 


#---------------------------------------------IMPORTANDO DADOS-------------------------------------
ws2 = xw.Book("Calibracao.xls").sheets['Calibracao']

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
    print("="*20 + "CALIBRAÇÃO NÃo CONCLUIDA" + "="*20  )
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
    print("="*20 + "CALIBRAÇÃO NÃo CONCLUIDA" + "="*20  )
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

#-----------------------------------------------------------------
end_time2= time.time()
elapsed_time2= end_time2 - start_time2
elapsed_time = elapsed_time1 + elapsed_time2
#-----------------------------------------------------------------

#wb.save()
#ws2.close()

print("Tempo de execução:", elapsed_time, "segundos")
print("="*20 + "CALIBRAÇÃO CONCLUIDA" + "="*20  )





