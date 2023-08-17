row, column = [int(el) for el in input().split()]

matrix = []
num_sqr_matrix = 0
for _ in range(row):
    matrix.append([el for el in input().split()])

for i in range(row-1):
    for j in range(column-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            num_sqr_matrix+=1

print(num_sqr_matrix)
