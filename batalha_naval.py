z = 0
x1 = []
y1 = []


while z < 4:
    xs = int(input("digite o x do submarino: "))
    ys = int(input("digite o y do submarino: "))
    x1.append(xs)
    y1.append(ys)
    z+=1
z = 0
for i in range(1,16):
    for j in range(1,16):
        if i == x1 and j == y1:
            print("xx-xx", end=" ")
        else:
            print(f"{i:02}-{j:02}", end=" ")       
    print()

print(x1)
print(y1)
