dicionario={}
i=1
dp2=222
dp3=333
dp4=444
dp5=555
dp6=666
while True:
#pergunta posições👇
    px=int(input(f"Escreva a posição  x do  {i}º submarino"))
    py=int(input(f"Escreva a posição y do  {i}º submarino"))
#--------------------------------------------------------------------------
#Salva valores em dicionário 👇   
    dicionario[f"valor {i}"] = (px * 7) + (py * 11)
    dicionario[f"x{i}"]=px
    dicionario[f"y{i}"]=py
#-------------------------------------------------------------------------------------------------------------------
#salva os valores do calcuo que serve pra vertificar se as coordenadas são iguais 👇
    dp1=dicionario["valor 1"]
    if "valor 2" in dicionario:
        dp2=dicionario["valor 2"]
    if "valor 3" in dicionario:
        dp3=dicionario["valor 3"]
    if "valor 4" in dicionario:
        dp4=dicionario["valor 4"]
    if "valor 5" in dicionario:
        dp5=dicionario["valor 5"]
    if "valor 6" in dicionario:
        dp5=dicionario["valor 5"]
#-------------------------------------------------------------------------------------------------------------------------
    #Adiciona os valores de x do dicionario a uma váriavel 👇
    p1x=dicionario["x1"]
    if "x2" in dicionario:
        p2x=dicionario["x2"]
    if "x3" in dicionario:
        p3x=dicionario["x3"]
    if "x4" in dicionario:
        p4x=dicionario["x4"]
    if "x5" in dicionario:
        p5x=dicionario["x5"]
    #------------------------------------------------------------------------------------------------------------------------
    #Adiciona os valores de y do dicionario a uma váriavel 👇
    p1y=dicionario["y1"]
    if "y2" in dicionario:
        p2y=dicionario["y2"]
    if "y3" in dicionario:
        p3y=dicionario["y3"]
    if "y4" in dicionario:
        p4y=dicionario["y4"]
    if "y5" in dicionario:
        p5y=dicionario["y5"]  
    #---------------------------------------------------------------------------------------------------------------------------    
    #Faz todas as verificações e encerra o while 👇
    if 0<i<6:
        #verifica se os valores são iguais 👇(ta meio bugado vc tem que escrever 6 valores pra 5 darem certo )
        if dp1==dp2 or dp1==dp3 or dp1==dp4 or dp1==dp5 or dp1==dp6 or dp2==dp3 or dp2==dp4 or dp2==dp5 or dp2==dp6 or dp3==dp4 or dp3==dp5 or dp3==dp6 or dp4==dp5 or dp4==dp6 or dp5==dp6:
            print("Voçê colocou duas cordenadas iguais")
            i-=1
        #------------------------------------------------------------------------------------------------------------------------------------
        #verifica se as pisições são valores válidos👇
        elif (6<py or py<0) and (6<px or px<0):
            print("As suas cordenadas x e y é inválida ")
            i-=1
        elif 6<px or px<0:
            print("Sua cordenada x é inválida ")
            i-=1
        elif 6<py or py<0:
            print("Sua cordenada y é inválida ")
            i-=1
        #---------------------------------------------------------------------------------------------------------------------
        #verifica se os submarinos estão em posições vizinhas 👇
        if "y2" in dicionario: 
            if "x2" in dicionario:   
                if ((p1x==p2x) and ((p2y==p1y+1) or (p2y==p1y-1))) or ((p1y==p2y) and ((p2x==p1x+1) or (p2x==p1x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y3" in dicionario: 
            if "x3" in dicionario:
                if ((p1x==p3x) and ((p3y==p1y+1) or (p3y==p1y-1))) or ((p1y==p3y) and ((p3x==p1x+1) or (p3x==p1x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1                   
        if "y4" in dicionario: 
            if "x4" in dicionario:
                if ((p1x==p4x) and ((p4y==p1y+1) or (p4y==p1y-1))) or ((p1y==p4y) and ((p4x==p1x+1) or (p4x==p1x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y5" in dicionario: 
            if "x5" in dicionario:
                if ((p1x==p5x) and ((p5y==p1y+1) or (p5y==p1y-1))) or ((p1y==p5y) and ((p5x==p1x+1) or (p5x==p1x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y2" in dicionario and "y3" in dicionario: 
            if "x2" in dicionario and "x3" in dicionario:
                if ((p2x==p3x) and ((p3y==p2y+1) or (p3y==p2y-1))) or ((p2y==p3y) and ((p3x==p2x+1) or (p3x==p2x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y2" in dicionario and "y4" in dicionario: 
            if "x2" in dicionario and "x4" in dicionario:
                if ((p2x==p4x) and ((p4y==p2y+1) or (p4y==p2y-1))) or ((p2y==p4y) and ((p4x==p2x+1) or (p4x==p2x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y2" in dicionario and "y5" in dicionario: 
            if "x2" in dicionario and "x5" in dicionario:
                if ((p2x==p5x) and ((p5y==p2y+1) or (p5y==p2y-1))) or ((p2y==p5y) and ((p5x==p2x+1) or (p5x==p2x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y3" in dicionario and "y4" in dicionario: 
            if "x3" in dicionario and "x4" in dicionario:
                if ((p3x==p4x) and ((p4y==p3y+1) or (p4y==p3y-1))) or ((p3y==p4y) and ((p4x==p3x+1) or (p4x==p3x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y3" in dicionario and "y5" in dicionario: 
            if "x3" in dicionario and "x5" in dicionario:
                if ((p3x==p5x) and ((p5y==p3y+1) or (p5y==p3y-1))) or ((p3y==p5y) and ((p5x==p3x+1) or (p5x==p3x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        if "y4" in dicionario and "y5" in dicionario: 
            if "x4" in dicionario and "x5" in dicionario:
                if ((p4x==p5x) and ((p5y==p4y+1) or (p5y==p4y-1))) or ((p4y==p5y) and ((p5x==p4x+1) or (p5x==p4x-1))):
                    print("Você colocou dois submarinos um do lado do outro e isso não é permitido")
                    i-=1
        #-------------------------------------------------------------------------------------------------------------------------------------
        i+=1
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    else:
        break
#-------------------------------------------------------------------------------------------------------------------------------------       
print(dicionario)
