# Agua = ◻ / agua atingida = ◼ / Navio atingido = X

posicao = []

for i in range(1, 12):
    c = []
    for j in range(1, 12):
        c.append(j)
    posicao.append(c)
    
vida_Pc = 3
vida_Jogador = 3

embarcacoes = 5
while embarcacoes > 0: 
    xs = int(input("Posicao 'X' da Embarcações: "))
    ys = int(input("Posicao 'Y 'da Embarcações: ")) 
    
    for i in range(1, len(posicao)):
       
        for j in range(1, len(posicao[i])):
            if xs == i + 1 and ys == posicao[i][j]:
                print(f"◼", end=" ")
            else:
                print(f"◻", end=" ")
        print() 

# while vida_Jogador > 0 and vida_Pc > 0:
#     rodada_Pc = 3
#     rodada_Jogador = 3
    
#     print("\n === Vez do jogador === \n")
    
#     while rodada_Jogador > 0:
#         xs = int(input("Posicao 'X' da Embarcações: "))
#         ys = int(input("Posicao 'Y ' do Embarcações: ")) 
    
    
    