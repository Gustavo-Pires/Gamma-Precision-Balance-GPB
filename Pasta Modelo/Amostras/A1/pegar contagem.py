import pandas as pd
import xlwings as xw

#df_new = pd.read_csv('amostra.csv', sep=';')
#GFG = pd.ExcelWriter('amostra.xlsx') 
#df_new.to_excel(GFG, index = False) 
#GFG.save() 

#except FileNotFoundError:
    #print("O arquivo 'amostra.csv' não foi encontrado.")

#--------------------------------------------CONVERTENDO CVS EM EXCEL#--------------------------------------------
#df = pd.read_csv('amostra.csv', sep=',')
#df.to_excel('amostra.xlsx', index=None, header=True)
#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------ARQUIVO CONTAGEM------------------------------------------------------
ws = xw.Book("amostra.xlsx").sheets['Worksheet']
 
ekev = ws.range("A7:A107").options(numbers=str).value
BG = ws.range("C7:C107").options(numbers=str).value
contagem = ws.range("D7:D107").options(numbers=str).value
incerteza = ws.range("E7:E107").options(numbers=str).value

#----------removendo celulas vazias----------
ekev= [x for x in  ekev if x is not None]
BG= [x for x in BG if x is not None]
contagem= [x for x in contagem if x is not None]
incerteza= [x for x in incerteza if x is not None]
#-----------------------------------------------------------------------------------------------------------------

#--------------------------------------------PLANILHA CALCULO-----------------------------------------------------

calculo= xw.Book("calculo.xlsx").sheets['calculo'] 

a=35.28

b=a-1
c=a+1
print(b,c)
posi_cont = []
posi_incer = []

for i in ekev:
    print(ekev)
    if b <= int(i) <= c:
        posi=i
        
        posi_cont.append(contagem[posi])
        posi_incer.append(incerteza[posi])

def encontrar_indice(ekev, contagem,incerteza, b, c):
    posi_cont = []
    posi_incer = []
    for i, ekev in enumerate(ekev):
        if b <= i <= c:
            posi=i
            print(posi)
            posi_cont.append(contagem[posi])
            posi_incer.append(incerteza[posi])

    return posi_cont, posi_incer

a=338
b=a-1
c=a+1

posi_cont, posi_incer = encontrar_indice(ekev, contagem, incerteza, b, c)
calculo['S5'].value = posi_cont
calculo['T5'].value =posi_incer
cont_338=calculo.range("W5").value 
inc_338= calculo.range("X5").value 
print(posi_cont)
print(posi_incer)

a=1460
posi_cont, posi_incer = encontrar_indice(ekev, contagem, incerteza, b, c)
calculo['S6'].value = posi_cont
calculo['T6'].value =posi_incer
cont_338=calculo.range("W6").value 
inc_338= calculo.range("X6").value 

a=911
posi_cont, posi_incer = encontrar_indice(ekev, contagem, incerteza, b, c)
calculo['S7'].value = posi_cont
calculo['T7'].value =posi_incer
cont_338=calculo.range("W7").value 
inc_338= calculo.range("X7").value 
