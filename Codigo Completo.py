# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 

from random import randint as rand
import os
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"  # Azul claro
DARK_BLUE = "\033[34m"  # Azul escuro
RESET = "\033[0m"


navios_jogador = 4
navios_oponente = 4

# Os "lev" irão determinar qual quadrado marcar
coordenada_marcada_1 = False
coordenada_marcada_2 = False
coordenada_marcada_3 = False
coordenada_marcada_4 = False


# Os "bt" irão determinar qual quadrado não pode marcar de novo
bt1 = 0
bt2 = 0
bt3 = 0
bt4 = 0

# Coordenada do Navio do Inimigo 👇
coordernada_X_1 = 0
coordernada_Y_1 = 0

coordernada_X_2 = 0
coordernada_Y_2 = 0

coordernada_X_3 = 0
coordernada_Y_3 = 0

coordernada_X_4 = 0
coordernada_Y_4 = 0

chance_total = 10

coordenadas_agua = ""

# enquanto as coordenadas forem iguais, ele continuarão a receber novos valores aleatorios👇
while (coordernada_X_1 == coordernada_X_2 or coordernada_X_1 == coordernada_X_3 or coordernada_X_1 == coordernada_X_4 or coordernada_X_2 == coordernada_X_3 or coordernada_X_2 == coordernada_X_4 or coordernada_X_3 == coordernada_X_4) and (coordernada_Y_1 == coordernada_Y_2 or coordernada_Y_1 == coordernada_Y_3 or coordernada_Y_1 == coordernada_Y_4 or coordernada_Y_2 == coordernada_Y_3 or coordernada_Y_2 == coordernada_Y_4 or coordernada_Y_3 == coordernada_Y_4):
   
    coordernada_X_1 = rand(1, 4)
    coordernada_Y_1 = rand(1, 4)
    coordernada_X_2 = rand(1, 4)
    coordernada_Y_2 = rand(1, 4)
    coordernada_X_3 = rand(1, 4)
    coordernada_Y_3 = rand(1, 4)
    coordernada_X_4 = rand(1, 4)
    coordernada_Y_4 = rand(1, 4)

print(f"{RED}\n|---------------------------|{RESET}")
print(f"{YELLOW}| ===== BATALHA NAVAL ===== |{RESET}")
print(f"{RED}|---------------------------|\n{RESET}")

print(f"|- Vidas Restantes do Jogador: {navios_jogador} -|")

#faz tabela (por enquanto inutil)👇
print("\n  | 1  2  3  4  |")
print("-----------------------")
for i in range(1, 5):
   print(i, end=" | ")
   for j in range(1, 5):
        print(f"◻", end="  ")
   print("| ")
print("-----------------------\n")

