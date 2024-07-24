INF = float('inf')

def solution(n, w, map_list):
    dp = [[INF for _ in range(n)] for _ in range(2)]

    dp[1][-1] = 0
    # 진행방향은 무조건 오른쪽 or 위쪽
    # not
    for i in range(n-1):
        dp[0][i] = dp[]
        if dp[0][i] + dp[1][i] <= w:
            dp[1][i] = min(dp[i][1], dp[i][0]+1)
        
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+1)
        


    answer = dp[1][n-1]

    # 1-8 
    dp = [[0 for _ in range(n)] for _ in range(2)]
    if dp[0][0] + dp[0][n-1] <= w:
        for i in range(n):
            for j in range(2):
        
        answer = max(answer, dp[1][n-1])

    # 9-16
    dp = [[0 for _ in range(n)] for _ in range(2)]
    if dp[1][0] + dp[1][n-1] <= w:

        answer = max(answer, dp[1][n-1])

    # 1-8 and 9-16
    dp = [[0 for _ in range(n)] for _ in range(2)]
    if dp[0][0] + dp[0][n-1] <= w and dp[1][0] + dp[1][n-1] <= w:

        answer = max(answer, dp[1][n-1])
        
    
    return answer

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(2)]
    answer = solution(N, W, map_list)
    
    print(answer)


# 1
# 8 100
# 70 60 55 43 57 60 44 50
# 58 40 47 90 45 52 80 40