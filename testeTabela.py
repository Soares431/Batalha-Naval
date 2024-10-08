posicao = []
for i in range(1, 16):
    c = []
    for j in range(1, 16):
        c.append(j)
    posicao.append(c)


for i in range(1, len(posicao)):
    for j in range(1, len(posicao[i])):

        linha_index = posicao 
        print(f"{i:02},{j:02}", end=" | ")
    print()