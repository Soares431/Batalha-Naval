# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 
xs1 = int(input("posicao do submarino: "))
ys1 = int(input("posicao do submarino: "))

for i in range(1, 10):
    for j in range(1, 10):
        if xs1 == i and ys1 == j:
            print(f"◼", end=" ")
        else: 
            print(f"◻", end=" ")
    print()
ax = int(input("Coordenada x para a bomba: "))
ay = int(input("Coordenada y para a bomba: "))
for i in range(1, 10):
    for j in range(1, 10):
        if xs1 == i and ys1 == j:
            if ax == xs1 and ay == ys1:
                print(f"▣", end=" ")
            else:
                print(f"◼", end=" ")
        else: 
            print(f"◻", end=" ")  
    print()
if xs1 != ax and ys1 != ay:
    print("A mira não tá em dia")