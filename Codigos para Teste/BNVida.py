#jogador = 29
jogador = 1
jogadorposx = [5, 4]
jogadorposy = [4, 5]

shoot = str(input("Atirar?: "))

x = int(input("Digite onde atirar: "))
y = int(input("Digite onde atirar: "))
posxindex = jogadorposx.index(x)
posyindex = jogadorposy.index(y)
while jogador > 0:
    if x == jogadorposx and y == jogadorposy and posxindex == posyindex:
        jogador -= 1
        print(f"BOMBA!!!! O jogador tem {jogador} vidas!")
        if jogador > 0:
            shoot = str(input("Continuar atirando?: "))
        else:
            print("Jogador derrotado! Guardando canhões!")        
            exit()
    else:
        print("ÁGUA!!!!! Foi um prazer lutar ao seu lado capitão.")
        print(posxindex)
        print(posyindex)
        print(x)
        print(y)
        print(jogadorposx)
        print(jogadorposy)
        exit()