# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 
# bru e resul fazem nada, mas bru existe só para ter um pouquinho mais de controle sobre o código
import random
pv = 1
ev = 1
xsa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ysb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resul = "agua"

while ev > 0 and pv > 0:
    bru = str(input("Continue?: "))
    xs = random.choice(xsa)
    ys = random.choice(ysb)
    print(xs)
    print(ys)
    print("A  B  C  D  E  F  G  H  I  J")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"◻", end="  ")
        print(i)
    perguntax = int(input("Diga a posição de y: "))
    perguntay = int(input("Diga a posição de x: "))
    if perguntax == xs and perguntay == ys:
        ev -=1
        resul = "bomba"
        for i in range(1, 11):
            for j in range(1, 11):
                if j == ys and i == xs:
                    print(f"▣", end="  ")
                else:
                    print(f"◻", end="  ")
            print(i)
        print("Bomba!")
    else:
        pv -=1
        print("Água!")   
if ev == 0:
    print("You Win!")
else:
    print("You Lose!")