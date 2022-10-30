#ANALISE SE ESTRA DENTRO DA MEDIA MUNDIAL
valor_analise=(500) #potassio 40 
elemento=("p40")
med_mundial=(400) 

def analise ():
    output_analise=()
    analise.append("--------------------------------ANALISE", elemento, "--------------------------------")
    def condicoes():
        if valor_analise < 350:
            analise.append("O ", elemento, " está abaixo da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (400-valor_analise), "Bq/kg a menos, o equivalente a ", (valor_analise/40),"vezes abaixo da média mundial, o que repretenta um valor", str((valor_analise*100)/400), "% abaixo da média mundial.")
        elif valor_analise > 450:
            analise.append("", elemento, " está avalor_analiseima da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (valor_analise-400), "Bq/kg a mais, o equivalente a ", (valor_analise/40),"vezes avalor_analiseima da média mundial, o que repretenta um valor", str((((valor_analise*100)/400)-100)), "% avalor_analiseima da média mundial.")
        else: 
            if valor_analise <400 :
                analise.append("", elemento, " está dentro dos limites da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (400-valor_analise), "Bq/kg, o equivalente a ", (valor_analise/40),"vezes abaixo da média mundial.", str(((valor_analise*100)/400)))
            elif valor_analise >400 :
                analise.append("O ", elemento, " está dentro dos limites da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (valor_analise-400), "Bq/kg, o equivalente a ", (valor_analise/40),"vezez abaixo da média mundial.", str(((valor_analise*100)/400)-100))
            else:
                analise.append("O ", elemento, " está exatamente dentro dos limites da média mundial. A média mundial é de 400 Bq/kg") 
    analise.append("-----------------------------------------------------------------------------------")
    elemento.remove(elemento)#ou tentar colcoar para remover o indice 0
    med_mundial.remove=(med_mundia)#ou tentar colcoar para remover o indice 0
    
#porcentagem=(((valor_analise*100)/400)-100)

with open('ANALISE.txt', 'w') as temp_file:
    for item in analise:
        temp_file.write("%s\n" % item)
    file = open('ANALISE.txt', 'r')
    print(file.read())
