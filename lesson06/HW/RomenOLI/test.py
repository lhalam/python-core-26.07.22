from random import randrange
mx = []
width, height = int(input("input width of matrix - ")), int(input("input height of matrix - "))
for i in range(width):
    mx.append([])
    for j in range(height):
        mx[i].append(randrange(0, 999))
    print(*mx[i])
    if i == 0:
        mx[i] = sorted(mx[i])
    print(*mx[i])
