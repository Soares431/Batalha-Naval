# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 
# a variável pulo só existe para ter melhor controle do código.
# bug de escolher o mesmo navio dnv e dnv para ganhar foi consertado.

from random import randint as rand

vida_jogaodor = 6
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
print(f"|- Vidas Restantes do Jogador: {vida_jogaodor} -|")

print("\n  | 1  2  3  4  5  |")
print("-----------------------")
for i in range(1, 6):
   print(i, end=" | ")
   for j in range(1, 6):
        print(f"◻", end="  ")
   print("| ")
print("-----------------------\n")
while vida_inimigo > 0 and vida_jogaodor > 0:
    
      while True:
         posicao_x = int(input("Posição X: "))
         posicao_y = int(input("Posição Y: "))
         
         if (posicao_x > 0 and posicao_x <= 5) and (posicao_y > 0 and posicao_y <= 5):
            break
         else:
            print("\n|- Coordenadas Digitadas Invalidas! -|\n")
      
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
         vida_jogaodor -=1
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
         print(f"|- Vidas Restantes do Jogador: {vida_jogaodor} -|\n")
         
      (input("\nPressiona Qualquer Tecla para continuar...\n"))
      
if vida_inimigo == 0:
    print("\n=== You Win! ===\n")
else:
    print("\n === You Lose! ===\n")