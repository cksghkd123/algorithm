def solution(n, stickers):
    result = 0


    dp = [[0 for _ in range(n)] for _ in range(2)]
    
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n == 1:
        result = max(*dp[0], *dp[1])
        return result

    dp[0][1] = dp[1][0] + stickers[0][1] 
    dp[1][1] = dp[0][0] + stickers[1][1]
    if n == 2:
        result = max(*dp[0], *dp[1])
        return result
    
    
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1] + stickers[0][i], dp[1][i-2] + stickers[0][i])
        dp[1][i] = max(dp[0][i-1] + stickers[1][i], dp[0][i-2] + stickers[1][i])
    
    result = max(dp[0][n-1], dp[1][n-1])

    return result

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    answer = solution(n, stickers)
    print(answer)
