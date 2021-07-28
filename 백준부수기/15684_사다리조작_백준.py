def ladder_check(ladder_info):
    result = []
    for c in range(h):
        one_col_sum = sum(map(lambda r: ladder_info[r][c],range(n)))
        result.append(one_col_sum)
    
    print(result)


n, m, h = map(int,input().split())
ladder_board = [[0]*n for _ in range(h)]

for _ in range(m):
    row, col = map(lambda x: int(x)-1 ,input().split())
    ladder_board[row][col] = 1
    ladder_board[row][col+1] = -1

print(ladder_board)
ladder_check(ladder_board)
