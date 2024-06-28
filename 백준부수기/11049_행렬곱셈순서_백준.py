N = int(input())

matrix_list = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    r, c = map(int, input().split())
    matrix_list.append((r, c))

for i in range(N-1):
    dp[i][i+1] = matrix_list[i][0] * matrix_list[i][1] * matrix_list[i+1][1]

for d in range(2, N):
    for i in range(N-d):
        dp[i][i+d] = min(dp[i][i+1] + matrix_list[i][0] * matrix_list[i+1][1] * matrix_list[i+d][1] + dp[i+2][i+d],
                         dp[i][i+d-2] + matrix_list[i][0] * matrix_list[i+d-2][1] * matrix_list[i+d][1] + dp[i+d-1][i+d],
                         matrix_list[i][0] * matrix_list[i][1] * matrix_list[i+d][1] + dp[i+1][i+d],
                         dp[i][i+d-1] + matrix_list[i][0] * matrix_list[i+d][0] * matrix_list[i+d][1])

answer = dp[0][N-1]

print(answer)
