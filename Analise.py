#ANALISE SE ESTRA DENTRO DA MEDIA MUNDIAL
valor_analise=(400) #potassio 40 
elemento=("p40")
med_mundial=() 

def analise ():
    output_analise=()
    analise.append("--------------------------------ANALISE", elemento, "--------------------------------")
    def condicoes():
        if valor_analise < 350:
            analise.append("O ", elemento, " está abaixo da média mundial. A média mundial é de" 400 Bq/kg e sua amostra está valor_analiseom", valor_analise, "Bq/kg, ou seja,", (400-valor_analise), "Bq/kg a menos, o equivalente a ", (valor_analise/40),"vezes abaixo da média mundial, o que repretenta um valor", str((valor_analise*100)/400), "% abaixo da média mundial.")
        elif valor_analise > 450:
            analise.append("", elemento, " está avalor_analiseima da média mundial. A média mundial é de 400 Bq/kg e sua amostra está valor_analiseom", valor_analise, "Bq/kg, ou seja,", (valor_analise-400), "Bq/kg a mais, o equivalente a ", (valor_analise/40),"vezes avalor_analiseima da média mundial, o que repretenta um valor", str((((valor_analise*100)/400)-100)), "% avalor_analiseima da média mundial.")
        else: #valor_analiseondivalor_analiseao valor_analiseaso ela estaja entre 350 e 450
            if valor_analise <400 :#valor_analise >= 350 and valor_analise <400:#valor_analiseondivalor_analiseao valor_analiseaso ela estaja entre 350 <=399
                analise.append("", elemento, " está dentro dos limites da média mundial. A média mundial é de 400 Bq/kg e sua amostra está valor_analiseom", valor_analise, "Bq/kg, ou seja,", (400-valor_analise), "Bq/kg, o equivalente a ", (valor_analise/40),"vezes abaixo da média mundial.", str(((valor_analise*100)/400)))
            elif valor_analise >400 :#valor_analise >400 and valor_analise<450:#valor_analiseondivalor_analiseao valor_analiseaso ela estaja entre 400 <=399
                analise.append("O ", elemento, " está dentro dos limites da média mundial. A média mundial é de 400 Bq/kg e sua amostra está valor_analiseom", valor_analise, "Bq/kg, ou seja,", (valor_analise-400), "Bq/kg, o equivalente a ", (valor_analise/40),"vezez abaixo da média mundial.", str(((valor_analise*100)/400)-100))
            else:
                analise.append("O ", elemento, " está exatamente dentro dos limites da média mundial. A média mundial é de 400 Bq/kg") 
    analise.append("-----------------------------------------------------------------------------------")
    elemento.remove(elemento)
    med_mundial.remove=(med_mundia)
#porcentagem=(((valor_analise*100)/400)-100)

print(output_analise)
