# Agua = ◻ / Navio = ◼ / Navio atingido = ▣ 
xs1 = int(input("posicao do submarino: "))
ys1 = int(input("posicao do submarino: "))
xs2 = int(input("posicao do submarino: "))
ys2 = int(input("posicao do submarino: "))
xs3 = int(input("posicao do submarino: "))
ys3 = int(input("posicao do submarino: "))
xs4 = int(input("posicao do submarino: "))
ys4 = int(input("posicao do submarino: "))

posicao = []
for i in range(1, 16):
    c = []
    for j in range(1, 16):
        c.append(str(j))
    posicao.append(c)

for i in range(1, 16):
    for j in range(1, 16):
        if xs1 == i and ys1 == j:
            print(f"◼", end=" ")
        elif xs2 == i and ys2 == j:
            print(f"◼", end=" ")
        elif xs3 == i and ys3 == j:
            print(f"◼", end=" ")
        elif xs4 == i and ys4 == j:
            print(f"◼", end=" ")
        else: 
            print(f"◻", end=" ")
    print()