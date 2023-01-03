
import pandas as pd
import xlwings as xw


#fazer um codigo que encontre o indice de um elemento da variavel ekev que esteja entre b e c
#essa funcao ela vai pegar o indice i do elemento na lista contagem e vai pegar o elemento da lista contagem que esta na mesma posicao i, dai vai colocar na lista posi_cont e  depois depois fazer a mesma coisa com a lista incerteza e colocar na lista posi_incer


ekev=(100, 200, 20, 399.90, 500, 338.5, 600, )
contagem= (1, 2, 3, 4, 777, 6, 7, 8, 9, 10)
incerteza= (1, 2, 3, 4, 999, 6, 7, 8, 9, 10)



  

ws=xw.Book("amostra.xlsx").sheets['Worksheet'] 
calculo= xw.Book("calculo.xlsx").sheets['1'] 


def encontrar_indice(ekev, contagem,incerteza, b, c):
    posi_cont = []
    posi_incer = []
  
    for i, valor in enumerate(ekev):
        if b <= valor <= c:
            posi=i
            posi_cont.append(contagem[posi])
            posi_incer.append(incerteza[posi])

    return posi_cont, posi_incer

a=338
b=a-1
c=a+1
posi_cont, posi_incer = encontrar_indice(ekev, contagem, incerteza, b, c)
calculo['S5'].value = posi_cont
calculo['T5'].value =posi_incer
cont_338=ws.range("W5").value 
inc_338= ws.range("X6").value 


