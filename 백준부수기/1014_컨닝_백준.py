def solution(n, m, map_list):
    dp = [[[0, 0] for _ in range(m)] for _ in range(n)]

    dp[0][0][1] = 1
    
    for i in range(1, n):
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1])
        if map_list[i][0] == '.':
            dp[i][0][1] = max(dp[i-1][0][0] + 1, dp[i-1][0][1] + 1)

    for i in range(1, m):
        dp[0][i][0] = max(dp[0][i-1][0], dp[0][i-1][1])
        if map_list[0][i] == '.':
            dp[0][i][1] = dp[0][i-1][0] + 1

    for r in range(1, n):
        for c in range(1, m):
            dp[r][c][0] = max
            
    print(dp)


C = int(input())



for _ in range(C):
    N, M = map(int, input().split())
    map_list = [list(input()) for _ in range(N)]

    answer = solution(N, M, map_list)