first_player, second_player = input().split(", ")

matrix = [input().split() for row in range(7)]
for i in range(7):
    for j in range(7):
        if (matrix[i][j]).isdigit():
            matrix[i][j] = int(matrix[i][j])

i, j = [int(el) for el in input()[1:-1].split(", ")]

first_player_result = 501
second_player_result = 501
turns = 1

while True:
    if 0<=i<7 and 0<=j<7:
        score = matrix[i][j]

        if score == "D":
            score = (matrix[i][0] + matrix[i][-1] + matrix[0][j] + matrix[-1][j]) * 2
        elif score == "T":
            score = (matrix[i][0] + matrix[i][-1] + matrix[0][j] + matrix[-1][j]) * 3
        elif score == "B":
            score = 501
        else:
            score = int(score)

        if turns % 2 != 0:
            first_player_result -= score
            if first_player_result <= 0:
                print(f"{first_player} won the game with {(turns + 1) // 2} throws!")
                break
        else:
            second_player_result -= score
            if second_player_result <= 0:
                print(f"{second_player} won the game with {(turns + 1) // 2} throws!")
                break

    turns += 1
    i, j = [int(el) for el in input()[1:-1].split(", ")]
