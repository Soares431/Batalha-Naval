
# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 

tabela_usuario = ""
coordernada_submarino = ""

posicao_x = 0
posicao_y = 0

espaco_vazio = True
posicao_submarino_aceita = False

submarinos_na_agua = 0
total_submarinos = 5

print("\n|---------------------------|")
print("| ===== BATALHA NAVAL ===== |")
print("|---------------------------|\n")

# Criar uma tabela 👇
for i in range(1, 7):
   print(f"{i:02}", end=" | ")
   for i in range(1, 7):
      print(f"◻", end=" ")  
   print(f" | ", end="")
   print()
   

print("\n|--- ADICIONE OS SUBMARINOS ---|\n")

#  Enquanto a quantidade de submarinos for menor do que a quantidade total que possa ser adicionado, esse "while" continuará executando 👇
while submarinos_na_agua < total_submarinos: 

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
               soma_da_coordenadas = 0
               for caracteres in range(0, len(coordenadas), 2): 
                  dois_caracteres = coordenadas[caracteres:caracteres+2]
               
                  soma_da_coordenadas += int(dois_caracteres[0]) + int(dois_caracteres[1])
               
               # Ainda esta bugado essa parte!👇
               if ((posicao_x + posicao_y) == (soma_da_coordenadas + 1)) or  ((posicao_x + posicao_y) == (soma_da_coordenadas - 1)):
                  
                  
                  print("\n| Os Submarinos não podem ser Vizinhos! |\n") 
                  break
                     
               elif((posicao_x + posicao_y) == (soma_da_coordenadas)):
                  
                  print("\n| Essa Coordenada ja foi preenchida! |\n")
                  break
                     
               else:
                     posicao_submarino_aceita = True
                     submarinos_na_agua +=1
                     print(f"\n| Novo Submarino Adicionado! pode ser colocado mais {total_submarinos - submarinos_na_agua}! \n")
                     break
         
         else:
            posicao_submarino_aceita = True
            submarinos_na_agua +=1
            print(f"\n| Novo Submarino Adicionado! pode ser colocado mais {total_submarinos - submarinos_na_agua} |\n")
   # ---------------------------
   
   # Quando a posição do novo submarino for aceita, atualizará a tabela 👇
   if posicao_submarino_aceita:   
      for i in range(1, 7):
         linha = i
         print(f"{linha:02}", end=" | ")
         for j in range(1, 7):

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
               print(f"◼", end=" ")
            else:
               print(f"◻", end=" ")
         
         print(f" | ", end="")
         print()
         posicao_submarino_aceita = False
         
   # ---------------------------
   
print("\n Navio Adcionados! \n")

# ---------------------------

