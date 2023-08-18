from collections import deque
rows, cols = [int(el) for el in input().split()]

matrix = []
snake = list(input())

k = 0
for  i in range(rows):
    if i % 2 == 0:
        matrix.append([])
        for j in range(cols):
            matrix[i].append(snake[k])
            k += 1
            if k == len(snake) - 1:
                k = k - len(snake)
    else:
        matrix.append(deque())
        for j in range(cols):
            matrix[i].appendleft(snake[k])
            k += 1
            if k == len(snake) - 1:
                k = k - len(snake)

for el in matrix:
    print(*el,sep='')








