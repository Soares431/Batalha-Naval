# Agua = ◻ / Submarino = ◼ / Submarino Atingido = ▣ 
# a variável pulo só existe para ter melhor controle do código.
# bug de escolher o mesmo navio dnv e dnv para ganhar foi consertado.

import random
pv = 5
ev = 5
xsa = [1, 2, 3, 4, 5, 6]
ysb = [1, 2, 3, 4, 5, 6]
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
while (xs1 == xs2 or xs1 == xs3 or xs1 == xs4 or xs1 == xs5 or xs2 == xs3 or xs2 == xs4 or xs2 == xs5 or xs3 == xs4 or xs3 == xs5 or xs4 == xs5) and (ys1 == ys2 or ys1 == ys3 or ys1 == ys4 or ys1 == ys5 or ys2 == ys3 or ys2 == ys4 or ys2 == ys5 or ys3 == ys4 or ys3 == ys5 or ys4 == ys5):
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

print("1  2  3  4  5  6")
for i in range(1, 7):
    for j in range(1, 7):
        print(f"◻", end="  ")
    print(i)

while ev > 0 and pv > 0:
    pulo = str(input("Continua?: "))
    print("x: ", ys1)
    print("y: ", xs1)
    print("x: ", ys2)
    print("y: ", xs2)
    print("x: ", ys3)
    print("y: ", xs3)
    print("x: ", ys4)
    print("y: ", xs4)
    print("x: ", ys5)
    print("y: ", xs5)
    perguntay = int(input("Diga a posição de x: "))
    perguntax = int(input("Diga a posição de y: "))
    if (perguntax == xs1 and perguntay == ys1) or (perguntax == xs2 and perguntay == ys2) or (perguntax == xs3 and perguntay == ys3) or (perguntax == xs4 and perguntay == ys4) or (perguntax == xs5 and perguntay == ys5):
        ev -=1
        for i in range(1, 7):
            for j in range(1, 7):
                if j == xs1 and xs1 == perguntax and i == ys1 and ys1 == perguntay:
                    lev1 = True
                    bt1 +=1
                if j == xs2 and xs2 == perguntax and i == ys2 and ys2 == perguntay:
                    lev2 = True
                    bt2 +=1
                if  j == xs3 and xs3 == perguntax and i == ys3 and ys3 == perguntay:
                    lev3 = True
                    bt3 +=1 
                if  j == xs4 and xs4 == perguntax and i == ys4 and ys4 == perguntay:
                    lev4 = True
                    bt4 +=1
                if  j == xs5 and xs5 == perguntax and i == ys5 and ys5 == perguntay:
                    lev5 = True
                    bt5 +=1
        print("1  2  3  4  5  6")            
        for i in range(1, 7):
            for j in range(1,7):
                if j == ys1 and i == xs1 and lev1 == True:
                    print(f"▣", end="  ")
                    bt1 == True
                elif j == ys2 and i == xs2 and lev2 == True:
                    print(f"▣", end="  ")
                    bt2 == True
                elif j == ys3 and i == xs3 and lev3 == True:
                    print(f"▣", end="  ")
                    bt3 == True
                elif j == ys4 and i == xs4 and lev4 == True:
                    print(f"▣", end="  ")
                    bt4 == True
                elif j == ys5 and i == xs5 and lev5 == True:
                    print(f"▣", end="  ")
                    bt5 == True
                else:
                    print(f"◻", end="  ")
            print(i)
        if bt1 > 1 or bt2 > 1 or bt3 > 1 or bt4 > 1 or bt5 > 1:
            ev +=1
            print("Esse navio já foi afundando, tente de novo")
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
            print("Bomba!")
    else:
        pv -=1
        print("1  2  3  4  5  6")
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