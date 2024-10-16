dicionario={}
i=1
dp2=222
dp3=333
dp4=444
dp5=555
while True:
    px=int(input(f"Escreva a posição  x do  {i}º submarino"))
    py=int(input(f"Escreva a posição y do  {i}º submarino"))
    dicionario[f"valor {i}"]=(px/py)+px
    dicionario[f"x{i}"]=px
    dicionario[f"y{i}"]=py
    dp1=dicionario["valor 1"]
    if "valor 2" in dicionario:
        dp2=dicionario["valor 2"]
    elif "valor 3" in dicionario:
        dp3=dicionario["valor 3"]
    elif "valor 4" in dicionario:
        dp4=dicionario["valor 4"]
    elif "valor 5" in dicionario:
        dp5=dicionario["valor 5"]
    if 0<i<6:
        if dp1==dp2 or dp1==dp3 or dp1==dp4 or dp1==dp5 or dp2==dp3 or dp2==dp4 or dp2==dp5 or dp3==dp4 or dp3==dp5 or dp4==dp5:
            print("Voçê colocou duas cordenadas iguais")
        elif (6<py or py<0) and (6<px or px<0):
            print("As suas cordenadas x e y é inválida ")
        elif 6<px or px<0:
            print("Sua cordenada x é inválida ")
        elif 6<py or py<0:
            print("Sua cordenada y é inválida ")
        else:
            i+=1
    else:
        break
        
print(dicionario)
