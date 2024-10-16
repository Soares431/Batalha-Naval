
# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 

tabela_usuario = ""
coordernada_submarino = ""

posicao_x = 0
posicao_y = 0

espaco_vazio = True
posicao_submarino_aceita = False

submarinos_na_agua = 0

print("\n|---------------------------|")
print("| ===== BATALHA NAVAL ===== |")
print("|---------------------------|\n")

print("\n|--- ADICIONE OS SUBMARINOS ---|\n")

# Criar uma tabela 👇
print("\n  | 1  2  3  4  5  |")
print("-----------------------")
for i in range(1, 6):
   print(i, end=" | ")
   for j in range(1, 6):
        print(f"◻", end="  ")
   print("| ")
print("-----------------------\n")

#  Enquanto a quantidade de submarinos for menor do que a quantidade total que possa ser adicionado, esse "while" continuará executando 👇
while submarinos_na_agua < 5: 

   #  Adiciona novos submarinos, caso a posicao de um novo submarino seja aceita, vai para a proxima parte, senão, continuará preso nesse "while" 👇
   while posicao_submarino_aceita == False:
      posicao_x = int(input("Posicao 'X' da Embarcações: "))
      posicao_y = int(input("Posicao 'Y 'da Embarcações: "))
      soma_da_coordenadas = 0
      
      if (posicao_x <= 0 or posicao_x > 6) or (posicao_y <= 0 or posicao_y > 6):
         print("\n| Coordenadas Informadas Invalidas. Não ultrapasse os Limites! |\n")
      
      else:
         if tabela_usuario != "":
            tabela_usuario_cortado = tabela_usuario.split(",")
         
            if tabela_usuario_cortado[1] == "":
               tabela_usuario_cortado.pop(1)
         
            for coordenadas in tabela_usuario_cortado:
              
               for caracteres in range(0, len(coordenadas), 2): 
                  soma_da_coordenadas = ""
                  dois_caracteres = coordenadas[caracteres:caracteres+2]
                  
                  soma_da_coordenadas = str(dois_caracteres[0]) + str(dois_caracteres[1])
                  print(str(dois_caracteres[0]))
                  print(soma_da_coordenadas)
               if((str(posicao_x) + str(posicao_y)) == (soma_da_coordenadas)):
                  posicao_submarino_aceita = False
                  print("\n| Essa Coordenada ja foi preenchida! |\n")
                  break
                     
               else:
                  posicao_submarino_aceita = True
                  submarinos_na_agua +=1
                  print(f"\n| Novo Submarino Adicionado! pode ser colocado mais {5 - submarinos_na_agua}! \n")
                  break
                  
         else:
            posicao_submarino_aceita = True
            submarinos_na_agua +=1
            print(f"\n| Novo Submarino Adicionado! pode ser colocado mais {5 - submarinos_na_agua} |\n")
   # ---------------------------
   
   # Quando a posição do novo submarino for aceita, atualizará a tabela 👇
   if posicao_submarino_aceita:   
      print("\n  | 1  2  3  4  5  |")
      print("-----------------------")
      for i in range(1, 6):
         linha = i
         print(i, end=" | ")
         for j in range(1, 6):

            coluna = j

            coordernada_submarino = str(posicao_x) + str(posicao_y)
            linha_coluna = str(linha) + str(coluna)

            if posicao_x == linha and posicao_y == coluna:
               tabela_usuario += coordernada_submarino + ","

            if tabela_usuario != "":
               tabela_usuario_cortado = tabela_usuario.split(",")
               
               if tabela_usuario_cortado[1] == "":
                  tabela_usuario_cortado.pop(1)
                  
               if len(tabela_usuario.split(",")) == 1:
                  espaco_vazio = False
               else:
                  if linha_coluna in tabela_usuario_cortado:
                     espaco_vazio = False
                  else:
                     espaco_vazio = True
         
            if espaco_vazio == False:
               print(f"◼", end="  ")
            else:
               print(f"◻", end="  ")
         
         print(f"| ", end="")
         print()
         posicao_submarino_aceita = False
      print("-----------------------\n")
         
         
   # ---------------------------
   