# Esse codigo continuará enquanto a vida do jogador e a vida do oponente for maior que 0 👇
while navios_oponente > 0 and navios_jogador > 0:

    print("=== Vez do Jogador === \n")
    chance_acerto = rand(1, chance_total)
    acerto = rand(1, chance_total)
      # pede ao Usuário digita as coordenadas para Acerta os Navios
      # Continuará enquanto as coordenada não forem validas. 👇

    if coordenadas_agua != "":
        print(f"Coordenadas Acertadas água: \n{coordenadas_agua}")

    while True:
        posicao_y = (input("Posição X: "))
        posicao_x = (input("Posição Y: "))
        
        if (posicao_x.isdigit()) and (posicao_y.isdigit()):
            posicao_y = int(posicao_y)
            posicao_x = int(posicao_x)
            if (posicao_x > 0 and posicao_x <= 4) and (posicao_y > 0 and posicao_y <= 4):
                break
            else:
                print("\n|- Coordenadas Digitadas Invalidas! -|\n")
        else:
            print("\n|- Valor Digitado Invalido! -|\n")
      
      # Se uma das coordenadas que foram digitas é iguail a coordenada de um navio. de maneira resumida. É impresso na tela "Bomba" e o oponente perde uma vida. caso contrario. É impresso na tela "água" e é o jogador que perde um vida. 👇 
    if (posicao_x == coordernada_X_1 and posicao_y == coordernada_Y_1) or (posicao_x == coordernada_X_2 and posicao_y == coordernada_Y_2) or (posicao_x == coordernada_X_3 and posicao_y == coordernada_Y_3) or (posicao_x == coordernada_X_4 and posicao_y == coordernada_Y_4) :
        navios_oponente -=1
        for i in range(1, 5):
            for j in range(1, 5):
                  if j == coordernada_X_1 and coordernada_X_1 == posicao_x and i == coordernada_Y_1 and coordernada_Y_1 == posicao_y:
                     coordenada_marcada_1 = True
                     bt1 +=1
                  if j == coordernada_X_2 and coordernada_X_2 == posicao_x and i == coordernada_Y_2 and coordernada_Y_2 == posicao_y:
                     coordenada_marcada_2 = True
                     bt2 +=1
                  if  j == coordernada_X_3 and coordernada_X_3 == posicao_x and i == coordernada_Y_3 and coordernada_Y_3 == posicao_y:
                     coordenada_marcada_3 = True
                     bt3 +=1 
                  if  j == coordernada_X_4 and coordernada_X_4 == posicao_x and i == coordernada_Y_4 and coordernada_Y_4 == posicao_y:
                     coordenada_marcada_4 = True
                     bt4 +=1
        print("\n  | 1  2  3  4  |")
        print("-----------------------")           
        for i in range(1, 5):
            print(i, end=" | ")
            for j in range(1,5):
                  if j == coordernada_Y_1 and i == coordernada_X_1 and coordenada_marcada_1 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_2 and i == coordernada_X_2 and coordenada_marcada_2 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_3 and i == coordernada_X_3 and coordenada_marcada_3 == True:
                     print(f"▣", end="  ")
                  elif j == coordernada_Y_4 and i == coordernada_X_4 and coordenada_marcada_4 == True:
                     print(f"▣", end="  ")
                
                  else:
                     print(f"◻", end="  ")
            print("| ")
        print("-----------------------\n")
        if bt1 > 1 or bt2 > 1 or bt3 > 1 or bt4 > 1:
            navios_oponente -=1
            print("\n|- Esse navio já foi afundando, tente de novo -|\n")
            if bt1 > 1:
                bt1 -=1
            if bt2 >1:
                bt2 -=1
            if bt3 > 1:
                bt3 -=1
            if bt4 > 1:
                bt4 -=1     
        else:
            print("\n| -Bomba! -|\n")
            if navios_oponente == 0:
                print("\n=== You Win! ===\n")
                break
            
            print(f"|- Navios Restantes do Oponente: {navios_oponente} -|\n")
    else:
        print("\n  | 1  2  3  4  |")
        print("-----------------------")
        for i in range(1, 5):
            print(i, end=" | ")
            for j in range(1, 5):
                if j == coordernada_Y_1 and i == coordernada_X_1 and coordenada_marcada_1 == True:
                        print(f"▣", end="  ")
                elif j == coordernada_Y_2 and i == coordernada_X_2 and coordenada_marcada_2 == True:
                        print(f"▣", end="  ")
                elif j == coordernada_Y_3 and i == coordernada_X_3 and coordenada_marcada_3 == True:
                        print(f"▣", end="  ")
                elif j == coordernada_Y_4 and i == coordernada_X_4 and coordenada_marcada_4 == True:
                        print(f"▣", end="  ")
                    
                else:
                    print(f"◻", end="  ")
            print("| ")
        print("-----------------------\n")
        print(coordernada_X_1)
        print(coordernada_Y_1)

        print(coordernada_X_2)
        print(coordernada_Y_2)

        print(coordernada_X_3)
        print(coordernada_Y_3)

        print(coordernada_X_4)
        print(coordernada_Y_4)

        coordenadas_agua += f"Y: {str(posicao_x)} - X: {str(posicao_y)} |\n"
        print("\n|- Água! -|\n ") 
    time.sleep(1.5)
    (input("Pressiona Qualquer Tecla para continuar...\n"))

    os.system("cls")

    print("\n === Vez do Oponente === \n")
    time.sleep(2.5)

    if acerto <= chance_acerto:
        navios_jogador -= 1
        print("|- Oponente Destroiu um Navio! -|")
        
        if navios_jogador == 0:
            print("\n === You Lose! ===\n")
            break
        
        print(f"|- Vidas Restantes do Jogador: {navios_jogador} -|\n")
    else:
        print("|- Oponente Errou um Navio -|\n")
    
    time.sleep(1.5)
    (input("Pressiona Qualquer Tecla para continuar...\n"))
    os.system("cls")

    chance_total += 10
