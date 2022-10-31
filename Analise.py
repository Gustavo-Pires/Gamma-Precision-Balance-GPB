#ANALISE SE ESTRA DENTRO DA MEDIA MUNDIAL
valor_analise=(340) #potassio 40 
elemento=("p40")
med_mundial=(400)
variacao_1_med_mundial=(med_mundial)- 50
variacao_2_med_mundial=(med_mundial)+50 

def analise():
    int(med_mundial).clear()
    int(elemento).clear()
    analise_amostra=()
    analise_amostra = analise_amostra +(("--------------------------------ANALISE", elemento, "--------------------------------"))
    def condicoes():
        if valor_analise < variacao_1_med_mundial: #350
            analise_amostra = analise_amostra + ("O ", elemento, " está abaixo da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (med_mundial-valor_analise), "Bq/kg a menos, o equivalente a ", (valor_analise/med_mundial),"vezes abaixo da média mundial, o que repretenta um valor", str((valor_analise*100)/med_mundial), "% abaixo da média mundial.")
        elif valor_analise > variacao_2_med_mundial: #450
            analise_amostra = analise_amostra +("O", elemento, " está avalor_analiseima da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (valor_analise-med_mundial), "Bq/kg a mais, o equivalente a ", (valor_analise/med_mundial),"vezes avalor_analiseima da média mundial, o que repretenta um valor", str((((valor_analise*100)/med_mundial)-100)), "% avalor_analiseima da média mundial.")
        else: 
            if valor_analise <med_mundial :#menor que 400
               analise_amostra = analise_amostra +("0", elemento, " está dentro dos limites da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (med_mundial-valor_analise), "Bq/kg, o equivalente a ", (valor_analise/med_mundial),"vezes abaixo da média mundial.", str(((valor_analise*100)/med_mundial)))
            elif valor_analise >med_mundial :#maior que 400
                analise_amostra = analise_amostra +("O ", elemento, " está dentro dos limites da média mundial. A média mundial é de", (med_mundial), "Bq/kg e sua amostra está com", (valor_analise), "Bq/kg, ou seja,", (valor_analise-med_mundial), "Bq/kg, o equivalente a ", (valor_analise/med_mundial),"vezez abaixo da média mundial.", str(((valor_analise*100)/med_mundial)-100))
            else: #igual a 400
                analise_amostra = analise_amostra +("O ", elemento, " está exatamente dentro dos limites da média mundial. A média mundial é de", (med_mundial), ".") 
    analise_amostra = tuple(analise_amostra +("-----------------------------------------------------------------------------------"))

    #elemento.remove(elemento)#ou tentar colcoar para remover o indice 0
    #med_mundial.remove=(med_mundia)#ou tentar colcoar para remover o indice 0

#porcentagem=(((valor_analise*100)/400)-100)

print(analise())

with open('ANALISE.txt', 'w') as temp_file:
    for item in analise:
        temp_file.write("%s\n" % item)
    file = open('ANALISE.txt', 'r')
    print(file.read())
