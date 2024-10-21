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

print(f"|- Navios do Jogador: {navios_jogador} -|")

#faz tabela do oponente

print("\n Tabela Do Oponente ")
print("-------------------")
print(f"{RED}  | 1  2  3  4  |{RESET}")
# print(f"{YELLOW}-------------------{RESET}")
for i in range(1, 5):
   print(f"{RED}{i}{RESET}", end=f"{YELLOW} |{RESET} ")
   for j in range(1, 5):
        print(f"{BLUE}◻{RESET}", end="  ")
   print(f"{YELLOW}|{RESET} ")
print(f"{YELLOW}-------------------{RESET}\n")

# Esse codigo continuará enquanto a vida do jogador e a vida do oponente for maior que 0 👇
while navios_oponente > 0 and navios_jogador > 0:

    print("=== Vez do Jogador === \n")
    chance_acerto = rand(1, chance_total)
    acerto = rand(1, chance_total)
      # pede ao Usuário digita as coordenadas para Acerta os Navios
      # Continuará enquanto as coordenada não forem validas. 👇

    if coordenadas_agua != "":
        print(f"Coordenadas 'da água': \n{coordenadas_agua}")

    while True:
        linha_tabela = (input("Digite a linha da tabela do oponente: "))
        coluna_tabela = (input("Digite a coluna da tabela do oponente: "))
        
        
        if (linha_tabela.isdigit()) and (coluna_tabela.isdigit()):
            coluna_tabela = int(coluna_tabela)
            linha_tabela = int(linha_tabela)
            if (linha_tabela > 0 and linha_tabela <= 4) and (coluna_tabela > 0 and coluna_tabela <= 4):
                break
            else:
                print("\n|- Coordenadas Digitadas Invalidas! -|\n")
        else:
            print("\n|- Valor Digitado Invalido! -|\n")
      
      # Se uma das coordenadas que foram digitas é iguail a coordenada de um navio. de maneira resumida. É impresso na tela "Bomba" e o oponente perde uma vida. caso contrario. É impresso na tela "água" e é o jogador que perde um vida. 👇 
    if (linha_tabela == coordernada_X_1 and coluna_tabela == coordernada_Y_1) or (linha_tabela == coordernada_X_2 and coluna_tabela == coordernada_Y_2) or (linha_tabela == coordernada_X_3 and coluna_tabela == coordernada_Y_3) or (linha_tabela == coordernada_X_4 and coluna_tabela == coordernada_Y_4) :
        navios_oponente -=1
        for i in range(1, 5):
            for j in range(1, 5):
                  if j == coordernada_X_1 and coordernada_X_1 == linha_tabela and i == coordernada_Y_1 and coordernada_Y_1 == coluna_tabela:
                     coordenada_marcada_1 = True
                     bt1 +=1
                  if j == coordernada_X_2 and coordernada_X_2 == linha_tabela and i == coordernada_Y_2 and coordernada_Y_2 == coluna_tabela:
                     coordenada_marcada_2 = True
                     bt2 +=1
                  if  j == coordernada_X_3 and coordernada_X_3 == linha_tabela and i == coordernada_Y_3 and coordernada_Y_3 == coluna_tabela:
                     coordenada_marcada_3 = True
                     bt3 +=1 
                  if  j == coordernada_X_4 and coordernada_X_4 == linha_tabela and i == coordernada_Y_4 and coordernada_Y_4 == coluna_tabela:
                     coordenada_marcada_4 = True
                     bt4 +=1
        print("\n Tabela Do Oponente ")
        print("-------------------")
        print(f"{RED}  | 1  2  3  4  |{RESET}")
        # print(f"{YELLOW}-------------------{RESET}")         
        for i in range(1, 5):
            print(f"{RED}{i}{RESET}", end=f"{YELLOW} |{RESET} ")
            for j in range(1,5):
                  if j == coordernada_Y_1 and i == coordernada_X_1 and coordenada_marcada_1 == True:
                     print(f"{DARK_BLUE}▣{RESET}", end="  ")
                  elif j == coordernada_Y_2 and i == coordernada_X_2 and coordenada_marcada_2 == True:
                     print(f"{DARK_BLUE}▣{RESET}", end="  ")
                  elif j == coordernada_Y_3 and i == coordernada_X_3 and coordenada_marcada_3 == True:
                     print(f"{DARK_BLUE}▣{RESET}", end="  ")
                  elif j == coordernada_Y_4 and i == coordernada_X_4 and coordenada_marcada_4 == True:
                     print(f"{DARK_BLUE}▣{RESET}", end="  ")
                
                  else:
                     print(f"{BLUE}◻{RESET}", end="  ")
            print(f"{YELLOW}|{RESET} ")
        print(f"{YELLOW}-------------------{RESET}")
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
                time.sleep(0.5)
                print(f"{GREEN}\n=== You Win! ===\n{RESET}")
                break
            
            print(f"|- Navios Restantes do Oponente: {navios_oponente} -|\n")
    else:
        print("\n Tabela Do Oponente ")
        print("-------------------")
        print(f"{RED}  | 1  2  3  4  |{RESET}")
        # print(f"{YELLOW}-------------------{RESET}")
        for i in range(1, 5):
            print(f"{RED}{i}{RESET}", end=f"{YELLOW} |{RESET} ")
            for j in range(1, 5):
                if j == coordernada_Y_1 and i == coordernada_X_1 and coordenada_marcada_1 == True:
                        print(f"{DARK_BLUE}▣{RESET}", end="  ")
                elif j == coordernada_Y_2 and i == coordernada_X_2 and coordenada_marcada_2 == True:
                        print(f"{DARK_BLUE}▣{RESET}", end="  ")
                elif j == coordernada_Y_3 and i == coordernada_X_3 and coordenada_marcada_3 == True:
                        print(f"{DARK_BLUE}▣{RESET}", end="  ")
                elif j == coordernada_Y_4 and i == coordernada_X_4 and coordenada_marcada_4 == True:
                        print(f"{DARK_BLUE}▣{RESET}", end="  ")
                else:
                    print(f"{BLUE}◻{RESET}", end="  ")
            print(f"{YELLOW}|{RESET} ")
        print(f"{YELLOW}-------------------{RESET}")

        coordenadas_agua += f"X: {str(linha_tabela)} - Y: {str(coluna_tabela)} |\n"
        print("\n|- Água! -|\n ") 
    time.sleep(1)
    (input("Pressiona Qualquer Tecla para continuar...\n"))

    # os.system("cls")

    print(" === Vez do Oponente === \n")
    time.sleep(2)

    if acerto <= chance_acerto:
        navios_jogador -= 1
        print("|- Oponente Destroiu um Navio! -|")
        
        if navios_jogador == 0:
            time.sleep(0.5)
            print(f"{RED}\n === You Lose! ===\n{RESET}")
            break
        
        print(f"|- Navios Restantes do Jogador: {navios_jogador} -|\n")
    else:
        print("|- Oponente Acertou na Água -|\n")
    
    time.sleep(1)
    (input("Pressiona Qualquer Tecla para continuar...\n"))
    # os.system("cls")

    chance_total += 10


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

chance_total = 10

coordenadas_agua = ""

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