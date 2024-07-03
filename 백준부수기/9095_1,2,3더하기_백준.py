def solution(n):
    if dp[n] != 0:
        return dp[n]
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
    return dp[n]
    

T = int(input())

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T):
    n = int(input())
    answer = solution(n)
    print(answer)