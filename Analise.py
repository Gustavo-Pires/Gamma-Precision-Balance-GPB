#ANALISE SE ESTRA DENTRO DA MEDIA MUNDIAL
a=() # uranio
b=()# torio
c=(500) #potassio 40 

#--------------------------------ANALISE POTASSIO 40--------------------------------
if c < 350:
    print("O Potassio-40 está abaixo da média mundial. A média mundial é de 400 Bq/kg e sua amostra está com", c, "Bq/kg, ou seja,", (400-c), "Bq/kg, o equivalente a ", (c/40),"vezes abaixo da média mundial, o que repretenta um valor" ((c*100)/400), "% abaixo da média mundial.")
elif c > 450:
    print("O Potassio-40 está acima da média mundial. A média mundial é de 400 Bq/kg e sua amostra está com", c, "Bq/kg, ou seja,", (c-400), "Bq/kg, o equivalente a ", (c/40),"vezes acima da média mundial." (((c*100)/400)-100))
else: 
    if c >= 350 and c <400:
        print("O Potassio-40 está dentro dos limites da média mundial. A média mundial é de 400 Bq/kg e sua amostra está com", c, "Bq/kg, ou seja,", (400-c), "Bq/kg, o equivalente a ", (c/40),"vezes abaixo da média mundial.((c*100)/400)")
    elif c >400 and <450:
        print("O Potassio-40 está dentro dos limites da média mundial. A média mundial é de 400 Bq/kg e sua amostra está com", c, "Bq/kg, ou seja,", (c-400), "Bq/kg, o equivalente a ", (c/40),"vezez abaixo da média mundial.(((c*100)/400)-100)")
    else:
print("O Potassio-40 está exatamente dentro dos limites da média mundial. A média mundial é de 400 Bq/kg") 

porcentagem=(((c*100)/400)-100)

print(porcentagem)
#400- 100
#c 