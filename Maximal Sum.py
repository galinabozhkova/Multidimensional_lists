from sys import maxsize

row, column = [int(el) for el in input().split()]

matrix = []
max_sum = -maxsize
first_element_index = []

for _ in range(row):
    matrix.append([int(el) for el in input().split()])

for i in range(row-2):
    for j in range(column-2):
        sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] +  matrix[i+1][j+1] +  matrix[i+1][j+2] +  matrix[i+2][j]+  matrix[i+2][j+1]+  matrix[i+2][j+2]
        if sum > max_sum:
            first_element_index = [i,j]
            max_sum = sum


print(f"Sum = {max_sum}")

k = first_element_index[0]
l = first_element_index[1]
print (f"{matrix[k][l]} {matrix[k][l+1]} {matrix[k][l+2]}")
print(f"{matrix[k+1][l]} {matrix[k+1][l + 1]} {matrix[k+1][l + 2]}")
print(f"{matrix[k+2][l]} {matrix[k+2][l + 1]} {matrix[k+2][l + 2]}")


