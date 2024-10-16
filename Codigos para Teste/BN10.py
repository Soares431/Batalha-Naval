# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 
# a variável pulo só existe para ter melhor controle do código.

import random
pv = 5
ev = 5
xsa = [1, 2, 3, 4, 5, 6]
ysb = [1, 2, 3, 4, 5, 6]
lev1 = False
lev2 = False
lev3 = False
lev4 = False
lev5 = False
ilist =[]
jlist =[]
for i in range(1,7):
    for j in range(1,7):
        ilist.append(i)
        jlist.append(j)

xs1 = random.choice(xsa)
ys1 = random.choice(ysb)
xs2 = random.choice(xsa)
ys2 = random.choice(ysb)
xs3 = random.choice(xsa)
ys3 = random.choice(ysb)
xs4 = random.choice(xsa)
ys4 = random.choice(ysb)
xs5 = random.choice(xsa)
ys5 = random.choice(ysb)
while xs1 == xs2 or xs1 == xs3 or xs1 == xs4 or xs1 == xs5 or xs2 == xs3 or xs2 == xs4 or xs2 == xs5 or xs3 == xs4 or xs3 == xs5 or xs4 == xs5 and ys1 == ys2 or ys1 == ys3 or ys1 == ys4 or ys1 == ys5 or ys2 == ys3 or ys2 == ys4 or ys2 == ys5 or ys3 == ys4 or ys3 == ys5 or ys4 == ys5:
    xs1 = random.choice(xsa)
    ys1 = random.choice(ysb)
    xs2 = random.choice(xsa)
    ys2 = random.choice(ysb)
    xs3 = random.choice(xsa)
    ys3 = random.choice(ysb)
    xs4 = random.choice(xsa)
    ys4 = random.choice(ysb)
    xs5 = random.choice(xsa)
    ys5 = random.choice(ysb)

while ev > 0 and pv > 0:
    pulo = str(input("Continua?: "))
    print("x: ", xs1)
    print("y: ", ys1)
    print("x: ", xs2)
    print("y: ", ys2)
    print("x: ", xs3)
    print("y: ", ys3)
    print("x: ", xs4)
    print("y: ", ys4)
    print("x: ", xs5)
    print("y: ", ys5)
    print("A  B  C  D  E  F")
    for i in range(1, 7):
        for j in range(1, 7):
            print(f"◻", end="  ")
        print(i)
    perguntax = int(input("Diga a posição de x: "))
    perguntay = int(input("Diga a posição de y: "))
    if perguntax == xs1 and perguntay == ys1 or perguntax == xs2 and perguntay == ys2 or perguntax == xs3 and perguntay == ys3 or perguntax == xs4 and perguntay == ys4 or perguntax == xs5 and perguntay == ys5:
        ev -=1
        for i in range(1, 7):
            for j in range(1, 7):
                if j == xs1 and xs1 == perguntax and i == ys1 and ys1 == perguntay:
                    lev1 = True
                if j == xs2 and xs2 == perguntax and i == ys2 and ys2 == perguntay:
                    lev2 = True
                if  j == xs3 and xs3 == perguntax and i == ys3 and ys3 == perguntay:
                    lev3 = True
                if  j == xs4 and xs4 == perguntax and i == ys4 and ys4 == perguntay:
                    lev4 = True
                if  j == xs5 and xs5 == perguntax and i == ys5 and ys5 == perguntay:
                    lev5 = True
        print("A  B  C  D  E  F")            
        for i in range(1, 7):
            for j in range(1,7):
                if j == ys1 and i == xs1 and lev1 == True:
                    print(f"▣", end="  ")
                elif j == ys2 and i == xs2 and lev2 == True:
                    print(f"▣", end="  ")
                elif j == ys3 and i == xs3 and lev3 == True:
                    print(f"▣", end="  ")
                elif j == ys4 and i == xs4 and lev4 == True:
                    print(f"▣", end="  ")
                elif j == ys5 and i == xs5 and lev5 == True:
                    print(f"▣", end="  ")
                else:
                    print(f"◻", end="  ")
            print(i)
        print("Bomba!")
    else:
        pv -=1
        print("A  B  C  D  E  F")
        for i in range(1, 7):
            for j in range(1, 7):
                if j == ys1 and i == xs1 and lev1 == True:
                    print(f"▣", end="  ")
                elif j == ys2 and i == xs2 and lev2 == True:
                    print(f"▣", end="  ")
                elif j == ys3 and i == xs3 and lev3 == True:
                    print(f"▣", end="  ")
                elif j == ys4 and i == xs4 and lev4 == True:
                    print(f"▣", end="  ")
                elif j == ys5 and i == xs5 and lev5 == True:
                    print(f"▣", end="  ")        
                else:
                    print(f"◻", end="  ")
            print(i)
        print("Água!")   
if ev == 0:
    print("You Win!")
else:
    print("You Lose!")