# def chaeck_command (current_matrix, row, col,coal_count,total_coal):
#     if current_matrix[row][col] == 'c':
#         col_index = (row, col)
#         coal_count += 1
#         if coal_count == total_coal:
#             return print(f'You collected all coal! {col_index}')
#         matrix[current_row][current_col] = '*'
#     elif matrix[current_row][current_col] == 'e':
#         print(f'Game over! ({current_row}, {current_col})')
# #         break
#
#     print(f"{sum_coal - col_count} pieces of coal left. ({col_index})")


n = int(input())
commands = input().split()
matrix = []
[matrix.append([el for el in input().split()]) for _ in range(n)]
sum_coal = sum([matrix[i].count('c') for i in range(n) if 'c' in matrix[i]])
Game_end = False

for i in range(n):
    if "s" in matrix[i]:
        current_col = matrix[i].index('s')
        current_row = i
        break

col_count=0
for el in commands:
    if el == 'left':
        if current_col > 0:
            current_col -= 1
            if matrix[current_row][current_col] == 'c':
                col_index = (current_row, current_col)
                col_count += 1
                if col_count == sum_coal:
                    print(f'You collected all coal! {col_index}')
                    Game_end = True
                    break
                else:
                    matrix[current_row][current_col] = '*'
            elif matrix[current_row][current_col] == 'e':
                print(f'Game over! ({current_row}, {current_col})')
                Game_end = True
                break
    elif el == 'right':
        if current_col < n-1:
            current_col += 1
            if matrix[current_row][current_col] == 'c':
                col_index = (current_row, current_col)
                col_count += 1
                if col_count == sum_coal:
                    print(f'You collected all coal! {col_index}')
                    Game_end = True
                    break
                else:
                    matrix[current_row][current_col] = '*'
            elif matrix[current_row][current_col] == 'e':
                print(f'Game over! ({current_row}, {current_col})')
                Game_end = True
                break
    elif el == 'up':
        if current_row > 0:
            current_row -= 1
            if matrix[current_row][current_col] == 'c':
                col_index = (current_row, current_col)
                col_count += 1
                if col_count == sum_coal:
                    print(f'You collected all coal! {col_index}')
                    Game_end = True
                    break
                else:
                    matrix[current_row][current_col] = '*'
            elif matrix[current_row][current_col] == 'e':
                print(f'Game over! ({current_row}, {current_col})')
                Game_end = True
                break
    elif el == 'down':
        if current_row < n - 1:
            current_row += 1
            if matrix[current_row][current_col] == 'c':
                col_index = (current_row, current_col)
                col_count += 1
                if col_count == sum_coal:
                    print(f'You collected all coal! {col_index}')
                    Game_end = True
                    break
                else:
                    matrix[current_row][current_col] = '*'
            elif matrix[current_row][current_col] == 'e':
                print(f'Game over! ({current_row}, {current_col})')
                Game_end = True
                break

# if matrix[current_row][current_col] == 'c':
#     col_index = (current_row,current_row)
#     col_count += 1
#     if col_count == sum_coal:
#         print(f'You collected all coal! {col_index}')
#         break
#     matrix[current_row][current_col] = '*'
# elif matrix[current_row][current_col] == 'e':
#     print(f'Game over! ({current_row}, {current_col})')
#     break
if not Game_end:
    print(f"{sum_coal-col_count} pieces of coal left. ({current_row}, {current_col})")


