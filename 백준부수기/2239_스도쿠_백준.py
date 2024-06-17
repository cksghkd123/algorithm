def square_index(i, j):
    return (i//3)*3 + j//3

game_board = [list(map(int, list(input()))) for _ in range(9)]


row_dic = [[False for _ in range(10)] for _ in range(9)]
col_dic = [[False for _ in range(10)] for _ in range(9)]
square_dic = [[False for _ in range(10)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        if game_board[i][j] == 0:
            continue
        else:
            row_dic[i][game_board[i][j]] = True
            col_dic[j][game_board[i][j]] = True
            square_dic[square_index(i, j)][game_board[i][j]] = True

found = False

def find(number):
    global found
    if found:
        return
    
    if number == 81:
        found = True
        return
    
    i = number // 9
    j = number % 9

    if game_board[i][j] != 0:
        find(number+1)
    else:
        for k in range(1,10):
            if row_dic[i][k] == False and col_dic[j][k] == False and square_dic[square_index(i,j)][k] == False:
                row_dic[i][k] = True
                col_dic[j][k] = True
                square_dic[square_index(i,j)][k] = True
                game_board[i][j] = k

                find(number+1)
                if found:
                    return

                row_dic[i][k] = False
                col_dic[j][k] = False
                square_dic[square_index(i,j)][k] = False
                game_board[i][j] = 0


find(0)
for i in range(9):
    for j in range(9):
        print(game_board[i][j], end="")
    print("")