print("\n Navio Adcionados! \n")

# ---------------------------

# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 

from random import randint as rand

vida_jogador = 5
vida_inimigo = 5

# Os "lev" irão determinar qual quadrado marcar
lev1 = False
lev2 = False
lev3 = False
lev4 = False
lev5 = False
# Os "bt" irão determinar qual quadrado não pode marcar de novo
bt1 = 0
bt2 = 0
bt3 = 0
bt4 = 0
bt5 = 0

# Coordenada do Navio do Inimigo 👇
coordernada_X_1 = 0
coordernada_Y_1 = 0

coordernada_X_2 = 0
coordernada_Y_2 = 0

coordernada_X_3 = 0
coordernada_Y_3 = 0

coordernada_X_4 = 0
coordernada_Y_4 = 0

coordernada_X_5 = 0
coordernada_Y_5 = 0


# enquanto as coordenadas forem iguais, ele continuarão a receber novos valores aleatorios👇
while (coordernada_X_1 == coordernada_X_2 or coordernada_X_1 == coordernada_X_3 or coordernada_X_1 == coordernada_X_4 or coordernada_X_1 == coordernada_X_5 or coordernada_X_2 == coordernada_X_3 or coordernada_X_2 == coordernada_X_4 or coordernada_X_2 == coordernada_X_5 or coordernada_X_3 == coordernada_X_4 or coordernada_X_3 == coordernada_X_5 or coordernada_X_4 == coordernada_X_5) and (coordernada_Y_1 == coordernada_Y_2 or coordernada_Y_1 == coordernada_Y_3 or coordernada_Y_1 == coordernada_Y_4 or coordernada_Y_1 == coordernada_Y_5 or coordernada_Y_2 == coordernada_Y_3 or coordernada_Y_2 == coordernada_Y_4 or coordernada_Y_2 == coordernada_Y_5 or coordernada_Y_3 == coordernada_Y_4 or coordernada_Y_3 == coordernada_Y_5 or coordernada_Y_4 == coordernada_Y_5):
   
    coordernada_X_1 = rand(1, 5)
    coordernada_Y_1 = rand(1, 5)
    coordernada_X_2 = rand(1, 5)
    coordernada_Y_2 = rand(1, 5)
    coordernada_X_3 = rand(1, 5)
    coordernada_Y_3 = rand(1, 5)
    coordernada_X_4 = rand(1, 5)
    coordernada_Y_4 = rand(1, 5)
    coordernada_X_5 = rand(1, 5)
    coordernada_Y_5 = rand(1, 5)

print("\n|---------------------------|")
print("| ===== BATALHA NAVAL ===== |")
print("|---------------------------|\n")

print("|- Diga Coordenadas para Acerta os Navios do Oponente -|")
print(f"|- Vidas Restantes do Jogador: {vida_jogador} -|")

#faz tabela (por enquanto inutil)👇
print("\n  | 1  2  3  4  5  |")
print("-----------------------")
for i in range(1, 6):
   print(i, end=" | ")
   for j in range(1, 6):
        print(f"◻", end="  ")
   print("| ")
print("-----------------------\n")

