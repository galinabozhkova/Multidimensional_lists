rows, cols = [int(el) for el in input().split()]
matrix = []
[matrix.append([el for el in input().split()]) for _ in range(rows)]

command = input()

while command!= 'END':
    swap_command = command.split()
    if swap_command[0] == 'swap' and len(swap_command) == 5:
        row1 = int(swap_command[1])
        col1 = int(swap_command[2])
        row2 = int(swap_command[3])
        col2 = int(swap_command[4])
        if 0<=row1 < rows and 0<=row2<rows and 0<=col1<cols and 0<=col2<cols:
            matrix[row1][col1], matrix[row2][col2] =  matrix[row2][col2], matrix[row1][col1]
            [print(*el) for el in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()




