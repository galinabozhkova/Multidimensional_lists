n = int(input())
matrix = []

primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    matrix.append([int(el) for el in input().split(", ")])

for i in range (n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n-1-i])


result = f"Primary diagonal: "

print (f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print (f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