# Esse codigo continuará enquanto a vida do jogador e a vida do oponente for maior que 0 👇
while vida_inimigo > 0 and vida_jogador > 0:

      # pede ao Usuário digita as coordenadas para Acerta os Navios
      # Continuará enquanto as coordenada não forem validas. 👇
      while True:
         posicao_x = int(input("Posição X: "))
         posicao_y = int(input("Posição Y: "))
         
         if (posicao_x > 0 and posicao_x <= 5) and (posicao_y > 0 and posicao_y <= 5):
            break
         else:
            print("\n|- Coordenadas Digitadas Invalidas! -|\n")
      
      # Se uma das coordenadas que foram digitas é iguail a coordenada de um navio. de maneira resumida. É impresso na tela "Bomba" e o oponente perde uma vida. caso contrario. É impresso na tela "água" e é o jogador que perde um vida. 👇 
      if (posicao_x == coordernada_X_1 and posicao_y == coordernada_Y_1) or (posicao_x == coordernada_X_2 and posicao_y == coordernada_Y_2) or (posicao_x == coordernada_X_3 and posicao_y == coordernada_Y_3) or (posicao_x == coordernada_X_4 and posicao_y == coordernada_Y_4) or (posicao_x == coordernada_X_5 and posicao_y == coordernada_Y_5):
         vida_inimigo -=1
         for i in range(1, 5):
            for j in range(1, 5):
                  if j == coordernada_X_1 and coordernada_X_1 == posicao_x and i == coordernada_Y_1 and coordernada_Y_1 == posicao_y:
                     lev1 = True
                     bt1 +=1
                  if j == coordernada_X_2 and coordernada_X_2 == posicao_x and i == coordernada_Y_2 and coordernada_Y_2 == posicao_y:
                     lev2 = True
                     bt2 +=1
                  if  j == coordernada_X_3 and coordernada_X_3 == posicao_x and i == coordernada_Y_3 and coordernada_Y_3 == posicao_y:
                     lev3 = True
                     bt3 +=1 
                  if  j == coordernada_X_4 and coordernada_X_4 == posicao_x and i == coordernada_Y_4 and coordernada_Y_4 == posicao_y:
                     lev4 = True
                     bt4 +=1
                  if  j == coordernada_X_5 and coordernada_X_5 == posicao_x and i == coordernada_Y_5 and coordernada_Y_5 == posicao_y:
                     lev5 = True
                     bt5 +=1
         print("\n  | 1  2  3  4  5  |")
         print("-----------------------")           
         for i in range(1, 6):
            print(i, end=" | ")
            for j in range(1,6):
                  if j == coordernada_Y_1 and i == coordernada_X_1 and lev1 == True:
                     print(f"▣", end="  ")
                     bt1 == True
                  elif j == coordernada_Y_2 and i == coordernada_X_2 and lev2 == True:
                     print(f"▣", end="  ")
                     bt2 == True
                  elif j == coordernada_Y_3 and i == coordernada_X_3 and lev3 == True:
                     print(f"▣", end="  ")
                     bt3 == True
                  elif j == coordernada_Y_4 and i == coordernada_X_4 and lev4 == True:
                     print(f"▣", end="  ")
                     bt4 == True
                  elif j == coordernada_Y_5 and i == coordernada_X_5 and lev5 == True:
                     print(f"▣", end="  ")
                     bt5 == True
                  else:
                     print(f"◻", end="  ")
            print("| ")
         print("-----------------------\n")
         if bt1 > 1 or bt2 > 1 or bt3 > 1 or bt4 > 1 or bt5 > 1:
            vida_inimigo -=1
            print("\n|- Esse navio já foi afundando, tente de novo -|\n")
            if bt1 > 1:
                  bt1 -=1
            if bt2 >1:
                  bt2 -=1
            if bt3 > 1:
                  bt3 -=1
            if bt4 > 1:
                  bt4 -=1
            if bt5 > 1:
                  bt5 -=1      
         else:
            print("\n| -Bomba! -|\n")
            print(f"|- Navios Restantes do Oponente: {vida_inimigo} -|\n")
      else:
         vida_jogador -=1
         print("\n  | 1  2  3  4  5  |")
         print("-----------------------")
         for i in range(1, 6):
            print(i, end=" | ")
            for j in range(1, 6):
                  if j == coordernada_Y_1 and i == coordernada_X_1 and lev1 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_2 and i == coordernada_X_2 and lev2 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_3 and i == coordernada_X_3 and lev3 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_4 and i == coordernada_X_4 and lev4 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_5 and i == coordernada_X_5 and lev5 == True:
                     print(f"▣", end="  ")
                  
                  else:
                     print(f"◻", end="  ")
            print("| ")
         print("-----------------------\n")
         print("\n|- Água! -") 
         print(f"|- Vidas Restantes do Jogador: {vida_jogador} -|\n")
         
      (input("\nPressiona Qualquer Tecla para continuar...\n"))
      
if vida_inimigo == 0:
    print("\n=== You Win! ===\n")
else:
    print("\n === You Lose! ===\n")