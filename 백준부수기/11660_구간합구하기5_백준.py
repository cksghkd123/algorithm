def solution(x1, y1, x2, y2, accumulate_board):
    return accumulate_board[x2][y2] - accumulate_board[x2][y1-1] - accumulate_board[x1-1][y2] + accumulate_board[x1-1][y1-1]

def make_accumulate_board(n, board):
    result = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            result[i][j] = result[i][j-1] + board[i][j]


    for i in range(1, n+1):
        for j in range(1, n+1):
            result[j][i] = result[j-1][i] + result[j][i]

    return result

N, M = map(int, input().split())

board = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]

accumulate_board = make_accumulate_board(N, board)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = solution(x1, y1, x2, y2, accumulate_board)
    print(answer)