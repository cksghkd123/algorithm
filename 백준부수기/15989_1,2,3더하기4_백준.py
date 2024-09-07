import sys
sys.setrecursionlimit(10**4)

def solution(n, i):
    if n > 3 and dp[n][i] == 0:
        dp[n][2] = dp[n][1] + solution(n-2, 2)
        dp[n][3] = dp[n][2] + solution(n-3, 3)

    return dp[n][i]

dp = [[0, 1, 0, 0] for _ in range(10001)]
dp[1][2] = 1
dp[1][3] = 1
dp[2][2] = 2
dp[2][3] = 2
dp[3][2] = 2
dp[3][3] = 3

T = int(input())

for _ in range(T):
    n = int(input())

    answer = solution(n, 3)

    print(answer)
