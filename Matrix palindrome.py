rows, cols = [int(el) for el in input().split()]

matrix = []

for i in range (0, rows):
    matrix.append([])
    for j in range(i, cols+i):
        matrix[i].append(chr(i+97) + chr(j+97) + chr(i+97))

for el in matrix:
    print(*el)

